def func(input):
    result=[]
    for i in range(len(input)):
        for j in range(i+1,len(input)):
            for k in range(j+1,len(input)):

                sum=input[i]+input[j]+input[k]
                if sum==0:
                    result.append([input[i],input[j],input[k]])

    li=[]
    for i in range(len(result)):
        result[i].sort()
        if result[i] not in li:
            li.append(result[i])
    print(li)

func([-25, -10, -7, -3, 2 , 4 , 8, 10])
func([-1,0,1,2,-1,-4])