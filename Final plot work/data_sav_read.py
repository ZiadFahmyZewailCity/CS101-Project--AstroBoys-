def data_sav(Lnxn_int_objcords,Lnxn_int_objecVel,Lnxn_in_objectSM,int_objectnum,int_T):
    str_SaveName = input("Please enter what you want your save file name to be: ")
    sav = open(str_SaveName,"w")
    sav.write(f"o{int_objectnum}\n")
    sav.write(f"s{int_T}\n")
    sav.write("v")
    for i in range(len(Lnxn_int_objecVel)):
        sav.write("\\")
        for j in range(len(Lnxn_int_objecVel[i])):
         sav.write(f"{Lnxn_int_objecVel[i][j]}")
         sav.write("\\")
    sav.write("\n")
    sav.write("p")
    for i in range(len(Lnxn_in_objectSM)):
        sav.write(f"\\{Lnxn_in_objectSM[i]}\\")
    sav.write("\n")
    sav.write("l")
    for i in range(len(Lnxn_int_objcords)):
        sav.write("\\")
        for j in range(len(Lnxn_int_objcords[i])):
            sav.write(f"{Lnxn_int_objcords[i][j]}")
            sav.write("\\")
    sav.write("\n")



def DatRea(str_SaveName):
    sav = open(str_SaveName, "r")
    for line in sav:
        if "o" in line:
            str_int_T = line[1:].strip()
            int_objectnum = int(str_int_T)
        elif "s" in line:
            str_int_T = line[1:].strip()
            int_T = int(str_int_T)
        elif "v" in line:
            L1xn_int_objvel = []
            t_str_T1 = line[2:-2].strip()
            t_str_T2 = t_str_T1.split("\\\\")
            for i in t_str_T2:
                t_str_T3 = (i.split("\\"))
                L1xn_int_objvel.append([float(t_str_T3[0]),float(t_str_T3[1])])


        elif "p" in line:
            Lnxn_in_objectSM = []
            t_str_T1 = line[2:-2].strip()
            t_str_T2 = t_str_T1.split("\\\\")
            for i in t_str_T2:
                Lnxn_in_objectSM.append(float(i))




        elif "l" in line:
            L1xn_int_objcords = []
            t_str_T1 = line[2:-2].strip()
            t_str_T2 = t_str_T1.split("\\\\")
            for i in t_str_T2:
                t_str_T3 = (i.split("\\"))
                L1xn_int_objcords.append([float(t_str_T3[0]),float(t_str_T3[1])])



    return L1xn_int_objcords,L1xn_int_objvel,Lnxn_in_objectSM,int_T,int_objectnum





