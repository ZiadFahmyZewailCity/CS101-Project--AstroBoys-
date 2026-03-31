

#Description: Converts object’s masses from solar masses to kg

#Inputs: Lnxn_in_objectSM(List of each objects masses (in solar masses)),

#Returns: Lnxn_in_objectkg(List of each object’s masses (In kg)),



def Mass_convert_calc(Lnxn_in_objectSM):
    Lnxn_in_objectkg =[]
    for i in range(len(Lnxn_in_objectSM)):
     Lnxn_in_objectkg.append(Lnxn_in_objectSM[i] * 1.989e30)
    return Lnxn_in_objectkg
