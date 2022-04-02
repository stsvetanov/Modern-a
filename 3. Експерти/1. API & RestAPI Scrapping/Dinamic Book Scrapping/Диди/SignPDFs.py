import PyPDF2
from reportlab.pdfgen import canvas
from PyPDF2 import PdfFileWriter, PdfFileReader
from reportlab.lib.pagesizes import A4, landscape
from shutil import copyfile
import os



def create_watermark(png_file_name, signature_with_names=True):
    if signature_with_names:
        new_watermark='signed_with_names.pdf'
        x,y,w,h=60,110,490,120
    else:
        new_watermark = 'just signed.pdf'
        x, y, w, h = 220, 70, 40, 40
    copyfile('watermark.pdf',new_watermark )
    c = canvas.Canvas(new_watermark)
    c.setPageSize(landscape(A4))
    c.drawImage(png_file_name, x,y,w,h,mask='auto')
    c.save()

problem_files=[]

folder_path_to_pdf_files='data'
folder_path_to_signatures='signatures'
export_to_folder='signed'

# MAIN
filelist_pdfs=sorted(os.listdir(folder_path_to_pdf_files))
filelist_signatures=sorted(os.listdir(folder_path_to_signatures))

for file in filelist_pdfs:
    if file.endswith(".pdf"):

        filename_string = folder_path_to_pdf_files + '/' + file
        check=True
        try:
            input_file = PdfFileReader(open(filename_string, "rb"))
        except:
            check=False
            problem_files.append("fopen+"+file)
        if check:
            abrev=file[-7:-4]
            check=False
            for fs in filelist_signatures:
                if fs[:3]==abrev and len(fs)==12:
                    watermark_fp=folder_path_to_signatures+"/"+ fs
                    check=True
                if fs[:3]==abrev and len(fs)==18:
                    watermark_lp=folder_path_to_signatures+"/"+ fs
                    check=True
            if check:
                create_watermark(watermark_lp)  # signed_with_names.pdf
                # print("Created watermark_lp")
                create_watermark(watermark_fp, False)  # just signed.pdf
                # print("Created watermark_fp")
                watermarkfp = PdfFileReader(open("just signed.pdf", "rb"))
                watermarklp = PdfFileReader(open("signed_with_names.pdf", "rb"))
                input_file_path=folder_path_to_pdf_files+"/"+file

                page_count = input_file.getNumPages()
                output_file = PdfFileWriter()
                # read content of the original file
                for page_number in range(page_count):
                    input_page = input_file.getPage(page_number)
                    if page_number == 0:
                        input_page.mergePage(watermarkfp.getPage(0))
                        output_file.addPage(input_page)
                    elif page_number == page_count - 1:
                        input_page.mergePage(watermarklp.getPage(-1))
                        output_file.addPage(input_page)
                    else:
                        output_file.addPage(input_page)

                output_path = export_to_folder+ "/"+file.split('.pdf')[0] + '_signed.pdf'
                # print(output_path)

                with open(output_path, "wb") as outputStream:
                    output_file.write(outputStream)
                    # print('Done')
            else:
                problem_files.append("missing_signature+"+file)
print("Problem files:\n")

for i in problem_files:
    print(i)




