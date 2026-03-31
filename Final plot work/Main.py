import deltaD_calc, deltaV_calc, Linspace_Function, Dis_calc, Mass_convert_calc, F_calc,  Input_object_data, \
    newton_check,collision_check,data_sav_read,data_T
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation


dT = 10000 # Size of dt approximation
Lnxn_int_FA = []  # Dictionary or list of all the forces on every object throughout entire simulation
Lnxn_int_objectVelA = [] # Dictionary or list of object's velocities  of object throughout entire simulation
Lnxn_int_objCordsA = [] # Dictionary or list of object's coordinates of object throughout entire simulation

bool_choose = True
bool_new = True
str_loadinput = input("Would you like to load a previous save file or start a new simulation, enter S for new simulation and L for load? (S/L): ")
while bool_choose:
    if str_loadinput.upper() != "S" and str_loadinput.upper() != "L":
        str_datainput = input("Sorry incorrect format re-enter,Would you like to see the data for an particular instant in time? (Y/N): ")
    elif str_loadinput.upper() == "S":
        break
    elif str_loadinput.upper() == "L":
        bool_new = False
        break


if bool_new == True:
    # User inputs how long the simulation should run
    int_T = int(input("Enter the time you want the to bodys to move for: ")) * 100000000

    # User inputs number of objects
    int_objectnum = int(input("Enter Num of objects: "))

    # Function allows user to input intial conditions and checks its valid
    Lnxn_in_objectSM, Lnxn_int_objecVel, Lnxn_int_objcords = Input_object_data.Input_object_data(int_objectnum)

    data_sav_read.data_sav(Lnxn_int_objcords, Lnxn_int_objecVel, Lnxn_in_objectSM, int_objectnum, int_T)
else:
    str_savefile = input("Enter same file name: ")
    Lnxn_int_objcords,Lnxn_int_objecVel,Lnxn_in_objectSM,int_T,int_objectnum = data_sav_read.DatRea(str_savefile)


# Linespace_Function creates a list of all the dts
L1xn_int_dT = Linspace_Function.linspace_step(0, int_T, dT)


for int_numdt in range(len(L1xn_int_dT)):
    # Converts masses of objects from solar mass to kilogram
    Lnxn_int_objectkg = Mass_convert_calc.Mass_convert_calc(Lnxn_in_objectSM)

    # Calculates distance between ever object and the other for dT
    Lnxn_int_D = Dis_calc.Dis_calc(Lnxn_int_objcords)
    # Checks if collision occurred:
    bool_coll = collision_check.collision_check(Lnxn_int_D)
    if bool_coll == True:
        break
    # Calculates the force on every Object for dT
    Lnxn_int_F = F_calc.F_calc(Lnxn_int_D, Lnxn_int_objectkg, Lnxn_int_objcords)
    Lnxn_int_FA.append(Lnxn_int_F)

    # Calculates the change in velocities of each object for dT
    Lnxn_int_objecVel = deltaV_calc.deltaV_calc(Lnxn_int_objectkg, Lnxn_int_objecVel, Lnxn_int_F,dT)
    Lnxn_int_objectVelA.append(Lnxn_int_objecVel)
    bool_newton = newton_check.newton_check(Lnxn_int_objecVel)

    # Calculates the change in distances of each object for dT
    Lnxn_int_dD = deltaD_calc.deltaD_calc(Lnxn_int_objcords,Lnxn_int_objecVel,dT)
    Lnxn_int_objCordsA.append(Lnxn_int_dD)
    # Update object coordinates for the next iteration
    Lnxn_int_objcords = Lnxn_int_dD


if bool_coll == False:
    dict_data = data_T.data_T(L1xn_int_dT,Lnxn_int_objCordsA,Lnxn_int_objectVelA,Lnxn_int_FA)

str_datainput = input("Would you like to see the data for an particular instant in time? (Y/N): ")
bool_data = True

