class Button():
    def __init__(self, tittle_text, x, y, appearance):
        self.tittle = tittle_text
        self.x = x
        self.y = y
        self.appearance = True

    def hide(self):
        self.appearance = False
    def show(self):
        self.appearance = True

    def print_info(self):
        print("Дані про віджет:")
        print(self.tittle, self.x, self.y, self.appearance)

button_1 = Button("ok", 100, 100)
button_1.print_info()
button_1.hide()
button_1.print_info()