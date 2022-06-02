if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    newlist=[]
# =============================================================================
#     for i in range(0,x+1):
#         for j in range(0,y+1):
#             for k in range(0,z+1):
#                if (i+j+k != n): 
#                 newlist.append([i,j,k])     
#     print(newlist)
# =============================================================================
 #  print(type(newlist)) 
 # newlist= [t for t in newlist if (x+y+z) != n]
# =============================================================================
#  print([[x, y, z] for [i, j, k] in [0, 0, 0] for x,y,z in [x, y, z]])
# =============================================================================
    print([[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if (i+j+k)!=n])