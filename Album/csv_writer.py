from artist_list_to_link_list import artist_link_dictionary
from parse_info import parse_info
from bs4 import BeautifulSoup 
import requests 
import re
import csv

csv_columns = ["Artist", "Album", "Type"]

csv_file = "album_classifications.csv"
with open(csv_file, 'w') as csvfile:
	writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
	writer.writeheader()



for artist, wikilink in artist_link_dictionary.items():
	request = requests.get(wikilink)
	soup = BeautifulSoup(request._content, "lxml")
	dict_data = parse_info(soup, artist)
	with open(csv_file, "a") as csvappend:
		writer = csv.DictWriter(csvappend, fieldnames = csv_columns)	
		for data in dict_data:
			writer.writerow(data)

	

