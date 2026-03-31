import math

l_x = []

x=input("Enter x-coordiant of Celestial Object: ").split()
x_c=[]
for l in x:
    x_c.append(float(l))
y=input("Enter y-coordiant of Celestial Object: ").split()
y_c=[]
for l in y:
    y_c.append(float(l))
m=input("Enter Celestial Object mass's in AU: ").split()
m_c=[]
for l in m:
    m_c.append(float(l))
r=[]
for i in range(len(m)):
    r.append([x_c[i],y_c[i]])
Dis=[]
dis=[]
for h in range(len(m)):
    R=r[h]
    for p in range(len(m)):
        l_x = (math.sqrt((((R[0])-r[p][0])**2)+(((R[1])-r[p][1])**2)))
    dis.append(l_x)

v=0
for u in range(len(m)):
    mc = (m_c[u])*(x_c[u])
    v += mc

center_of_mass_x = v/sum(m_c)
print(center_of_mass_x)










