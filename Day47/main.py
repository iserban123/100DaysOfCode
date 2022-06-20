#http://myhttpheader.com/
import requests
from bs4 import BeautifulSoup
import lxml
import smtplib
import os

YOUR_EMAIL = os.environ.get("YOUR_EMAIL")
YOUR_PASSWORD = os.environ.get("YOUR_PASSWORD")
url = "https://www.amazon.com/dp/B09Q5YQ863/ref=sbl_dpx_kitchen-electric-cookware_B08GC6PL3D_0"
head = {
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36",
  "Accept-Language": "en-US,en;q=0.9,ro;q=0.8,de;q=0.7,it;q=0.6,es;q=0.5",
}

response = requests.get(url=url, headers=head)
answer = response.text
soup = BeautifulSoup(answer, "lxml")
#print(soup.prettify())
price = soup.find(class_="a-offscreen").getText()
nprice = float(price.split("$")[1])
print(nprice)

BUY_PRICE = 200

if nprice < BUY_PRICE:
    message = f" is now {nprice}"

    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        connection.starttls()
        result = connection.login(YOUR_EMAIL, YOUR_PASSWORD)
        connection.sendmail(
            from_addr=YOUR_EMAIL,
            to_addrs=YOUR_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"
        )
