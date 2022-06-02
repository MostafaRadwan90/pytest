7
if __name__ == '__main__':
    n = int(input().strip())
if n%2!= 0:
 print("Weird")
 print("1")
elif (n%2==0 and 2<=n and n>=5) :
 print("Not Weird")
 print("2")
elif (n%2==0 and 6 <= n >= 20):
 print("Weird")
 print("3")
elif (n%2==0 and n>20):
 print("Not Weird")
 print("4")
  
