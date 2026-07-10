import string
def isPalindrome(str):
    # gera uma lista de caracteres que são pontuações '!', '.', ',', ':', etc.
    exclude = set(string.punctuation)
    
    # vefifica se na str tem algum caracter na lista e troca ele por ''
    ## detalhe: se na palavra tiver um espaço vazio, ele não está na lista, então permanece lá.
    str=''.join(ch for ch in str if str not in exclude)
    
    # troca os espaços vazios por nada
    str=str.replace(" ", "").lower()
    
    ## agora vefifica se o texto lido de trás para frente continua igual
    if (str==str[::-1]):
        return True
    else: return False

# Prompt the user to enter the sentence
def main():
  userInput = input("Enter a WORD to be tested as a palindrome: ")

  if (isPalindrome(userInput)):
    print(userInput + " is a palindrome!")
  else:
    print(userInput + " is NOT a palindrome!")

if __name__ == "__main__":
    main()
