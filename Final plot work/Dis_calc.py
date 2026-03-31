#Calculate the distance between each object and the other and put them in a list.
#Inputs
#Lnxn_int_objcords: List of object coordinates

#Returns
#Lnxn_int_Dis: List of distances between objects


def Dis_calc(Lnxn_int_objcords):
    import math
    Lnxn_int_D = []  # a List of distance between every object
    for i in range(len(Lnxn_int_objcords)):
        t_Ln_R = Lnxn_int_objcords[i]
        t_Lnxn_int_D = []
        for j in range(len(Lnxn_int_objcords)):
                t_Lnxn_int_D.append(math.sqrt((((t_Ln_R[0]) - Lnxn_int_objcords[j][0]) ** 2) + (((t_Ln_R[1]) - Lnxn_int_objcords[j][1]) ** 2)))

        Lnxn_int_D.append(t_Lnxn_int_D)


    return Lnxn_int_D

