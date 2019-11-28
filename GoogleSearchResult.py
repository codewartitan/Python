from googlesearch import search
dataset='planning Commission'+'CHEROKEE'+'ga'+'US'

for url in search(dataset, tld='com', stop=5):
    print(url)
