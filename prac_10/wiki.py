"""
CP1404/CP5632
Mason McKenzie
"""

import wikipedia

search_phrase = input("Search phrase: ")
while search_phrase != "":
    try:
        page = wikipedia.page(search_phrase, auto_suggest=False)
        print(page.title)
        print(page.summary)
        print(page.url)
    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)
    search_phrase = input("Page title/search phrase: ")

