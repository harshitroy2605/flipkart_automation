import requests
import bs4
import time
import tkinter
from tkinter import messagebox


while True :
	pixel= requests.get("https://www.flipkart.com/google-pixel-4a-just-black-128-gb/p/itm023b9677aa45d")
	soup=bs4.BeautifulSoup(pixel.text,'lxml')
	price=soup.find("",{"class":'_1vC4OE _3qQ9m1'})
	prices=[]
	prices.append(price.text)
	actual_price=prices[0]
	actual_price=actual_price[1:3]+actual_price[4:7]
	price=int(actual_price)
	time.sleep(10)
	if price<29000:
		tkinter.messagebox.showinfo(title="hello",message="buy buy buy ")

	elif price>29000:
		tkinter.messagebox.showinfo(title="hello",message="buy not buy not buy ")
