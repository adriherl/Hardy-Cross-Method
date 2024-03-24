import math

#input => PIPE PROPERTIES: Darcy friction factor, pipe length, pipe diameter, 
print('PIPE PROPERTIES')
print('Darcy friction factor (f):')
f = int(input())

#Variabel properties

print('Pipe length and Diameter:')
pipes_prop = {'AB':[0,0,0,0], 'BC':[0,0,0,0], 'ED':[0,0,0,0], 'AE':[0,0,0,0], 'BD':[0,0,0,0], 'DC':[0,0,0,0]}
circuit1 = ['AB','ED','AE','BD']
circuit2 = ['BC','BD','DC']

#Input panjang pipa
for i,j in pipes_prop.items():
    if i == 'AB' and pipes_prop['AB'][0]==0:
        print('AB=ED length:')
        length = int(input())
        pipes_prop[i][0] = length
    elif i == 'BC'and pipes_prop['BC'][0]==0:
        print('BC length:')
        length = int(input())
        pipes_prop[i][0] = length
    elif i == 'AE'and pipes_prop['AE'][0]==0:
        print('AE=BD length:')
        length = int(input())
        pipes_prop[i][0] = length
    else:
        pipes_prop['ED'][0] = pipes_prop['AB'][0]
        pipes_prop['BD'][0] = pipes_prop['AE'][0]
        pipes_prop['DC'][0] = math.sqrt(pipes_prop['BD'][0]**2+pipes_prop['BC'][0]**2)

#Input diameter pipa
for i,j in pipes_prop.items():
    print(i+' diameter:')
    diameter = int(input())
    pipes_prop[i][1] = diameter

#Hitung friction coefficient (K')
for i,j in pipes_prop.items():
    pipes_prop[i][2] = 0.2517 * f * pipes_prop[i][0] / (pipes_prop[i][1]**2)

#Guess the flow rate for each pipes

#Input flow pada tiap titik, + jika masuk, - jika keluar
flow = {'A':0, 'B':0, 'C':0, 'D':0, "E":0}
total_flow = 0
for i in flow:
    print('Flow of '+i+':')
    frate = int(input())
    flow[i]=frate
    total_flow = total_flow + flow[i]
print(total_flow)
while total_flow != 0:
    total_flow = 0
    print('Total flow harus sama dengan 0')
    for i in flow:
        print('Flow of '+i+':')
        frate = int(input())
        flow[i]=frate
        total_flow = total_flow + flow[i]

#dimulai dari A, ika ada 2 alur tidak diketahui maka arus dibagi 2
    
#initial
pipes_prop['AB'][3] = flow['A']/2
pipes_prop['AE'][3] = -flow['A']/2
pipes_prop['ED'][3] = -(pipes_prop['AE'][3] + flow['E'])
pipes_prop['BD'][3] = (pipes_prop['AB'][3] + flow['B'])/2
pipes_prop['BC'][3] = (pipes_prop['AB'][3] + flow['B'])/2
pipes_prop['DC'][3] = -(pipes_prop['BD'][3] + pipes_prop['ED'][3] + flow['D'])

#Arah Putar

#delta
delta1 = 1
delta2 = 1

hasil = {'AB':0, 'BC':0, 'ED':0, 'AE':0, 'BD':0, 'DC': 0}

def iteration():
    global delta1
    global delta2
    #-kQ^n = eq1
    eq1 = 0
    eq2 = 0
    for i in circuit1:
        eq1 = eq1 + (pipes_prop[i][2]*pipes_prop[i][3]**5) 
    eq1 = -eq1
    for i in circuit2:
        eq2 = eq2 + (pipes_prop[i][2]*pipes_prop[i][3]**5) 
    eq2 = -eq2

    #2kQ = eqt2
    eqt1 = 0
    eqt2 = 0
    for i in circuit1:
        eqt1 = eqt1 + (2*pipes_prop[i][2]*pipes_prop[i][3]) 
    for i in circuit2:
        eqt2 = eqt2 + (2*pipes_prop[i][2]*pipes_prop[i][3]) 
        

    #dibagi untuk mendapatkan delta
    delta1 = eq1/eqt1
    delta2 = eq2/eqt2

    #hasil tiap circuit

    for i in hasil:
        for j in circuit1:
            pipes_prop[j][3] = pipes_prop[j][3] + delta1
        for k in circuit2:
            pipes_prop[k][3] = pipes_prop[k][3] + delta2

#Diiterasi sampai delta dengan keakuratan 0.01
while delta1 >= 0.01 or delta2 >= 0.01:
    iteration()
    
for i in hasil:
    for j in circuit1:
        hasil[j] = pipes_prop[j][3] 
    for k in circuit2:
        hasil[k] = pipes_prop[k][3] 





for keys,values in pipes_prop.items():
    print(keys)
    print(values)
for keys,values in flow.items():
    print(keys)
    print(values)
for keys,values in hasil.items():
    print(keys)
    print(values)
print('delta1:')
print(delta1)
