# Script that checks if a text string is a palindrome

# Function that checks if a text is a palindrome
def isPalindrome(text):
  start = 0
  end = len(text) - 1
    
  while text[start] == text[end]:
    if start >= end:
      return True

    start += 1
    end -= 1

  return False

# Function that checks if a text is a palindrome in a recursive way.
def isPalindromeRecursive(text, start, end):
  if start >= end:
    return True
  
  if text[start] == text[end]:
    return isPalindromeRecursive(text, start + 1, end - 1)
  
  else:
    return False

# Function that takes care of replacing special characters
def replaceSpecialCharacters(text):
  text = text.lower() # Convert text to lowercase
  
  # Replace the following characters
  text = text.replace(" ", "")
  text = text.replace("á", "a")
  text = text.replace("é", "e")
  text = text.replace("í", "i")
  text = text.replace("ó", "o")
  text = text.replace("ú", "u")

  return text

# Store the value entered by the user in a variable
text = str(input("Please enter a text to check if this is a palindrome: "))

# Call the function to replace special characters in the text
normalizedText = replaceSpecialCharacters(text)

# Check if is palindrome without recursive function
print("\nWithout recursive function:")

if isPalindrome(normalizedText):
  print("The character sequence '{}' is a palindrome.".format(text))

else:
  print("The sequence of characters '{}' is not considered a palindrome.".format(text))

# Check if is palindrome with recursive function
print("\nWith recursive function:")

if isPalindromeRecursive(normalizedText, 0, len(normalizedText) - 1):
  print("The character sequence '{}' is a palindrome.".format(text))

else:
  print("The sequence of characters '{}' is not considered a palindrome.".format(text))