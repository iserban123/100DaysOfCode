import requests
import datetime
from twilio.rest import Client
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
A_KEY1 = "LAQ1GEFVBJA2SSK5"
A_KEY2 = "2266437234e14234ae9ee69e8fa50b32"
account_sid = ""
auth_token = ""
## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
today = datetime.datetime.now()
y = today.date()
yesterday = str(y - datetime.timedelta(days=3))
twodaysago = str(y - datetime.timedelta(days=4))

Endpoint1 = "https://www.alphavantage.co/query"
Endpoint2 = "https://newsapi.org/v2/everything"

param1 = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK,
    "apikey" : A_KEY1,
    "outputsize": 2,
}

param2 = {
    #"function" : "TIME_SERIES_DAILY",
    "q" : "tesla",
    "apikey" : A_KEY2,
    "from" : y,
    "sortBy": "publishedAt"
}

r = requests.get(Endpoint1, params=param1)
n = requests.get(Endpoint2, params=param2)

data1low = float(r.json()["Time Series (Daily)"][yesterday]["3. low"])
data1hi = float(r.json()["Time Series (Daily)"][yesterday]["2. high"])

data2low = float(r.json()["Time Series (Daily)"][twodaysago]["3. low"])
data2hi = float(r.json()["Time Series (Daily)"][twodaysago]["2. high"])


if (data1hi * 0.02 < (data1hi - data1low)) or (data2hi * 0.02 < (data2hi - data2low)):
    lista = []
    diction = {}
    for x in range(0,3):
       news1 = n.json()["articles"][x]["title"]
       news2 = n.json()["articles"][x]["description"]
       print(news1, news2)
       diction.update({"title" : news1, "desc" : news2})
       lista.append(diction.copy())

    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body = f"{lista}",
        from_='+16074994596',
        to='+4915223386087'
    )

    print(message.status)




