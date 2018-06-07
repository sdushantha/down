#!/usr/bin/env python3

import sys
import requests

good = "\033[92m✔\033[0m"
bad = "\033[91m✘\033[0m"

# Header is needed for some sites or else they will think
# that a bot is accessing the site wont return 200
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0'}

def show_help():
    help_message = """
    Usage: python3 down.py [file] [url]

    Example
      python3 down.py url_list.txt
      python3 down.py https://www.example.com
    """

    print(help_message)
    sys.exit()

def printStatus(up, site):
    good = "\033[92m✔\033[0m"
    bad = "\033[91m✘\033[0m"
    print("{}   {}".format(good if up else bad, site))


def _file(file):
    try:
        with open(file, "r") as f:
            for site in f:
                site = site.strip()
                _url(site)
    except FileNotFoundError:
        print("No such file: " + file)

def _url(site):
    try:
        r = requests.get(site)
        if r.status_code != 200:
            printStatus(False, site)
        else:
            printStatus(True, site)
    except:
        printStatus(False, site)
        
if len(sys.argv) == 1 or sys.argv[1] == "-h":
    show_help()

# Checking if url or file    
if sys.argv[1].startswith("http"):
    _url(sys.argv[1])
    sys.exit()

_file(sys.argv[1])

