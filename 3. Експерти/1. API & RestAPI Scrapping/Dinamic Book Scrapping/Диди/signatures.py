from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape
from PyPDF2 import PdfFileWriter, PdfFileReader
import os
import pandas as pd
from shutil import copyfile
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
"""
Refer to an image if you want to add an image to a watermark.
Fill in text if you want to watermark with text.
Alternatively, following settings will skip this.
picture_path = None
text = None
"""

def create_watermark(text):
    pdfmetrics.registerFont(TTFont('DejaVuSerif', 'DejaVuSerif.ttf'))
    copyfile('watermark.pdf','next_watermark.pdf')
    c = canvas.Canvas('next_watermark.pdf')
    c.setPageSize(landscape(A4))
    c.setFontSize(14)
    c.setFont('DejaVuSerif',14)
    c.drawString(15, 15, text)
    c.save()



microdata=pd.read_csv('микро.csv',sep=";")
print(microdata.head())
print(len(microdata.iloc[0,0]))
problem_files=[]

folder_path='data'
filelist=sorted(os.listdir(folder_path))
for file in filelist:
    if file.endswith(".pdf"):
        output_file = PdfFileWriter()
        filename_string = folder_path + '/' + file
        check=True
        try:
            input_file = PdfFileReader(open(filename_string, "rb"))
        except:
            check=False
            problem_files.append("fopen+"+file)
        if check:
            fname = file[:len(file) - 3] + 'xlsx'
            filter = microdata.iloc[:, 0] == fname
            f=list(filter)
            if True in list(f):
                print(microdata.loc[filter])
                hh = microdata.loc[filter].iloc[0, 1]
                text = 'Признати часове след проверка на личния отчет: '
                text = text + str(hh)
                print(text)
                create_watermark(text)

                watermark = PdfFileReader(open("next_watermark.pdf", "rb"))
                page_count = input_file.getNumPages()
                for page_number in range(page_count):
                    input_page = input_file.getPage(page_number)
                    input_page.mergePage(watermark.getPage(0))
                    output_file.addPage(input_page)
                output_path = 'wtm/'+ file.split('.pdf')[0] + '_watermarked' + '.pdf'
                print(output_path)
                with open(output_path, "wb") as outputStream:
                    output_file.write(outputStream)
                    print('Done')
            else:
                problem_files.append("micro+"+file)
print("Problem files:\n")

for i in problem_files:
    print(i)