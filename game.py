import tkinter as tk
from .view import View
from .fighter import Fighter
import json
import time
import random


class Game:
    def __init__(self):
        self.root = tk.Tk()
        self.view = View(self.root)
        self.fighters = []
        self.parse_data()
        self.start()
        self.root.mainloop()

    def parse_data(self):
        with open('data.json', 'r') as myfile:
            data = myfile.read()
            obj = json.loads(data)
            for key, value,  in obj.items():
                print(key, value)
                self.fighters.append(Fighter(key, dict(zip(value['actions'], value['damages']))))
                print(self.fighters[-1].arsenal)

    def start(self):
        self.show_names()
        self.show_health()
        self.root.update()
        while all([f.health > 0 for f in self.fighters]):
            self.view.set_label_text('', 4)
            self.view.set_label_text('', 5)
            self.move()
        self.show_winner()

    def show_winner(self):
        for i, f in enumerate(self.fighters):
            if f.health > 0:
                self.view.labels[i].config(fg='red')
                self.root.update()


    def move(self):
        time.sleep(0.5)
        n = random.choice([0, 1])
        fighter = self.fighters[n]
        acceptor = self.fighters[(n + 1) % len(self.fighters)]
        action, damage = random.choice(list(fighter.arsenal.items()))
        self.view.set_label_text(action, 4+n)
        acceptor.got_damage(damage=damage)
        self.show_health()
        self.root.update()



    def show_names(self):
        for i in range(len(self.fighters)):
            self.view.set_label_text(self.fighters[i].name, i)

    def show_health(self):
        for i in range(len(self.fighters)):
            health = self.fighters[i].health
            print(health)
            self.view.set_label_text(self.fighters[i].health, i+2)

