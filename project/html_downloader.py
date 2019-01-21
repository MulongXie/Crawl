import urllib.request as ur
from urllib.parse import quote
import string

class Downloader:

    def download(self, url):
        if url is None:
            return
        response = ur.urlopen(quote(url, safe=string.printable))
        if response.getcode() != 200:
            print('No response')
            return
        return response.read()
