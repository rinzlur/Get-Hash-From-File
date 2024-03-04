# Will Smith :: Find A File Hash:

# We need hashLib to handle hashes:
# We also need os to handle the console:
import hashlib
import os

# used to clear the console before starting:
def clearConsole():
    os.system('cls' if os.name == 'nt' else 'clear') 

# def = define function:
def hash(fileName):

    # make a hash of the passed file:
    h = hashlib.sha1()

    # open the file binarily: 
    with open(fileName, 'rb') as file:

        # iterate through the file:
        chunk = 0
        while chunk != b'':
            # read file at consistent 1024 bytes/s:
            chunk = file.read(1024)
            h.update(chunk);

    # Return the hex representation:
    return h.hexdigest();

def main():
    # clear the console before starting:
    clearConsole()
    print("Welcome, please enter a file path:")

    while True:
        try:
            # get filepath from user:
            file_path = input("Enter the path to the file, or 'quit' to quit:")
            # check input before iterating:
            if file_path.lower() == 'quit':
                break

            # get hash value from file and print:
            hash_value = hash(file_path)
            print(f"|---------------------------------------------------------------------------------------------------------|")
            print(f"|  --> FILE: '{file_path}'")
            print(f"|  --> HASH: '{hash_value}' ")
            print(f"|---------------------------------------------------------------------------------------------------------|")
        except FileNotFoundError:
            print(f"|---------------------------------------------------------------------------------------------------------|")
            print(f"|  --> Error: Filepath '{file_path}' is not recognized as a valid path.")
            print(f"|---------------------------------------------------------------------------------------------------------|")

if __name__ == "__main__":
    main()
