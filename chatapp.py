import tkinter as tk
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw()
        self.name = ""
        self.entry = None

    def layout(self, name):
        self.name = name
        self.root.deiconify()
        self.root.geometry("400x400")

        label_name = tk.Label(self.root, text="User: " + self.name)
        label_name.place(x=10, y=10)

        line_label = tk.Label(self.root, width=50)
        line_label.place(x=10, y=30)

        text_area = tk.Text(self.root)
        text_area.place(x=10, y=50, height=300, width=380)

        self.entry = tk.Entry(self.root)
        self.entry.place(x=10, y=360, width=300)

        line = tk.Label(self.root, text="-------------------------------------------------------------------")
        line.place(x=10, y=380)

        send_button = tk.Button(self.root, text="Send", command=self.send_message)
        send_button.place(x=320, y=360)

        scrollbar = tk.Scrollbar(self.root)
        scrollbar.place(x=390, y=50, height=300)
        text_area.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=text_area.yview)

        self.root.mainloop()

    def send_message(self):
        message = self.entry.get()
        self.write(message)
        self.entry.delete(0, "end")

    def write(self, message):
        pass

    def show_message(self, message):
        pass

def goAhead():
    name = input("Enter your name: ")
    gui = GUI()
    gui.layout(name)

if __name__ == "__main__":
    goAhead()

