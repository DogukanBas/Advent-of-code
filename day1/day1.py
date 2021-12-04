#part one
f=open("input.txt","r")
cnt=0

input_list=  list(map(lambda line:int(line.strip("\n")),f.readlines()))

for i in range(1,len(input_list)):
    if input_list[i]>input_list[i-1]:
        cnt+=1

print(cnt)

#part two

cnt1=0
prev=sum(input_list[0:3])
for i in range(0,len(input_list)-3):
    next=sum(input_list[i+1:i+4])
    if next>prev:
        cnt1+=1
    prev=next
print(cnt1)
