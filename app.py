from flask import Flask, render_template, request, redirect, url_for, flash
import telebot
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure key

# Replace with your actual Telegram Bot Token and Chat ID
TELEGRAM_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
TELEGRAM_CHAT_ID = 'YOUR_TELEGRAM_CHAT_ID'
bot = telebot.TeleBot(TELEGRAM_TOKEN)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        tele_msg = f"New Contact Us Message:\nName: {name}\nEmail: {email}\nMessage: {message}"
        try:
            bot.send_message(TELEGRAM_CHAT_ID, tele_msg)
            flash('Message sent! We will get back to you soon.', 'success')
        except Exception as e:
            flash('Failed to send message. Please try again later.', 'danger')
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)