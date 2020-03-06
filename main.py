from ascii_encryptor import encrypt, decrypt
from symmetric_encryption_util import PUBLIC_KEY, key_gen

SHARED_KEY = ""

def setup():
    global SHARED_KEY
    print("ASCII Encryption Utility\n")
    print("Send your public key to recipient:")
    print(PUBLIC_KEY)
    print("\nEnter recipient's public key:")
    SHARED_KEY = key_gen(input())
    print("\nSetup Complete")

def main():
    global SHARED_KEY
    print("\n\n")
    print("0. Exit")
    print("1. Encrypt message")
    print("2. Decrypt message\n")
    print("Choose an option:")
    choice = input()
    if choice == "0":
        pass
    elif choice == "1":
        print("Enter message to be encrypted:")
        encryptedmessage=encrypt(SHARED_KEY, input())
        print("Encrypted message:")
        print(encryptedmessage)
        main()
    elif choice == "2":
        print("Enter message to be decrypted:")
        decryptedmessage=decrypt(SHARED_KEY, input())
        print("Decrypted message:")
        print(decryptedmessage)
        main()
    else:
        print("Invalid choice")
        main()

setup()
main()
