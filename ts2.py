if __name__ == '__main__':
    list1=[]
    n=int(input())
    for i in range(n):
        name = input()
        score = float(input())
        list1.append([name,score])    
# =============================================================================
# sorted1= list1.sort()    
    print(list1) 
    list2=sorted(list1)           
    print(list2)
    lowest=list2[0][1]
    flag=False
    print(" list2 2nd and fourth ",list2[2],list2[4][1],list2[2][1]>list2[4][1])
# =============================================================================
    for t in range(1,n,1):
       # print(list2[t][1])
    #print(sorted(list1))
      # print("before if value of list index of t-1 , and t is, and current lowest is  ", list2[t-1][1], list2[t][1], lowest)
       if lowest<list2[t][1] :
           lowest=lowest
           if flag==False:
              seclowest=list2[t][1]
              kk=t
              flag=True
              #print(" in if current t-1 ",t-1 ," current t is ", t, " lowest is ",lowest, "sec lowest and flag is ",seclowest, flag)
       else:
           lowest=list2[t][1]
           lowestname=t
          # print(" in else current t-1 ",t-1 ," current t is ", t, " lowest is ",lowest)
    #print("lowest is and seclowest is ",lowest,seclowest)
    
# =============================================================================
#   """ to find second lowest"""  
# =============================================================================
    for ttt in range(0,n,1):
      #print("seclowest is ",seclowest, " and ttt is ",ttt )
      if seclowest>lowest:
           #print(" inside 1st if  ttt lowest seclowest and[ttt] ",ttt,lowest,seclowest, list2[ttt][1])
           if seclowest<list2[ttt][1]:
             seclowest=seclowest
           elif lowest<list2[ttt][1]:
             seclowest=list2[ttt][1]
      else:
          pass
    print("seclowest is ",seclowest )
    for tt in range(0,n,1):
        if list2[tt][1]==seclowest:
            print(list2[tt][0])
    
# =============================================================================
#     print(list2[lowestname][0]) 
#     for kk in range(lowestname,n-1,1):
#       if list2[kk][1]==list2[kk+1][1]:
#        print(list2[kk+1][0])
# 
# =============================================================================
     