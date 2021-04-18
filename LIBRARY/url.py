import urllib
import webbrowser
weburl = urllib.request.urlopen('https://github.com/vanshika0111/python')
html = weburl.read()
data = weburl.getcode()
url = weburl.geturl()
hd = weburl.headers
inf = weburl.info()
print("The url is", url)
print("HTTP status code is: ",data)
print("headers returned \n",hd)
print("The info() returned: \n", inf)
print("Now opening the url",url)
webbrowser.open_new(url)