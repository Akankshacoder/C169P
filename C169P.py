import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


class CreateElements:
    def __init__(self, root):
        print("This is CreateElements class")
        self.root = root

    def createLabel(self):
        label = tk.Label(self.root, text="A new label has been created using class", fg="blue")
        label.pack()

    def createButton(self):
        button = tk.Button(self.root, text="Button", command=self.message)
        button.pack(padx=10, pady=10)

    def createDropdown(self):
        values = [1, 2, 3]
        self.combobox = ttk.Combobox(self.root, values=values, state="readonly")
        self.combobox.pack()

    def choose(self):
        global element
        element = self.combobox.get()
        if element == "Label":
            self.createLabel()
        elif element == "Button":
            self.createButton()
        elif element == "Dropdown":
            self.createDropdown()

    def message(self):
        showinfo("Message", "You clicked the button created using class")

root = tk.Tk()
root.title("Dynamic Element Creator")
root.geometry("600x600")

# Create a combobox
elements = ["Label", "Button", "Dropdown"]
combobox = ttk.Combobox(root, values=elements, state="readonly")
combobox.pack()

# Instantiate the class
creator = CreateElements(root)

# Create a button to create the selected element
create_button = tk.Button(root, text="Create Element", command=creator.choose)
create_button.pack(padx=10, pady=10)

root.mainloop()
