from models.match import Match_Model
from models.player import Player_Model
from models.score import Score_Model
from models.tournament import Tournament_Model


class Tournament_controller:
    """
        Class to save data in model and get data
    """
    model = Tournament_Model()
    player_model = Player_Model()
    score = Score_Model()
    match = Match_Model()

    def __init__(self):
        self.id = None
        self.name = None
        self.location = None
        self.date = None
        self.num_of_rounds = None

    def save_tournament(self, name, location, start_date, end_date, description, no_of_round=4):
        """
            Save tournament information to the data model.

            This method takes the provided parameters, generates a unique tournament ID,
            and creates a new tournament entry with the given details. If there are existing
            tournaments, it increments the ID based on the last stored tournament. The default
            number of rounds is set to 4 if not explicitly provided.

            Args:
                name (str): The name of the tournament.
                location (str): The location where the tournament is held.
                start_date (str): The start date of the tournament.
                end_date (str): The end date of the tournament.
                description (str): A brief description of the tournament.
                no_of_round (int, optional): The number of rounds in the tournament (default is 4).

            Returns:
                None

            Note:
            The method first checks if there is existing tournament data. If present, it
            generates a new tournament ID based on the last stored tournament. If no data
            exists, it creates the first tournament with ID "TN1". The tournament's current
            round is set to 1, and the status is initially set to False, indicating that
            the tournament has not started. The tournament data, including player information,
            is then saved using the data model.

            Example Usage:
            save_tournament("Chess Championship", "City Hall", "2023-01-01", "2023-01-15",
                            "Exciting chess tournament with top players", 6)
        """

        # Calling Tournament Model to get Tournament data
        tournament_data = self.model.get_data()

        # Checking if tournament data exist or not
        if tournament_data:

            # Last saved Tournament ID
            last_id = list(tournament_data.keys())[-1]

            # Generating New Tournament ID
            tournament_id = "TN" + str(int(last_id[2:]) + 1)

            current_round = 1

            # Tournament Data
            data = {
                "name": name,
                "location": location,
                "start_date": start_date,
                "end_date": end_date,
                "number_of_rounds": no_of_round,
                "current_round": current_round,
                "description": description,
                "status": False,
                "players": [],
                "started": False
            }
            # Adding data into JSON
            tournament_data[tournament_id] = data

            # Calling Tournament model.save() method to store data id JSON file
            self.model.save_data(tournament_data)
        else:
            # New Tournament ID
            tournament_id = "TN1"
            current_round = 1

            # Tournament Data
            data = {
                tournament_id: {
                    "name": name,
                    "location": location,
                    "start_date": start_date,
                    "end_date": end_date,
                    "number_of_rounds": no_of_round,
                    "current_round": current_round,
                    "description": description,
                    "status": False,
                    "players": [],
                    "started": False
                }
            }
            # Calling Tournament model.save() method to store data id JSON file
            self.model.save_data(data)

    def list_all_tournaments(self):
        """
            Retrieve a list of all tournaments with their names and IDs.

            This method fetches tournament data from the model and constructs a list
            containing information about each tournament, including its unique ID and name.

            Args:
                None

            Returns:
                list: A list of lists, where each inner list contains the ID and name of a tournament.

            Note:
            The method first retrieves the tournament data from the model. If there are existing
            tournaments, it iterates through the data and creates a list for each tournament,
            combining its ID and name. These lists are then aggregated into a final list that
            is returned. If no tournament data exists, a message is printed, and False is returned.

            Example Usage:
            list_all_tournaments()
            # Output: [['TN1 Chess Championship'], ['TN2 French Chess League']]
        """

        # Calling Tournament Model to get Tournament data
        tournament_data = self.model.get_data()

        # Checking if tournament data exist or not
        if tournament_data:

            # List to store Tournament ID and Name
            output_data = []

            # Iterating Over List to get Each Tournament Data
            for i in tournament_data:
                current_data = [i + "  " + tournament_data[i]["name"]]
                output_data.append(current_data)

            # Returning Output
            return output_data
        else:
            print("Not A single Tournament is created.")
            return False

    def tournament_details(self, tournament_id):
        """
            Retrieve details for a specific tournament based on its ID.

            This method takes a tournament ID as input, fetches the tournament data from the model,
            and returns the details of the tournament with the specified ID.

            Args:
                tournament_id (str): The unique ID of the tournament for which details are requested.

            Returns:
                dict or False: A dictionary containing the details of the tournament if the ID is found,
                              otherwise, a message is printed, and False is returned.

            Note:
            The method first retrieves the tournament data from the model. If the provided ID exists
            in the list of tournament IDs, it returns the details of that tournament. If the ID is not
            found, an error message is printed, and False is returned.

            Example Usage:
            tournament_details("TN2")
            # Output: {'name': 'Chess League', 'location': 'Paris', 'start_date': '2023-02-01',
            # 'end_date': '2023-03-15', 'number_of_rounds': 6, 'current_round': 3,
            # 'description': 'National Chess League', 'status': True,
            # 'player': ['AB12345', 'AB0001']}

            tournament_details("TN5")
            # Output: Tournament ID is incorrect, Please enter correct ID
        """

        # Calling Tournament Model to get Tournament data
        tournament_data = self.model.get_data()

        # Checking if tournament data exist or not
        if tournament_data:
            if tournament_id in list(tournament_data.keys()):
                return tournament_data[tournament_id]
            else:
                print("Tournament ID is incorrect, Please enter correct ID")
                return False
        else:
            print("Tournament Data dose not exist.")

    def add_player(self, tournament_id, player_id):
        """
            Add a player to a specific tournament.

            This method takes a tournament ID and a player ID as input, validates the IDs against
            the existing tournament and player data, and adds the player to the specified tournament.

            Args:
                tournament_id (str): The unique ID of the tournament to which the player will be added.
                player_id (str): The unique ID of the player to be added to the tournament.

            Returns:
                None or False: None is returned if the player is successfully added,
                              otherwise, an error message is printed, and False is returned.

            Note:
            The method first retrieves both tournament and player data. It checks if the provided
            player ID exists in the list of player IDs and if the tournament ID exists in the list
            of tournament IDs. If both conditions are met, the player is added to the tournament's
            player list, and the updated data is saved. If either the player ID is invalid or the
            tournament ID is incorrect, an error message is printed, and False is returned.

            Example Usage:
            add_player("TN2", "AB12345")
            # Output: Player Details Added Successfully.

            add_player("TN5", "AB00001")
            # Output: Player ID is not valid or Tournament ID is not correct
        """
        # Calling Tournament Model to get Tournament data
        tournament_data = self.model.get_data()

        if tournament_data:
            if tournament_id in list(tournament_data.keys()):
                #  will get current round
                if tournament_data[tournament_id]["status"]:
                    print("Tournament is already completed")
                    return
                elif tournament_data[tournament_id]["started"]:
                    print("Tournament is already Started")
                    return
            else:
                print("Tournament Dose not exist")
                return

        # Calling Player Model to get Player Data
        player_data = self.player_model.get_data()

        # Checking if player_id and tournament_id exist or not
        if player_data:
            if player_id in list(player_data.keys()) and tournament_id in list(tournament_data.keys()):

                # Checking if player is added to tournament or not
                if not player_id in tournament_data[tournament_id]["players"]:
                    tournament_data[tournament_id]["players"].append(player_id)

                    # Saving Data into Tournament Model
                    self.model.save_data(tournament_data)
                    print("Player Details Added Successfully.")
                else:
                    print("Player is already Added to tournament")


            else:
                print("Player ID is not valid or Tournament ID is not correct")
        else:
            print("Player Data dose not exist.")
        return False

    def list_tournament_player(self, tournament_id):
        """
            Retrieve a list of players participating in a specific tournament.

            This method takes a tournament ID as input, fetches the tournament and player data,
            and returns a list of players (IDs and names) associated with the specified tournament.

            Args:
                tournament_id (str): The unique ID of the tournament for which player details are requested.

            Returns:
                list or False: A list of strings, where each string contains the player ID and name
                              if the tournament ID is valid. If the tournament ID is incorrect, an
                              error message is printed, and False is returned.

            Note:
            The method first retrieves both tournament and player data. It checks if the provided
            tournament ID exists in the list of tournament IDs. If the ID is valid, it retrieves
            the list of player IDs associated with the tournament, and for each player, it constructs
            a string containing the player ID and name. These strings are then aggregated into a list
            that is returned. If the tournament ID is incorrect, an error message is printed, and False
            is returned.

            Example Usage:
            list_tournament_player("TN2")
            # Output: ['P1 John Doe', 'P2 Jane Smith']

            list_tournament_player("TN5")
            # Output: Tournament ID is not correct
        """
        # Calling Tournament Model to get Tournament data
        tournament_data = self.model.get_data()

        # Calling Player Model to get Player Data
        player_data = self.player_model.get_data()

        # List for saving player data
        player_output_data = []

        # Checking if tournament_id exist or not
        if tournament_data:
            if tournament_id in list(tournament_data.keys()):

                # List of all players in Tournaments
                players_list = tournament_data[tournament_id]["players"]

                # Iterating through player_list list
                for i in players_list:
                    # Saving data of each student id first_name last_name into player_list
                    player_output_data.append(i + "  " + player_data[i]["first_name"] + " " + player_data[i]["first_name"])
            else:
                print("Tournament ID is not correct")
        else:
            print("Tournament Data dose not exist.")

        # Returning player Data
        return player_output_data

    def create_fixture(self, tournament_id):
        """
            Create a fixture for the current round of a specific tournament.

            This method takes a tournament ID as input, fetches the tournament data,
            retrieves the current round, and generates a fixture for the current round
            based on the player scores and matchups.

            Args:
                tournament_id (str): The unique ID of the tournament for which the fixture is to be created.

            Returns:
                None or False: None is returned if the fixture is successfully created,
                              otherwise, False is returned.

            Note:
            The method first retrieves the tournament data and checks if the provided
            tournament ID exists in the list of tournament IDs. If the ID is valid, it
            retrieves the current round of the tournament. The method then creates a score
            model and generates a fixture based on player scores. The fixture is constructed
            by pairing players with similar scores. Finally, the method calls the create_match
            method to create match entries for the fixture. If any step fails, False is returned.

            Example Usage:
            create_fixture("TN2")
            # Output: Fixture created successfully for the current round.

            create_fixture("TN5")
            # Output: Tournament ID is not correct
        """
        # Calling Tournament Model to get Tournament data
        tournament_data = self.model.get_data()

        # Checking if tournament_id exist or not
        if tournament_data:
            if tournament_id in list(tournament_data.keys()):
                #  will get current round
                if not tournament_data[tournament_id]["status"]:
                    current_round = tournament_data[tournament_id]["current_round"]
                else:
                    print("Tournament is already completed")
                    return
            else:
                print("Tournament Dose not exist")
                return
        else:
            print("Tournament data dose not exist.")
            return

        # calling create_score_model to create score data of each player for each round
        self.create_score_model(tournament_id, current_round, self.list_tournament_player(tournament_id))

        # List for saving fixture
        fixture = []

        # Calling Score Model to get Score data
        score_data = self.score.get_data()
        print(score_data)

        # Using Lambda function to sort player on their score
        score_data_sorted = sorted(list(score_data[tournament_id]["final"].items()), reverse=True)

        # Generating fixture pair for current round
        for pair in zip(score_data_sorted[::2], score_data_sorted[1::2]):
            fixture.append(pair)

        # Calling create_match method to save match details corresponding tournament_id, round and fixture
        self.create_match(tournament_id, current_round, fixture)
        # return False

        tournament_data[tournament_id]["started"] = True
        self.model.save_data(tournament_data)
        return False

    def create_score_model(self, tournament_id, match_round, player_data):
        """
            Create a score model for a specific round of a tournament.

            This method takes a tournament ID, match round, and player data as input,
            and creates a score model containing initial scores for each player in the round.

            Args:
                tournament_id (str): The unique ID of the tournament for which the score model is to be created.
                match_round (int): The current round of the tournament.
                player_data (list): A list of strings, each containing the player ID and name.

            Returns:
                bool: True if the score model is successfully created, False otherwise.

            Note:
            The method first checks if there is existing score data. If present, it ensures that
            the score model for the given round doesn't already exist. If not, it initializes the
            scores for each player to 0 in the specified round and saves the updated data. If no
            score data exists, it creates a new score model and initializes scores for each player.
            The final scores are also initialized to 0. The method returns True if successful and
            False if the model for the specified round already exists.

            Example Usage:
            create_score_model("TN2", 3, ['AB12345 John Doe', 'AB12346 Jane Smith'])
            # Output: Score model created successfully for round 3.

            create_score_model("TN5", 2, ['AB00001 Alice Johnson', 'AB00002 Bob Williams'])
            # Output: Score model already exists for this round.
        """
        # Match Dictionary
        data = {
            tournament_id: {
                match_round: {},
                "final": {}
            }
        }

        # Calling Score Model to get Score data
        score_data = self.score.get_data()
        # Checking if score data exist or not
        if score_data:

            # Checking if tournament_id exist or not
            if tournament_id in list(score_data.keys()):

                # Checking fixture for current match if exist it will not create score model
                if not str(match_round) in list(score_data[tournament_id].keys()):

                    # Iterate through each player and generate score dictionary for each
                    score_data[tournament_id][match_round] = {}
                    for i in player_data:
                        score_data[tournament_id][match_round][i.split(' ')[0]] = 0

                    # Saving Data into Score Model
                    self.score.save_data(score_data)
                else:
                    print("Fixture is already created for this round.")
                    return False
            else:
                import pdb
                pdb.set_trace()
                score_data[tournament_id] = {match_round:{}, "final":{}}
                # iterating for player data to generate a new score model
                for i in player_data:
                    # Saving data into match current round
                    score_data[tournament_id][match_round][i.split(' ')[0]] = 0

                    # Saving data into match final round
                    score_data[tournament_id]["final"][i.split(' ')[0]] = 0

                # Saving Data into Score Model
                self.score.save_data(score_data)
        else:
            # iterating for player data to generate a new score model
            for i in player_data:
                # Saving data into match current round
                data[tournament_id][match_round][i.split(' ')[0]] = 0

                # Saving data into match final round
                data[tournament_id]["final"][i.split(' ')[0]] = 0

            # Saving Data into Score Model
            self.score.save_data(data)
        return True

    def create_match(self, tournament_id, match_round, fixture_data):
        """
            Create match entries for a specific round of a tournament.

            This method takes a tournament ID, match round, and fixture data as input,
            and creates match entries based on the fixture information. Match entries
            include player IDs, completion status, winner information, and result details.

            Args:
                tournament_id (str): The unique ID of the tournament for which matches are to be created.
                match_round (int): The current round of the tournament.
                fixture_data (list): A list of tuples, each containing two tuples representing player pairs.

            Returns:
                None or False: None is returned if the matches are successfully created,
                              otherwise, False is returned.

            Note:
            The method first checks if there is existing match data. If present, it ensures that
            match entries for the given tournament ID and round don't already exist. If not,
            it initializes match entries based on the provided fixture data and saves the updated data.
            If no match data exists, it creates a new set of match entries using the provided fixture data.
            The completion status, winner, and result details are initially set to default values.
            The method returns None if successful and False if match entries for the specified round already exist.

            Example Usage:
            create_match("TN2", 3, [(['AB12345', 'John Doe'], ['AB12346, 'Jane Smith']), (['AB12347', 'Alice Johnson'],
            ['AB12348', 'Bob Williams'])])
            # Output: Matches created successfully for round 3.

            create_match("TN5", 2, [(['AB00001', 'Charlie Brown'], ['AB00002', 'David White'])])
            # Output: Match entries already exist for this round.
        """

        # Calling match Model to get match data
        match_data = self.match.get_data()

        # Checking if match data exist or not
        if match_data:

            # Checking if tournament_id and match_round exist or not
            if tournament_id in list(match_data.keys()):
                if str(match_round) in list(match_data[tournament_id].keys()):
                    print("Fixture is already Created")
                else:
                    # Define match id if not exist
                    match_id = 0
                    match_data[tournament_id][match_round] = {"completed": False}

                    # Adding fixture details into match
                    for i in fixture_data:
                        # Match ID for each match
                        match_id += 1

                        # Adding data into each match object
                        match_data[tournament_id][match_round][match_id] = {
                            "player1": i[0][0],
                            "player2": i[1][0],
                            "completed": False,
                            "winner": None,
                            "result": ""
                        }

                    # Saving Data into Match Model
                    self.match.save_data(match_data)
            else:
                # Define match id if not exist
                match_id = 0
                match_data[tournament_id] = {match_round: {"completed": False}}
                # match_data[tournament_id][match_round] = {"completed": False}
                # Adding fixture details into match
                for i in fixture_data:
                    # Match ID for each match
                    match_id += 1

                    # Adding data into each match object
                    match_data[tournament_id][match_round][match_id] = {
                        "player1": i[0][0],
                        "player2": i[1][0],
                        "completed": False,
                        "winner": None,
                        "result": ""
                    }

                # Saving Data into Match Model
                self.match.save_data(match_data)
        else:
            # Define match id if not exist
            match_id = 0

            # Data formate for storing data into match model
            data = {
                tournament_id: {
                    match_round: {
                        "completed": False
                    },

                }
            }

            # Adding fixture details into match
            for i in fixture_data:
                # Match ID for each match
                match_id += 1

                # Adding data into each match object
                data[tournament_id][match_round][match_id] = {
                    "player1": i[0][0],
                    "player2": i[1][0],
                    "completed": False,
                    "winner": None,
                    "result": ""
                }

            # Saving Data into Match Model
            self.match.save_data(data)
        return False

    def tournament_fixture(self, tournament_id):
        """
            Fetch details of each match in a specific tournament.

            This method takes a tournament ID as input, retrieves the match data for the tournament,
            and returns a list containing details for each match, including the tournament round.

            Args:
                tournament_id (str): The unique ID of the tournament for which match details are requested.

            Returns:
                list or False: A list of dictionaries, each containing details for a match in the tournament
                              if the tournament ID is valid. If the ID is incorrect or the tournament has not
                              been created yet, an error message is printed, and False is returned.

            Note:
            The method first retrieves the match data for the tournament. If the tournament ID exists in the
            list of tournament IDs, it iterates through the match data and constructs a list of dictionaries,
            each containing details for a match. The tournament round is added to each match dictionary.
            If the tournament ID is incorrect or the tournament has not been created yet, an error message is
            printed, and False is returned.

            Example Usage:
            tournament_fixture("TN2")
            # Output: [{'player1': 'AB0001', 'player2': 'AB0002', 'completed': False, 'winner': None, 'result': '', 'tournament_round': '3'},
            #           {'player1': 'AB0003', 'player2': 'AB0004', 'completed': False, 'winner': None, 'result': '', 'tournament_round': '3'}]

            tournament_fixture("TN5")
            # Output: Tournament does not exist
        """

        # Calling tournament Model to get tournament data
        tournament_data = self.match.get_data()

        # List to store tournament details
        return_data = []

        # Checking id tournament exist or not
        if tournament_data:

            # If tournament ID exist or not
            if tournament_id in list(tournament_data.keys()):

                # Iterating for each tournament data
                for i in tournament_data[tournament_id]:

                    # Checking if tournament round is numeric or not
                    if i.isnumeric():
                        tournament_data[tournament_id][i]["tournament_round"] = i
                        return_data.append(tournament_data[tournament_id][i])
                return return_data
            else:
                print("Tournament dose not started.")
        else:
            print("Tournament is not created yet.")
        return False

    def update_match(self, tournament_id, match_id, result):
        """
            Update the result of a specific match in a tournament.

            This method takes a tournament ID, match ID, and result as input, validates the IDs against
            existing tournament and match data, and updates the match details including completion status,
            result, and winner information.

            Args:
                tournament_id (str): The unique ID of the tournament for which the match result is to be updated.
                match_id (str): The unique ID of the match to be updated.
                result (str): The result of the match, which can be a player ID or "Draw".

            Returns:
                None or False: None is returned if the match result is successfully updated,
                              otherwise, False is returned.

            Note:
            The method first retrieves both tournament and match data. It checks if the provided tournament ID
            exists in the list of tournament IDs and if the current round is available. If both conditions are
            met and the match is not already marked as completed, the match details are updated with the result,
            winner, and completion status. The match data is saved, and the player scores are updated using
            the update_score method. If the match is already completed or if the tournament or match IDs are
            incorrect, an error message is printed, and False is returned.

            Example Usage:
            update_match("TN2", "1", "AB00001")
            # Output: Match Data updated.

            update_match("TN5", "3", "Draw")
            # Output: Please enter the correct Tournament ID and Match ID
        """

        # Calling match Model to get match data
        tournament_match_data = self.match.get_data()

        # Calling tournament Model to get tournament data
        tournament_data = self.model.get_data()

        # checking if tournament_id exist or not
        if tournament_data:
            if tournament_id in list(tournament_data.keys()):
                # Get current tournament round
                current_round = str(tournament_data[tournament_id]["current_round"])
        else:
            print("Tournament Data dose not exist.")

        # Checking if match data exist or not
        if tournament_match_data:

            # Checking if tournament_id, current_round and match_id exist or not
            if tournament_id in list(tournament_match_data.keys()) and current_round in \
                    list(tournament_match_data[tournament_id].keys()) and \
                    match_id in list(tournament_match_data[tournament_id][current_round]):

                # Checking if match data is updated or not, if not updated will update the match details
                if not tournament_match_data[tournament_id][current_round][match_id]["completed"]:

                    # Saving match status to complete
                    tournament_match_data[tournament_id][current_round][match_id]["completed"] = True

                    # if result is draw then will update result as draw.
                    if result.upper() == "DRAW":
                        tournament_match_data[tournament_id][current_round][match_id]["result"] = "Draw"
                    else:
                        tournament_match_data[tournament_id][current_round][match_id][
                            "result"] = "{} win the match".format(result)
                        tournament_match_data[tournament_id][current_round][match_id]["winner"] = result

                    # Update tournament match data
                    self.match.save_data(tournament_match_data)

                    # method to call update score for current round
                    self.update_score(tournament_id, current_round,
                                      tournament_match_data[tournament_id][current_round][match_id])
                    print("Match Data updated.")
                else:
                    print("Match Details already updated.")

                self.update_current_round(tournament_id)
            else:
                print("Please enter the correct Tournament ID and Match ID.")
        else:
            print("Match is not created yet")
        return False

    def update_score(self, tournament_id, round_number, match_data):
        """
            Update player scores after a match in a tournament.

            This method takes a tournament ID, round number, and match data as input,
            retrieves the score data, and updates the scores of players based on the match result.

            Args:
                tournament_id (str): The unique ID of the tournament for which scores are to be updated.
                round_number (int): The current round of the tournament.
                match_data (dict): A dictionary containing details of the match, including player IDs, winner, and result.

            Returns:
                None or False: None is returned if the player scores are successfully updated,
                              otherwise, False is returned.

            Note:
            The method first retrieves the score data. If the data is available, it checks if a winner
            is declared in the match. If a winner exists, the winner's score for the current round and
            overall tournament is incremented. If the match is a draw, each player receives 0.5 points
            for the current round and overall. The updated score data is saved. If the score data is not
            available, an error message is printed, and False is returned.

            Example Usage:
            update_score("TN2", 3, {'player1': 'AB12345', 'player2': 'AB12346', 'completed': True, 'winner': 'AB12345', 'result': 'P1 win the match'})
            # Output: Player scores updated successfully.

            update_score("TN5", 2, {'player1': 'AB12345', 'player2': 'AB12346', 'completed': True, 'winner': None, 'result': 'Draw'})
            # Output: Score Data is not Available.
        """

        # Calling score Model to get score data
        score_data = self.score.get_data()

        # Check if score data exist or not
        if score_data:

            # Update score if winner exist
            if match_data["winner"]:
                score_data[tournament_id][str(round_number)][match_data["winner"]] += 1
                score_data[tournament_id]["final"][match_data["winner"]] += 1

            # Update Score 0.5 for each player in case of draw
            else:
                score_data[tournament_id][str(round_number)][match_data["player1"]] += 0.5
                score_data[tournament_id]["final"][match_data["player1"]] += 0.5
                score_data[tournament_id][str(round_number)][match_data["player2"]] += 0.5
                score_data[tournament_id]["final"][match_data["player2"]] += 0.5
            self.score.save_data(score_data)
        else:
            print("Score Data is not Available.")
        return False

    def get_tournament_score(self, tournament_id):
        """
            Get the score data for a specific tournament.

            This method takes a tournament ID as input, retrieves the score and tournament data,
            and returns a list containing the scores for the current round and overall tournament.

            Args:
                tournament_id (str): The unique ID of the tournament for which scores are to be retrieved.

            Returns:
                list or False: A list containing two dictionaries, one with scores for the current round and
                              another with overall tournament scores, if the tournament ID is valid.
                              If the ID is incorrect or score data is not available, an error message is
                              printed, and False is returned.

            Note:
            The method first retrieves both score and tournament data. It checks if the provided tournament ID
            exists in the list of tournament IDs and if the current round is available. If both conditions are
            met and the score data is available, it constructs a list containing the scores for the current round
            and overall tournament. If the tournament ID is incorrect or score data is not available, an error
            message is printed, and False is returned.

            Example Usage:
            get_tournament_score("TN2")
            # Output: [{'AB12345': 2, 'AB00001': 1, 'AB12346': 3, 'AB12347': 0}, {'AB12345': 4, 'AB12346': 3,
            'AB12347': 5, 'AB00001': 1}]

            get_tournament_score("TN5")
            # Output: Tournament does not exist.
        """

        # Calling score Model to get score data
        score_data = self.score.get_data()

        # Calling tournament Model to get tournament data
        tournament_data = self.model.get_data()

        # checking if tournament_id exist or not
        if tournament_data:
            if tournament_id in list(tournament_data.keys()):
                # Get current tournament round
                current_round = str(tournament_data[tournament_id]["current_round"])
        else:
            print("Tournament Data dose not exist.")

        # Check if score data exist or not
        if score_data:

            # Checking if tournament_id and match_round exist or not
            if tournament_id in list(score_data.keys()):
                print(current_round)
                if current_round in list(score_data[tournament_id].keys()):
                    return_data = [{"current_round": score_data[tournament_id][current_round]},
                                   {"final_score": score_data[tournament_id]["final"]}]
                    return return_data
                elif int(current_round)>1 and str(int(current_round)-1) in list(score_data[tournament_id].keys()):
                    return_data = [{"current_round": score_data[tournament_id][str(int(current_round)-1)]},
                                   {"final_score": score_data[tournament_id]["final"]}]
                    return return_data
            else:
                print("Tournament Dose not exist.")
        else:
            print("Score data is not exist")
        return False

    def update_current_round(self, tournament_id):
        """
            Update the current round of a specific tournament.

            This method takes a tournament ID as input, retrieves the match and tournament data,
            and updates the current round of the tournament based on completed matches.

            Args:
                tournament_id (str): The unique ID of the tournament for which the current round is to be updated.

            Returns:
                None or False: None is returned if the current round is successfully updated,
                              otherwise, False is returned.

            Note:
            The method first retrieves both match and tournament data. It checks if the provided tournament ID
            exists in the list of tournament IDs and retrieves the current round. If the match data is available,
            it counts the number of completed matches in the current round. If the count is equal to the total
            number of matches in the round, the current round is incremented. If the new round is the last round
            of the tournament, the tournament status is set to True. The updated tournament data is saved.
            If the tournament ID is incorrect or data is not available, an error message is printed, and False is returned.

            Example Usage:
            update_current_round("TN2")
            # Output: Current round updated successfully.

            update_current_round("TN5")
            # Output: Tournament Data does not exist.
        """

        # Calling match Model to get match data
        tournament_match_data = self.match.get_data()

        # Calling tournament Model to get tournament data
        tournament_data = self.model.get_data()

        # checking if tournament_id exist or not
        if tournament_data:
            if tournament_id in list(tournament_data.keys()):
                # Get current tournament round
                current_round = str(tournament_data[tournament_id]["current_round"])
        else:
            print("Tournament Data dose not exist.")

        # Checking if match data exist or not
        if tournament_match_data:
            count = 0
            for i in tournament_match_data[tournament_id][current_round]:
                if i != "completed":
                    if tournament_match_data[tournament_id][current_round][i]["completed"]:
                        count += 1
            if count >= len(tournament_match_data[tournament_id][current_round])-1:
                if int(current_round) < int(tournament_data[tournament_id]["number_of_rounds"]):

                    tournament_match_data[tournament_id][current_round]["completed"] = True
                    tournament_data[tournament_id]["current_round"] += 1
                elif int(current_round) == int(tournament_data[tournament_id]["number_of_rounds"]):
                    tournament_data[tournament_id]["status"] = True

            self.model.save_data(tournament_data)
        else:
            print("Tournament Data dose not exist")
        return False
