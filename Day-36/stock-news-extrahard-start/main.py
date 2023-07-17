import requests
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

api_key_alpha_advantage = "WXEDY5OHIAP7HS5V"
api_key_newsapi = "b15bef1b905745a5bf7303301eaa1da3"





#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file 
by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the 
coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file 
by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the 
coronavirus market crash.
"""

parameters = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": "TSLA",
    "apikey": "WXEDY5OHIAP7HS5V"
}

news_parameters = {
    "q": "tsla",
    "apiKey": "b15bef1b905745a5bf7303301eaa1da3"
}
tsla_response = requests.get("https://www.alphavantage.co/query", params=parameters)
tsla_response.raise_for_status()
tsla_data = tsla_response.json()
# # print(tsla_data)
# # https://newsapi.org/v2/everything?q=tsla&apiKey=b15bef1b905745a5bf7303301eaa1da3
#
news_tesla_response = requests.get("https://newsapi.org/v2/everything", params= news_parameters)
news_tesla_response.raise_for_status()
news_data = news_tesla_response.json()
# print(news_data)

yesterday = float(tsla_data["Time Series (Daily)"]["2023-07-14"]["4. close"])
day_before_yesterday = float(tsla_data["Time Series (Daily)"]["2023-07-13"]["4. close"])
# print(data, data2)

first_tesla_title = news_data["articles"][0]["title"]
first_tesla_description = news_data["articles"][0]["description"]
second_tesla_title = news_data["articles"][1]["title"]
second_tesla_description = news_data["articles"][1]["description"]
third_tesla_title = news_data["articles"][2]["title"]
third_tesla_description = news_data["articles"][2]["description"]


# print(tesla_news)


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.

percentage = 100 * (yesterday - day_before_yesterday) / day_before_yesterday
final_percentage = '{:,.2f}'.format(abs(percentage))

for news_index in range(3):
    if percentage >= 1:
        print("Get News")
        print(f""""{STOCK}: 🔺{final_percentage}%
        Headline: {news_data["articles"][news_index]["title"]}
        Brief: {news_data["articles"][news_index]["description"]}""")
    else:
        print(f""""{STOCK}: 🔻{final_percentage}%
            Headline: {news_data["articles"][news_index]["title"]}
            Brief: {news_data["articles"][news_index]["description"]}""")

