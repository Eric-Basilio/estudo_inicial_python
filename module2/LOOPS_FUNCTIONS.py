# LEARNING FOR LOOP
for i in range(10):
  print(i)
## FOR LOOP WHIT INCREMENT OTHER THEN + 1
for i in range(0, 10, 3):
  print(i)

### FOR EACH
for i in "hello!":
  print(i)

#### FOR EACH WITH VARIABLE
string = "hello world!"
for i in range(0, len(string), 2):
  print(str(i) + "th letter is "+ string[i])

##### WHILE LOOP
while (count < 10):
  print(count)

  # IMPORTANT!!! Updating the counter!
  count += 1

###### WHILE WITH VARIABLE
while True:
  user = input("Enter something to be repeated: ")

  ## When break is triggered, the print() below will NOT run
  ## The program will break out of the loop when this keyword is read. 
  if user=="end":
    print("Terminate the program!!!")
    break
  print(user)

###### BREAKING WORDS 'CONTINUE' OR BREAK
count = 1

# WHILE loop implementation
while count + 1 <= 20:
  if count % 5 == 0:
    print("SKIP")
    count += 1
    continue
  print(count)
  count += 1

####### FUNCTION

def isRightTriangle(a, b, c):

  # Reassign variable values to ensure c is the longest length
  if (max(a,b,c) != c):

    # tmp stores the previous c values, that's not the longest length
    tmp = c
    c = max(a,b,c)

    if a == c:
      a = tmp
    elif b == c:
      b = tmp
    

  # Apply the formula  
  if a**2 + b**2 == c**2:
    print("Right Triangle")

    # If the program sees a return statement, this is the END of the program/function
    return True
  
  # These two lines will ONLY run when the IF condition is false
  print("NOT a right triangle")
  return False


# Prompt the user to enter 3 lengths
def main():
  a = input("Enter the length for the first edge of the traingle:")
  b = input("Enter the length for the second edge of the traingle:")
  c = input("Enter the length for the last edge of the traingle:")

  # User inputs are stored as a string, so we cast them to be int
  return isRightTriangle(int(a), int(b), int(c))

if __name__ == "__main__":
    main()

===========================================================================================

## exercício

import string
def isPalindrome(str):
    # gera uma lista de caracteres que são pontuações '!', '.', ',', ':', etc.
    exclude = set(string.ponctuation)
    
    # vefifica se na str tem algum caracter na lista e troca ele por ''
    ## detalhe: se na palavra tiver um espaço vazio, ele não está na lista, então permanece lá.
    str=''.join(ch for ch in str if str not in exclude)
    
    # troca os espaços vazios por nada
    str=str.replace(" ", "").lower()
    
    ## agora vefifica se o texto lido de trás para frente continua igual
    if (str==str[::-1]):
        return true
    else return false

# Prompt the user to enter the sentence
def main():
  userInput = input("Enter a WORD to be tested as a palindrome:")

  if (isPalindrome(userInput)):
    print(userInput + " is a palindrome!")
  else:
    print(userInput + " is NOT a palindrome!")

if __name__ == "__main__":
    main()
