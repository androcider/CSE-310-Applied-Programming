import arcade
import time
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Hangman"
PANEL_HEIGHT = 200
Music_volume = 6

class Theme:
    def __init__(self, background_image, button_image):
        self.background_image = background_image
        self.button_image = button_image

# Define themes
space_theme = Theme("media/planet-in-space-background-desktop-wallpaper.jpg", "media/asteroid.jpg")
western_theme = Theme("media/aesthetic-western-background-desktop-wallpaper.jpg", "media/fabrics_0066_cylinder_600.png")
halloween_theme = Theme("media/night-mystery-city-desktop-wallpaper.jpg", "media/jack o lantern.jpg")


# Background images
background = arcade.load_texture("media/aesthetic-western-background-desktop-wallpaper.jpg")
vertical_wood = arcade.load_texture("media/photos_2023_7_4_fst_old-wood-cracked-knots_vertical.jpg")
horizontal_wood = arcade.load_texture("media/photos_2023_7_4_fst_old-wood-cracked-knots_horizontal.jpg")
rope = arcade.load_texture("media/fabrics_0066_cylinder_600.png")
DEFAULT_FONT_SIZE = 50
dummy_color= arcade.color.BLACK
# List of words
words = ["abruptly","absurd","abyss","affix","askew","avenue","awkward","axiom","azure","bagpipes","bandwagon","banjo","bayou","beekeeper",
        "bikini","blitz","blizzard","boggle","bookworm","boxcar","boxful","buckaroo","buffalo","buffoon","buxom","buzzard","buzzing","buzzwords",
        "caliph","cobweb","cockiness","croquet","crypt","curacao","cycle","daiquiri","dirndl","disavow","dizzying","duplex","dwarves","embezzle",
        "equip","espionage","euouae","exodus","faking","fishhook","fixable","fjord","flapjack","flopping","fluffiness","flyby","foxglove","frazzled",
        "frizzled","fuchsia","funny","gabby","galaxy","galvanize","gazebo","giaour","gizmo","glowworm","glyph","gnarly","gnostic","gossip","grogginess",
        "haiku","haphazard","hyphen","hymn","iatrogenic","icebox","injury","ivory","ivy","jackpot","jaundice","jawbreaker","jaywalk","jazziest",
        "jazzy","jelly","jigsaw","jinx","jiujitsu","jockey","jogging","joking",'jovial',"joyful","juicy","jukebox",'jumbo',"kayak","kazoo",
        "keyhole","khaki","kilobyte","kiosk","kitsch","kiwifruit","klutz","knapsack","larynx","lengths","lucky","luxury","lymph","marquis",
        "matrix","megahertz","microwave","mnemonic","mystify","naphtha","nightclub","nowadays","numbskull","nymph","onyx","ovary","oxidize",
        "oxygen","pajama","peekaboo","phlegm","pixel","pizazz","pneumonia","polka","pshaw","psyche","puppy","puzzling","quartz","queue","quips",
        "quixotic","quiz","quizzes","quorum","razzmatazz","rhubarb","rhythm","rickshaw","schnapps","scratch","shiv","snazzy","sphinx",
        "spritz","squawk","staff","strength","strengths","stretch","stronghold","stymied","subway","swivel","syndrome","thriftless","thumbscrew",
        "topaz","transcript","transgress","transplant","triphthong","twelfth","twelfths","unknown","unworthy","unzip",'uptown',"vaporize","vixen",
        "vodka","voodoo","vortex","voyeurism","walkway","waltz","wave","wavy","waxy","wellspring","wheezy","whiskey",'whizzing',"whomever","wimpy",
        "witchcraft","wizard","woozy","wristwatch","wyvern","xylophone","yachtsman","yippee","yoked","youthful","yummy","zephyr","zigzag","zigzagging",
        "zilch","zipper","zodiac","zombie"]

