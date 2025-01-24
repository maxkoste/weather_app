from weather_api import connect
import tkinter as tk

class gui(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Weather App")
        self.geometry("500x500")
        self.resizable(False, False)

        self.label = tk.Label(self, text="weather app lets go!")
        self.label.pack()

        self.city_label = tk.Label(self, text="Enter City: ")
        self.city_label.pack()

        #get the city entry from the user
        self.entry = tk.Entry(self, width=30)
        self.entry.pack()

        self.get_weather_button = tk.Button(self, text="Get Weather", command = self.get_city)
        self.get_weather_button.pack()

        self.quit_button = tk.Button(self, text="exit", command=self.quit)
        self.quit_button.pack()

    def get_city(self):
        city = self.entry.get()
        weather_data = connect(city)
        self.display_weather(weather_data)

    def display_weather(self, weather_data):
        """Displays the weather information."""

        # Check if 'current' data exists in the response
        if 'current' in weather_data:
            # Extract the necessary information from the JSON
            temp = weather_data['current']['temperature']
            weather_description = weather_data['current']['weather_descriptions'][0]
            humidity = weather_data['current']['humidity']
            local_time = weather_data['location']['localtime']
            wind_speed = weather_data['current']['wind_speed']
            feels_like = weather_data['current']['feelslike']

            # Display the information in the label
            self.label.config(
                text=f"The weather is {weather_description}.\n"
                    f"Local Time: {local_time}\n"
                    f"Temperature: {temp}°C\n"
                    f"Feels Like: {feels_like}°C\n"
                    f"Humidity: {humidity}%\n"
                    f"Wind Speed: {wind_speed} m/s"
            )
        else:
            self.label.config(text="Could not retrieve weather data.")
