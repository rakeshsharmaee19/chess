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
            print("".center(60, "-"))
            print("Tournament Menu".center(40, "-"))
            print("1. Create Tournament.")
            print("2. View Tournament.")
            print("0. Exit")

            choice = input("Please Enter your choice : ")
            if choice in ["1", "2", "3", "0"]:
                if choice == "1":
                    return self.create_tournament()
                elif choice == "2":
                    return self.tournament_view()
                else:
                    return False
            else:
                print("Invalid choice. Please try again.")

    def create_tournament(self):
        """
            Method to create tournament data in JSON file
        """

        print("Please Enter Below Details".center(40, "-"))
        name = input("Enter the Name of Tournament")
        location = input("Enter Tournament Location: ")
        while True:
            start_date = input("Enter Tournament Start Date in YYYY-MM-DD: ")
            if validate(start_date):
                break

        while True:
            end_date = input("Enter Tournament End Date in YYYY-MM-DD: ")
            if datetime.datetime.strptime(start_date, "%Y-%m-%d") > datetime.datetime.strptime(end_date, "%Y-%m-%d"):
                print("Tournament End Date is Before Start Date")
            else:
                break

        while True:
            no_of_rounds = input("Enter Tournament Total Rounds: ")
            if no_of_rounds.isnumeric():
                no_of_rounds = int(no_of_rounds)
                break
            else:
                print("Enter in Number : ")

        description = input("Enter Tournament Description: ")
        self.controller.save_tournament(name, location, start_date, end_date, description, no_of_rounds)

    def tournament_view(self):
        """
            Menu to select Tournament Stats and Update Tournament
        """
        while True:
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

            choice = input("Please Enter your choice : ")
            if choice in ["1", "2", "3", "4", "5", "6", "7", "8", "0"]:
                if choice == "1":
                    data = self.controller.list_all_tournaments()
                    if data:
                        print("".center(60, "-"))
                        for i in data:
                            print(i)
                elif choice == "2":
                    tournament_id = input("Enter the tournament ID : ")
                    print(self.controller.tournament_details(tournament_id))
                elif choice == "3":
                    tournament_id = input("Enter tournament ID to add player : ")
                    self.player_view.list_all_player()
                    player_id = input("Enter player ID from above to add in tournament : ")
                    self.controller.add_player(tournament_id, player_id)
                elif choice == "4":
                    tournament_id = input("Enter tournament ID to get Player Details : ")
                    print("List of players for tournament {}".format(tournament_id))
                    for i in self.controller.list_tournament_player(tournament_id):
                        print(i)
                elif choice == "5":
                    tournament_id = input("Enter tournament ID to get Fixture Details : ")
                    print(self.controller.tournament_fixture(tournament_id))
                elif choice == "6":
                    tournament_id = input("Enter tournament ID to Create Fixture : ")
                    self.controller.create_fixture(tournament_id)
                elif choice == "7":
                    tournament_id = input("Enter tournament ID to Create Fixture : ")
                    print(self.controller.tournament_fixture(tournament_id))
                    match_id = input("Enter the Match ID : ")
                    winner = input("Enter the winner ID or Draw for Tie Match : ")
                    self.controller.update_match(tournament_id, str(match_id), winner)
                elif choice == "8":
                    tournament_id = input("Enter tournament ID to Create Fixture : ")
                    print(self.controller.get_tournament_score(tournament_id))
                return False
            else:
                print("Invalid choice. Please try again.")


