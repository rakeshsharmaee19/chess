from controllers.tournament import Tournament_controller
import datetime

from views.player import Player


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
    player_view = Player()
    controller = Tournament_controller()
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
            print("2. View Tournament : ")
            print("0. Exit.")

            print("\n")

            # Getting user input for menu choice
            choice = input("Please Enter your choice : ")
            print("\n")

            # Validating user input
            if choice in ["1", "2", "3", "0"]:

                # Performing actions based on user choice
                if choice == "1":
                    return self.create_tournament()
                elif choice == "2":
                    return self.tournament_view()
                else:
                    return False
            else:
                # Displaying an error message for invalid choice
                print("Invalid choice. Please try again : ")

    def create_tournament(self):
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
        self.controller.save_tournament(name, location, start_date, end_date, description, no_of_rounds)
        print("Tournament Created Successfully.")

    def tournament_view(self):
        """
            Menu to select Tournament Stats and Update Tournament
        """
        while True:
            # Displaying Tournament Menu options

            print("Display Tournament Menu".center(40, "-"))
            print("\n")
            print("1. List All Tournaments.")
            print("2. Tournaments Details.")
            print("3. Add Player in Tournament : ")
            print("4. List All Player in Tournament.")
            print("5. List of all completed round and matches of round.")
            print("6. Create Match Schedule for current round : ")
            print("7. Update Match Result : ")
            print("8. Get Score.")
            print("9. View Tournament with Date.")
            print("0. Exit.")
            print("\n")
            # Getting user input for menu choice
            choice = input("Please Enter your choice : ")

            # Validating user input
            if choice in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
                if choice == "1":

                    # Listing all tournaments
                    data = self.controller.list_all_tournaments()
                    if data:
                        print("".center(60, "-"))
                        for i in data:
                            print(i)

                elif choice == "2":

                    # Getting tournament details based on ID
                    tournament_id = input("Enter the tournament ID : ")
                    if self.controller.tournament_details(tournament_id):
                        display_tournament(self.controller.tournament_details(tournament_id))

                elif choice == "3":

                    # Adding player to a tournament
                    tournament_id = input("Enter tournament ID to add player : ")
                    self.player_view.list_all_player()
                    player_id = input("Enter player ID from above to add in tournament : ")
                    self.controller.add_player(tournament_id, player_id)
                    print()

                elif choice == "4":

                    # Listing players for a specific tournament
                    tournament_id = input("Enter tournament ID to get Player Details : ")
                    print("\n")
                    print("List of players for tournament {}".format(tournament_id))
                    print("\n")
                    # self.diplaye_value(self.controller.list_tournament_player(tournament_id))
                    for i in self.controller.list_tournament_player(tournament_id):
                        print(i)
                        print("".center(60, "-"))

                elif choice == "5":

                    # Getting fixture details for a tournament
                    tournament_id = input("Enter tournament ID to get Tournament Match Details : ")
                    display_result(self.controller.tournament_fixture(tournament_id))

                elif choice == "6":

                    # Creating fixture for the current round
                    tournament_id = input("Enter tournament ID to Create match schedule : ")
                    self.controller.create_fixture(tournament_id)
                    print("Match schedule is created for current round")

                elif choice == "7":

                    # Updating match result
                    tournament_id = input("Enter tournament ID to Update Match : ")
                    if self.controller.tournament_fixture(tournament_id):
                        display_result(self.controller.tournament_fixture(tournament_id))
                        match_id = input("Enter the Match ID : ")
                        winner = input("Enter the winner ID or Draw for Tie Match : ")
                        self.controller.update_match(tournament_id, str(match_id), winner)

                elif choice == "8":

                    # Getting tournament score
                    tournament_id = input("Enter tournament ID to Get Score : ")

                    if self.controller.get_tournament_score(tournament_id):
                        if self.controller.get_tournament_score(tournament_id)[1]:
                            print("Tournament is Completed.")
                        else:
                            print("Ongoing Tournament.")
                        display_score(self.controller.get_tournament_score(tournament_id)[0])

                elif choice == "9":

                    # getting tournament details with date
                    tournament_id = input("Enter the tournament ID : ")
                    print(self.controller.tournament_details_date(tournament_id))

                elif choice == "0":
                    return False

            else:
                print("Invalid choice. Please try again!")

            if not return_choice():
                return False


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


def display_tournament(data):
    """
        Method to display Tournament display.
    """
    print("".center(60, "-"))
    for key_name in data:
        print("{} ==> {}".format(key_name, data[key_name]))
