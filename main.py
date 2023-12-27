from controllers.tournament import Tournament_controller
from controllers.player import Player_controller


def main():

    while True:
        print("".center(60, "-"))
        print("1. Tournament Menu")
        print("2. Player Menu")
        print("0. Exit")
        print("\n")
        choice = input("Enter your choice: ")
        print("\n")
        if choice == "1":
            tournament_controller = Tournament_controller()
            tournament_controller.tournament_options()
        elif choice == "2":
            player_controller = Player_controller()
            player_controller.player_menu()
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
