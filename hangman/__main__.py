# Basic arcade program
# Displays a white window with a blue circle in the middle

# Imports
import arcade
import arcade.gui
import os
from arcade import Section
import random

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Hangman"
PANEL_HEIGHT = 200
os.chdir(os.path.dirname(os.path.abspath(__file__)))
#background image variable
background = arcade.load_texture("media/aesthetic-western-background-desktop-wallpaper.jpg")
vertical_wood = arcade.load_texture("media/photos_2023_7_4_fst_old-wood-cracked-knots_vertical.jpg")
horizontal_wood = arcade.load_texture("media/photos_2023_7_4_fst_old-wood-cracked-knots_horizontal.jpg")
rope = arcade.load_texture("media/fabrics_0066_cylinder_600.png")

class game_window(arcade.View):


    def __init__(self):
        #starts the game
        super().__init__()


        #setting up sprites
        self.letters_list = arcade.SpriteList()
        self.body_parts_list = arcade.SpriteList()
        self.all_sprites = arcade.SpriteList()
        self.panel = Alphabet_Panel(0,0,SCREEN_WIDTH, PANEL_HEIGHT)
        self.map = Map(0, 0,SCREEN_WIDTH, SCREEN_HEIGHT)
        self.section_manager.add_section(self.map)
        self.section_manager.add_section(self.panel)
class Hidden_word:#creates the word
    def __init__(self):
        secret_word=self.word_hide
        word = self.choose_word

    def word_list(self,filename):#acesses my word list file and creates a list of those words
        list_of_words = []
        with open(filename) as file:
            for line in file:
                list_of_words.append(line.rstrip('\n'))
        word_list = list_of_words
        return word_list

    def choose_word(self,word_list):#chooses a random word from the list
        word = random.choice(word_list)
        self.word = word
        return word
    def word_hide(self,word):#changes the word to underscores
        self.secret_word = ''
        temp_word = word
        for l in temp_word:
            if l != ' ':
                self.secret_word = self.secret_word + '_'
            else:
                self.secret_word = self.secret_word + ' '

        return self.secret_word
    def show_letter(self, word, secret_word, letter,director):#checks if the choosen letter is in the word and then reveals it if it is, if it is not it tells the director to remove a life
        
        list_word = list(word)
        list_secret_word = list(secret_word)
        for i in range(len(list_word)):
            if letter == list_word[i]:
                list_secret_word[i] = letter
                self.secret_word = "".join(list_secret_word)
   
        if letter not in list_word:
            director.lives = 1
        return self.secret_word
class Map(Section):
    def __init__(self, left:int, bottom:int, Width:int, Height:int):
        
        super().__init__( left, bottom, Width, Height)

    def on_draw(self):
        # Set the background color
        arcade.set_background_color(arcade.color.WHITE)

        # Clear the screen and start drawing
        arcade.start_render()

        #set background
        arcade.draw_lrwh_rectangle_textured(0, 0,SCREEN_WIDTH, SCREEN_HEIGHT,background)

        #create gallows
        arcade.draw_lrwh_rectangle_textured(50,250,25,300,vertical_wood)
        arcade.draw_lrwh_rectangle_textured(165,455,10,50,rope)
        arcade.draw_lrwh_rectangle_textured(25,500,175,25,horizontal_wood)




class Alphabet_Panel(Section):
    def __init__(self, left:int, bottom:int, Width:int, Height:int):
        
        super().__init__( left, bottom, Width, Height)
        
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        self.h_box = arcade.gui.UIBoxLayout(vertical=False)
        A_button = arcade.gui.UIFlatButton(text="A", width=20)
        self.h_box.add(A_button.with_space_around(right=10))
        B_button = arcade.gui.UIFlatButton(text="B", width=20)
        self.h_box.add(B_button.with_space_around(right=10))
        C_button = arcade.gui.UIFlatButton(text="C", width=20)
        self.h_box.add(C_button.with_space_around(right=10))
        D_button = arcade.gui.UIFlatButton(text="D", width=20)
        self.h_box.add(D_button.with_space_around(right=10))
        E_button = arcade.gui.UIFlatButton(text="E", width=20)
        self.h_box.add(E_button.with_space_around(right=10))
        F_button = arcade.gui.UIFlatButton(text="F", width=20)
        self.h_box.add(F_button.with_space_around(right=10))
        G_button = arcade.gui.UIFlatButton(text="G", width=20)
        self.h_box.add(G_button.with_space_around(right=10))
        H_button = arcade.gui.UIFlatButton(text="H", width=20)
        self.h_box.add(H_button.with_space_around(right=10))
        I_button = arcade.gui.UIFlatButton(text="I", width=20)
        self.h_box.add(I_button.with_space_around(right=10))
        J_button = arcade.gui.UIFlatButton(text="J", width=20)
        self.h_box.add(J_button.with_space_around(right=10))
        K_button = arcade.gui.UIFlatButton(text="K", width=20)
        self.h_box.add(K_button.with_space_around(right=10))
        L_button = arcade.gui.UIFlatButton(text="L", width=20)
        self.h_box.add(L_button.with_space_around(right=10))
        M_button = arcade.gui.UIFlatButton(text="M", width=20)
        self.h_box.add(M_button.with_space_around(right=10))
        N_button = arcade.gui.UIFlatButton(text="N", width=20)
        self.h_box.add(N_button.with_space_around(right=10))
        O_button = arcade.gui.UIFlatButton(text="O", width=20)
        self.h_box.add(O_button.with_space_around(right=10))
        P_button = arcade.gui.UIFlatButton(text="P", width=20)
        self.h_box.add(P_button.with_space_around(right=10))
        Q_button = arcade.gui.UIFlatButton(text="Q", width=20)
        self.h_box.add(Q_button.with_space_around(right=10))
        R_button = arcade.gui.UIFlatButton(text="R", width=20)
        self.h_box.add(R_button.with_space_around(right=10))
        S_button = arcade.gui.UIFlatButton(text="S", width=20)
        self.h_box.add(S_button.with_space_around(right=10))
        T_button = arcade.gui.UIFlatButton(text="T", width=20)
        self.h_box.add(T_button.with_space_around(right=10))
        U_button = arcade.gui.UIFlatButton(text="U", width=20)
        self.h_box.add(U_button.with_space_around(right=10))
        V_button = arcade.gui.UIFlatButton(text="V", width=20)
        self.h_box.add(V_button.with_space_around(right=10))
        X_button = arcade.gui.UIFlatButton(text="X", width=20)
        self.h_box.add(X_button.with_space_around(right=10))
        Y_button = arcade.gui.UIFlatButton(text="Y", width=20)
        self.h_box.add(Y_button.with_space_around(right=10))
        Z_button = arcade.gui.UIFlatButton(text="Z", width=20)
        self.h_box.add(Z_button.with_space_around(right=10))



        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center",

                anchor_y="center",
                align_y = -250,
                child=self.h_box)
        )
    def on_draw(self):
        self.manager.draw()
def main():
    window = arcade.Window(resizable=True)
    game = game_window()

    window.show_view(game)

    window.run()


# Display everything
if __name__ == "__main__":
    main()