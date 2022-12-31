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
       "function" : "TIME_SERIES_DAILY_ADJUSTED",
       "symbol": STOCK_NAME,
       "apikey":"Your ApiKey",
}


#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
response = requests.get(url=STOCK_ENDPOINT,params=Stock_Change)
print(response.json())
data = response.json()["Time Series (Daily)"]["2022-12-30"]
yesterday_data = [value for (key,value) in data.items() if value == data["4. close"]]

#TODO 2. - Get the day before yesterday's closing stock price
data = response.json()["Time Series (Daily)"]["2022-12-29"]
day_before_yesterday_data = [value for (key,value) in data.items() if value == data["4. close"]]

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

differences= abs(float(yesterday_data[0])-float(day_before_yesterday_data[0]))
up_down = None
if differences > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation

diff_percent = round((differences / float(day_before_yesterday_data[0]))*100)
if diff_percent > 1 :
       response = requests.get("https://newsapi.org/v2/everything?q=TSLA&from=2022-12-30&sortBy=popularity&apiKey=28f97ac1bd2f465d8cabe19c5dbd00d4")
       data  = response.json()['articles']
       three_articles = data[:3]
       #TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
       formatted_articles = [
              f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}"
              for article in three_articles
       ]

       # headlines = [data[i]["title"]for i,item in enumerate(data)]
       # description = [data[i]["description"]for i,item in enumerate(data)]

       #TODO 9. - Send each article as a separate message via Twilio.
       client = Client(account_sid, auth_token)
       message = client.messages \
              .create(
              body=formatted_articles,
              from_='+16086023128',
              to='+9779817071189'
       )
print(message.status)