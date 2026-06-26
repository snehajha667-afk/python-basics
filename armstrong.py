num=int(input("Enter number:"))
temp=num
digits=len(str(num))
sum_num=0
while temp>0:
  digit=temp%10
  sum_num+=digit**digits
  temp//=10
  if sum_num==num
  print("Arstrong Number")
else:
  print("Not Armstrong Number")
