f=open("input.txt","r")
cnt=0

input_list=  f.readlines()
for i in range(1,len(input_list)):
    if int(input_list[i].strip("\n"))>int(input_list[i-1].strip("\n")):
        cnt+=1

print(cnt)
