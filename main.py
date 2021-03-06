#Ighoise Odigie
#One-Day
#May, 5 2020
#Youtube: https://www.youtube.com/channel/UCud4cJjtCjEwKpynPz-nNaQ?
#Github: https://github.com/Iggy-o
#Preview: https://repl.it/@IghoiseO/Password-Validator

#<!--First Part: The Settings-->
#This prints out the program Header
header = "--Password Validator--"
print(header)

#This variable controls the number of times the password can be entered
attempts = 4

#These variables control the requirements for the password
''' 
Note: -Try modifying these settings to your liking
      -You can set them to 0 to turn them off
      -Mess around and Have Fun!!
'''
lengthRequirement = 8
numberRequirement = 1
capitalRequirement = 1
lowercaseRequirement = 1
specialRequirement = 1

specialCharacters = '!#$%&()*+-./:;<=>?@[\]^_`{|}~'
bannedCharacters = ' '

#These variables store the user prompts and messages which will be used later
password_text = "\nPassword -> "
validPassword_text = "\n\n--Password Valid--"
requirements_text = f"\n-{lengthRequirement} or more character(s)\n-{numberRequirement} number(s)\n-{capitalRequirement} capital letter(s)\n-{lowercaseRequirement} lowercase letter(s)\n-{specialRequirement} special character(s)\n-No prohibited characters (Ex. Spaces)"
invalidPassword_text = f"--\nYour password must contain the following: {requirements_text}\n--"
passwordConfirmation_text = "Please repeat your password once more to confirm -> "
passwordConfirmed_text = "\n\n--Password Confirmed--"
passwordDifferent_text = "\n\n--Password did not match--"
lockedOut_text = "\n!!!Too many failed attempts, please try again later!!!"



#<!--Second Part: Validation-->
#Loops through the validation process until the maximum number of attempts are reached 
for i in range(attempts):
  
  #The user is asked for a password which will be later verified
  password = str(input(password_text))
  
  #This variable checks the length of the password
  lengthCheck = len(password) >= lengthRequirement
  
  #This variable becomes True if the password contains a number
  numberCheck = False
  
  #This variable becomes True if the password contains a capital letter
  capitalCheck = False

  #This variable becomes True if the password contains a special character
  lowerCheck = False

  #This variable becomes True if the password contains a special character
  specialCheck = False
  
  #This variable becomes False if the password contains a banned character
  bannedCheck = True

  #Loops through each character in the password in search of numbers or capital letters
  numbers = 0
  capitals = 0
  lowercase = 0
  specials = 0
  for i in range(len(password)):
    
    #If the number of numbers in the string reaches the requirement, numberCheck becomes True
    if (password[i].isdigit() or numberRequirement == 0):
      numbers += 1
      if (numbers >= numberRequirement):
        numberCheck = True
      
    #If the number of capital letters in the string reaches the requirement, capitalCheck becomes True
    if (password[i].isupper() or capitalRequirement == 0):
      capitals += 1
      if (capitals >= capitalRequirement):
        capitalCheck = True
    
    #If the number of lowercase letters in the string reaches the requirement, lowerCheck becomes True
    if (password[i].islower() or lowercaseRequirement == 0):
      lowercase += 1
      if (lowercase >= lowercaseRequirement):
        lowerCheck = True
    
    #If the number of special letters in the string reaches the requirement, specialCheck becomes True
    if (password[i] in specialCharacters or specialRequirement == 0):
      specials += 1
      if (specials >= specialRequirement):
        specialCheck = True

    #If their are any banned characters, bannedCheck becomes False
    if (password[i] in bannedCharacters):
      bannedCheck = False
  
  #The requirements are compiled into this variable which will return true or false in the verification process
  requirements = lengthCheck and numberCheck and capitalCheck and lowerCheck and specialCheck and bannedCheck
  
  #If the password meets the requirments, it is marked as valid and the loop is broken
  if (requirements):
    valid = True
    print(validPassword_text)
    break
  
  #If the password does not meet the requirements, the loop continues and the user must enter a new password
  else:
    valid = False
    print(invalidPassword_text)



#<!--Third Part: Confirmation-->
#If the password is still invalid after the attempts have expired, it prints the locked out text
if (valid == False):
  print(lockedOut_text)

#If the password is valid, it must be confirmed
elif (valid == True):

  #Loops through the validation of the repeated password until the maximum attempts are reached
  for i in range(attempts):
    
    #The user is asked to confirm their password
    passwordConfirmation = str(input(passwordConfirmation_text))
    
    #If the repeated password matches the user entry, the loop is broken 
    if (passwordConfirmation == password):
      match = True
      print(passwordConfirmed_text)
      break
    
    #If the password does not match, the user is prompted to try again until the max attempts are met
    else:
      match = False
      print(passwordDifferent_text)
   
  #If the user failed to match the password they are locked out
  if (match == False):
    print(lockedOut_text)
  
  #If the user matches the password, they recieve confirmation
  else:
    print(f"Your password: {password}")
    
    
    
#<!--Program Complete-->
