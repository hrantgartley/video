import os
from random import randint

from genericpath import exists


def main():
    path: str = os.getcwd()
    path: str = os.path.join(path, 'gront')
    os.mkdir('gront' + str(randint(1, 2)))

    user_choice: str = input("would you like to make another directory: (y/n)")
    if user_choice.lower() == 'y' and exists(path):
        print("Directory already exists")
    else:
        os.mkdir(path + str(randint(1, 2)))
        print("Directory created")


if __name__ == "__main__":
    main()
