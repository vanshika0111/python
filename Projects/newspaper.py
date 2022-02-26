# news api usage

import requests
import json

def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__ == '__main__':
    speak("News for today")
    url = "https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=8a2b514bf45d4c60b7cbfb36cdbc2f7e"
    news = requests.get(url).text
    news = json.loads(news)
    # print(news["status"])
    print(news["articles"])
    articles = news['articles']
    for article in articles:
        speak(article['title']) 
        speak("Moving on to the next news.")
    speak("Thanks for listening.")