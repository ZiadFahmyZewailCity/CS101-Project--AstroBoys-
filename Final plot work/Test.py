dic = {6:"34",10:"320"}

int_keydic = 6
bool_startdata = True
while bool_startdata:
    if int_keydic not in dic.keys():
        int_keydic = input("unrecognized instant in time please enter again")
    else:
        print(dic[int_keydic])
        bool_startdata = False
