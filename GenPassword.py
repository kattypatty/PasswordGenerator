# This program generate the string password with length of 12 
#  concatenation of letters lowercase and uppercase letters
# the numbers 0 to 9
# the string of all special characters

import random
import string

def password_gen():
  letters = string.ascii_letters
  numbers = string.digits
  spec_char = string.punctuation

  # to get password 
  password = letters + numbers + spec_char
  
  passw_rand = ' '
  passw_length = 12
  for i in range (passw_length):
    passw_rand += ' '.join(random.choice(password))

  return passw_rand

print("Your generated password is:", password_gen())