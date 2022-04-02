import pandas as pd
from Advanced.Lecture_11_Examples.catalog import load_catalog

CATALOG_FILENAME = "catalog_sample.csv"

df = pd.read_csv("sales.csv", delimiter=",", names=['ID', "COUNTRY", "TOWN", "TIME", "PRICE"])

total=df["PRICE"].sum()
print("Общата сума на продажбите е:",total)
min_cena=df["PRICE"].min()
print("Минималната цена е:",min_cena)
cena_count=df["PRICE"].count()
print("Общия брой на продажбите е:",cena_count)
max_cena=df["PRICE"].max()
print("Максималната цена е:",max_cena)

country=df["COUNTRY"]
d=dict()
for n in country:
    d[n]=d.get(n,0)+1
bigc=None
bigw=None
for word in d:
    value=d[word]
    if bigc is None or value>bigc:
        bigw=word
        bigc=value
print("Най-много продажби има в  "+bigw,"с "+str(bigc)+" продажби")

id=df["ID"]
d=dict()
for n in id:
    d[n]=d.get(n,0)+1


bigc=None
bigw=None
for word in d:
    value=d[word]
    if bigc is None or value > bigc:
        bigw=word
        bigc=value


# parfum_name_dict={"538352":a"TYGUN II"}
parfum_name_dict = load_catalog(CATALOG_FILENAME)

bigw=(parfum_name_dict["538352"])
print("Най-продаваната стока е с наименование "+bigw,"с "+str(bigc)+" продажби")

