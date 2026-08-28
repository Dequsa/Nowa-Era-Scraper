import requests
from bs4 import BeautifulSoup

'''
https://flipbook.nowaera.pl/dokumenty/Flipbook/NOWA_To_jest_chemia-Podrecznik_liceum_technikum%5Bkl_1%5D%5BZP%5D%5Bpr_2024%5D/files/mobile/14.jpg?200914095513
'''

class WebScraper:
    def __init__(self):
        self.base_url = 'https://flipbook.nowaera.pl/dokumenty/Flipbook/NOWA_To_jest_chemia-Podrecznik_liceum_technikum[kl_1][ZP][pr_2024]/files/mobile/'
        self.base_file = '.jpg?200914095513'
  

    def get_pages(self):
        MAX_PAGES = 50
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:154.0) Gecko/20100101 Firefox/154.0',
            'Accept': 'image/avif,image/webp,image/png,image/svg+xml,image/*;q=0.8,*/*;q=0.5',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br, zstd',
            'Connection': 'keep-alive',
            'Referer': 'https://flipbook.nowaera.pl/dokumenty/Flipbook/NOWA_To_jest_chemia-Podrecznik_liceum_technikum%5Bkl_1%5D%5BZP%5D%5Bpr_2024%5D/index.html',
            'Sec-Fetch-Dest': 'image',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Site': 'same-origin',
            'Priority': 'u=0, i',
            'TE': 'trailers',
        }
        for page_number in range(1, MAX_PAGES):
            url = self.base_url + page_number + base_file
            response = requests.get(url, headers=headers)
