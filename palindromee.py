def isPalindrome(string):
    if (string == string[::-1]):
        print("is a palindrome")
    else :
        print("not a palindrome")
        
string = 'rada'
print(isPalindrome(string))        