class game_window(arcade.View):
    def __init__(self, chosen_word, theme):
        super().__init__()

        # Initialize game components
        self.chosen_word = chosen_word
        self.hidden_word_instance = Hidden_word()
        self.hide_word = self.hidden_word_instance.word_hide(chosen_word)
        self.game_over = False  # Flag to track if the game is over
        self.lives = 6  # Initialize lives attribute to 6
        self.theme = theme  # Initialize the current theme

        # Initialize theme buttons list
        self.theme_buttons = []

        # Create buttons for each theme
        self.create_theme_buttons()
        # Load background image
        self.background = arcade.load_texture(theme.background_image)
        print("Background image:", theme.background_image)  # Add this line to check the path

        # UI components
        self.buttons = []
        self.replay_button = None  # Initialize replay button to None

        # Create buttons for each letter of the alphabet
        self.create_buttons()
        self.create_replay_button()  # Create replay button

        # Load the texture for the win/lose sprite
        self.win_lose_sprite_texture = arcade.load_texture("media/fabrics_0066_cylinder_600.png")

        # Create a new sprite object for win/lose sprite with the loaded texture
        self.win_lose_sprite = arcade.Sprite()
        self.win_lose_sprite.texture = self.win_lose_sprite_texture
        self.win_lose_sprite.center_x = SCREEN_WIDTH - 400  # Adjust the position as needed
        self.win_lose_sprite.center_y = SCREEN_HEIGHT - 75  # Adjust the position as needed
        self.win_lose_sprite.width = 350  # Adjust the width as needed
        self.win_lose_sprite.height = 100  # Adjust the height as needed
        self.win_lose_sprite_text = None  # Text to display on win/lose sprite

        self.show_win_lose_sprite = False  # Flag to track whether to show win/lose sprite

    def create_theme_buttons(self):
            # Define button properties
            button_width = 150
            button_height = 50
            button_spacing = 10
            start_x = SCREEN_WIDTH - button_width + 50  # Align with the right side of the screen
            start_y = PANEL_HEIGHT + button_spacing + 200  # Start below the panel

            # Define themes and their respective buttons
            themes = [
                ("Space Theme", space_theme, "media/planet-in-space-background-desktop-wallpaper.jpg"),
                ("Western Theme", western_theme, "media/aesthetic-western-background-desktop-wallpaper.jpg"),
                ("Halloween Theme", halloween_theme, "media/night-mystery-city-desktop-wallpaper.jpg")
            ]

            # Create buttons for each theme
            for theme_name, theme, theme_image_path in themes:
                button = ThemeButton(start_x, start_y, button_width, button_height, theme_name, theme_image_path, self.switch_theme)
                self.theme_buttons.append(button)
                start_y -= button_height + button_spacing

    def create_buttons(self):
        button_width = 25
        button_spacing = 5
        start_x = 20
        start_y = 50

        for i, letter in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
            button = Button("media/fabrics_0066_cylinder_600.png", start_x + i * (button_width + button_spacing), start_y, letter, self.on_button_click)
            self.buttons.append(button)

    def create_replay_button(self):
        # Create replay button at top right corner
        replay_button = ReplayButton("media/fabrics_0066_cylinder_600.png", SCREEN_WIDTH - 75, SCREEN_HEIGHT - 50, self.restart_game)
        self.replay_button = replay_button

    def on_button_click(self, letter):
        if not self.game_over:  # Only update hidden word if the game is not over
            print("Button clicked! Letter:", letter)
            self.update_hidden_word(letter)
            print("Updated hidden word:", self.hide_word)

    def on_draw(self):
        arcade.start_render()

        # Draw the background images
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)

        arcade.draw_lrwh_rectangle_textured(50, 250, 25, 300, vertical_wood)
        arcade.draw_lrwh_rectangle_textured(165, 455, 10, 50, rope)
        arcade.draw_lrwh_rectangle_textured(25, 500, 175, 25, horizontal_wood)

        # Draw the buttons
        for button in self.buttons:
            button.draw()
        # Draw theme buttons
        for button in self.theme_buttons:
            button.draw()
        # Draw the hidden word
        revealed_word_width = len(self.hide_word.replace(" ", "")) * 20
        start_x = (SCREEN_WIDTH - revealed_word_width) / 2
        start_y = 150  # Adjusted to display lower
        for i, char in enumerate(self.hide_word):
            arcade.draw_text(char,
                            start_x + i * 20,  # Adjusted for letter spacing
                            start_y,
                            arcade.color.BLACK,
                            font_size=30)  # Adjusted font size

        if self.lives == 6:
            pass  # No parts to draw for 6 lives remaining
        elif self.lives == 5:
            arcade.draw_circle_outline(170, 445, 20, dummy_color, 8)  # Head
        elif self.lives == 4:
            arcade.draw_circle_outline(170, 445, 20, dummy_color, 8)  # Head
            arcade.draw_line(170, 425, 170, 350, dummy_color, 8)  # Body
        elif self.lives == 3:
            arcade.draw_circle_outline(170, 445, 20, dummy_color, 8)  # Head
            arcade.draw_line(170, 425, 170, 350, dummy_color, 8)  # Body
            arcade.draw_line(170, 415, 190, 375, dummy_color, 8)  # Right arm
        elif self.lives == 2:
            arcade.draw_circle_outline(170, 445, 20, dummy_color, 8)  # Head
            arcade.draw_line(170, 425, 170, 350, dummy_color, 8)  # Body
            arcade.draw_line(170, 415, 190, 375, dummy_color, 8)  # Right arm
            arcade.draw_line(170, 415, 150, 375, dummy_color, 8)  # Left arm
        elif self.lives == 1:
            arcade.draw_circle_outline(170, 445, 20, dummy_color, 8)  # Head
            arcade.draw_line(170, 425, 170, 350, dummy_color, 8)  # Body
            arcade.draw_line(170, 415, 190, 375, dummy_color, 8)  # Right arm
            arcade.draw_line(170, 415, 150, 375, dummy_color, 8)  # Left arm
            arcade.draw_line(170, 350, 190, 300, dummy_color, 8)  # Right leg
        elif self.lives == 0:
            arcade.draw_circle_outline(170, 445, 20, dummy_color, 8)  # Head
            arcade.draw_line(170, 425, 170, 350, dummy_color, 8)  # Body
            arcade.draw_line(170, 415, 190, 375, dummy_color, 8)  # Right arm
            arcade.draw_line(170, 415, 150, 375, dummy_color, 8)  # Left arm
            arcade.draw_line(170, 350, 190, 300, dummy_color, 8)  # Right leg
            arcade.draw_line(170, 350, 150, 300, dummy_color, 8)  # Left leg

        if self.game_over:
            self.replay_button.draw()  # Draw replay button if the game is over
        # Draw the win/lose sprite if needed
        if self.show_win_lose_sprite:
            self.win_lose_sprite.draw()
            if self.win_lose_sprite_text:
                arcade.draw_text(self.win_lose_sprite_text,
                                self.win_lose_sprite.center_x,
                                self.win_lose_sprite.center_y - self.win_lose_sprite.height / 2 +45,  # Adjust vertical offset
                                arcade.color.BLACK,
                                font_size=20,
                                anchor_x="center",
                                anchor_y="center")

    def on_mouse_press(self, x, y, button, modifiers):
        for button in self.buttons:
            button.on_mouse_press(x, y, button, modifiers)

        if self.game_over:
            self.replay_button.on_mouse_press(x, y, button, modifiers)  # Handle click on replay button

    def show_letter(self, word, secret_word, letter):
        new_secret_word = list(secret_word)
        for i, chosen_letter in enumerate(word):
            if chosen_letter.lower() == letter.lower():
                new_secret_word[i * 2] = chosen_letter
        return ''.join(new_secret_word)

    def update_hidden_word(self, clicked_letter):
        print("Updating hidden word...")
        print("Chosen Word:", self.chosen_word)
        print("Hidden Word Before Update:", self.hide_word)
        
        # Check if the game is not over and player has lives left
        if not self.game_over and self.lives > 0:
            letter_found = False
            new_secret_word = list(self.hide_word)
            for i, chosen_letter in enumerate(self.chosen_word):
                if chosen_letter.lower() == clicked_letter.lower():
                    new_secret_word[i * 2] = chosen_letter
                    letter_found = True
            if not letter_found:
                self.lives -= 1  # Decrement lives if letter is not found
                print("Incorrect guess! Lives remaining:", self.lives)  # Print remaining lives
            self.hide_word = ''.join(new_secret_word)
            print("Hidden Word After Update:", self.hide_word)

            # Check if all letters are revealed
            if self.hide_word.replace(" ", "") == self.chosen_word:
                self.show_win_lose_sprite = True
                self.game_over = True
                self.display_win_message()  # Display win message if all letters are revealed

                print("You win!")
        else:
            self.game_over = True
            if self.lives == 0:
                print("Game over! You ran out of lives.")
                self.show_win_lose_sprite = True
                self.display_lose_message()  # Display lose message if player runs out of lives

            else:
                print("Game over! You've already won.")

    def display_win_message(self):
        self.show_win_lose_sprite = True
        self.win_lose_sprite_text = " You win!"

    def display_lose_message(self):
        self.show_win_lose_sprite = True
        self.win_lose_sprite_text = " You lose!"


    def restart_game(self):
        # Reset game state for a new game
        chosen_word = random.choice(words)
        self.chosen_word = chosen_word
        self.hide_word = self.hidden_word_instance.word_hide(chosen_word)
        self.game_over = False
        self.lives = 6
        self.show_win_lose_sprite = False  # Hide win/lose sprite when restarting game
        # Reset the clicked flag for each button
        for button in self.buttons:
            button.reset()

