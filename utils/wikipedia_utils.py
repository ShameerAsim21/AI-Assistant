import wikipedia

def wikipedia_search(query):
    try:
        page = wikipedia.page(query, auto_suggest=True)
        summary = wikipedia.summary(query, sentences=4)
        url = page.url
        return page, f"**{page.title}**\n\n{summary}\n\n[Read more on Wikipedia]({url})"
    except:
        return None, "Sorry, I couldn't find any information on that."
