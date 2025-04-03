def translate_card(card_code):
    if card_code[0:2] == '10':
        value = '10'
        suit = card_code[2]
    else:
        value = card_code[0]
        suit = card_code[1]

    value_dict = {
        'A': 'ace',
        'J': 'jack',
        'Q': 'queen',
        'K': 'king',
        'a': 'ace',
        'j': 'jack',
        'q': 'queen',
        'k': 'king',
        '2': '2',
        '3': '3',
        '4': '4',
        '5': '5',
        '6': '6',
        '7': '7',
        '8': '8',
        '9': '9',
        '10': '10'
    }

    suit_dict = {
        'D': 'diamonds',
        'H': 'hearts',
        'S': 'spades',
        'C': 'clubs',
        'd': 'diamonds',
        'h': 'hearts',
        's': 'spades',
        'c': 'clubs'
    }

    translated_value = value_dict[value]
    translated_suit = suit_dict[suit]

    return translated_value + " of " + translated_suit

card_code = input()

print(translate_card(card_code))