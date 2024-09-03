# main.py
# Created by Chloe Kershner
import sys
from datetime import datetime
import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QSizePolicy,
                             QHBoxLayout, QMessageBox, QTextEdit, QDialog)
from PyQt5.QtCore import Qt

# Weather app class
class WeatherApp(QWidget):

    # Initialize features for app
    def __init__(self):
        super().__init__()
        self.title = QLabel("Weather App", self) # Label for title
        self.name = QLabel("created by Chloe Kershner", self) # Label for name
        self.get_info_button = QPushButton("PM Accelerator Info", self) #Label for get info to show company info for PM Accelerator
        self.city_label = QLabel("Enter city name: ", self) # Label for prompt to enter city name
        self.city_input = QLineEdit(self) # Input box for user to enter city
        self.get_weather_button = QPushButton("Get Weather", self) # Button to get the weather
        self.get_forecast_button = QPushButton("5-Day Forecast")  # Button for 5-day forecast
        self.temperature_label = QLabel(self) # Label for temperature
        self.emoji_label = QLabel(self) # Label for emoji based on weather
        self.description_label = QLabel(self) # Label for the weather description
        self.sunrise_label = QLabel(self) # Label for sunrise info
        self.sunset_label = QLabel(self) # Label for sunset info
        self.toggle_button = QPushButton("Toggle °F/°C", self)  # Toggle button for temperature units
        self.is_fahrenheit = True  # Variable to track the temperature unit
        self.initUI() # Call the function to initialize the UI

    def initUI(self):
        self.setWindowTitle("Weather App") # Name the Window Weather App

        # add Widgets for all of the labels and buttons
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        vbox.addWidget(self.title)
        vbox.addWidget(self.name)
        hbox.addWidget(self.get_info_button, alignment=Qt.AlignCenter)
        vbox.addLayout(hbox)
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.get_forecast_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)
        vbox.addWidget(self.sunrise_label)
        vbox.addWidget(self.sunset_label)
        vbox.addWidget(self.toggle_button)
        self.setLayout(vbox)

        # Center align all labels and buttons
        self.title.setAlignment(Qt.AlignCenter)
        self.name.setAlignment(Qt.AlignCenter)
        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)
        self.sunrise_label.setAlignment(Qt.AlignCenter)
        self.sunset_label.setAlignment(Qt.AlignCenter)

        # Name label and button objects
        self.title.setObjectName("welcome_label")
        self.name.setObjectName("name_label")
        self.get_info_button.setObjectName("get_info_button")
        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.get_forecast_button.setObjectName("get_forecast_button")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")
        self.sunrise_label.setObjectName("sunrise_label")
        self.sunset_label.setObjectName("sunset_label")
        self.toggle_button.setObjectName("toggle_button")

        # Set the minimum height of the city_input
        self.city_input.setMinimumHeight(60)
        self.city_input.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        # Set the minimum Width of the get_info_button
        self.get_info_button.setMinimumWidth(30)
        self.get_info_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        # Set style for all labels and buttons
        self.setStyleSheet("""
             QLabel, QPushButton {
                font-family: Helvetica;
            }
            QLabel#welcome_label {
                font-family: Optima;
                font-size: 55px;
                font-weight: bold;
            }
             QLabel#name_label {
                font-family: Optima;
                font-size: 16px;
            }
            QPushButton#get_info_button, QPushButton#get_forecast_button, QPushButton#toggle_button {
                font-size: 20px;
            }
            QLabel#city_label {
                font-family: Helvetica;
                font-size: 40px;
                font-style: italic;
            }
            QLineEdit#city_input {
                font-size: 40px;
                padding: 10px;
            }
            QPushButton#get_weather_button {
                font-size: 30px;
                font-weight: bold;
            }
            QLabel#temperature_label {
                font-size: 75px;
            }
            QLabel#emoji_label {
                font-size: 100px;
                font-family: Apple Color Emoji;
            }
            QLabel#description_label {
                font-size: 50px;
            }
            QLabel#sunrise_label, QLabel#sunset_label {
                font-size: 25px;
            }
        """)

        # Handle button clicks
        self.get_info_button.clicked.connect(self.show_info) # Connect get info button to method
        self.get_weather_button.clicked.connect(self.get_weather) # Connect get weather button to method
        self.get_forecast_button.clicked.connect(self.show_forecast)  # Connect forecast button to method
        self.toggle_button.clicked.connect(self.toggle_temperature)  # Connect toggle button to method

    # Method to display PM Accelerator information
    def show_info(self):
        info_text = (
            "The Product Manager Accelerator Program is designed to support PM professionals through every stage of their career. "
            "From students looking for entry-level jobs to Directors looking to take on a leadership role, our program has helped over "
            "hundreds of students fulfill their career aspirations.\n\n"
            "Our Product Manager Accelerator community are ambitious and committed. Through our program they have learnt, honed and developed "
            "new PM and leadership skills, giving them a strong foundation for their future endeavours.\n\n"
            "Learn product management for free today on our YouTube channel:\n"
            "https://www.youtube.com/c/drnancyli?sub_confirmation=1\n\n"
            "Interested in PM Accelerator Pro?\n"
            "Step 1: Attend the Product Masterclass to learn more about the program details, price, different packages, and stay until the end to get FREE AI Course.\n\n"
            "Learn how to create a killer product portfolio in two weeks that will help you land any PM job (traditional or AI), even if you were laid off or have zero PM experience:\n"
            "https://www.drnancyli.com/masterclass\n\n"
            "Step 2: Reserve your early bird ticket and submit an application to talk to our Head of Admission.\n\n"
            "Step 3: Successful applicants join our PMA Pro community to receive customized coaching!\n\n"
            "Website: http://www.drnancyli.com\n"
            "Phone: +1 6176106855"
        )

        QMessageBox.information(self, "PM Accelerator Info", info_text) # Set the text as the information to be displayed

    # Method to get the weather using openweathermap.org
    def get_weather(self):
        api_key = "cb3431d20f7843aa2783316da181bd29"
        city = self.city_input.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

        # Try to get the data
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            # If the data is successfully retrieved, call the display weather method using the data
            if data["cod"] == 200:
                self.display_weather(data)
        # Exception handling
        except requests.exceptions.HTTPError:
            match response.status_code:
                case 400:
                    self.display_error_message("Please enter a valid input.")
                case 401:
                    self.display_error_message("Invalid API key")
                case 403:
                    self.display_error_message("Access denied")
                case 404:
                    self.display_error_message("City not found, please enter a valid city name.")
                case 500:
                    self.display_error_message("Internal Server Error")
                case 502:
                    self.display_error_message("Bad Gateway")
                case 503:
                    self.display_error_message("Server is down")
                case 504:
                    self.display_error_message("Gateway Timeout")
                case _:
                    self.display_error_message(f"HTTP Error")

        except requests.exceptions.ConnectionError:
            self.display_error_message("Connection Error. Check your internet connection.")
        except requests.exceptions.Timeout:
            self.display_error_message("Timeout Error. The request timed out.")
        except requests.exceptions.TooManyRedirects:
            self.display_error_message("Too many redirects.")
        except requests.exceptions.RequestException:
            self.display_error_message("Something went wrong.")

    # Method to display error message (used in get_weather)
    def display_error_message(self, message):
        self.temperature_label.setStyleSheet("font-size: 25px")
        self.temperature_label.setText(message) # Display the error message
        self.emoji_label.clear() # Clear emoji label
        self.description_label.clear() # Clear the weather description

    # Method to display the weather
    def display_weather(self, data):
        self.temperature_label.setStyleSheet("font-size: 75px")
        # Store the temperature from the data retrieved (given in Kelvin)
        temp_kelvin = data["main"]["temp"]

        # If button is toggled to fahrenheit, convert the weather to fahrenheit
        if self.is_fahrenheit:
            temp_fahrenheit = int((temp_kelvin * 9 / 5) - 459.67)
            temp_display = f"{temp_fahrenheit}°F" # Display the calculated temperature
        # else, it is toggled to celsius, so convert to celsius
        else:
            temp_celsius = int(temp_kelvin - 273.15)
            temp_display = f"{temp_celsius}°C" # Display the calculated temperature

        weather_id = data["weather"][0]["id"] # Store the weather id from the data
        weather_description = data["weather"][0]["description"] # Store the weather description from the data

        timezone_offset = data["timezone"]  # Store the timezone offset in seconds
        sunrise_unix = data["sys"]["sunrise"] + timezone_offset  # Adjusting for local time
        sunset_unix = data["sys"]["sunset"] + timezone_offset  # Adjusting for local time

        sunrise_time = datetime.utcfromtimestamp(sunrise_unix).strftime('%I:%M %p') # Store the sunrise time
        sunset_time = datetime.utcfromtimestamp(sunset_unix).strftime('%I:%M %p') # Store the sunset time

        self.temperature_label.setText(temp_display) # Display temperature label
        self.emoji_label.setText(self.get_weather_emoji(weather_id)) # Display tbe emoji label
        self.description_label.setText(weather_description) # Display the description label
        self.sunrise_label.setText(f"☀️ Sunrise: {sunrise_time}")  # Display sunrise time
        self.sunset_label.setText(f"☽ Sunset: {sunset_time}")  # Display sunset time

    # Method to get the weather emoji using the weather id
    def get_weather_emoji(self, weather_id):
        if weather_id // 100 == 2:
            return "⛈️"  # Thunderstorm
        elif weather_id // 100 == 3:
            return "🌧️"  # Drizzle
        elif weather_id // 100 == 5:
            return "🌧️"  # Rain
        elif weather_id // 100 == 6:
            return "❄️"  # Snow
        elif weather_id // 100 == 7:
            return "🌫️"  # Atmosphere (fog, dust, etc.)
        elif weather_id == 800:
            return "☀️"  # Clear
        elif weather_id == 801:
            return "🌤️"  # Few clouds
        elif weather_id == 802:
            return "⛅"  # Scattered clouds
        elif weather_id == 803:
            return "🌥️"  # Broken clouds
        elif weather_id == 804:
            return "☁️"  # Overcast clouds
        else:
            return "🌡️"  # Default for any other weather condition

    # Method to format the time
    def format_time(self, timestamp):
        dt = datetime.utcfromtimestamp(timestamp)
        return dt.strftime("%I:%M %p")

    # Method to handle fahrenheit and celsius toggle button
    def toggle_temperature(self):
        self.is_fahrenheit = not self.is_fahrenheit
        # Refresh the weather display if weather data is already available
        if self.temperature_label.text():
            city = self.city_input.text()
            if city:
                self.get_weather()  # Refresh weather data to update the temperature display

    # Method to show the 5 day forecast
    def show_forecast(self):
        api_key = "cb3431d20f7843aa2783316da181bd29"
        city = self.city_input.text()
        url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}"

        # Try to retrieve data
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            # If retrieved successfully, call to display the 5 day forecast using the data
            if data["cod"] == "200":
                self.display_forecast(data)
        # Exception handling
        except requests.exceptions.HTTPError:
            match response.status_code:
                case 400:
                    self.display_error_message("Please enter a valid input.")
                case 401:
                    self.display_error_message("Invalid API key")
                case 403:
                    self.display_error_message("Access denied")
                case 404:
                    self.display_error_message("City not found, please enter a valid city name.")
                case 500:
                    self.display_error_message("Internal Server Error")
                case 502:
                    self.display_error_message("Bad Gateway")
                case 503:
                    self.display_error_message("Server is down")
                case 504:
                    self.display_error_message("Gateway Timeout")
                case _:
                    self.display_error_message(f"HTTP Error")

        except requests.exceptions.ConnectionError:
            self.display_error_message("Connection Error. Check your internet connection.")
        except requests.exceptions.Timeout:
            self.display_error_message("Timeout Error. The request timed out.")
        except requests.exceptions.TooManyRedirects:
            self.display_error_message("Too many redirects.")
        except requests.exceptions.RequestException:
            self.display_error_message("Something went wrong.")

    # Method to display the forecast
    def display_forecast(self, data):
        forecast_dialog = QDialog(self)
        forecast_dialog.setWindowTitle("5-Day Forecast")
        layout = QVBoxLayout()

        forecast_text = QTextEdit()
        forecast_text.setReadOnly(True)

        forecast_info = ""
        for i in range(0, len(data['list']), 8):  # Get daily data (every 8th entry)
            forecast = data['list'][i]
            date = datetime.utcfromtimestamp(forecast['dt']).strftime('%m-%d-%Y')
            temp_kelvin = forecast['main']['temp']

            # If toggled fahrenheit, calculate and display the temperature in fahrenheit
            if self.is_fahrenheit:
                temp_fahrenheit = int((temp_kelvin * 9 / 5) - 459.67)
                temp_display = f"{temp_fahrenheit}°F"
            # else, calculate and display the weather in celsius
            else:
                temp_celsius = int(temp_kelvin - 273.15)
                temp_display = f"{temp_celsius}°C"

            # store the weather description and forecast info
            description = forecast['weather'][0]['description']
            forecast_info += f"Date: {date}\nTemperature: {temp_display}\nWeather: {description}\n\n"

        # Set the text and add Widgets for the 5 day forecast
        forecast_text.setText(forecast_info)
        layout.addWidget(forecast_text)
        forecast_dialog.setLayout(layout)
        forecast_dialog.exec_()

# Start the weather app
if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())
