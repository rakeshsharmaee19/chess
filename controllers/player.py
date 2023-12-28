from models.player import Player_Model
from views.player import Player


class Player_controller:
    """
        Class to save data in model and get data
    """
    model = Player_Model()
    player_view = Player()

    def player_menu(self):

        # Get user choice from the player menu
        choice = self.player_view.player_menu()

        # Add a new player
        if choice["choice"] == "1":
            self.save_player(choice["chess_id"], choice["first_name"], choice["last_name"], choice["player_dob"])

        # List all players
        elif choice["choice"] == "2":
            # Retrieve the list of all players from the controller
            player_list = self.list_all_player()

            # If the player list is not empty, print each player's details
            if player_list:
                self.player_view.view_all_player(player_list)
            else:
                self.player_view.view_all_player(False)

        # Display player profile
        elif choice["choice"] == "3":
            self.player_view.view_player(self.get_player_profile(choice["player_id"]))

        # Exit from player menu
        elif choice["choice"] == "0":
            return

    def save_player(self, player_id, first_name, last_name, player_dob):
        """
            Method to save player data into a JSON file.

            This method retrieves existing player data from the model, creates a new
            data entry for the specified player, and saves the updated data back to
            the JSON file. It performs checks to ensure the uniqueness of player IDs
            and prints a message indicating the success of the operation.

            :param player_id: The national chess ID of the player.
            :param first_name: The first name of the player.
            :param last_name: The last name of the player.
            :param player_dob: The date of birth of the player.

            :return: False after completing the save operation.
        """
        # Calling player Model to get player data
        player_data = self.model.get_data()

        data = {
                "first_name": first_name,
                "last_name": last_name,
                "dob": player_dob
            }

        # Checking if data existing or not
        if player_data:

            # List of Registered Player ID
            chess_key_list = list(player_data.keys())

            # Checking User exist or Not
            if player_id in chess_key_list:
                self.player_view.print_message("Player ID already exist, Please enter correct ID")
                return False

            # Calling JSON Save method to save Player Data into model
            player_data[player_id] = data

            # Calling model module to save player data
            self.model.save_data(player_data)
            self.player_view.print_message("Player Data added successfully")
        else:
            output_data = {player_id: data}

            # Calling model module to save player data into empty JSON file
            self.model.save_data(output_data)
            self.player_view.print_message("Player Data added successfully")
        return False

    def list_all_player(self):
        """
            Method to retrieve and format a list of all players from the model.

            This method calls the player model to get the player data and organizes
            it into a formatted list. If player data exists, it creates a list of player
            information sorted alphabetically by name. The method returns this formatted
            list or False if there are no players in the database.

            :return: A formatted list of player data sorted by name, or False if no players exist.
        """
        # Calling player Model to get player data
        player_data = self.model.get_data()

        # Checking is player data exist or not
        if player_data:
            # Player List to store each player Data
            player_list = []

            # Iterating Over Existing Player Data and saving into player List
            for i in player_data:
                current_data = [i, player_data[i]["first_name"] + "  " + player_data[i]["last_name"]]
                player_list.append(current_data)

            # Sorting Player List on Basis of Name
            player_list.sort(key=lambda x: x[1])

            # Defining List to return data
            output_list = []

            # Iterating each data and converting into single string
            for i in player_list:
                output_list.append(i[0]+"  "+i[1])
            return output_list
        else:
            self.player_view.print_message("There in No player in Database")
            return False

    def get_player_profile(self, player_id):
        """
            Method to retrieve the profile of a specific player based on their ID.

            This method calls the player model to get the player data and checks if
            the player with the specified ID exists. If the player exists, the method
            adds the player ID to the data and returns the player's profile. If the
            player ID is not valid or the player data does not exist, the method
            prints an appropriate message and returns False.

            :param player_id: The national chess ID of the player.
            :return: The player's profile data including the player ID, or False if
                     the player ID is not valid or the player data does not exist.
        """
        # Calling player Model to get player data
        player_data = self.model.get_data()

        # Checking is player data exist or not
        if player_data:
            if player_id in list(player_data.keys()):

                # Adding player ID to the data
                player_data[player_id]["id"] = player_id
                return player_data[player_id]
            else:
                self.player_view.print_message("Player ID is not valid.")
                return False
        else:
            self.player_view.print_message("Player Dose nat exist")
            return False
