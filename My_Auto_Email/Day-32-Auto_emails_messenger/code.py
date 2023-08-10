import pandas
from datetime import datetime
import smtplib
import time
import os
MY_EMAIL = os.environ["MY_EMAIL"]
MY_PASSWORD = os.environ["MY_PASSWORD"]

today = datetime.now()
present_day = today.weekday()
sent = 0

data = pandas.read_csv("../../../birthdays.csv")
for (index, data_row) in data.iterrows():
    if present_day == 0:
        file_path = f"letter_templates/letter_2.txt"
        with open(file_path) as letter_file:
            contents = letter_file.read()
            letter = contents.replace("[NAME]", data_row["name"])
            letter2 = letter.replace("[gender]", data_row["gender"])
            # letter3 = letter2.replace("[emoji]", "🌹")
        # print(letter2)
        # with smtplib.SMTP("smtp.gmail.com") as connection:
        #     connection.starttls()
        #     connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        #     connection.sendmail(from_addr=MY_EMAIL,
        #                         to_addrs=data_row["email"],
        #                         msg=f"Subject:Monday Roses  for you {data_row['name']}\n\n"
        #                             f"{letter2}".encode("utf-8"),
        #                         )
        # with smtplib.SMTP("smtp.gmail.com") as connection:
        #     connection.starttls()
        #     connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        #     connection.sendmail(from_addr=MY_EMAIL,
        #                         to_addrs=data_row["email"],
        #                         msg=f"Subject:Monday situationship report 😊 for you {data_row['name']}\n\n"
        #                             f"{letter2}".encode("utf-8"),
        #                         )
        sent += 1
        print(f"{sent}. {data_row['name']} done")
        # time.sleep(3)
# if present_day == 6:
#     file_path = f"letter_templates/letter_3.txt"
#     with open(file_path) as letter_file:
#         contents = letter_file.read()
#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(user=MY_EMAIL, password=MY_PASSWORD)
#         connection.sendmail(from_addr=MY_EMAIL,
#                             to_addrs="ezertobi@gmail.com",
#                             msg=f"Subject:Hello Ezer\n\n{contents}",
#                             )
#     print(contents)
