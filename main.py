from bs4 import BeautifulSoup
import lxml
import smtplib
import requests


product_url = "https://www.amazon.in/dp/B01LF9EX1G/ref=nav_signin?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-14&pf_rd_r=6JHRYP96TB6G18FX9G95&pf_rd_t=101&pf_rd_p=3bc2337e-bc76-4407-9a47-5e23412c707b&pf_rd_i=1380072031&claim_type=EmailAddress&new_account=1&"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Accept-Language": "en-US,en;q=0.5"
}
response = requests.get(url=product_url, headers=headers)
data = response.text
# print(data)
soup = BeautifulSoup(data, "lxml")
price = soup.find(id="priceblock_ourprice").get_text().split()[1]
price_f = price.split(",")
total_price = float(price_f[0]+price_f[1])
# print(total_price)

BUY_PRICE = 12000.0
title = soup.find(id="productTitle").getText()

if total_price < BUY_PRICE:
    email_id = "sarahmatheww2000@gmail.com"
    password = "Sarah@123"
    message = f"{title} is now {total_price}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(email_id, password)
        connection.sendmail(from_addr=email_id, to_addrs="shobhaa24092001@gmail.com", msg=f"Subject:Amazon Price Alert\n\n{message}\n{product_url}")


