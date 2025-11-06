import random

# Symbols that can appear in each column
SYMBOLS = ["🍒", "🍊", "🍋", "🍇", "7️⃣", "💎"]

def spin_column():
    """Returns a random symbol from the SYMBOLS list"""
    return random.choice(SYMBOLS)

def draw_display(col1, col2, col3):
    """Draws the slot machine display with the three columns"""
    print("\n=================")
    print(f"| {col1} | {col2} | {col3} |")
    print("=================")

def get_score(col1, col2, col3):
    """Calculate the number of tickets won based on the symbols"""
    # All symbols match
    if col1 == col2 == col3:
        if col1 == "💎":  # Three diamonds
            return 100
        elif col1 == "7️⃣":  # Three sevens
            return 70
        else:  # Three of any other matching symbols
            return 50
    
    # Two symbols match
    elif col1 == col2 or col2 == col3 or col1 == col3:
        return 20
    
    # No matches
    return 5


