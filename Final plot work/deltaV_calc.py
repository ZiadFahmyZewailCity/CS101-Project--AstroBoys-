#Calculates the change in velocity of each object at some instance in time and puts them into a list

#Inputs
#Lnxn_int_Fx: List of forces on each object
#Lnxn_in_objectKg: List of each object's masses
#Lnxn_int_objecVel: List of each object's Velocity for each dT
#Lnxn_int_objectVelA: List of each object's Velocity's throughout sim

#Returns
#Lnxn_int_Vel: List of object’s velocities
#Lnxn_intVelA: List of each object's Velocity's throughout sim


def deltaV_calc(Lnxn_in_objectKg,Lnxn_int_objecVel,Lnxn_int_F,dT):
        #for i in range(len(Lnxn_int_F)):
            #for j in range(len(Lnxn_int_objecVel[1])):
                # Calculates dV and adds to velocties at previous dt
                #Lnxn_int_objecVel[i][j] = Lnxn_int_objecVel[i][j] + ((Lnxn_int_F[i][j] * dT) / Lnxn_in_objectKg[i])
        t_Lnxn_int_objecVelX=0
        t_Lnxn_int_objecVely=0
        total_vilocity=[]
        for i in range(len(Lnxn_int_F)):
            t_Lnxn_int_objecVelX = Lnxn_int_objecVel[i][0] + ((Lnxn_int_F[i][0] * dT) / Lnxn_in_objectKg[i])
            t_Lnxn_int_objecVely = Lnxn_int_objecVel[i][1] + ((Lnxn_int_F[i][1] * dT) / Lnxn_in_objectKg[i])

            total_vilocity.append([t_Lnxn_int_objecVelX,t_Lnxn_int_objecVely])

        Lnxn_int_objecVel.append(total_vilocity)

        return total_vilocity
