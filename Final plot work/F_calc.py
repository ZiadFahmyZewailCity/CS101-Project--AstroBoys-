#Calculates force on each object and places them in a list. Stores all the forces on the objects throughout time.

#Inputs:
#Lnxn_int_Dis: List of distances between objects
#Lnxn_int_objcords: List of object coordinates
#Lnxn_int_FxA: List of forces on each object throughout time


#Returns:
#Lnxn_int_Fx: List of forces on each object

def F_calc(Lnxn_int_D, Lnxn_int_objectkg, Lnxn_int_objcords):
    G = 6.6743e-11
    Lnxn_int_F = []  # List of All forces on object at instance dt
    for i in range(len(Lnxn_int_objectkg)):
        t_int_Fx = 0
        t_int_Fy = 0
        for j in range(len(Lnxn_int_objectkg)):

            if i != j:
                if len(Lnxn_int_objcords)==len(Lnxn_int_objectkg):
                    t_int_Fx += (Lnxn_int_objectkg[i] * G * Lnxn_int_objectkg[j] * (Lnxn_int_objcords[j][0] - Lnxn_int_objcords[i][0]) * (1 / Lnxn_int_D[i][j]) ** 3)
                    t_int_Fy += (Lnxn_int_objectkg[i] * G * Lnxn_int_objectkg[j] * (Lnxn_int_objcords[j][1] - Lnxn_int_objcords[i][1]) * (1 / Lnxn_int_D[i][j]) ** 3)


        Lnxn_int_F.append([t_int_Fx, t_int_Fy])


    return Lnxn_int_F
