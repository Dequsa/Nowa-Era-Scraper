import img2pdf
from pathlib import Path
from os import listdir
from os.path import isfile, join


class PdfConverter:
    BOOK_DIRS = ["Chemia_1", "Fizyka_1", "Geografia_1"]
   
    @staticmethod
    def _convert(file):
        return img2pdf.convert(file)

    def __call__(self):
        for folder in self.BOOK_DIRS:
            dir = f"../{folder}/"
            onlyfiles = [f for f in listdir(dir) if isfile(join(dir, f))]
            with open(f"{dir}/{folder}.pdf", "ab") as pdf:
                for file in onlyfiles:
                    with open(f"{dir}/{file}", "rb") as image, with open(f"{dir}/{file}.pdf", "ab") as tmp_pdf:
                        pdf.write(self._convert(image))
