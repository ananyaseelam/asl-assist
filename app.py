from camerahands import run_fingerspelling
from detectwords import detect_words

# import camerahands
# import detectwords


def main():
    print("WELCOME TO THE ASL ASSIST APPLICATION")
    print("Please select one of these options by typing 1 or 2 and hitting enter: ")
    print("(1) Detect Fingerspelling ASL: ")
    print("(2) Detect ASL Words: ")
    option = input()

    if option == '1':
        print("Please wait while we load the video camera...")
        run_fingerspelling()
    elif option == '2':
        print("Please wait while we load the video camera...")
        detect_words()


main()
