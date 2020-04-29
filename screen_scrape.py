import requests
import urllib.request
import time
from bs4 import BeautifulSoup


url = 'http://web.mta.info/developers/turnstile.html'
response = requests.get(url)
# print(response.text)
# print(response)

soup = BeautifulSoup(response.text, 'html.parser')

#a_tags = soup.findAll('a')
# link = one_a_tag['href']
#print(a_tags[37])

for each_tag in soup.findAll('a')[36:47]: # using the findAll method on tmy soup object
    link = each_tag['href'] # since this is an objet, there are different defined attributes, href is one of them
    download_url = 'http://web.mta.info/developers/'+ link # concatenating the base url plus each individual file path (link)
    file_name = link.find('ile/') + 4 # I am looking for th efirst occurance of tehse letters whcih rerutns the index for the first letter, then I add 4
    file_name_path = '/Users/lingle/downloads/'+ link[file_name: ] #file_name contsins the index to start at)
    urllib.request.urlretrieve(download_url, filename=file_name_path)
    time.sleep(1)
    
    
