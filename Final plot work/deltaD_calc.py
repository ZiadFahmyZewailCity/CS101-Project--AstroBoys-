

#Calculates new position of every object for a given dT

#Inputs:
#Lnxn_in_objectKg: List of each object's masses
#Lnxn_int_objecVel: List of each object's Velocity for each dT

#Returns:
#Lnxn_int_dD: List of changes in object’s displacement


def deltaD_calc(Lnxn_int_objcords,Lnxn_int_objecVel,dT):
    t_Lnxn_int_objecCordsX = 0
    t_Lnxn_int_objecCordsY = 0
    total_Coordinat = []
    for i in range(len(Lnxn_int_objecVel)):
        t_Lnxn_int_objecCordsX = Lnxn_int_objcords[i][0] + (Lnxn_int_objecVel[i][0] * dT)
        t_Lnxn_int_objecCordsY = Lnxn_int_objcords[i][1] + (Lnxn_int_objecVel[i][1] * dT)

        total_Coordinat.append([t_Lnxn_int_objecCordsX, t_Lnxn_int_objecCordsY])


    return total_Coordinat

