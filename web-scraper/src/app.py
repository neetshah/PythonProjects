__author__ = 'shahn17'

import requests 
from bs4 import BeautifulSoup

request = requests.get("https://www.amazon.ca/Bluetooth-TaoTronics-Resistant-bluetooth-Microphone/dp/B00SYFNP28/ref=gbps_img_s-3_aa60_6364ef0a?smid=A21BN97ZLZ79FQ&pf_rd_p=b013a60b-0b5a-4a66-8ff5-66b6cedeaa60&pf_rd_s=slot-3&pf_rd_t=701&pf_rd_i=gb_main&pf_rd_m=A3DWYIK6Y9EEQB&pf_rd_r=F8DS4MD2MZ2AB2JH7ABK")
content = request.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("span", {"id": "priceblock_dealprice", "class": "a-size-medium a-color-price"})
price = element.text.strip()
#<span id="priceblock_dealprice" class="a-size-medium a-color-price">CDN$ 19.99</span>

print("The price of the item is "+ price)