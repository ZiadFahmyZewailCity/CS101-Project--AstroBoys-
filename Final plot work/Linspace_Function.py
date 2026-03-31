# Get even spaces between two values

#Input(Start Number , End Number , Number of steps to go from one to another)


def linspace_numstep(float_str,float_end,int_num_step):
    sum = 0
    L_1xn_linspace = []
    int_dif = float_end - float_str
    step = int_dif/int_num_step
    for i in range(int(int_num_step)):
        sum += step
        L_1xn_linspace.append(sum)

    return L_1xn_linspace

def linspace_step(float_str,float_end,float_step):
    sum = 0
    L_1xn_linspace = []
    int_dif = float_end - float_str
    int_num_step = int_dif/float_step
    for i in range(int(int_num_step)):
        sum += float_step
        L_1xn_linspace.append(sum)

    return L_1xn_linspace


