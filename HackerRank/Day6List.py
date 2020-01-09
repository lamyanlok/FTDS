if __name__ == '__main__':
    N = int(input())
    z= []
    for i in range (N):
        x = input()
    
        y = x.split()
        if y[0] == "insert":
            z.insert(int(y[1]),int(y[2]))
        
        if y[0] =="print":
            print(z)
        
        if y[0] == "remove":
            z.remove(int(y[1]))
        
        if y[0] == "append":
            z.append(int(y[1]))

        if y[0] == "sort":
            z.sort()
        
        if y[0] == "pop":
            z.pop()

        if y[0] == "reverse":
            z.reverse()
        


