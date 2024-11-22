import hashlib

h = hashlib.new("SHA256")
correct_password = "Mukaro12345"

h.update(correct_password.encode())
password_hash = h.hexdigest()
print(password_hash,"\n")

user_input = input("ENTER YOUR PASSWORD:")
h = hashlib.new("SHA256")
h.update(user_input.encode())
input_hash = h.hexdigest
print(input_hash)
#print(h.digest)
if input_hash == password_hash:
    print("AUNTHENTICATED\n")
    print(correct_password)
else:
    print("wrong password")

 
        