import datetime


def return_choice():
    """
        Method for taking user Input for return option
    """
    print("\n")
    print("Enter Y or Yes if you want to continue or else for exit to main Menu.")
    return_option = input("Please Enter your Choice : ")

    # condition to check user choice
    if return_option.upper() == "Y" or return_option.upper() == "YES":
        return True
    else:
        return False


def validate(date_text):
    """
        Method to Validate Entered Date
    """
    try:
        datetime.date.fromisoformat(date_text)
        return True
    except ValueError:
        return False


class Tournament:
    """
        Class for displaying All Tournament Menu
    """

    def tournament_menu(self):
        """
            Display tournament main menu and call user's choice
        """

        while True:
            # Displaying the main menu options
            print("Tournament Menu".center(40, "-"))
            print("1. Create Tournament : ")
            print("2. List All Tournaments.")
            print("3. Tournaments Details.")
            print("4. Add Player in Tournament : ")
            print("5. List All Player in Tournament.")
            print("6. List of all completed round and matches of round.")
            print("7. Create Match Schedule for current round : ")
            print("8. Update Match Result : ")
            print("9. Get Score.")
            print("10. View Tournament with Date.")
            print("0. Exit.")
            print("\n")
            # Getting user input for menu choice
            choice = input("Please Enter your choice : ")

            # Validating user input
            if choice in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "0"]:

                if choice == "1":
                    tournament_data = self.create_tournament()
                    tournament_data["choice"] = "1"
                    return tournament_data

                elif choice == "2":
                    return {"choice": "2"}

                elif choice == "3":

                    # Getting tournament details based on ID
                    tournament_id = input("Enter the tournament ID : ")

                    return {"choice": "3",
                            "tournament_id": tournament_id}

                elif choice == "4":

                    # Adding player to a tournament
                    tournament_id = input("Enter tournament ID to add player : ")
                    print("\n Please check the all available players from Player Menu.")
                    player_id = input("Enter player ID to add in tournament : ")
                    return {"choice": "4",
                            "tournament_id": tournament_id,
                            "player_id": player_id}

                elif choice == "5":

                    # Listing players for a specific tournament
                    tournament_id = input("Enter tournament ID to get Player Details : ")
                    print("\n")
                    print("List of players for tournament {}".format(tournament_id))
                    print("\n")

                    return {"choice": "5",
                            "tournament_id": tournament_id}

                elif choice == "6":

                    # Getting fixture details for a tournament
                    tournament_id = input("Enter tournament ID to get Tournament Match Details : ")
                    return {"choice": "6",
                            "tournament_id": tournament_id}

                elif choice == "7":

                    # Creating fixture for the current round
                    tournament_id = input("Enter tournament ID to Create match schedule : ")
                    return {"choice": "7",
                            "tournament_id": tournament_id}

                elif choice == "8":

                    # Updating match result
                    tournament_id = input("Enter tournament ID to Update Match : ")
                    return {"choice": "8",
                            "tournament_id": tournament_id}

                elif choice == "9":

                    # Getting tournament score
                    tournament_id = input("Enter tournament ID to Get Score : ")
                    return {"choice": "9",
                            "tournament_id": tournament_id}

                elif choice == "10":

                    # getting tournament details with date
                    tournament_id = input("Enter the tournament ID : ")
                    return {"choice": "10",
                            "tournament_id": tournament_id}

                elif choice == "0":
                    return {"choice": "0"}

            else:
                print("Invalid choice. Please try again!")

            if not return_choice():
                return {"choice": "0"}

    @staticmethod
    def create_tournament():
        """
            Method to create tournament data in JSON file
        """

        # Prompting user for tournament details
        print("Please Enter Below Details".center(40, "-"))

        # Getting tournament name from user
        name = input("Enter the Name of Tournament : ")

        # Getting tournament location from user
        location = input("Enter Tournament Location : ")

        # Validating and getting tournament start date from user
        while True:
            start_date = input("Enter Tournament Start Date in YYYY-MM-DD : ")
            if validate(start_date):
                break

        # Validating and getting tournament end date from user
        while True:
            end_date = input("Enter Tournament End Date in YYYY-MM-DD : ")
            if validate(end_date):
                if datetime.datetime.strptime(start_date, "%Y-%m-%d") > datetime.datetime.strptime(end_date,
                                                                                                   "%Y-%m-%d"):
                    print("Tournament End Date is Before Start Date!")
                else:
                    break

        # Validating and getting the number of rounds from user
        while True:
            no_of_rounds = input("Enter Tournament Total Rounds : ")
            if no_of_rounds.isnumeric():
                break
            else:
                print("Enter in Number : ")

        # Getting tournament description from user
        description = input("Enter Tournament Description : ")

        # Saving tournament data using the controller
        return {
            "name": name,
            "location": location,
            "start_date": start_date,
            "end_date": end_date,
            "description": description,
            "no_of_rounds": no_of_rounds
        }

    @staticmethod
    def display_score(data):
        """
            Display scores from the provided data.

            Parameters:
            - data (list): A list of dictionaries representing the scores for each round or category.
                           Each dictionary should have a single key representing the round or category,
                           and the corresponding value is another dictionary with player names and scores.

            Returns:
            None
        """

        for score_row in data:

            # Print a horizontal line as a separator
            print("".center(60, "-"))

            # Extract the key (e.g., round number or category) for the current score row
            display_key = list(score_row.keys())[0]

            # Print the display key (e.g., round number or category)
            print(display_key)

            # Iterate through each player in the current score row and display their name and score
            for name in score_row[display_key]:
                print("{} ==> {}".format(name, score_row[display_key][name]))

    @staticmethod
    def display_result(data):
        """
            Display tournament results including match details and round information.

            Args:
                data (list): List of dictionaries containing match and round information.

            This method takes a list of dictionaries as input, where each dictionary represents a tournament round with
            match details. It iterates through the data, printing information about each round and its corresponding
            matches,
            including match ID, players, completion status, winner, and result.

            Example:
            result_data = [
                 {"tournament_round": 1, "completed": True, "1": {"player1": "John", "player2": "Jane", "completed":
                 True, "winner": "John", "result": "2-1"}},
                 {"tournament_round": 2, "completed": False, "2": {"player1": "Bob", "player2": "Alice", "completed":
                 False, "winner": None, "result": None}},
                 # ... additional rounds and matches
            ]
            display_result(result_data)
            ------------------------------------------------------------
            Tournament Current Round ==> 1
            current round completed ==> True
            ------------------------------
            Match ID ==> 1
            Player1 ==> John
            Player2 ==> Jane
            Completed ==> True
            Winner ==> John
            Result ==> 2-1
            ------------------------------------------------------------
            Tournament Current Round ==> 2
            current round completed ==> False
            ------------------------------
            Match ID ==> 2
            Player1 ==> Bob
            Player2 ==> Alice
            Completed ==> False
            Winner ==> None
            Result ==> None
            ------------------------------------------------------------

        """

        # Iterate over each row in the data
        if data:
            for match_row in data:

                # Print a separator line for better readability
                print("".center(60, "-"))

                # Display information about the tournament round
                print("Tournament Current Round ==> {}".format(match_row["tournament_round"]))
                print("current round completed ==> {}".format(match_row["completed"]))

                # Iterate over each match in the current round
                for match_number in list(match_row.keys()):

                    # Check if the match_number is numeric (to filter out non-match keys)
                    if match_number.isnumeric():
                        # Print a separator line for each match
                        print("".center(30, "-"))

                        # Display information about the match
                        print("Match ID ==> {}".format(match_number))
                        print("Player1 ==> {}".format(match_row[match_number]["player1"]))
                        print("Player2 ==> {}".format(match_row[match_number]["player2"]))
                        print("Completed ==> {}".format(match_row[match_number]["completed"]))
                        print("Winner ==> {}".format(match_row[match_number]["winner"]))
                        print("result ==> {}".format(match_row[match_number]["result"]))
        else:
            print("Tournament dose not Exist")

    @staticmethod
    def display_tournament(data):
        """
            Method to display Tournament display.
        """
        print("".center(60, "-"))
        for key_name in data:
            print("{} ==> {}".format(key_name, data[key_name]))

    def display_all_tournament(self, tournament_list):
        """
        Display details of all tournaments.

        Parameters:
        - tournament_list (list): A list containing tournament details.

        Returns:
        None
        """
        # Print a separator line
        print("".center(60, "-"))

        # Iterate through each tournament in the list and print its details
        for tournament in tournament_list:
            print(tournament)

    def list_tournament_player(self, player_list):
        """
        Display a list of tournament players.

        Parameters:
        - player_list (list): A list containing player details.

        Returns:
        None
        """

        # Iterate through each player in the list and print their details
        for player in player_list:
            print(player)

            # Print a separator line after each player's details
            print("".center(60, "-"))

    def display_tournament_details(self, tournament_details):
        """
        Display details of a tournament with Start date and End date.

        Parameters:
        - tournament_details (str): Details of the tournament to be displayed.

        Returns:
        None
        """
        # Print the tournament details with start date and end date
        print(tournament_details)

    def display_tournament_score(self, tournament_score):
        """
        Display the score of a tournament.

        Parameters:
        - tournament_score (tuple): A tuple containing tournament completion status and scores.
          - tournament_score[0] (dict): Dictionary containing player scores.
          - tournament_score[1] (bool): True if the tournament is completed, False if ongoing.

        Returns:
        None
        """

        # Check if the tournament is completed or ongoing and print the corresponding message
        if tournament_score[1]:
            print("Tournament is Completed.")
        else:
            print("Ongoing Tournament.")

        # Display the scores using the provided display_score method
        self.display_score(tournament_score[0])

    def display_tournament_not_exist(self, data):
        """
        Response message indicating that the tournament does not exist or has not been created.

        Parameters:
        - data (int): An integer indicating the reason for non-existence or incorrect ID.
          - 1: Tournament does not exist or has not been created.
          - 2: Incorrect Tournament ID.

        Returns:
        None
        """
        # Check the value of 'data' and print the corresponding message
        if data == 1:
            print("Tournament dose not exist/created.")
        elif data == 2:
            print("Tournament ID is incorrect, Please enter correct ID")

    def print_message(self, message):
        """
        Print the provided message.

        Parameters:
        - message (str): The message to be printed.

        Returns:
        None
        """
        print(message)
