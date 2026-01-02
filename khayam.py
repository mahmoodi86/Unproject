#khayam
def khayam_pascal(line):
    if line==1:
        return([[1]])
    khayam=[[1],[1,1]]
    for item in range(2,line):
        line_1=[1]*(item+1)
        for i in range(1,item):
            line_1[i]=khayam[item-1][i-1]+khayam[item-1][i]
        khayam.append(line_1)
    return(khayam)
n=int(input())
pascal_list=khayam_pascal(n)
for i in pascal_list:
    for j in i:
        print(j,end=' ')
    print()

