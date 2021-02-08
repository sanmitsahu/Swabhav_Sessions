mylist=[10,20,30,40]
new_list = [i for i in mylist if i>20]
print(new_list)

new_list = [i if i>20 else 0 for i in mylist ]
print(new_list)