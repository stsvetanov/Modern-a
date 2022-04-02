# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
from bs4 import BeautifulSoup

sibling_soup = BeautifulSoup("<a><b>text1</b><c>text2</c><d><f>text3</f><e>text4</e></d></a>", features="lxml")
print(type(sibling_soup))
print(sibling_soup.prettify())
# print(sibling_soup.b.next_sibling)
#
# print(sibling_soup.c.previous_sibling)

print(sibling_soup.a.findChildren())
#
print(sibling_soup.f.parent.parent)

# property_type_list = soup.find_all("a", class_=["lnk1", "lnk2"])
# # print(property_type_list)