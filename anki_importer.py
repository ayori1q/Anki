# This script automates the process of adding word pairs to an Anki deck.
# Ensure that AnkiConnect is installed, Anki is open, and the necessary decks are created before running this script.

import requests
import json

# Load the configuration file
with open('config.json') as config_file:
    config = json.load(config_file)
deck_name = config['deck_name']

def invoke(action, params={}):
    request = {'action': action, 'params': params, 'version': 6}
    response = requests.post(config['anki_connect_url'], json=request).json()
    if len(response) != 2:
        raise Exception('response has an unexpected number of fields')
    if 'error' not in response:
        raise Exception('response is missing required error field')
    if 'result' not in response:
        raise Exception('response is missing required result field')
    if response['error'] is not None:
        raise Exception(response['error'])
    return response['result']

def add_note(deck_name, front, back):
    note = {
        'deckName': deck_name,
        'modelName': 'Basic',
        'fields': {
            'Front': front,
            'Back': back
        },
        'options': {
            'allowDuplicate': False
        },
        'tags': []
    }
    response = invoke('addNote', {'note': note})
    return response

# Data for word pairs
word_pairs = [
    # Add word pairs, ("front", "back")
    ("undue", "過度の, 必要以上の"),
    ("irresistible", "抵抗できない, 抑えられない"),
    ("homogeneous", "同種の, 同質の, 均質の"),
    # Add more word pairs...
]

# Add word pairs to Anki
for front, back in word_pairs:
    result = add_note(deck_name, front, back)
    print('Added note:', result)
    