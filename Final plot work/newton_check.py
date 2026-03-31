def newton_check(Lnxn_int_objecVel):
    bool_newton = False
    for i in range(len(Lnxn_int_objecVel)):
        if bool_newton == True:
            break
        for j in range(len(Lnxn_int_objecVel[i])):
            int_percentage = (Lnxn_int_objecVel[i][j] / 299792458) * 100
            if int_percentage > 1:
                bool_newton = True
                print("Simulation inaccurate non-newtonian")
                break


    return bool_newton
