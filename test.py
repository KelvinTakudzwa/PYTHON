# Adding the plaintext password and its hash to the rainbow table
with open(rainbow_table_file, 'a') as f:  # Open the file in append mode
    f.write(f"{password}:{hashed_password}\n")  # Write the new entry
print("Added to the rainbow table.")