staff=input("password:")
count=0;
sum=0;
print("enter rating between 1-5")
n=10
while(n!=0):
    rating=int(input("rating:"))
    if(rating==n):
        break
    elif(rating>=1and rating<=5):
        sum=sum+rating
        count=count+1
    else:
        print("enter a valid rating")
print("enter pwd to see avg")
pwd=input("password:")
if(staff==pwd):
    avg=sum/count
    print("Average is ",avg)
else:
    print("pwd inavalid")
    
