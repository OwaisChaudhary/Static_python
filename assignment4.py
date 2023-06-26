#Loop manupulation with break
print("\nLoop manupulation with break:")
for a in range(1,11):
     if a==3:
         break
     else:
         print(a)

#Loop manupulation with continue
print("\nLoop manupulation with comtinue:")
for b in range(1,11):
     if b==3:
         continue
     else:
         print(b)

#Loop manupulation with pass
print("\nLoop manupulation with pass:")
for c in range(1,11):
     if c==3:
         pass
     else:
         print(c)

# For loop with else 
print("\nFor loop with else:")
for m in range(1,11):
     print(m)
else:
     print("There is no break statement.")

#While loop with else
print("\nWhile loop with else:")
i=5
while i>=5:
     print(i)
     i-=1
else:
     print("There's no break statement.")

