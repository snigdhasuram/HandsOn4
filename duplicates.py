array= list(map(int,input("Input: array = ").split(",")))
output = []
for i in range(len(array)):
    if(array[i] not in output):
        output.append(array[i])
print("output: array = ",output)
