#part one


f=open("input.txt","r")
cnt=0

input_list=  list(map(lambda line:int(line.strip("\n")),f.readlines()))

for i in range(1,len(input_list)):
    if int(input_list[i])>int(input_list[i-1]):
        cnt+=1

print(cnt)

#part two
cnt1=0
triple_list = list()
for i in range(0,len(input_list)-2):
    triple_list.append(input_list[i]+input_list[i+1]+input_list[i+2])
for i in range(1,len(triple_list)):
    if triple_list[i]>triple_list[i-1]:
        cnt1+=1
print(cnt1)