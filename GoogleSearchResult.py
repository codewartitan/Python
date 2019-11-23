from googlesearch import search

for url in search('planning commission ga FULTON US', tld='com', stop=1):
    print(url)
