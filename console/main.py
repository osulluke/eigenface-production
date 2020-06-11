import sys


def main():
    # Declare variables to be used
    active = 1

    # Display menu
    while active == 1:
        print("Welcome to EigenFace Filter v1.0")
        print("Release Date: 2020 June 11")
        print("Brought to you by 'Oh My Py'\n")

        # Loop back to menu selection on invalid entry
        while 1 == 1:
            try:
                # Get user menu selection
                print("Main Menu")
                print("-----------------")
                print("1. Upload video file (mpeg4)")
                print("2. View Data")
                print("3. About this software")
                print("4. Exit\n")
                menu_selection = int(input("Please make a selection (1-4): "))
            except ValueError:
                menu_selection = -1

            if menu_selection < 0 or menu_selection > 4:
                print("\nUnrecognized menu selection!\n")
                continue

            if menu_selection == 1:
                print("-----------------")
                print("Upload video file")
                file_path = ("Enter path to video (ex: ./test.mp4): ")
                print("Loading video at " + file_path + ".....\n")

            if menu_selection == 2:
                print("-----------------")
                print("Data Table")
                print("")

            if menu_selection == 3:
                print("-----------------")
                print("About this software")

            if menu_selection == 4:
                print("\nExiting EigenFace Filter")
                sys.exit(0)

if __name__ == "__main__":
    main()