from tkinter import *
import random
from dict import *


class Main(Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()

    def init_main(self):
        game_start = Label(text='Выберите уровень сложности', font="16")
        game_start.place(x=70, y=5)

        easy_lvl = Button(text='Легкий', command=self.open_easy)
        easy_lvl.place(x=158, y=40)

        medium_lvl = Button(text='Средний', command=self.open_medium)
        medium_lvl.place(x=153, y=80)

        hard_lvl = Button(text='Тяжелый', command=self.open_hard)
        hard_lvl.place(x=152, y=120)

    def open_easy(self):
        Easy_lvl()

    def open_medium(self):
        Medium_lvl()

    def open_hard(self):
        Hard_lvl()


class Easy_lvl(Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child()
        self.view = app

    def init_child(self):
        self.geometry("400x420+500+200")
        self.title('Легкий уровень')
        self.new_button = Button(self, text="Получить новое слово", command=self.get_word)
        self.new_button.pack()
        global lab
        lab = Label(self, width=20, height=1)
        lab.pack()
        self.text = Label(self, text="Введите слово без ошибок").place(x=120, y=48)

        self.entry_word = Entry(self, width=25)
        self.entry_word.pack()
        self.entry_word.place(x=120, y=70)

        self.word = self.get_word()

        check_button = Button(self, text="Проверить!", command=self.result)
        check_button.place(x=155, y=120)

    def get_word(self):
        self.word = random.choice(list(short_words.items()))
        self.labres = Label(self, text=self.word[1][0], width=50, height=10, wraplength=150)
        self.labres.place(x=18, y=160)
        self.word_new = list(self.word[0])
        self.word_new[random.randint(0, len(self.word[0]) - 1)] = '*'
        lab['text'] = self.word_new
        return self.word

    def result(self):
        self.content = Entry.get(self.entry_word)
        if self.content == self.word[0]:
            self.labres = Label(self, text="Right  ", fg="#1AA81C")
            self.labres.place(x=170, y=97)
            self.labres.update()
        else:
            self.labres = Label(self, text="Wrong", fg='#FF2400')
            self.labres.place(x=170, y=97)
            self.labres.update()


class Medium_lvl(Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child()
        self.view = app

    def init_child(self):

        self.geometry("400x420+500+200")
        self.title('Средний уровень')
        self.new_button = Button(self, text="Получить новое слово", command=self.get_word)
        self.new_button.pack()
        global lab
        lab = Label(self, width=20, height=1)
        lab.pack()
        self.text = Label(self, text="Введите слово без ошибок").place(x=120, y=48)

        self.entry_word = Entry(self, width=25)
        self.entry_word.pack()
        self.entry_word.place(x=120, y=70)

        self.word = self.get_word()

        check_button = Button(self, text="Проверить!", command=self.result)
        check_button.place(x=155, y=120)

    def get_word(self):
        self.word = random.choice(list(medium_words.items()))
        self.labres = Label(self, text=self.word[1][0], width=50, height=10, wraplength=150)
        self.labres.place(x=18, y=160)
        word_new = list(self.word[0])
        counter = 0
        while counter < 4:
            index = random.randint(0, len(word_new) - 1)
            if word_new[index] != '*':
                word_new[index] = '*'
                counter += 1
        lab['text'] = word_new
        return self.word

    def result(self):
        self.content = Entry.get(self.entry_word)
        if self.content == self.word[0]:
            self.labres = Label(self, text="Right  ", fg="#1AA81C")
            self.labres.place(x=170, y=97)
            self.labres.update()
        else:
            self.labres = Label(self, text="Wrong", fg='#FF2400')
            self.labres.place(x=170, y=97)
            self.labres.update()


class Hard_lvl(Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child()
        self.view = app

    def init_child(self):
        self.geometry("400x420+500+200")
        self.title('Тяжелый уровень')
        self.new_button = Button(self, text="Получить новое слово", command=self.get_word)
        self.new_button.pack()
        global lab
        lab = Label(self, width=20, height=1)
        lab.pack()
        self.text = Label(self, text="Введите слово без ошибок").place(x=120, y=48)

        self.entry_word = Entry(self, width=25)
        self.entry_word.pack()
        self.entry_word.place(x=120, y=70)

        self.word = self.get_word()

        check_button = Button(self, text="Проверить!", command=self.result)
        check_button.place(x=155, y=120)

    def get_word(self):
        self.word = random.choice(list(long_words.items()))
        self.labres = Label(self, text=self.word[1][0], width=50, height=10, wraplength=150)
        self.labres.place(x=18, y=160)
        self.word_new = list(self.word[0])
        for i in range(len(self.word_new)):
            self.word_new[i] = '*'
        lab['text'] = self.word_new
        return self.word

    def result(self):
        self.content = Entry.get(self.entry_word)
        if self.content == self.word[0]:
            self.labres = Label(self, text="Right  ", fg="#1AA81C")
            self.labres.place(x=170, y=97)
            self.labres.update()
        else:
            self.labres = Label(self, text="Wrong", fg='#FF2400')
            self.labres.place(x=170, y=97)
            self.labres.update()


if __name__ == "__main__":
    root = Tk()
    app = Main(root)
    app.pack()
    root.title("Learn English words")
    root.geometry("350x250+300+150")
    root.resizable(False, False)
    root.mainloop()