import tkinter as tk

class MyRoot:
	def __init__(self, master):
		self.master = master
		self.label = None
		self.button = None
	def set_label(self, txt):
		self.label = tk.Label(self.master, text=txt, font=('Courier', 30))
		self.label.pack()
	def set_button(self, txt):
		self.button = tk.Button(self.master, text='Click', font=('Courier', 30))
		self.button.pack()
		self.button['command'] = lambda x=self.label: self.handler(x, txt)
	def handler(self, widget, value):
		widget.config(text=value)

		
if __name__ == '__main__':
	root = tk.Tk()
	mr = MyRoot(root)
	mr.set_label('This is a label')
	mr.set_button('Button clicked!!!')
	root.mainloop()

		