class ThemeButton(arcade.Sprite):
    def __init__(self, x, y, width, height, theme_name, theme_image, on_click):
        super().__init__(theme_image, center_x=x, center_y=y)  # Load the theme image as the button's texture
        self.width = width
        self.height = height
        self.theme_name = theme_name
        self.on_click = on_click

    def on_mouse_press(self, x, y, button, modifiers):
        if self.collides_with_point((x, y)):
            self.on_click(self.theme_name)  # Pass the theme name when the button is clicked

    def draw(self):
        super().draw()
        arcade.draw_text(self.theme_name, self.center_x - self.width // 2, self.center_y - self.height // 2 + 10,
                         arcade.color.BLACK, 14, align="center", width=self.width)

class ReplayButton(arcade.Sprite):
    def __init__(self, image, x, y, on_click):
        super().__init__(image, center_x=x, center_y=y)
        self.width = 150
        self.height = 50
        self.on_click = on_click
        self.text_color = arcade.color.BLACK
        self.text_size = 20

    def on_mouse_press(self, x, y, button, modifiers):
        if self.collides_with_point((x, y)):
            self.on_click()

    def draw(self):
        super().draw()
        arcade.draw_text("Replay", self.center_x - 45, self.center_y - 10, self.text_color, self.text_size)

class Hidden_word:
    def __init__(self):
        pass

    def word_hide(self, word):
        secret_word = ''
        for l in word:
            if l != ' ':
                secret_word += '_ '
            else:
                secret_word += ' '
        return secret_word
