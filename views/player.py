from controllers.player import Player_controller


def validate_id(chess_id):
    if len(chess_id) != 7:
        return False
    elif not chess_id[:2].isalpha():
        return False
    elif not chess_id[2:].isnumeric():
        return False
    else:
        return True


class Player:
    """
        Class for player view
    """
    controller = Player_controller()

    def player_menu(self):
        """
            Display player main menu and call user's choices
        """
        while True:
            print("Tournament Menu".center(40, "-"))
            print("1. Create Player Profile.")
            print("2. List All Player. ")
            print("3. View Player Profile.")
            print("0. Exit")

            choice = input("Please Enter your choice : ")
            if choice in ["1", "2", "3", "0"]:
                if choice == "1":
                    return self.create_player()
                elif choice == "2":
                    return self.list_all_player()
                elif choice == "3":
                    return self.player_view()
                else:
                    return False
            else:
                print("Invalid choice. Please try again.")

    def create_player(self):
        """
            Method to create user data in JSON file
        """

        print("Please Enter Below Details".center(40, "-"))
        while True:
            chess_id = input("Enter the player national  chess ID ex- AB12345 : ")
            if validate_id(chess_id):
                break
        first_name = input("Enter player first name : ")
        last_name = input("Enter player last name : ")
        player_bob = input("Enter player date of birth : ")

        # calling save methode to save data into JSON
        self.controller.save_player(chess_id, first_name, last_name, player_bob)

    def list_all_player(self):
        """
            Method to List All Player in JSON file
        """

        print("".center(40, "-"))
        player_list = self.controller.list_all_player()
        if player_list:
            for i in player_list:
                print(i)
        return False

    def player_view(self):
        """
            Menu to View  Player Stats and Update Tournament
        """
        print("".center(40, "-"))
        player_id = input("Please Enter the player ID(ex:AB12345) : ")

        # Calling Method to get player details
        print(self.controller.get_player_profile(player_id))
        return False

