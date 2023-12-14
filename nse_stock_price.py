import re
import urllib.request

user_search = str(input("WHICH STOCK PRICE YOU WANT TO KNOW: "))
url = f'https://www.google.com/finance/quote/{user_search.replace(" ","")}:NSE' #only Indian company and removing space
data = urllib.request.urlopen(url).read()
data = data.decode("utf-8")

string = re.search('<div class="YMlKec fxKbKc">', data)
end = string.end() + 15

final_string = data[string.end():end]

end2 = re.search("</div>", final_string)

final_string2 = final_string[:end2.start()]
print(final_string2)