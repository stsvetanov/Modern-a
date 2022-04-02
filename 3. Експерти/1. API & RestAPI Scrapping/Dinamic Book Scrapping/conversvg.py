import cairosvg as ca
# import requests as r

s='/Users/valerina/PycharmProjects/1386/Book Scrapping/анубис/'
for i in range(1,5):

    svgf=s+'%d.svg'%(i)
    pdff=s+'pdfs/%d.pdf'%(i)

    print(svgf)
    print(pdff)
    # fo=open(svg,'r')
    # ca.svg2png(file_obj = fo, write_to = pdf)
    ca.svg2png(url=svgf, write_to=pdff)
    # image = pv.Image.new_from_file(svg, dpi=300)
    # image.write_to_file(png)
    # fo.close()