import os

def main():
    """The main function which executes the script"""
    files = os.listdir()
    print(files)

# This is a useful guard to ensure code is only executed when it is being run as the main program and not when imported into another module
if __name__ == '__main__':
    main()