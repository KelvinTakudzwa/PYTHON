
def check_palindrome(word: str):
    control = -1
    while control != -len(word):
        for i in word:
            if i != word[control]:
                return"not a palindrome"
            control = control - 1
        return "is palindrome"
        
print(check_palindrome("rar")) 
    
    
    