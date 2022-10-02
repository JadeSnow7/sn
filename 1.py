
#!/usr/bin/python3
#输入成绩，计算平均数
print("Please input the number of the students:",end=" ")
n1=int(input())
course=['Chinese','math','English']
#score=[]
name=['0' for i in range(0,n1+1)]
total=0
for i in range(0,n1):
    print("Please input your name:")
    name[i]=str(input())
name[n1]="average"
score=[[0]*(len(name)+1) for _ in range(len(course)+1)]
for i in range(0,n1):
    print("Please input the scores of ",name[i])
    total=0
    for j in range(0,3):
        print(course[j],end=':')
        score[j][i]=int(input())
        total+=score[j][i]
    score[3][i]=total/3  
for j in range(0,4):
    total=0
    for i in range(0,n1):
        total+=score[j][i]
    score[j][n1]=total/n1


print("name".ljust(20) , "Chinese".ljust(20) , "math".ljust(20),"English".ljust(20),"average".ljust(20))
for i in range(0,n1):
    print(name[i].ljust(20),f"{score[0][i]}".ljust(20),f"{score[1][i]}".ljust(20),f"{score[2][i]}".ljust(20),f"{format(score[3][i],'.2f')}".ljust(20))
print("average:".ljust(20),f"{format(score[0][n1],'.2f')}".ljust(20),f"{format(score[1][n1],'.2f')}".ljust(20),f"{format(score[2][n1],'.2f')}".ljust(20),f"{format(score[3][n1],'.2f')}".ljust(20))