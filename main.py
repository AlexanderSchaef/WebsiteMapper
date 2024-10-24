"""
Main Idea:
From a link to a webpage, make a tree for every folder for that website that can be found.


"""

import csv
from lxml import html
import requests
from urllib.parse import urljoin


def get_links_from_html(url_):
    """
        Grabs all a href links from an html/xml page

        Parameters:
        url_ (string): Some url (needs to be a valid html/xml page and searchable)

        Returns:
        Array[string] links_: All links on the page as a list of strings of those hyperlink destinations

    """
    response = requests.get(url_)
    tree = html.fromstring(response.content)
    links_ = tree.xpath('//a/@href')
    return links_
    #return convert_to_absolute_path(links_)


def convert_to_absolute_path(base_url, relative_urls):
    return 0
    


if __name__ == '__main__':
    
    # Start up block for first time run

    # Arbitrary file input
    with open("start_location.txt") as source:
        url = source.read()
    
    # find all links on the current page
    links = get_links_from_html(url)
    
    print(f"URL: {url}")

    relations = []
    with open("file_relations.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            relations.append(row)
    
    # stored all rows in csvfile into variable relations
    print("READ COMPLETED") 
    
    # Start appended to file those hyperlinks that are not currently in the file
    num_writes = 0
    with open("file_relations.csv", "a") as csvfile:
        for link in links:
            for row in relations:
                if row[0] != url and row[1] != link:
                    csvfile.write(f"\"{url}\",\"{link}\"\n")
                    num_writes += 1
                else:
                    print(f"({url},{link}) already in file")
