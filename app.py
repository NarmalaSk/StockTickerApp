from dotenv import load_dotenv
import os
from flask import Flask, render_template, request, redirect, url_for, session
import requests
from mailjet_rest import Client
import threading
import time
import logging
from flask_cors import CORS
from pymongo import MongoClient

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')
CORS(app)

api_secret = os.getenv('API_SECRET')
api_key = os.getenv('API_KEY')
mailjet = Client(auth=(api_key, api_secret), version='v3.1')

access_key = os.getenv('ACCESS_KEY')

logging.basicConfig(level=logging.INFO)

client = MongoClient(os.getenv('MONGO_URI'))
db = client["stock_notifications"]
collection = db["notifications"]
from_email = os.getenv('FROM_EMAIL')

def send_email(from_email, to_email, message, stock_name, time_at_stock):
    email_data = {
        'Messages': [
            {
                "From": {
                    "Email": from_email,
                    "Name": "Stock Tracker"
                },
                "To": [
                    {
                        "Email": to_email,
                        "Name": "Recipient Name"
                    }
                ],
                "Subject": f"Stock Tracker - {time_at_stock}",
                "TextPart": f"The current price of {stock_name} is: ₹{message}\n\nUpgrade to our premium tier to get more detailed info and quicker updates on stock prices."
            }
        ]
    }
    response = mailjet.send.create(data=email_data)
    if response.status_code == 200:
        logging.info("Email sent successfully!")
        log_notification(stock_name, to_email, message, time_at_stock)
    else:
        logging.error(f"Failed to send email. Status code: {response.status_code}")
        logging.error(response.text)

def get_stock_price(stock_symbol):
    url = "https://api.marketstack.com/v1/eod"
    querystring = {"access_key": access_key, "symbols": stock_symbol}
    response = requests.get(url, params=querystring)
    data = response.json()
    if "data" in data and len(data["data"]) > 0:
        stock_data = data["data"][0]
        return stock_data.get("close")
    return None

def log_notification(stock_name, email, price, time_at_stock):
    notification = {
        "stock_name": stock_name,
        "email": email,
        "price": price,
        "time": time_at_stock
    }
    collection.insert_one(notification)
    logging.info(f"Logged notification for {stock_name} to {email} at {time_at_stock}.")

def process_request(stock_name, email, interval):
    from_email = os.getenv('FROM_EMAIL')
    logging.info(f"Started processing request for {stock_name} to {email} every {interval} minutes.")
    while True:
        stock_price = get_stock_price(stock_name)
        time_at_stock = time.strftime("%H:%M:%S")
        if stock_price:
            message = f"The current price of {stock_name} is: ₹{stock_price}"
        else:
            message = f"Could not fetch the stock price for {stock_name}."
        logging.info(f"Sending email to {email}: {message}")
        send_email(from_email, email, message, stock_name, time_at_stock)
        time.sleep(interval * 60)

@app.route('/')
def home():
    return render_template('indexe.html')

@app.route('/submit', methods=['POST'])
def submit():
    stock_name = request.form['stock_name']
    email = request.form['email']
    interval = int(request.form['interval'])
    session['stock_name'] = stock_name
    session['email'] = email
    session['interval'] = interval
    threading.Thread(target=process_request, args=(stock_name, email, interval), daemon=True).start()
    return redirect(url_for('home'))
