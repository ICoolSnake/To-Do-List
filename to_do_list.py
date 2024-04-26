import tkinter as tk
from tkinter import messagebox
import hashlib
from add_book import TodoList


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Application")
        self.geometry("1024x720")
        self.attributes("-alpha", 0.8)
        self.configure(bg="#000000")
        self.frame = None
        self.check_integrity()

    def display_welcome(self, name):
        self.clear_frame()
        self.frame = tk.Frame(self, bg="#000000")
        # Ana çerçeveyi eklerken pencere boyutuna göre genişlet
        self.frame.pack(fill=tk.BOTH, expand=True)

        # İçerik çerçevesi pencerenin merkezine yerleştirilecek
        content_frame = tk.Frame(self.frame, bg="#000000")
        content_frame.pack(
            fill=tk.X, pady=50,  padx=152
        )  # yatay eksende genişleyecek, dikeyde 50px üstten boşluk ile

        welcome_label = tk.Label(
            content_frame,
            text=f"Welcome, {name} ♥",
            font=("Roboto Mono", 20),
            fg="white",
            bg="#000000",
        )
        welcome_label.pack(pady=10)  # Label'ı dikey olarak merkeze yerleştir

        self.todo_list = TodoList(content_frame)  # TodoList'i içerik çerçevesine ekle

    def get_user_name(self):
        self.clear_frame()
        self.frame = tk.Frame(self, bg="#000000")
        self.frame.pack(expand=True)

        label = tk.Label(
            self.frame,
            text="Please enter your name:",
            font=("Roboto Mono", 14),
            fg="white",
            bg="#000000",
        )
        label.pack(pady=20)

        entry = tk.Entry(self.frame, font=("Roboto Mono", 14), validate="key")
        entry["validatecommand"] = (entry.register(self.check_length), "%P")
        entry.pack(pady=10)
        entry.focus()

        submit_button = tk.Button(
            self.frame,
            text="Submit",
            command=lambda: self.save_name(entry.get()),
            font=("Roboto Mono", 14),
        )
        submit_button.pack(pady=10)

    def check_length(self, text):
        return len(text) <= 40

    def save_name(self, name):
        name = " ".join(name.split())
        if name:
            with open("username.txt", "w") as file:
                file.write(name)

            # Calculate and save the hash of the file
            hash_value = hashlib.sha256(name.encode()).hexdigest()
            with open("hash.txt", "w") as hash_file:
                hash_file.write(hash_value)

            self.display_welcome(name)
        else:
            messagebox.showerror("Error", "Please enter a name.")

    def check_integrity(self):
        try:
            with open("username.txt", "r") as file:
                name = file.read().strip()
                if name:
                    with open("hash.txt", "r") as hash_file:
                        saved_hash = hash_file.read().strip()
                        current_hash = hashlib.sha256(name.encode()).hexdigest()
                        if saved_hash == current_hash:
                            self.display_welcome(name)
                        else:
                            self.get_user_name()
                else:
                    self.get_user_name()
        except FileNotFoundError:
            self.get_user_name()

    def clear_frame(self):
        if self.frame is not None:
            self.frame.destroy()
            self.frame = None


if __name__ == "__main__":
    app = Application()
    app.mainloop()
