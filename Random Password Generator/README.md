## \# Random Password Generator



###### This is a basic Python script that generates a random password using letters, digits, and special characters.  

###### It uses Python's built-in `random` and `string` modules to generate secure, unpredictable passwords.



---



## \## 📌 How it works:



###### 1\. The script creates a pool of characters using:

###### &nbsp;  - Uppercase and lowercase letters (`string.ascii\_letters`)

###### &nbsp;  - Digits (`string.digits`)

###### &nbsp;  - Special characters (`string.punctuation`)



###### 2\. It randomly selects 6 characters from this pool using `random.choices()`



###### 3\. It then prints the password as a single line using `print(i, end='')` inside a loop  

###### &nbsp;  \*(Alternatively, it can use `"".join()` to join the list into a string directly)\*



