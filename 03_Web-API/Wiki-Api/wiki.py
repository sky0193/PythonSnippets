#https://www.thepythoncode.com/article/access-wikipedia-python

import wikipedia
import argparse
import csv

language = "de"
wikipedia.set_lang(language)
MAXIMUM_OPTIONS = 5

term="Schnittstelle"

def get_summary(term):
    wiki_term_summary = {}

    try:
       summary = wikipedia.summary(term, auto_suggest=False)
       wiki_term_summary[term] = summary
    except wikipedia.DisambiguationError as e:
            options_counter = 0
            for option in e.options:
                if(options_counter < MAXIMUM_OPTIONS):
                    options_counter = options_counter + 1
                    summary = wikipedia.summary(option, auto_suggest=False)
                    wiki_term_summary[option] = summary

    with open('Names.csv', 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        for key, value in wiki_term_summary.items():
            writer.writerow([term, key, value])


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("terms_path", metavar='terms',
                        help="path for terms in txt")
    get_summary(term)
    