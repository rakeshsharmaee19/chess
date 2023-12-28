
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
                    return {"choice": "2"}
                elif choice == "3":
                    print("".center(40, "-"))

                    # Prompt the user to enter the player ID
                    player_id = input("Please Enter the player ID(ex:AB12345) : ")
                    return {"choice": "3", "player_id": player_id}
                else:
                    return {"choice": "0"}
            else:
                print("Invalid choice. Please try again.")

    @staticmethod
    def create_player():
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

        # Return data in JSON format
        return {
            "chess_id": chess_id,
            "first_name": first_name,
            "last_name": last_name,
            "player_dob": player_bob,
            "choice": "1"
        }

    def view_all_player(self, player_list_data):
        """
        Display details of all players.

        Parameters:
        - player_list_data (list): A list containing player details.

        Returns:
        None
        """

        # Print a separator line
        print("".center(40, "-"))

        # If the player list is not empty, print each player's details
        if player_list_data:
            # Iterate through each player's details and print them
            for i in player_list_data:
                print(i)
        else:
            # Print a message if the player list is empty
            print("Player List is empty.")

    def view_player(self, data):
        """
        Display details of a player.

        Parameters:
        - data (dict): A dictionary containing player details with player IDs as keys.

        Returns:
        None
        """

        # Check if the player details dictionary is not empty
        if data:
            # Iterate through each player's details and print them
            for i in data:
                print("Player {} ==> {}".format(i, data[i]))
        else:
            # Print a message if the player does not exist
            print("Player does not exist.")

    def print_message(self, message):
        """
        Print the provided message.

        Parameters:
        - message (str): The message to be printed.

        Returns:
        None
        """
        print(message)
