rainbow_table = {}

def load_rainbow_table(file_path):
    with open(file_path, 'r') as file:
        for line in file:

            hash_value, password = line.strip().split(':')
            rainbow_table[hash_value] = password


rainbow_table_file = "rainbow_table.txt"  
load_rainbow_table(rainbow_table_file)

target_hash = "hash_of_target_password"
recovered_password = rainbow_table.get(target_hash)

if recovered_password:
    print("Password recovered:", recovered_password)
else:
    print("Password not found in the rainbow table.")
    