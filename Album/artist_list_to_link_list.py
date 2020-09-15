from bs4 import BeautifulSoup 
import requests 
import re 


source = requests.get("https://en.wikipedia.org/wiki/List_of_Universal_Music_Group_artists").text
soup = BeautifulSoup(source, "lxml")

artist_blocks = soup.find_all("div", class_ ="div-col columns column-width")
artist_list = []
wikilink_list = []



for block in artist_blocks:
	for artist in block.ul.find_all("li"):
		name = artist.text
		#remove words in parentheses and brackets
		name = re.sub("[\(\[].*?[\)\]]", "", name)
		name = name.rstrip()
		artist_list.append(name)
		name = name.replace(" ", "_")
		link = "https://en.wikipedia.org/wiki/" + name 
		wikilink_list.append(link)

artist_link_dictionary = dict(zip(artist_list, wikilink_list))






		

