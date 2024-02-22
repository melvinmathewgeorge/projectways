def max1(list1):
  max_val=list1[0]
  for i in list1:
     if i>max_val:
      max_val=i
  return max_val



list1=[2,3,4,87,1,5,9]
print(max1(list1))

def min1(list2):
 min_val=list2[0]
 n=len(list2)
 for i in range(1,n):
   if list2[i]< min_val:
       min_val=i
 return min_val
list2=[12,3,4,87,1,5,9]
print(min1(list2))


list3=[6,4,5,1]
n=len(list3)
temp=0
for i in range(n):
  for j in range(n):
    if list3[j]>list3[i]:
         temp=list3[i]
         list3[i]=list3[j]
         list3[j]=temp
print(list3[i-1])

         



