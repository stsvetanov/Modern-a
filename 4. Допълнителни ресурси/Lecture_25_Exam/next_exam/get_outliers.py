def get_outliers(data_set):
    average = sum(data_set)/len(data_set)
    outliers = []
    for element in data_set:
        if element > 2*average or element < average/2:
            outliers.append(element)

    return outliers


data_set = [1,200,189,587,1000]
print(get_outliers(data_set))