import os
import json

import json
import os

class Languages:

    def __init__(self):

        self.translations = {}
        self.default_lang = "en-US"

        base_path = 'utils/languages/translations'

        for file in os.listdir(base_path):
            if not file.endswith('.json'):
                continue

            lang = file.split(".")[0]
            self.translations[lang] = {}

            # Load JSON file properly
            with open(f"{base_path}/{file}", "r", encoding="utf-8") as f:
                data = json.load(f)

            # Add all key/value pairs into the language dictionary
            for key, value in data.items():
                self.translations[lang][key] = value


    def getText(self, key, *args, lang = None):

        if not lang:
            lang = self.default_lang

        string = self.translations[lang][key]

        parts = string.split("%s")
        result = []

        for i, part in enumerate(parts):
            result.append(part)
            if i < len(args):
                result.append(str(args[i]))

        return "".join(result)
