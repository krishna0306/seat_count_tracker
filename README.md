# seat_count_tracker
The Seat Count Tracker Telegram Bot is a Python script that leverages the RapidAPI and Telegram API to monitor seat availability on specific train routes. This tool allows users to set a threshold for seat availability, and when the count falls below the specified limit, the bot sends real-time notifications via Telegram


# Seat Count Tracker Telegram Bot

Welcome to the Seat Count Tracker Telegram Bot project! This Python script enables real-time monitoring of train seat availability through the RapidAPI and sends Telegram notifications when seats are running low. Whether you're a traveler needing to secure a seat or a developer looking to learn about API integration and automated alerts, this project is for you.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Example](#example)
- [Screenshots](#screenshots)
- [Dependencies](#dependencies)
- [Contact](#contact)
- [License](#license)

## Installation

1. Clone this repository to your local machine.
2. Install required dependencies using `pip install -r requirements.txt`.
3. Obtain your RapidAPI key and Telegram bot token.
4. Configure the `config.py` file with your API keys and preferences.

## Usage

1. Run the script: `python seat_count_tracker.py`.
2. Follow the on-screen prompts to input train details and seat threshold.
3. The bot will fetch seat availability data and send Telegram notifications when seats are below the threshold.

## Configuration

Before running the script, make sure to:
- Set up a Telegram bot and obtain a token.
- Obtain a RapidAPI key for accessing train data.
- Configure the `config.py` file with your API keys and preferences.

## Example

Run the script with the following command:
```sh
python seat_count_tracker.py

![ss-1](https://github.com/krishna0306/seat_count_tracker/assets/94451390/1f883d8d-d65c-4e8a-aba8-cb2d3faa5348)



