# WeatherApp

WeatherApp is a simple desktop application developed using PyQt5 to display current weather and a 5-day forecast for a specified city. It utilizes the OpenWeatherMap API to fetch weather data and provides a user-friendly interface to interact with.

## Features

- **Current Weather**: Displays temperature, weather description, sunrise, and sunset times.
- **5-Day Forecast**: Shows a detailed forecast for the next 5 days.
- **Temperature Toggle**: Switch between Fahrenheit and Celsius temperature units.
- **PM Accelerator Info**: Provides information about the Product Manager Accelerator Program.

## Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/yourusername/weatherapp.git

## Usage

- Run the application:
- python main.py

## Interact with the application:

- Enter a city name in the input box.
- Click "Get Weather" to view current weather details.
- Click "5-Day Forecast" to see the forecast for the next 5 days.
- Use the "Toggle °F/°C" button to switch between Fahrenheit and Celsius.
- Click "PM Accelerator Info" to get details about the Product Manager Accelerator Program.

## Configuration

- API Key: The application uses the OpenWeatherMap API. Replace cb3431d20f7843aa2783316da181bd29 in the main.py file with your own API key for production use.

## Code Overview

- WeatherApp Class: The main class that defines the user interface and functionality.
- initUI(): Initializes and sets up the user interface components.
- show_info(): Displays information about the PM Accelerator Program.
- get_weather(): Fetches and displays the current weather based on user input.
- display_weather(): Updates the UI with weather data.
- get_weather_emoji(): Returns an emoji representing the weather condition.
- toggle_temperature(): Toggles between Fahrenheit and Celsius temperature units.
- show_forecast(): Fetches and displays a 5-day weather forecast.
- display_forecast(): Displays the 5-day forecast in a dialog.

## Dependencies

- Python 3.x
- PyQt5: For creating the GUI.
- Requests: For making HTTP requests to the OpenWeatherMap API.
