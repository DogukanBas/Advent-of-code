#part1
f=open("input.txt","r")
inputs= [i.strip("\n") for i in f.readlines()]


gamma_array=[0,0,0,0,0,0,0,0,0,0,0,0]
gamma=""
epsilon=""


for binary in inputs:
    for count, value in enumerate(binary):

        gamma_array[count]+=int(value)


for value in gamma_array:
    if value>500:
        gamma+="1"
        epsilon+="0"
    else:
        gamma += "0"
        epsilon += "1"

power_consumption=int(gamma,2)*int(epsilon,2)
print(power_consumption)

#part two
ogr=inputs.copy()
cdo=inputs.copy()
cdo_updtd=inputs.copy()
ogr_updtd=inputs.copy()

def most_least_common_bit(array,index,most):
    amount=len(array)
    sum=0
    i=0
    while sum<=(amount/2) and i<amount:
        sum=sum+int(array[i][index])
        i=i+1
    if (sum>=(amount/2) and most) or (sum<amount/2 and not most):
        return "1"
    else:
        return "0"



for i in range(0,len(cdo[0])):
    lcb=most_least_common_bit(cdo_updtd,i,False)
    cdo=cdo_updtd.copy()
    for j in range(0,len(cdo)):
        if cdo[j][i]!=lcb and len(cdo_updtd)!=1:
            cdo_updtd.remove(cdo[j])



for i in range(0,len(ogr[0])):
    mcb=most_least_common_bit(ogr_updtd,i,True)
    ogr=ogr_updtd.copy()
    for j in range(0,len(ogr)):

        if ogr[j][i]!=mcb and len(ogr_updtd)!=1:
            ogr_updtd.remove(ogr[j])

oxygen_rating=int(ogr_updtd[0],2)*int(cdo_updtd[0],2)

print(oxygen_rating)

