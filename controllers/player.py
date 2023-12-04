from models.player import Player_Model


class Player_controller:
    """
        Class to save data in model and get data
    """
    model = Player_Model()

    def save_player(self, player_id, first_name, last_name, player_dob):
        """
            Method to save player data into JSON
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
                print("Player ID already exist, Please enter correct ID")
                return False

            # Calling JSON Save method to save Player Data into model
            player_data[player_id] = data

            # Calling model module to save player data
            self.model.save_data(player_data)
            print("Player Data added successfully")
        else:
            output_data = {player_id: data}
            # Calling model module to save player data into empty JSON file
            self.model.save_data(output_data)
            print("Player Data added successfully")
        return False

    def list_all_player(self):
        """
            Method to get all player from the model
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
            print("There in No player in Database")
            return False

    def get_player_profile(self, player_id):
        """
            Method to get all player from the model
        """
        # Calling player Model to get player data
        player_data = self.model.get_data()

        # Checking is player data exist or not
        if player_data:
            if player_id in list(player_data.keys()):
                player_data[player_id]["id"] = player_id
                return player_data[player_id]
            else:
                print("Player ID is not valid.")
                return False
        else:
            print("Player Dose nat exist")
            return False
