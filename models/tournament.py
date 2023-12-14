# -*- coding: utf-8 -*-
import json
import io


class Tournament_Model:
    """
        Model to save Tournament data to json file and fetch bata from json
    """
    def save_data(self, data):
        """
            Method to save tournament data to tournament.json file
        """
        try:
            to_unicode = unicode
        except NameError:
            to_unicode = str
        with io.open('json_data/tournament.json', 'w', encoding='utf8') as tournament:

            str_ = json.dumps(data,
                              indent=4, sort_keys=True,
                              separators=(',', ': '), ensure_ascii=False)
            tournament.write(to_unicode(str_))

    def get_data(self):
        """
            Method to Fetch JSON data of Tournament
        """
        try:
            with open('json_data/tournament.json', 'r+') as data_file:
                data_loaded = json.load(data_file)
                return data_loaded
        except (json.JSONDecodeError, FileNotFoundError):
            return None
