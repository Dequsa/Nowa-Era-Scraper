import requests
from pathlib import Path

"""
https://flipbook.nowaera.pl/dokumenty/Flipbook/NOWA_To_jest_chemia-Podrecznik_liceum_technikum%5Bkl_1%5D%5BZP%5D%5Bpr_2024%5D/files/mobile/14.jpg?200914095513
https://flipbook.nowaera.pl/dokumenty/Flipbook/NOWE_Odkryc_fizyke-Podrecznik_liceum_technikum\[kl_1\]\[ZP\]\[pr_2024\]/files/mobile/1.jpg?200914095513
https://flipbook.nowaera.pl/dokumenty/Flipbook/NOWE_Oblicza_geografii-Podrecznik_liceum_technikum%5Bkl_1%5D%5BZP%5D%5Bpr_2024%5D/files/mobile/5.jpg?200914095513
"""

BOOK_TYPES = {
    "Chemia_1": "NOWA_To_jest_chemia-Podrecznik_liceum_technikum",
    "Fizyka_1": "NOWE_Odkryc_fizyke-Podrecznik_liceum_technikum",
    "Geografia_1": "NOWE_Oblicza_geografii-Podrecznik_liceum_technikum",
}

SPECIAL_BOOKS = {
    "Matmetyka_1_R": "",
}


class WebScraper:
    def __init__(self, book_type: str, base_file=None):
        self.book_type = book_type
        self.base_url = f"https://flipbook.nowaera.pl/dokumenty/Flipbook/{BOOK_TYPES[self.book_type]}[kl_1][ZP][pr_2024]/files/mobile/"

        if base_file is None:
            self.base_file = ".jpg?200914095513"
        else:
            self.base_file = base_file

    def get_pages(self):
        MAX_PAGES = 500
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:154.0) Gecko/20100101 Firefox/154.0",
            "Accept": "image/avif,image/webp,image/png,image/svg+xml,image/*;q=0.8,*/*;q=0.5",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Connection": "keep-alive",
            "Sec-Fetch-Dest": "image",
            "Sec-Fetch-Mode": "no-cors",
            "Sec-Fetch-Site": "same-origin",
            "Priority": "u=0, i",
            "TE": "trailers",
        }
        TIMEOUT = 2
        print()
        print(f">>> Currnet book: {self.book_type}")
        current_dir = f"books/{self.book_type}"
        Path(current_dir).mkdir(parents=True, exist_ok=True)

        for page_number in range(1, MAX_PAGES):
            url = self.base_url + str(page_number) + self.base_file
            try:
                print(f"> Current page: {page_number}")
                response = requests.get(url, headers=headers, timeout=TIMEOUT)
                response.raise_for_status()
            except requests.exceptions.Timeout:
                break
            except requests.exceptions.HTTPError:
                break
            file_name = f"{current_dir}/{page_number}.jpg"
            with open(file_name, "wb") as f:
                f.write(response.content)


if __name__ == "__main__":
    for book in BOOK_TYPES:
        wb = WebScraper(book)
        wb.get_pages()
