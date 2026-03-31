import math
x_c=[] #x-coordinat
y_c=[] #y-coordinat
m_c=[] #mass in AU
r=[]   #position of all objects
Dis=[] #Distance between every two objects

x=input("Enter x-coordiant of Celestial Object: ").split()

for i in x:
    x_c.append(float(i))


y=input("Enter y-coordiant of Celestial Object: ").split()

for i in y:
    y_c.append(float(i))

m=input("Enter Celestial Object mass's in AU: ").split()

for i in m:
    m_c.append(float(i))


for i in range(len(m)):
    r.append([x_c[i],y_c[i]])

for i in range(len(m)):
    R=r[i]
    for j in range(len(m)):
        Dis.append(math.sqrt((((R[0])-r[j][0])**2)+(((R[1])-r[j][1])**2)))
v=0
for i in range(len(m)):
    mc=(m_c[i])*(x_c[i])
    v+=mc

center_of_mass_x=v/sum(m_c)
print(Dis)










