import random
import string


pass_len = 10
varchar = string.ascii_letters + string.digits + string.punctuation

password = ""

for i in range(pass_len):
    password += random.choice(varchar)

print("your random password is ", password)

# or

# using the list comprehension  [ function for i in range (n)] 
# password = "".join([random.choice(varchar) for i in range(pass_len)])

# print("your random password is ", password)