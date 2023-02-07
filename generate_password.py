# Module to generate password

# Import the random module
import random

# DEFINE SETTINGS
MIN_PASSWORD_LENGTH = 6

# Create the content that will populate the passwords
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# Set the lowercase letters by lowercasing all the uppercase letters
lowercase_letters = uppercase_letters.lower()
digits = "0123456789"
special_characters = "!@#$%^&*()_+=-}{[]':;<,>.?/~`"

# Function to join two strings together
def remove_spaces(str):
  return str.replace(" ", "")

# Function to shuffle a string
def shuffle_str(str):
  shuffled_str = ''.join(random.sample(str, len(str)))
  return shuffled_str

# Function to randomize the upper and lower case of a string
def randomize_caps(str):
  # Create a new string with all uppercase of the str argument
  all_upper = str.upper()
  # Create a new string with all lowercase of the str argument
  all_lower = str.lower()

  # For each character in the string pair a lowercase and uppercase
  # Select either lower or uppercase at random
  return ''.join(random.choice(x) for x in zip(all_upper, all_lower))

# Function to split a string
def split_str(str):
  first_part, second_part = str[:len(str)//2], str[len(str)//2:]
  return [first_part, second_part]

# Function to create password by putting the input at the end of the password
def suffix_input(input, pwd):
  return pwd + input

# Function to create password by putting the input in the middle of the password
def sandwich_input_str(input, pwd):
  # Split the pwd
  split_pwd = split_str(pwd)

  # Place the input str in the middle
  return split_pwd[0] + input + split_pwd[1]

# Function to create password by putting the password in the middle of the input
def sandwich_random_str(input, pwd):
  # Split the input word/phrase
  split_input = split_str(input)

  # Place the randomized password in the middle
  return split_input[0] + pwd + split_input[1]

# Function to generate passwords
def generate_password(args, input):
  characters = ""
  temp_password = ""

  # randomly select at least one character from each character set above
  random_digit = random.choice(digits)
  random_upper = random.choice(uppercase_letters)
  random_lower = random.choice(lowercase_letters)
  random_symbol = random.choice(special_characters)

  # If lowercase is true then add a random lowercase to the temporary password
  if(args["lowercase"]):
    temp_password += random_lower
    characters += lowercase_letters

  # If uppercase is true then add a random digit to the temporary password
  if(args["uppercase"]):
    temp_password += random_upper
    characters += uppercase_letters

  # If numbers is true then add a random number to the temporary password
  if(args["numbers"]):
    temp_password += random_digit
    characters += digits

  # If symbols is true then add a random special character to the temporary password
  if(args["symbols"]):
    temp_password += random_symbol
    characters += special_characters

  # Set the password as 12 if there is no input from user
  max_length = MIN_PASSWORD_LENGTH if len(input) > 0 else 12

  # Add the required length of random characters to complete the random string
  for x in range(max_length - len(temp_password)):
    temp_password += random.choice(characters)

  # Shuffle the temporary password to avoid patterns at the beginning
  temp_password = shuffle_str(temp_password)

  # Randomize the case of the input
  input_str = remove_spaces(input)
  input_str = randomize_caps(input_str)

  # Create three different passwords using the three different patterns
  pattern1Password = sandwich_random_str(input_str, temp_password)
  pattern2Password = suffix_input(input_str, temp_password)
  pattern3Password = sandwich_input_str(input_str, temp_password)

  # Select one password to return from the three different patters at random
  password = random.choice([pattern1Password, pattern2Password, pattern3Password])

  # If the password selected is below 8 characters, maybe because of user input then
  # Add random characters to the password
  if (len(password) < 8):
    for x in range(8 - len(password)):
      password+= random.choice(characters)

  # Return the password
  return password
