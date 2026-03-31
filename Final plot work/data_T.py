def data_T(L1xn_int_dT,Lnxn_int_objCordsA,Lnxn_int_objectVelA,Lnxn_int_FA):
    dic_dt = {}
    for i in range(len(L1xn_int_dT)):
         dic_dt[L1xn_int_dT[i]] = Lnxn_int_objCordsA[i],Lnxn_int_objectVelA[i],Lnxn_int_FA[i]


    return dic_dt

