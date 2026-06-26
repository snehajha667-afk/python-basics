str1=input("Enter first word:")
str2=input("Enter second word:")
if sorted(str1.lower())==sorted(str2.lower()):
  print("Anagram")
else:
  print("Not Anagram")
  
