from urllib.request import urlopen

import sys


def fetch_words(url):
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf8').split()
            for word in line_words:
                story_words.append(word)
    return story_words

def print_items(items):
    for item in items:
        print(item)

def main(url):
    words = fetch_words(url)
    print_items(words)

'''
__name__ evaulates differently when importing vs running your .py file as a executable script.
As an executable script, it evaulates to __main__
Whereas, when importing, __name__ evaulates to the module name which is words in this case
'''
if __name__ == "__main__":
    url = sys.argv[1]
    main(url)

