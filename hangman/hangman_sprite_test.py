import arcade
import os
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Hangman"
PANEL_HEIGHT = 200

# Background images
background = arcade.load_texture("media/aesthetic-western-background-desktop-wallpaper.jpg")
vertical_wood = arcade.load_texture("media/photos_2023_7_4_fst_old-wood-cracked-knots_vertical.jpg")
horizontal_wood = arcade.load_texture("media/photos_2023_7_4_fst_old-wood-cracked-knots_horizontal.jpg")
rope = arcade.load_texture("media/fabrics_0066_cylinder_600.png")
DEFAULT_FONT_SIZE = 50

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
    def __init__(self, chosen_word):
        super().__init__()

        # Initialize game components
        self.chosen_word = chosen_word
        self.hidden_word_instance = Hidden_word()
        self.hide_word = self.hidden_word_instance.word_hide(chosen_word)

        print("Chosen word:", chosen_word)
        # UI components
        self.buttons = []

        # Create buttons for each letter of the alphabet
        self.create_buttons()

    def create_buttons(self):
        button_width = 25
        button_spacing = 5
        start_x = 20
        start_y = 50

        for i, letter in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
            button = Button("media/fabrics_0066_cylinder_600.png", start_x + i * (button_width + button_spacing), start_y, letter, self.on_button_click)
            self.buttons.append(button)

    def on_button_click(self, letter):
        print("Button clicked! Letter:", letter)
        self.update_hidden_word(letter)
        print("Updated hidden word:", self.hide_word)

    def on_draw(self):
        arcade.start_render()

        # Draw the background images
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, background)
        arcade.draw_lrwh_rectangle_textured(50, 250, 25, 300, vertical_wood)
        arcade.draw_lrwh_rectangle_textured(165, 455, 10, 50, rope)
        arcade.draw_lrwh_rectangle_textured(25, 500, 175, 25, horizontal_wood)

        # Draw the buttons
        for button in self.buttons:
            button.draw()
            arcade.draw_text(button.letter,
                            button.center_x - button.width // 2,
                            button.center_y - button.height // 2+13,
                            arcade.color.BLACK,
                            font_size=20,
                            align="center",
                            width=button.width)
        
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
            
    def on_mouse_press(self, x, y, button, modifiers):
        for button in self.buttons:
            button.on_mouse_press(x, y, button, modifiers)

    def show_letter(self, word, secret_word, letter):
        new_secret_word = list(secret_word)  # Convert the secret_word string to a list for easier manipulation
        for i, chosen_letter in enumerate(word):
            if chosen_letter.lower() == letter.lower():
                new_secret_word[i * 2] = chosen_letter  # Update the corresponding position in the new_secret_word list
        return ''.join(new_secret_word)

    def update_hidden_word(self, clicked_letter):
        print("Updating hidden word...")
        print("Chosen Word:", self.chosen_word)
        print("Hidden Word Before Update:", self.hide_word)
        self.hide_word = self.show_letter(self.chosen_word, self.hide_word, clicked_letter)
        print("Hidden Word After Update:", self.hide_word)

class Button(arcade.Sprite):
    def __init__(self, image, x, y, letter, on_click):
        super().__init__(image, center_x=x, center_y=y)
        self.width = 30
        self.height = 50
        self.letter = letter
        self.on_click = on_click


    def on_mouse_press(self, x, y, button, modifiers):
        if self.collides_with_point((x, y)):
            self.on_click(self.letter)

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

def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, resizable=True)
    chosen_word = random.choice(words)
    game = game_window(chosen_word)
    window.show_view(game)
    arcade.run()

if __name__ == "__main__":
    main()
