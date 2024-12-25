[![CI](https://github.com/NarmalaSk/StockTickerApp/actions/workflows/action.yml/badge.svg)](https://github.com/NarmalaSk/StockTickerApp/actions/workflows/action.yml)
# StockTickerApp

![Screenshot 2024-12-19 232948](https://github.com/user-attachments/assets/3a42f47f-6b6d-49ef-9687-47849c284948)
![WhatsApp Image 2024-12-19 at 23 34 58_1aba927b](https://github.com/user-attachments/assets/c8bc2d4f-851a-4d03-b200-7c56ed6da04d)

## Overview

The **StockTickerApp** is a simple web application that provides real-time stock prices to users. It allows users to subscribe to stock price notifications at customizable intervals (e.g., 5, 10, 20, 30 minutes). This application is built for educational purposes and is free to use. Please note that notifications may sometimes be marked as spam by email providers, so be sure to check your spam folder if you don’t see the notifications in your inbox.

## Features

- **Real-time Stock Price Updates**: Get up-to-date stock prices using the Marketstack API.
- **Custom Notification Intervals**: Set notification intervals (5, 10, 20, 30 minutes) to get timely updates on selected stocks.
- **Email Notifications**: Notifications are sent to users via Mailjet API.
- **Logging**: Stock prices are logged into MongoDB for record-keeping and analysis.
  
## Tech Stack

### Frontend
- **HTML**: Basic structure of the webpage.
- **CSS**: Styling for a clean, responsive, and user-friendly interface.

### Backend
- **Flask**: The backend framework to handle API requests and send notifications.
- **CORS**: Cross-Origin Resource Sharing enabled for secure communication between frontend and backend.

### Database
- **MongoDB**: Used for logging stock prices and storing user subscription data.

### APIs
- **Marketstack API**: Provides real-time stock price data.
- **Mailjet API**: Handles email notifications to users.

## How to Set Up the App Locally

To set up the StockTickerApp on your local machine, follow these steps:

### Prerequisites

Make sure you have the following installed on your system:
- Python 3.x
- pip (Python package installer)
- MongoDB (can be installed locally or use a cloud service like MongoDB Atlas)

### Step-by-Step Guide

1. **Clone the Repository**:
   Open your terminal and run the following command to clone this repository:

   ```bash
   git clone https://github.com/your-username/StockTickerApp.git
   cd StockTickerApp
Set Up Virtual Environment: It's recommended to use a virtual environment for managing dependencies. Run the following commands:

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
Install Dependencies: Install the required Python packages using pip:

bash
Copy code
pip install -r requirements.txt
The requirements.txt file should include:

Flask
Flask-CORS
requests
pymongo
marketstack (or any API client for Marketstack)
mailjet-rest
Set Up Environment Variables: Create a .env file in the root of the project to store your API keys and MongoDB URI. Example:

bash
Copy code
MARKETSTACK_API_KEY=your_marketstack_api_key
MAILJET_API_KEY=your_mailjet_api_key
MAILJET_SECRET_KEY=your_mailjet_secret_key
MONGODB_URI=your_mongodb_connection_string
Replace the placeholders with your actual API keys and MongoDB URI.

Run the Application: Start the Flask app by running:

bash
Copy code
python app.py
The app should now be running at http://127.0.0.1:5000.

Access the App: Open your browser and visit http://127.0.0.1:5000 to start using the application.

Features
Stock Price Notifications: Users can input their email, select a stock symbol (e.g., AAPL, TSLA), and set a notification interval to receive updates on stock prices.

MongoDB Logging: Stock prices and user data are logged into MongoDB for further analysis or record-keeping.

Email Notifications: Users will receive notifications about stock price changes via email using the Mailjet API.

Troubleshooting
Email in Spam Folder: If you’re not receiving the stock price notifications in your inbox, check your spam folder. Some email providers may mark automated notifications as spam.

API Rate Limits: Be aware of the rate limits imposed by the Marketstack API. If you exceed the free tier’s limits, you may experience delays or failures in fetching stock prices.

License
