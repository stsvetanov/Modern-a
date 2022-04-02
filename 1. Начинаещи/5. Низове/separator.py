def split_str(str):
    ref_dict = {
        '\x07':'a',
        '\x08':'b',
        '\x0C':'f',
        '\n':'n',
        '\r':'r',
        '\t':'t',
        '\x0b':'v',
    }

    res_arr = []
    temp = ''

    for i in str:
        if not i == '\\':
            if i in ref_dict:
                if not temp == "":
                    res_arr.append(temp)
                res_arr.append(ref_dict[i])
                temp = ''
            else:
                temp += i
        else:
            if not temp == '':
                res_arr.append(temp)
            temp = ''
    res_arr.append(temp)
    return res_arr


str = "a\a\b\f\n\r\t\v\c\d\e\f\i"
# str = input("Enter")
print(split_str(str))