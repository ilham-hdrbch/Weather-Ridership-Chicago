# Weather-Ridership-Chicago

In this project, I analyzed passenger data (bus and train) and weather data for the city of Chicago to understand how weather conditions can impact the number of passengers and to create a machine learning model that predicts whether the transportation of the day will be crowded or not based on the weather conditions. I also created a user-friendly website for the citizens of Chicago, providing predictive information on public transport crowding for the upcoming day. This can help the citizens of Chicago avoid crowds if they wish.

## Datasets:
I have used two datasets:

weather_df:
I obtained the data from this link: NASA POWER Data Access Viewer.
transport_df:
I downloaded the CSV file of the dataset from this link: CTA Ridership Daily Boarding Totals.

Finally, I created a new dataset based on these two sources, which you can find on Hugging Face: IlhamHadarbach/chicago_public_transit_ridership_weather_2001_2023.

## Interface :
For the graphical interface, I created a website using Django. This site utilizes weather data from the OpenWeatherMap API (temperature and wind speed) for the city of Chicago, along with the date and month. It performs calculations to determine the type of day and then uses all this data to predict whether public transportation will be crowded or not on that day.
![Capture d’écran (134)](https://github.com/ilham-hdrbch/Weather-Ridership-Chicago/assets/106122424/17819f24-df6b-4bdd-a7e5-e1b7071f1ed6)


