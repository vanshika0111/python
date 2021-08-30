# coroutines

def searcher():
    import time
    book = "moral scape"
    time.sleep(4)

    while True:
        text = (yield)
        if text in book:
            print("Text in the book")
        else:
            print("Text not in the book")

search = searcher()   # coroutine created
print("Search started")
next(search)
print("Searching for next round")
search.send("moral")
input("Press any key")
search.send("moral solace")
input("Press any key")
search.send("hello")
search.close()