while bool_data:
    if str_datainput.upper() != "Y" and str_datainput.upper() != "N":
        str_datainput = input("Sorry incorrect format re-enter,Would you like to see the data for an particular instant in time? (Y/N): ")
    else:
        bool_startdata = True
        print(f"available instants in time {dict_data.keys()}")
        int_keydic = int(input("Please enter instant in time you want: "))
        print(int_keydic)
        bool_data = False

while bool_startdata:
    if int_keydic not in dict_data.keys():
        print(f"available instants in time {dict_data.keys()}")
        int_keydic = input("unrecognized instant in time please enter again")
    else:
        print(dict_data[int_keydic])
        break






## Convert the lists to NumPy arrays for easier plotting
Lnxn_int_objCordsA = np.array(Lnxn_int_objCordsA)

# Create a 1x2 subplot grid
fig, axs = plt.subplots(1, 2, figsize=(12, 5))

# Plotting the trajectories of each object with color representing time
for obj_idx in range(int_objectnum):
    sc = axs[0].scatter(
        Lnxn_int_objCordsA[:, obj_idx, 0],
        Lnxn_int_objCordsA[:, obj_idx, 1],
        c=np.arange(len(Lnxn_int_objCordsA)),
        cmap='viridis',  # You can choose any colormap you like
        label=f'Object {obj_idx + 1}',
        marker='o'
    )

axs[0].set_title('Object Trajectories with Time')
axs[0].set_xlabel('X-coordinate')
axs[0].set_ylabel('Y-coordinate')
axs[0].legend()
fig.colorbar(sc, ax=axs[0], label='Time')  # Add a colorbar to represent time

# Plotting the trajectories of each object
if bool_coll == False:
    for obj_idx in range(int_objectnum):
        axs[1].plot(Lnxn_int_objCordsA[:, obj_idx, 0], Lnxn_int_objCordsA[:, obj_idx, 1], label=f'Object {obj_idx + 1}', marker='o')

    axs[1].set_title('Object Trajectories')
    axs[1].set_xlabel('X-coordinate')
    axs[1].set_ylabel('Y-coordinate')
    axs[1].legend()

# Adjust layout to prevent clipping of labels
plt.tight_layout()

plt.show()
# Assuming Lnxn_int_objCordsA is a list of coordinates for each object over time
# It should be a list of lists, where each inner list represents the coordinates of objects at a specific time step.

# Convert the list to a numpy array for easier manipulation
obj_cords_array = np.array(Lnxn_int_objCordsA)

# Get the number of objects
num_objects = len(obj_cords_array[0])

# Set up the figure and axis
fig, ax = plt.subplots()

# Plot initial positions of the objects
scatter_objects = ax.scatter(obj_cords_array[0, :, 0], obj_cords_array[0, :, 1], marker='o', label='Objects')

# Set axis labels and title
ax.set_xlabel('X Coordinate')
ax.set_ylabel('Y Coordinate')
ax.set_title('Objects Motion Over Time')

# Add legend
ax.legend()

# Function to update the plot for each animation frame
def update(frame):
    scatter_objects.set_offsets(obj_cords_array[frame, :, :2])  # Update X and Y coordinates

# Create animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 10), interval=1, blit=False) #len(L1xn_int_dT)

plt.show()

figure, ax = plt.subplots()

# Setting limits for x and y axis
ax.set_xlim(0, 100e100)
ax.set_ylim(0, 12e100)

# Since plotting a single graph
line, = ax.plot(0, 0)


def animation_function(i):
    x_coordinat_matrix.append(i * 15)
    y_coordinat_matrix.append(i)

    line.set_xdata(x_coordinat_matrix)
    line.set_ydata(y_coordinat_matrix)
    return line,


animation = FuncAnimation(figure,
                          func=animation_function,
                          frames=np.arange(0, 10, 0.1),
                          interval=10)
plt.show()







