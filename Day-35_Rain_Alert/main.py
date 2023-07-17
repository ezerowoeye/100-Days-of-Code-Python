import requests
import os
from twilio.rest import Client

api_key = "3b9c7a5934d411f5d62f8f8c8c4b4cb8"
account_sid = "AC3fded91ae307f2e8a163108ef2f2bb22"
auth_token = "adcb7e5e427aca53d46085b9b1eb4100"

number = +12055741799
# https://api.openweathermap.org/data/2.5/forecast?lat=7.544510&lon=4.556030&appid=3b9c7a5934d411f5d62f8f8c8c4b4cb8
parameters = {
    "lat": 7.544510,
    "lon": 4.556030,
    "appid": api_key

}
response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
# print(response.raise_for_status())

weather_data = response.json()
# print(data)
weather_condition = []
# made use of a 3-hour weather forcast. 3 x 4 == 12 hours.
# using slices:
weather_slice = weather_data["list"][:4]

will_rain = False
# for hour_data in weather_slice:
#     condition_code = hour_data["weather"][0]["id"]
#     if int(condition_code) < 700:
#         will_rain = True.
for x in range(4):
    weather_id = weather_data["list"][x]["weather"][0]["id"]
    # print(weather)
    if weather_id < 700:
        will_rain = True
    weather_condition.append(weather_id)

# ☔

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today, Remember to bring an Umbrella",
        from_='+12055741799',
        to='+2347064938773'
    )
    print(message.status)
# print(condition)

# import os
# from twilio.rest import Client
#
#
# # Find your Account SID and Auth Token at twilio.com/console
# # and set the environment variables. See http://twil.io/secure
# account_sid = os.environ['TWILIO_ACCOUNT_SID'] AC3fded91ae307f2e8a163108ef2f2bb22
# auth_token = os.environ['TWILIO_AUTH_TOKEN'] adcb7e5e427aca53d46085b9b1eb4100
# client = Client(account_sid, auth_token)
#
# message = client.messages \
#                 .create(
#                      body="Join Earth's mightiest heroes. Like Kevin Bacon.",
#                      from_='+15017122661',
#                      to='+15558675310'
#                  )
#
# print(message.sid)
# set TWILIO_ACCOUNT_SID=AC3fded91ae307f2e8a163108ef2f2bb22
# set TWILIO_AUTH_TOKEN=adcb7e5e427aca53d46085b9b1eb4100


