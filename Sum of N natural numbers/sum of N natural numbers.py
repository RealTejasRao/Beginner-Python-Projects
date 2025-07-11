n= int(input("Enter a number: "))


print('OUTPUT USING FOR LOOP')

sum=0

for i in range(n+1):
    sum+=i
print(sum)

print('OUTPUT USING WHILE LOOP')

j=0
sum2= 0

while j<n:
    j+=1
    sum2+=j
print(sum2)