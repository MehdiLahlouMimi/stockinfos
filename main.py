"""
An international stock price seeker
author : @Crun 
"""


#importement
from bs4 import BeautifulSoup as bs 
import requests, colorama

#modules initialisation
colorama.init()



#colorama codes 
reset = '\033[39m'
green = "\033[92m"
red = '\033[31m'


#functions
def search_and_give_price(stock) :
	"""
	A simple function to get and give the price of a stock
	"""

	root = "https://www.boursorama.com/cours/"        #the common root of all the links
	searching_link = root + stock                     #particular link

	page = requests.get(searching_link)
	soup = bs(page.content, 'html.parser')            #html elements

	price = soup.find("span", class_ = "c-instrument c-instrument--last")                       #the price element

	return price.text


def search_and_give_variation(stock) :
	"""
	A simple function to get and give the variation of a stock
	"""

	root = "https://www.boursorama.com/cours/"        #the common root of all the links
	searching_link = root + stock                     #particular link

	page = requests.get(searching_link)
	soup = bs(page.content, 'html.parser')            #html elements

	last_variation = soup.find("span", class_ = "c-instrument c-instrument--variation")         #the last variation element

	return last_variation.text


def search_and_give_name(stock) : 
	"""
	A simple function to get and give the company's name of a stock
	"""

	root = "https://www.boursorama.com/cours/"        #the common root of all the links
	searching_link = root + stock                     #particular link

	page = requests.get(searching_link)
	soup = bs(page.content, 'html.parser')            #html elements

	last_variation = soup.find("a", class_ = "c-faceplate__company-link")                      #the name

	return last_variation.text



def main() : 
	"""
	Main function
	"""
	wanted_stock = input("What is the name of the stock you wanna gather informations about ? : ")          #taking the user's input

	print("Gathering data about {0}\n".format(wanted_stock))

	try : 

		wanted_stock_name = search_and_give_name(wanted_stock)                                              #its name
		wanted_stock_price = search_and_give_price(wanted_stock)                                            #its price
		wanted_stock_variation = search_and_give_variation(wanted_stock)                                    #its last variation  

			#the output
		print(wanted_stock_name)
		print(wanted_stock_price) 

		if wanted_stock_variation[0] == "+" :                                     #color signal of raise of lower
			print(green + f" {wanted_stock_variation}" + reset)

		else : 
			print(red + f" {wanted_stock_variation}" + reset)

	

	except AttributeError :                      #if the stock does not exist
		print("{} does not exist".format(wanted_stock))

	


	input("\nPress ENTER to see another stock ")                #to let time to the user to see the informations


#program
	#START
while True :                            
	print(colorama.ansi.clear_screen())
	main()
	#END	