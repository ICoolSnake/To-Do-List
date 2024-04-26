import tkinter as tk


class TodoList:
    def __init__(self, parent, font=("Roboto Mono", 14)):
        self.parent = parent
        self.frame = tk.Frame(parent, bg="#000000")  # Ana çerçevenin arkaplanı siyah
        self.frame.pack(fill=tk.X, expand=True, padx=10, pady=10)

        # Entry for new tasks
        self.task_entry = tk.Entry(
            self.frame, font=font, bg="#000000", fg="white", insertbackground="white"
        )
        self.task_entry.grid(row=0, column=0, sticky="ew", padx=(0, 5))
        self.frame.grid_columnconfigure(0, weight=3)

        # Add/Delete Task button
        self.task_button = tk.Button(
            self.frame,
            text="Add Task",
            font=font,
            bg="#000000",
            fg="white",
            command=self.add_or_delete_task,
        )
        self.task_button.grid(row=0, column=1, sticky="ew")
        self.frame.grid_columnconfigure(1, weight=1)

        # Listbox to display tasks
        self.task_listbox = tk.Listbox(
            self.frame, height=15, font=font, bg="#000000", fg="white"
        )
        self.task_listbox.grid(row=1, column=0, sticky="ew", columnspan=2)
        self.task_listbox.bind("<<ListboxSelect>>", self.on_select)

        self.selected_index = None

    def add_or_delete_task(self):
        if self.selected_index is not None:
            self.task_listbox.delete(self.selected_index)
            self.task_button.config(text="Add Task")
            self.selected_index = None
        else:
            task = self.task_entry.get()
            if task:
                self.task_listbox.insert(tk.END, task)
                self.task_entry.delete(0, tk.END)

    def on_select(self, event):
        selection = event.widget.curselection()
        if selection:
            self.selected_index = selection[0]
            self.task_button.config(text="Delete Task")
        else:
            self.selected_index = None
            self.task_button.config(text="Add Task")
