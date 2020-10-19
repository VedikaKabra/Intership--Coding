staff=input("password:") #takes a alphanumeric input from staff as password
count=0;
sum=0;
print("enter rating between 1-5") #users give the rating
n=10 #if 10 is entered the loop ends
while(n!=0):
    rating=int(input("rating:"))
    if(rating==n):
        break
    elif(rating>=1and rating<=5): #users are told to give the rating between 1 and 5
        sum=sum+rating
        count=count+1
    else:
        print("enter a valid rating")
print("enter pwd to see avg") #to see the average of rating the staff can enter the pwd
pwd=input("password:")
if(staff==pwd): #if pwd of staff and the entered pwd matches then avg is displayed
    avg=sum/count
    print("Average is ",avg)
else:
    print("pwd inavalid")
    
