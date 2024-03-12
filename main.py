import os

def generate_key(passphrase):
    pass

def save_key(key):
    with open("./KEY.txt", "w") as key_file:
        key_file.write(key)

def load_key():
    with open("./KEY.txt") as key_file:
        return key_file.read()

def encrypt(file, key, out_file):
    pass

def decrypt(file, key, out_file):
    pass

def main():

    while True:
        print()
        selector = input("1) Load Key \n2) Generate Key \n3) Exit")

        if selector == "1":
            key = load_key()
            break
        elif selector == "2":
            passphrase = input("Enter your passphrase: ")

            key = generate_key(passphrase)

            print(f"Your key is {key}")

            save = input("Would you like to save it? (y/n)")

            if save == "y" or save == "yes":
                save_key(key)
            break
        elif selector == "3":
            exit()
        else:
            print("\n Bad input")

    while True:
        print()
        selector = input("1) Encrypt \n2) Decrypt \n3) Exit \n")

        if selector == "1":

            filename = input("\nEnter file name in files plaintext folder: ")
            path = f"./files/plaintext/{filename}"
            out_path = f"./files/encrypted/{filename}.enc"

            encrypt(path, key, out_path)

            print(f"\nThe file: {filename} has been encrypted at destination {out_path} with the key {key}")

        elif selector == "2":

            filename = input("Enter file name in files encrypted folder: ")
            path = f"./files/encrypted/{filename}"
            out_path = f"./files/decrypted/{filename}.txt"

            print(f"\nThe file: {filename} has been decrypted at destination {out_path} with the key {key}")

            encrypt(path, key, out_path)

        elif selector == "3":
            exit()
        else:
            print("\nBad Input")

if __name__ == "__main__":
    main()
