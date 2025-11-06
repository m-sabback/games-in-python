import  arcade_game
input("Press enter to spin! ")
col1 = arcade_game.spin_column()
col2 = arcade_game.spin_column()
col3 = arcade_game.spin_column()
arcade_game.draw_display(col1, col2, col3)

tickets = arcade_game.get_score(col1, col2, col3)
print("You won " + str(tickets) + " tickets!")

