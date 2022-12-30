import requests
import os
from twilio.rest import Client
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"


account_sid =os.environ.get("ACCOUNT_SID")
auth_token =os.environ.get("AUTH_TOKEN")

client = Client(account_sid, auth_token)
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
Stock_Change = {
       "function" : "FX_DAILY",
       "from_symbol": "EUR",
       "to_symbol":"USD",
       "apikey":"3FYOQQHQA9KPXXML",
}

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
response = requests.get(url=STOCK_ENDPOINT,params=Stock_Change)
data = response.json()["Time Series FX (Daily)"]["2022-12-29"]
data_list_1 = [value for (key,value) in data.items() if value == data["4. close"]]
print(data_list_1)
#TODO 2. - Get the day before yesterday's closing stock price
data = response.json()["Time Series FX (Daily)"]["2022-12-28"]
data_list_2 = [value for (key,value) in data.items() if value == data["4. close"]]
print(data_list_2)
#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
differences= abs(float(data_list_1[0])-float(data_list_2[0]))

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
percentage = differences / float(data_list_2[0])
#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation

if percentage <= 1 or percentage >=1:
       response = requests.get("https://newsapi.org/v2/everything?q=TSLA&from=2022-12-30&sortBy=popularity&apiKey=28f97ac1bd2f465d8cabe19c5dbd00d4")
       data  = response.json()['articles'][0:3]

       #TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
       headlines = [data[i]["title"]for i,item in enumerate(data)]
       description = [data[i]["description"]for i,item in enumerate(data)]
       #TODO 9. - Send each article as a separate message via Twilio.
       client = Client(account_sid, auth_token)
       message = client.messages \
              .create(
              body=f"TSLA:🔺%{percentage}\nHeadline: {headlines}\nBrief: {description}",
              from_='+16086023128',
              to='+9779817071189'
       )
print(message.status)

#Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

