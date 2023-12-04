from controllers.tournament import Tournament_controller
import datetime

from views.player import Player


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
            print("".center(60, "-"))
            print("Tournament Menu".center(40, "-"))
            print("1. Create Tournament.")
            print("2. View Tournament.")
            print("0. Exit")

            # Getting user input for menu choice
            choice = input("Please Enter your choice : ")

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
                print("Invalid choice. Please try again.")

    def create_tournament(self):
        """
            Method to create tournament data in JSON file
        """

        # Prompting user for tournament details
        print("Please Enter Below Details".center(40, "-"))

        # Getting tournament name from user
        name = input("Enter the Name of Tournament: ")

        # Getting tournament location from user
        location = input("Enter Tournament Location: ")

        # Validating and getting tournament start date from user
        while True:
            start_date = input("Enter Tournament Start Date in YYYY-MM-DD: ")
            if validate(start_date):
                break

        # Validating and getting tournament end date from user
        while True:
            end_date = input("Enter Tournament End Date in YYYY-MM-DD: ")
            if validate(end_date):
                if datetime.datetime.strptime(start_date, "%Y-%m-%d") > datetime.datetime.strptime(end_date, "%Y-%m-%d"):
                    print("Tournament End Date is Before Start Date")
                else:
                    break

        # Validating and getting the number of rounds from user
        while True:
            no_of_rounds = input("Enter Tournament Total Rounds: ")
            if no_of_rounds.isnumeric():
                break
            else:
                print("Enter in Number : ")

        # Getting tournament description from user
        description = input("Enter Tournament Description: ")

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
            print("1. List All Tournaments.")
            print("2. Tournaments Details.")
            print("3. Add Player in Tournament.")
            print("4. List All Player in Tournament.")
            print("5. List of all completed round and matches of round.")
            print("6. Create Fixture for current round.")
            print("7. Update Match Result.")
            print("8. Get Score")
            print("0. Exit.")

            # Getting user input for menu choice
            choice = input("Please Enter your choice : ")

            # Validating user input
            if choice in ["1", "2", "3", "4", "5", "6", "7", "8", "0"]:
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
                    print(self.controller.tournament_details(tournament_id))

                elif choice == "3":

                    # Adding player to a tournament
                    tournament_id = input("Enter tournament ID to add player : ")
                    self.player_view.list_all_player()
                    player_id = input("Enter player ID from above to add in tournament : ")
                    self.controller.add_player(tournament_id, player_id)

                elif choice == "4":

                    # Listing players for a specific tournament
                    tournament_id = input("Enter tournament ID to get Player Details : ")
                    print("List of players for tournament {}".format(tournament_id))
                    for i in self.controller.list_tournament_player(tournament_id):
                        print(i)

                elif choice == "5":

                    # Getting fixture details for a tournament
                    tournament_id = input("Enter tournament ID to get Fixture Details : ")
                    print(self.controller.tournament_fixture(tournament_id))

                elif choice == "6":

                    # Creating fixture for the current round
                    tournament_id = input("Enter tournament ID to Create Fixture : ")
                    self.controller.create_fixture(tournament_id)

                elif choice == "7":

                    # Updating match result
                    tournament_id = input("Enter tournament ID to Update Match: ")
                    print(self.controller.tournament_fixture(tournament_id))
                    match_id = input("Enter the Match ID : ")
                    winner = input("Enter the winner ID or Draw for Tie Match : ")
                    self.controller.update_match(tournament_id, str(match_id), winner)

                elif choice == "8":

                    # Getting tournament score
                    tournament_id = input("Enter tournament ID to Get Score: ")
                    print(self.controller.get_tournament_score(tournament_id))
                return False
            else:
                print("Invalid choice. Please try again.")