class Button(arcade.Sprite):
    def __init__(self, image, x, y, letter, on_click):
        super().__init__(image, center_x=x, center_y=y)
        self.width = 30
        self.height = 50
        self.letter = letter
        self.on_click = on_click
        self.clicked = False  # Flag to track if the button has been clicked
        self.visible = True  # Flag to track if the button should be drawn

    def on_mouse_press(self, x, y, button, modifiers):
        if not self.clicked:  # Check if the button has already been clicked
            if self.collides_with_point((x, y)):
                self.on_click(self.letter)
                self.clicked = True  # Set clicked flag to True when the button is clicked
                self.visible = False  # Hide the button when clicked

    def draw(self):
        if self.visible:  # Only draw the button if it's visible
            super().draw()

            arcade.draw_text(self.letter,
                            self.center_x - self.width // 2,
                            self.center_y - self.height // 2 + 13,
                            arcade.color.BLACK,
                            font_size=20,
                            align="center",
                            width=self.width)
    def reset(self):
        self.clicked = False  # Reset the clicked flag to False when the game is restarted
        self.visible = True  # Make the button visible again when the game is restarted

def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, resizable=True)
    chosen_word = random.choice(words)
    game = game_window(chosen_word, western_theme)
    window.show_view(game)
    arcade.run()

if __name__ == "__main__":
    main()
