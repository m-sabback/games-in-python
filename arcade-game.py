"""Runs a luck-based arcade game that matches symbols for tickets."""

import random

def spin_column():
    """Returns a random item symbol."""
    item = random.randint(1, 4)

    if item == 1:
        return "*"
    elif item == 2:
        return "$"
    elif item == 3:
        return "?"
    else:
        return "@"

def get_score(item1, item2, item3):
    """Returns the score of the given three items."""
    if all_match(item1, item2, item3):
        return 50
    elif exactly_two_match(item1, item2, item3):
        return 10
    else:
        return 0

def draw_display(item1, item2, item3):
    """Draws the arcade machine display with the given items."""
    item_row = "| " + item1 + " | " + item2 + " | " + item3 + " |"
    border = len(item_row) * "-"

    print(border)
    print(item_row)
    print(border)

def all_match(item1, item2, item3):
    """Returns True if all three items are the same."""
    return item1 == item2 and item2 == item3

def exactly_two_match(item1, item2, item3):
    """Returns True if exactly two items are the same."""
    first_match = item1 == item2 and item2 != item3
    second_match = item2 == item3 and item3 != item1
    third_match = item3 == item1 and item1 != item2

    return first_match or second_match or third_match
