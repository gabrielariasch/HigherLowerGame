# HigherLowerGame

This code is a game that compares the follower counts of two social media accounts. Here's a breakdown of how the code works:

The code imports three modules: game_data, random, and art. These modules provide functionality for accessing game data, generating random values, and displaying ASCII art, respectively.

The variables score and game_on are initialized. score keeps track of the player's score, and game_on determines whether the game should continue or end.

The variable dir is assigned the value of game_data.data. It suggests that the game_data module contains a data object or dictionary that holds information about social media accounts.

The function format_data(account) takes an account as input, extracts specific details (name, description, and country) from it, and returns a formatted string.

The function check_guess(guess, a_followers, b_followers) compares the number of followers of two accounts (A and B) and checks if the player's guess is correct. It returns True if the guess is correct and False otherwise.

The main game loop (while game_on) runs as long as game_on is True.

Inside the loop, two random social media accounts are chosen from dir using the random.choice() function. These accounts are assigned to the variables random1 and random2.

The game's ASCII art logo and the details of the two accounts are printed using the print() function and the art module.

The player is prompted to guess which account has more followers by inputting 'A' or 'B'. The input is converted to lowercase using the lower() method and assigned to the variable guess.

The follower counts of the two random accounts are extracted from the random1 and random2 dictionaries and assigned to the variables random1_follower_count and random2_follower_count, respectively.

The function check_guess() is called with the guess and follower count variables as arguments. The result is stored in the variable is_correct.

If the guess is correct (is_correct is True), the player's score is incremented by 1, and a message is printed to indicate a correct answer along with the current score.

If the guess is incorrect (is_correct is False), a message is printed indicating an incorrect answer along with the final score.

The game_on variable is set to False to end the game, and the break statement exits the loop.
