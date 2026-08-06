import json
import os

class Translator:
    def __init__(self, lang='fa'):
        self.lang = lang
        self.messages = self._load_messages()
    
    def _load_messages(self):
        file_path = os.path.join('locales', f'{self.lang}.json')
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def get(self, key, **kwargs):
        text = self.messages.get(key, key)
        if kwargs:
            return text.format(**kwargs)
        return text

# Default language
default = Translator('fa')