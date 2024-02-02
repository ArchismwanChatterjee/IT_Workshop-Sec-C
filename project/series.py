#Find the nth value of this series: 1,1,2,3,4,9,8,27,...

n=int(input("Enter the nth term: "))

a=0 # counter for 2^n
b=0 # counter for 3^n

if n>0:

    for i in range(n):
        
        if(i%2==0):
            val=int(pow(2,a))
            a+=1
        
        else:
            val=int(pow(3,b))
            b+=1
    
    print("The nth term of the given series is ",val)
    
else:
    
    pass

'''
1) Enter the nth term: 1
The nth term of the given series is  1

2) Enter the nth term: 18
The nth term of the given series is  6561

3) Enter the nth term: 10
The nth term of the given series is  81

4) Enter the nth term: -20 
'''