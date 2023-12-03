from views.player import Player
from views.tournament import Tournament


def main():

    while True:
        print("".center(60,"-"))
        print("1. Tournament Menu")
        print("2. Player Menu")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            view = Tournament()
            view.tournament_menu()
        elif choice == "2":
            view = Player()
            view.player_menu()
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
