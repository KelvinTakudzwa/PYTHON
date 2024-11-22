import hashlib

rainPassword = [None]*10
rainHash = [None]*10
i=0
j=0
user_input = input("ENTER YOUR PASSWORD:")
user_input = rainPassword[i]

def hashCode(rainPassword) :
    h = hashlib.new("SHA256")
    h.update(rainPassword[i].encode())
    input_hash = h.hexdigest
    input_hash = rainHash[j]

print(rainHash,rainPassword)