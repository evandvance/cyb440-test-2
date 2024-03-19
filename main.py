import subprocess
from shutil import which
import glob

MASTERPASSWORD:str = "cryptography"

def is_tool(name:str) -> bool:
    """A function to check if a command line tool is installed

    Args:
        name (str): Name of the command line tool to check for

    Returns:
        bool: If the command line tool is installed the function returns True.
    """
    return which(name) is not None


def run_command(command:list[str]) -> str:
    """Run a command in the shell environment

    Args:
        command (list[str]): The command broken up into a list of strings by word.

    Raises:
        RuntimeError: If the command fails in some way it will end the program and print the commands error on the console

    Returns:
        str: The commands command line output
    """
    output = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if output.returncode != 0:
        raise RuntimeError(output.stderr.decode("utf-8"))

    return output.stdout.decode("utf-8").strip()


def generate_key(passphrase:str) -> str:
    """This function generates a hexkey with some automatically generated salt using the SCRYPT alogrithmn. 


    Args:
        passphrase (str): The passphrase used to help generate entropy in the key generation process

    Returns:
        str: The hexkey
    """
    salt = run_command(["openssl", "rand", "-hex", "16"])
    return run_command(["openssl", "kdf", "-keylen", "32", "-kdfopt", f"hexsalt:{salt}", "-kdfopt", f"pass:{passphrase}", "-kdfopt", "n:65536", "-kdfopt", "r:8", "-kdfopt", "p:1", "SCRYPT"])


def save_key(key:str) -> None:
    """Writes a string to a ./KEY.text but it is used in this program specifically for writing the hexkey

    Args:
        key (str): The hexkey
    """
    with open("./KEY.txt", "w") as key_file:
        key_file.write(key)


def load_key() -> str:
    """A function to load a hexkey from ./KEY.txt.

    Returns:
        str: The key
    """
    with open("./KEY.txt") as key_file:
        return key_file.read()

#TODO ADD support for hashing files and creating MACs


def encrypt_file(input_file:str, output_file:str, key:str) -> None:
    """Encrypts a file using aes-256-cbc and a key

    Args:
        input_file (str): Path to the input file
        output_file (str): Path to the output file
        key (str): Key for encryption
    """
    run_command(["openssl", "enc", "-aes-256-cbc", "-pbkdf2", "-pass", f"pass:{key}", "-in", input_file, "-out", output_file])
    print(f"\nThe file: {input_file} has been encrypted at destination {output_file} with the key {key}")


def decrypt_file(input_file:str, output_file:str, key:str) -> None:
    """Decrypts a file that has been encrypted with aes-256-cbc

    Args:
        input_file (str): Path to the input file
        output_file (str): Path to the output file
        key (str): Key for decryption
    """
    run_command(["openssl", "enc", "-d", "-aes-256-cbc", "-pbkdf2", "-pass", f"pass:{key}", "-in", input_file, "-out", output_file])
    print(f"\nThe file: {input_file} has been decrypted at destination {output_file} with the key {key}")



def encrypt_all(key:str) -> None:
    """A function to encrypt every file in the plaintext folder

    Args:
        key (str): The key used for encryption
    """
    files = [file for file in glob.glob("./files/plaintext/*.txt")]

    for file in files:
        encrypt_file(file, f"./files/encrypted/{file.replace("./files/plaintext/","")}",key)


def decrypt_all(key:str) -> None:
    """A function to decrypt every file in the encrypted folder using a key passed to it

    Args:
        key (str): The key used to encrypt the files
    """
    files = [file for file in glob.glob("./files/encrypted/*.txt")]

    for file in files:
        decrypt_file(file, f"./files/decrypted/{file.replace("./files/encrypted/","")}", key)


def main():
    """The entry point for the program. It creates a command line interface for performing actions."""

    #Rewrite the file pathing for less/more reliable/more readable code
    if not is_tool("openssl"):
        print("Install openssl to continue")
        exit()

    while True:
        print()
        selector = input("1) Load Key \n2) Generate Key \n3) Exit\n")

        if selector == "1":
            key = load_key()
            break
        elif selector == "2":
            passphrase = input("Enter your passphrase: ")

            key = generate_key(passphrase or MASTERPASSWORD)

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

            filename = input("\nEnter file name in files plaintext folder or press enter to do them all: ")

            if filename == "":
                encrypt_all(key)
            else:
                path = f"./files/plaintext/{filename}"
                out_path = f"./files/encrypted/{filename}.enc"

                encrypt_file(path, key, out_path)


        elif selector == "2":

            filename = input("Enter file name in files encrypted folder or press enter to do all: ")

            if filename == "":
                decrypt_all(key)

            else:
                path = f"./files/encrypted/{filename}"
                out_path = f"./files/decrypted/{filename}.txt"

                decrypt_file(path, key, out_path)

        elif selector == "3":
            exit()
        else:
            print("\nBad Input")


if __name__ == "__main__":
    main()
