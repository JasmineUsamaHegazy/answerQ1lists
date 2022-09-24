keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

con_dict = dict

for item in range(len(keys)):
    con_dict.update({keys[item]: values[item]})

print(con_dict)
