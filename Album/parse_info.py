from bs4 import BeautifulSoup 
import requests 
import re
import csv 

def parse_info(soup, artist):

	dictionary_list = []


	pattern_adjective_album = re.compile("(\\w+)(\\s\\balbum)")
	pattern_studio = re.compile("(?i)studio")
	pattern_boxset = re.compile("(?i)box")    
	pattern_EP = re.compile("(?i)play")  
	pattern_mixtape = re.compile("(?i)mixtape") 
	pattern_soundtrack = re.compile("(?i)sound") 
	pattern_collab = re.compile("(?i)collab")
	pattern_compilation = re.compile("(?i)compil")
	pattern_remix = re.compile("(?i)remix")
	pattern_video = re.compile("(?i)video")
	pattern_other = re.compile("(?i)other")
	pattern_cover = re.compile("(?i)cover")
	pattern_tribute = re.compile("(?i)tribute")
	pattern_posthumous = re.compile("(?i)posthum")
	pattern_live = re.compile("(?i)live")

	common_pattern_list = []
	common_pattern_list.extend([pattern_posthumous, pattern_tribute,
		pattern_collab, pattern_cover, pattern_compilation, pattern_other,
		pattern_video, pattern_remix, pattern_boxset, pattern_EP, 
		pattern_soundtrack, pattern_mixtape, pattern_studio, 
		pattern_live])

	for div in soup.find_all("div", class_ ="navbox"):
		try:
			for tr in div.table.tbody.find_all("tr"):
				try:	
					if re.search(pattern_adjective_album, tr.th.text):
						for li in tr.td.div.ul.find_all("li"):
							dictionary = {"Artist": artist, "Album": "", "Type": ""}
							if re.search(pattern_collab, tr.th.text): 
								dictionary["Type"] = "Collaboration" 
							elif is_not_common_type(tr.th.text):
								dictionary["Type"] = "Other"
							elif re.search(re.compile("(?i)under"), tr.th.text) or re.search(re.compile("(?i)music"), tr.th.text):
								continue
							else:
								dictionary["Type"] = re.search(pattern_adjective_album, tr.th.text).group(1).title()
							try:
								dictionary["Album"] = li.i.b.text
								dictionary_list.append(dictionary)
							except Exception as wrongformat:
								try:
									dictionary["Album"] = li.a.text
									dictionary_list.append(dictionary)
								except Exception as wrongformat:
									continue

					if re.search(pattern_compilation, tr.th.text) and not re.search(
						pattern_adjective_album, tr.th.text):
						for li in tr.td.div.ul.find_all("li"):
							dictionary = {"Artist": artist, "Album": "", "Type": ""}
							dictionary["Type"] = "Compilation"
							try:
								dictionary["Album"] = li.i.b.text
								dictionary_list.append(dictionary)
							except Exception as wrongformat:
								try:
									dictionary["Album"] = li.a.text
									dictionary_list.append(dictionary)
								except Exception as wrongformat:
									continue

					if re.search(pattern_boxset, tr.th.text) and not re.search(
						pattern_adjective_album, tr.th.text):
						for li in tr.td.div.ul.find_all("li"):
							dictionary = {"Artist": artist, "Album": "", "Type": ""}
							dictionary["Type"] = "Box set"
							try:
								dictionary["Album"] = li.i.b.text
								dictionary_list.append(dictionary)
							except Exception as wrongformat:
								try:
									dictionary["Album"] = li.a.text
									dictionary_list.append(dictionary)
								except Exception as wrongformat:
									continue	

					if re.search(pattern_EP, tr.th.text) and not re.search(
						pattern_adjective_album, tr.th.text):
						for li in tr.td.div.ul.find_all("li"):
							dictionary = {"Artist": artist, "Album": "", "Type": ""}
							dictionary["Type"] = "Extended Play"
							try:
								dictionary["Album"] = li.i.b.text
								dictionary_list.append(dictionary)
							except Exception as wrongformat:
								try:
									dictionary["Album"] = li.a.text
									dictionary_list.append(dictionary)
								except Exception as wrongformat:
									continue	
					
					if re.search(pattern_mixtape, tr.th.text) and not re.search(
						pattern_adjective_album, tr.th.text):
						for li in tr.td.div.ul.find_all("li"):
							dictionary = {"Artist": artist, "Album": "", "Type": ""}
							dictionary["Type"] = "Mixtape"
							try:
								dictionary["Album"] = li.i.b.text
								dictionary_list.append(dictionary)
							except Exception as wrongformat:
								try:
									dictionary["Album"] = li.a.text
									dictionary_list.append(dictionary)
								except Exception as wrongformat:
									continue

					if re.search(pattern_collab, tr.th.text) and not re.search(
						pattern_adjective_album, tr.th.text):
						for li in tr.td.div.ul.find_all("li"):
							dictionary = {"Artist": artist, "Album": "", "Type": ""}
							dictionary["Type"] = "Collaboration"
							try:
								dictionary["Album"] = li.i.b.text
								dictionary_list.append(dictionary)
							except Exception as wrongformat:
								try:
									dictionary["Album"] = li.a.text
									dictionary_list.append(dictionary)
								except Exception as wrongformat:
									continue

					if re.search(pattern_soundtrack, tr.th.text) and not re.search(
						pattern_adjective_album, tr.th.text):
						for li in tr.td.div.ul.find_all("li"):
							dictionary = {"Artist": artist, "Album": "", "Type": ""}
							dictionary["Type"] = "Soundtrack"
							try:
								dictionary["Album"] = li.i.b.text
								dictionary_list.append(dictionary)
							except Exception as wrongformat:
								try:
									dictionary["Album"] = li.a.text
									dictionary_list.append(dictionary)
								except Exception as wrongformat:
									continue

					if re.search(pattern_remix, tr.th.text) and not re.search(
						pattern_adjective_album, tr.th.text):
						for li in tr.td.div.ul.find_all("li"):
							dictionary = {"Artist": artist, "Album": "", "Type": ""}
							dictionary["Type"] = "Remix"
							try:
								dictionary["Album"] = li.i.b.text
								dictionary_list.append(dictionary)
							except Exception as wrongformat:
								try:
									dictionary["Album"] = li.a.text
									dictionary_list.append(dictionary)
								except Exception as wrongformat:
									continue	

					def is_not_common_type(album_type):
						for pattern in common_pattern_list:
							if re.search(pattern, album_type):
								return False
						return True			

				except Exception as wrongformat:
					continue 
		except Exception as wrongformat:
			continue		
	return dictionary_list






