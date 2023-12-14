import re
import urllib.request

user_input = str(input("PLACE WHERE YOU WANT TO KNOW ABOUT: "))

url = str(f"https://www.msn.com/en-in/weather/forecast/in-{user_input.lower()}") # url for webcrawler

raw_data = urllib.request.urlopen(url).read()

decoded_data = raw_data.decode("utf-8") # whole decoded css/html page for searching key words


search1 = re.search('<p class="summaryDescCompact-E1_1">',decoded_data) # search for required pattern
search2 = re.search('</p></div></div><div class="detailContainer', decoded_data)

final_result = decoded_data[search1.end():search2.start()]

print(f"WEATHER OF {user_input}: \n {final_result}")