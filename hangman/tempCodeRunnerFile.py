    def on_mouse_press(self, x, y, button, modifiers):
        print("Mouse Clicked at:", x, y)
        for button in self.buttons:
            button.on_mouse_press(x, y, button, modifiers)

        if self.game_over:
            self.replay_button.on_mouse_press(x, y, button, modifiers)  # Handle click on replay button
