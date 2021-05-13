import urllib
import requests

def book_to_words(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    booktxt = urllib.request.urlopen(book_url).read().decode()
    bookascii = booktxt.encode('ascii','replace')
    return bookascii.split()

def radix_a_book(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    a1 = book_to_words(book_url)
    mcapacity = len(max(a1, key=len))
    
    for x in range(mcapacity):
        a1 = presort(a1, x, mcapacity - 1)
    
    return a1

def presort(book, idx, max):
    ret = [0 for x in range(len(book))]
    count = [0 for x in range(128)]

    for word in book:
        if max - idx < len(word):
            count[word[max - idx]] += 1
        else:
            count[0] += 1
    
    for x in range(128):
        count[x] += count[x-1]

    for x in range(len(book) -1, -1, -1):
        if max - idx < len(book[x]):
            ret[count[book[x][max - idx]] - 1] = book[x]
            count[book[x][max - idx]] -= 1
        else:
            ret[count[0] - 1] = book[x]
            count[0] -= 1
    
    return ret
