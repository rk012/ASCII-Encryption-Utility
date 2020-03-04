import random

def encrypt(seed, message):
  random.seed(seed)
  encryptedmessage=""
  for i in range(0, len(message)):
    encryptedmessage = encryptedmessage+chr((((ord(message[i])-32)+random.randint(0, 95))%96)+32)

  return encryptedmessage

def decrypt(seed, encryptedmessage):
  random.seed(seed)
  message=""

  for i in range(0, len(encryptedmessage)):
    message = message+chr((((ord(encryptedmessage[i])-32)-random.randint(0, 95))%96)+32)

  return message

def main():
  print("ASCII Encryption Utility\n")
  print("0. Exit")
  print("1. Encrypt text")
  print("2. Decrypt text\n")
  print("Please select an option:")
  choice = input()

  if(choice == "0"):
    pass
  elif(choice == "1"):
    print("Enter message to be encrypted:")
    message = input()
    print("Enter seed")
    seed = input()
    print("Encrypted message:\n"+encrypt(seed, message)+"\n\n")
    main()
  elif(choice == "2"):
    print("Enter message to be decrypted:")
    encryptedmessage = input()
    print("Enter seed")
    seed = input()
    print("Decrypted message:\n"+decrypt(seed, encryptedmessage)+"\n\n")
    main()
  else:
    print(choice)
    print("invalid choice\n\n")
    main()


main()
