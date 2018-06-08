#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import requests

good = "\033[92m✔\033[0m"
bad = "\033[91m✘\033[0m"

# Header is needed for some sites or else they will think
# that a bot is accessing the site wont return 200
headers = {
    'User-Agent':
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) '
        'Gecko/20100101 Firefox/55.0'
    }


def show_help():
    """
    Show the help message
    """

    help_message = """
    Usage: python3 down.py [file] [url]

    Example
      python3 down.py url_list.txt
      python3 down.py https://www.example.com
    """

    sys.stdout.write(help_message)
    sys.exit()


def print_status(up, site):
    """
    Print the status of the site to stdout
    :param up: Is the site up? True or False
    :type up: bool
    :param site: The site URL
    :type site: str
    """

    sys.stdout.write("{}   {}\n".format(good if up else bad, site))


def _file(file):
    """
    Check if file exists

    :param file: The path to the file
    :type file: str
    """
    try:
        with open(file, "r") as f:
            for site in f:
                site = site.strip()
                _url(site)
    except FileNotFoundError:
        sys.stdout.write("No such file: {}".format(file))


def _url(site):
    """
    Check if site is up
    :param site: The url of the site
    :type site: str
    """
    try:
        r = requests.get(site)
        if r.status_code != 200:
            print_status(False, site)
        else:
            print_status(True, site)
    except requests.ConnectionError:
        print_status(False, site)


if len(sys.argv) == 1 or sys.argv[1] == "-h":
    show_help()

# Checking if url or file    
if sys.argv[1].startswith("http"):
    _url(sys.argv[1])
    sys.exit()

_file(sys.argv[1])
