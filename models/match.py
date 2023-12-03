# -*- coding: utf-8 -*-
import json
import io


class Match_Model:
    """
        Model to save player score data to json file and fetch data from json
    """

    def save_data(self, data):
        try:
            to_unicode = unicode
        except NameError:
            to_unicode = str
        with io.open('json_data/match.json', 'w', encoding='utf8') as player:
            str_ = json.dumps(data,
                              indent=4,
                              separators=(',', ': '), ensure_ascii=False)
            player.write(to_unicode(str_))

    def get_data(self):
        """
            Method to Fetch JSON data of player
        """
        try:
            with open('json_data/match.json', 'r+') as data_file:
                data_loaded = json.load(data_file)
                return data_loaded
        except (json.JSONDecodeError, FileNotFoundError):
            return None
