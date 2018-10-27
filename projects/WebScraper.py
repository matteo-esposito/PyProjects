#-----------------------------------------------------------------------#
# 						Fall 2018 | Web Scraper      					#
#																		#
# Objectives: 															#
#	Find = [rent price, location, length of post, bed/bath, footprint]	#
#	Site = duproprio.com												#
#-----------------------------------------------------------------------#

# Libraries
import requests
from bs4 import BeautifulSoup
from csv import writer

# Duproprio scrape setup
response = requests.get("https://duproprio.com/fr/rechercher/liste?search=true&is_for_sale=1&with_builders=1&parent=1&pageNumber=1&sort=-published_at")
soup = BeautifulSoup(response.text, "html.parser")
container = soup.find(class_="container")
posting_list = container.find(class_="search-results-listings-list")

# List of postings
posting_elements = posting_list.find_all(class_="search-results-listings-list__item")

# "Open" csv to start writing scraped data
with open("housing_data.csv", "w") as csv_file:
	csv_writer = writer(csv_file)
	csv_writer.writerow(["Rent Price", "Location", "# Bed", "# Bath", "Footprint", "Length of Post"])

	for posting in posting_elements:
		# Prices
		posting_price_elem = posting.find(class_="search-results-listings-list__item-description__price")													
		# Location
		location_elem = posting.find(class_="search-results-listings-list__item-description__item search-results-listings-list__item-description__city")	
		# Number of beds
		#bed_elem = 
		# Number of baths
		#bath_elem = 

		if posting_price_elem is not None:
			price_val = posting_price_elem.find("h2").text	

		if location_elem is not None:
			location_val = posting_price_elem.find("span",class_='').text
			print(location_val)
	
		# 	# Write to csv file
		# 	csv_writer.writerow([price_val,location_val])

