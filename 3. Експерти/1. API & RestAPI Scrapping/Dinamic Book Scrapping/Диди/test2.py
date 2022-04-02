from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape

from PyPDF2 import PdfFileWriter, PdfFileReader
import os
import pandas as pd
import reportlab
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from shutil import copyfile

def create_watermark(text):
    pdfmetrics.registerFont(TTFont('DejaVuSerif', 'DejaVuSerif.ttf'))
    copyfile('watermark.pdf','next_watermark.pdf')
    c = canvas.Canvas('next_watermark.pdf')
    c.setPageSize(landscape(A4))
    c.setFontSize(14)
    c.setFont('DejaVuSerif',14)
    c.drawString(15, 15, text)
    c.save()
folder_path='data'
file="2020_05_10a_Tech_ZZY.pdf"
filename_string="data/2020_05_10a_Tech_ZZY.pdf"
input_file = PdfFileReader(open(filename_string, "rb"))
text = 'Признати часове след проверка на личния отчет: 72'

create_watermark(text)

watermark = PdfFileReader(open("next_watermark.pdf", "rb"))
output_file = PdfFileWriter()
page_count = input_file.getNumPages()
for page_number in range(page_count):
    input_page = input_file.getPage(page_number)
    input_page.mergePage(watermark.getPage(0))
    output_file.addPage(input_page)
output_path = folder_path + '/'+ file.split('.pdf')[0] + '_watermarked' + '.pdf'
print(output_path)
with open(output_path, "wb") as outputStream:
    output_file.write(outputStream)
    print('Done')