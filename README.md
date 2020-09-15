# UMGwebscrape
Webscrape of all Universal Music Group artists' albums and their classifications (Live, Studio, EP, Compilation, Other) Done with Python libraries 
Beautiful Soup, Requests, RegEx, CSV

The EDA is done with Pandas in jupyter notebooks. The scraped data is cleaned, explored, and exported in the ipython notebooks. 

The code starts with a request to one wiki page with all Universal Music  Group Artists. I use this page to create a list of all artists' wiki pages and then 
my code goes through each page and scrapes the bottom of the page Albums box (HTML). I hard coded it so it is ugly and long, but the result is some beatiful big data 
crowdsourced for us by Wikipedia pages. Don't worry I did try to find a HTTP request that did this and there wasn't one!!

artist_list_to_link_list.py - request to original Wiki page with all artists, 
  parse_info.py - scrape data, 
     csv_writer.py - write to CSV

