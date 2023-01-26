import requests
import smtplib
from bs4 import BeautifulSoup
headers = {
    "Accept-Language":"en-US,en;q=0.9",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.61"
}
response = requests.get(url="https://www.amazon.com/Windows-Desktop-Computer-Intel-Gemini/dp/B09VXG2FGP/ref=sr_1_2?crid=D7K1CTZQBSH1&keywords=mini%2Bpc&qid=1674732613&sprefix=mini%2Bp%2Caps%2C437&sr=8-2&th=1",
                        headers=headers)
website = response.text

soup = BeautifulSoup(website,"html.parser")
price = soup.find(name="span",class_="a-offscreen").text
price = price.split("$")[1]
name =  soup.find(id="productTitle").text
print(name)
print(price)
if  float(price) < 129.99:
    connection = smtplib.SMTP("smtp.gmail.com.",port=587)
    connection.starttls()
    connection.login("testperpose56@gmail.com","difxmcqvovolbafy")
    connection.sendmail(from_addr="testperpose56@gmail.com",
                        to_addrs="testperpose56@gmail.com",
                        msg=f"Subject:Amazon Price Alert\n\n{name}is now ${price}.")
    connection.quit()

