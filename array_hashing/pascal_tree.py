def generate( numRows: int) :
        rep=[[1]]
        for i in range(numRows-1):
            temp = [0]+rep[-1]+[0]
            res = []
            for j in range(len(rep[-1])+1):
                res.append(temp[j]+temp[j+1])
            rep.append(res)
        return rep

print(generate(5))
        

 
