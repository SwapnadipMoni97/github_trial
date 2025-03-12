def is_palindrome(s):
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned = ''
    for char in s:
        if char.isalnum():
            cleaned += char.lower()
    
    # Check if the cleaned string is equal to its reverse using a for loop
    length = len(cleaned)
    for i in range(length // 2):
        if cleaned[i] != cleaned[length - 1 - i]:
            return False
    return True

# Example usage
if __name__ == "__main__":
    user_input = input("Enter a string to check if it is a palindrome: ")
    print(f"Is the string '{user_input}' a palindrome? {is_palindrome(user_input)}")