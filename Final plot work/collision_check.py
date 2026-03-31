#Calculates if the simulation has become inaccurate or not and returns a true of false value

#Inputs
#Lnxn_int_Vel: List of object’s velocities

#Returns
#bool_newton: True/False


def collision_check(Lnxn_int_D):
    bool_col = False

    for i in range(len(Lnxn_int_D)):
        count = 0
        for j in range(len(Lnxn_int_D[0])):
            if Lnxn_int_D[i][j] == 0:
                count += 1
        if count >= 2:
            bool_col = True
            print("collision occurred")
    return bool_col




