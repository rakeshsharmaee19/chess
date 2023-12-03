# -*- coding: utf-8 -*-
import json
import io


class Player_Model:
    """
        Model to save player data to json file and fetch bata from json
    """

    def save_data(self, data):
        try:
            to_unicode = unicode
        except NameError:
            to_unicode = str
        with io.open('json_data/player.json', 'w', encoding='utf8') as player:
            str_ = json.dumps(data,
                              indent=4, sort_keys=True,
                              separators=(',', ': '), ensure_ascii=False)
            player.write(to_unicode(str_))

    def get_data(self):
        """
            Method to Fetch JSON data of player
        """
        try:
            with open('json_data/player.json', 'r+') as data_file:
                data_loaded = json.load(data_file)
                return data_loaded
        except (json.JSONDecodeError, FileNotFoundError):
            return None
