word= input("Enter a word: ").strip().lower()

vowels= ['a','e', 'i','o', 'u']

vowel_count=0
conso_count=0

for i in range(0,len(word)):
    if word[i].isalpha():
        if word[i] in vowels:
            print("This is a vowel")
            vowel_count+=1
    
        else:
            print("This is a consonant")
            conso_count+=1
    
    else:
        print("Not a letter, skipping")

print("There are", vowel_count, "number of vowels")
print("There are", conso_count, "number of consonants")


