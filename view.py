import tkinter as tk


class View:
    def __init__(self, root):
        self.root = root
        self.grids = ((0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1))
        self.labels = []
        for (i, j) in self.grids:
            self.labels.append(tk.Label(self.root, text=f'Label {i}{j}', font=('Arial', 17), width=20))
            self.labels[-1].grid(row=i, column=j)

    def set_label_text(self, text, num):
        if num in range(len(self.labels)):
            self.labels[num]['text'] = text


