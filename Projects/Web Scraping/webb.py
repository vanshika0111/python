# pip install requests
# pip install bs4

import requests
from bs4  import BeautifulSoup as bs

GitHubUser = input("Enter GitHub username: ")
# url = 'https://github.com/'+GitHubUser
url =  'https://github.com/vanshika0111'
req = requests.get(url)
print(req)
beautify = bs(req.content, 'html.parser')
ProfileImage = beautify.find('img')['src']
print(ProfileImage) 