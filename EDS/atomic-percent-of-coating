import matplotlib.pyplot as plt
import math

def calc_Volume(radius):
    '''
    this function will return volume of spherical shape with given radius.
    '''
    pi = math.pi
    volume = pi * pow(radius, 3) * (3/4)
    return volume



# set simulation parameters
thickness = 20 #Thickness of coating placed on particle
awPt = 195.08 #Atomic weight of Platinum
awNb = 92.91 #Atomic weight of Niobium
awC = 12.01 #Atomic weight of Carbon

dPt = 21.45 #density of Pt
dNbC = 7.82 #density of Niobium Carbide

awNbC = awNb + awC #Molecular weight of Niobume Carbide

x_data = [] #Set empty list for storing x-data value.
y_data = [] #Set empty list for storing y-data value.

x=1 #Initiation Value(1nm or 1 arb. unit)
while x < 200:
    vol_NbC = calc_Volume(x) #Volume of sperical shaped Niobium Carbide.
    vol_Pt = calc_Volume(x + thickness) - calc_Volume(x) #Volume of Platinium coated on surface of Niobium Carbide.
    mol_Pt = (vol_Pt * dPt)/(awPt) #Molar mass of Platinum
    mol_NbC = (vol_NbC * dNbC)/(awNbC) #Molar mass of Niobium Carbide
    atPt = ((mol_Pt)/(mol_NbC+mol_Pt))*100 #Atomic fraction of Platinum.
    x_data.append(2*x) #Append diameter in x_data list.
    y_data.append(atPt) #Append atomic fraction of platinum in y_data list.
    x = x+1

# Plot setup.
plt.style.use('ggplot')
plt.plot(x_data, y_data)
plt.xlabel('radius(nm)')
plt.ylabel('at%')
plt.title('NbC particle size - Pt at%, 20nm Pt thickness')
plt.show()
