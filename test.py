import urllib.request
from bs4 import BeautifulSoup

if __name__ == "__main__":
    # Stack Overflow code: https://stackoverflow.com/questions/24153519/how-to-read-html-from-a-url-in-python-3
    fp = urllib.request.urlopen("https://www.uvm.edu/~rsingle/stat2510/F24/index.html")
    mybytes = fp.read()

    mystr = mybytes.decode("utf8")
    fp.close()

    # print(mystr)

    soup = BeautifulSoup(mystr, 'html.parser')


    links = soup.find_all('a')
    for link in links:
        print(link.get('href'))