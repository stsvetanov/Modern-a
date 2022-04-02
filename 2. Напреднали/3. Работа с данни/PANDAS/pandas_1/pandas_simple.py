import pandas as pd
D={"name":"Iwa","age":12}
L_1=["name","age"]
L_2=["Iva",12]
Dseries=pd.DataFrame.from_dict(data=D)
print(Dseries)
# l1series=pd.Series(L_1)
# l2series=pd.Series(L_2)
# df=pd.concat([l1series,l2series])
# print(df)