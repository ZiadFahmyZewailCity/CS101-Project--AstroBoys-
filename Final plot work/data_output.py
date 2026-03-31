def data_output(dict_data,int_keydic):
   Lnxn_int_objCords, Lnxn_int_objectVel, Lnxn_int_F = dict_data[int_keydic]
   for i in range(len(Lnxn_int_objCords)):
      print(F"object {i} coordinates {Lnxn_int_objCords[i]}")
      print(F"object {i} velocities {Lnxn_int_objectVel[i]}")
      print(F"object {i} forces {Lnxn_int_F[i]}")


