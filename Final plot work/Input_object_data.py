


#Takes in the users input of number of objects then allows him to enter the mass, (x,y) positions, and (Vx,Vy) of every
#object, it converts these values to integers and puts them into lists. It also checks if inputs are valid or not

#Inputs:
#int_objectnum:Number of objects
#Returns:
#Lnxn_in_objectSM:List of each objects masses
#Lnxn_int_objecVel:List of object velocities
#Lnxn_int_objcords:List of object coordinates



def Input_object_data(int_objectnum):
 Lnxn_int_objcords = []  # position of all objects
 Lnxn_in_objectSM = []  # Mass of Objects
 Lnxn_int_objecVel = []  # velocity of all objects

 for i in range(int_objectnum):
    bool_check_1 = True
    bool_check_2 = True
    bool_check_3 = True
    t_coords_conv = []
    t_Vel_conv = []

    while bool_check_1:
        try:
            t_int_objectSM = float(input(f"Enter the mass of object {i + 1} in solar mass: "))
            if t_int_objectSM > 0:
                bool_check_1 = False
            else:
                int("f")
        except:
            print("Sorry, mass must be a positive integer")
    while bool_check_2:
        try:
            t_Lnxn_int_objcords = list(map(float, input(
                f"Enter x and y coordinates of Celestial Object {i + 1} in this format (x,y): ").split(",")))
            if len(t_Lnxn_int_objcords) == 2:
                bool_check_2 = False
            else:
                int("f")
        except:
            print(f"sorry incorrect formatting")


    while bool_check_3:
        try:
            t_Lnxn_int_objecVel = list(map(float, input(
                f"Enter the velocity in x and y direction of Celestial Object {i + 1} in this format (Vx,Vy): ").split(
                ",")))
            if len(t_Lnxn_int_objecVel) == 2:
                bool_check_3 = False
            else:
                int("f")
        except:
            print(f"sorry incorrect formatting")

    for j in range(0, 2):
        t_coords_conv.append(t_Lnxn_int_objcords[j] * 1.496e11)
        t_Vel_conv.append(t_Lnxn_int_objecVel[j] * 10 ** 3)
    Lnxn_in_objectSM.append(t_int_objectSM)
    Lnxn_int_objecVel.append(t_Vel_conv)
    Lnxn_int_objcords.append(t_coords_conv)

 return Lnxn_in_objectSM,Lnxn_int_objecVel,Lnxn_int_objcords


