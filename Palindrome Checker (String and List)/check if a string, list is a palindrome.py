##Checking if a string is a palindrome

word= input("Enter a word: ").lower().strip()

if word[::-1]==word:
    print(word, "is a palindrome")

else: 
    print(word, 'is not a palindrome')


##Checking if a list with integers is palindrome

grp= list(map(int,input("Enter the numbers separated by commas: ").split(',')))

grp2= grp.copy()
grp2.reverse()

if grp==grp2:
    print("The given list is a palindrome")

else: 
    print('This list is not a palindrome')

##Checking if a list with strings is a palindrome

band= [item.strip().lower() for item in input("Enter the words separated by commas: ").split(',')]

band2= band.copy()
band2.reverse()

if band==band2:
    print("This list is a palindrome")

else:
    print('This list is not a palindrome')


"""

The code to check if the list is a palindrome or not, for both strings and integers,
is written in different format, the bottom one being the cleaner and more effective one in
my opinion. To take the input for integers the same way, we do: 

grp= [int(item.strip()) for item in input("Enter the numbers separated by commas: ").split(',')]

"""

# Also, we do not need to create band2/grp2 as there is a a better way to compare lists.
# grp==grp[::-1] and band==band[::-1] . Just like when we checked if a string is a palindrome. 