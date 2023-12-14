from controllers.player import Player_controller


def validate_id(chess_id):
    """
        Validate a chess ID based on specific criteria.

        Args:
            chess_id (str): The chess ID to be validated.

        Returns:
            bool: True if the chess ID is valid, False otherwise.

        This function validates a chess ID based on the following criteria:
        1. The ID must be exactly 7 characters long.
        2. The first two characters must be alphabetic.
        3. The remaining characters (from index 2 onward) must be numeric.

        Returns True if all criteria are met; otherwise, it returns False.

        Example:
        validate_id("AB12345")
        False
        validate_id("AB123456")
        True
    """

    # Check if the length of the chess ID is exactly 7 characters
    if len(chess_id) != 7:
        return False

    # Check if the first two characters are alphabetic
    elif not chess_id[:2].isalpha():
        return False

    # Check if the remaining characters (from index 2 onward) are numeric
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
            Display player main menu and handle user's choices.

            This method presents a menu for player-related actions, including options
            to create a player profile, list all players, view a player profile, or exit.
            The user's choice is then processed accordingly by calling the respective
            methods. The loop continues until a valid choice is made.

            :return: False if the user chooses to exit, otherwise calls the
                     corresponding player-related method based on user's choice.
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
            Method to gather and store player information in a JSON file.

            This method guides the user through entering details such as the player's
            national chess ID, first name, last name, and date of birth. The entered
            data is then validated, and if valid, the information is saved using the
            controller's save_player method, which writes the data to a JSON file.

            :return: None
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
            Method to retrieve and display a list of all players from the JSON file.

            This method calls the controller's list_all_player method to retrieve a
            list of all player data from the associated JSON file. If the player list
            is not empty, it iterates through the list and prints each player's details.
            Finally, the method returns False to indicate that the operation is complete.

            :return: False
        """

        print("".center(40, "-"))

        # Retrieve the list of all players from the controller
        player_list = self.controller.list_all_player()

        # If the player list is not empty, print each player's details
        if player_list:
            for i in player_list:
                print(i)

        return False

    def player_view(self):
        """
            Method to view details of a specific player based on their ID.

            This method prompts the user to input a player ID (e.g., AB12345) and
            then calls the controller's get_player_profile method to retrieve and
            print the details of the specified player. The method returns False
            to indicate the completion of the operation.

            :return: False
        """

        print("".center(40, "-"))

        # Prompt the user to enter the player ID
        player_id = input("Please Enter the player ID(ex:AB12345) : ")

        # Call the controller's method to get player details and print them
        print(self.controller.get_player_profile(player_id))
        return False
