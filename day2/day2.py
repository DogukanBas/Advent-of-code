#part one
f=open("input.txt","r")
commands_list=  list(map(lambda line:line.strip("\n"), f.readlines()))
forward=0
depth=0

for i in commands_list:
    if i.startswith("forward"):
        forward=forward+int(i.strip("forward "))
    elif i.startswith("down"):
        depth=depth+int(i.strip("down "))
    else:
        depth=depth-int(i.strip("up "))
print(forward*depth)

#part two
aim=0
horizontal=0
depth2=0

for i in commands_list:
    if i.startswith("forward"):
        value=int(i.strip("forward "))
        horizontal=horizontal+value
        depth2=depth2+aim*value
    elif i.startswith("down"):
        value=int(i.strip("down "))
        aim=aim+value
    else:
        value=int(i.strip("up "))
        aim=aim-value

print(depth2*horizontal)

