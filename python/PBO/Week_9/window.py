import tkinter as t

class PBOTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PBO")

        # Konfigurasi grid root agar kolom bisa melebar
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.rowconfigure(3, weight=1)  # Text area bisa melebar ke bawah

        # Label
        self.label = t.Label(self.root, text="Masukkan Nama Anda", font=("Arial", 16))
        self.label.grid(row=0, column=0, columnspan=2, padx=10, pady=(20, 10), sticky="ew")

        # Entry
        self.entry = t.Entry(self.root, font=("Arial", 14))
        self.entry.grid(row=1, column=0, columnspan=2, padx=10, pady=(0, 20), sticky="ew")

        # Frame untuk button
        button_frame = t.Frame(self.root)
        button_frame.grid(row=2, column=0, columnspan=2, pady=(0, 10), sticky="ew")

        # Biarkan button-frame bisa melar
        button_frame.columnconfigure(0, weight=1)
        button_frame.columnconfigure(1, weight=1)

        # Button Tampil
        self.button = t.Button(button_frame, text="Click Me", command=self.show_message, bg="lightgreen", font=("Arial", 12))
        self.button.grid(row=0, column=0, padx=5, sticky="ew")

        # Button Reset
        self.reset_button = t.Button(button_frame, text="Reset", command=self.reset, bg="lightcoral", font=("Arial", 12))
        self.reset_button.grid(row=0, column=1, padx=5, sticky="ew")

        # Text Area untuk output
        self.text_area = t.Text(self.root, font=("Arial", 12))
        self.text_area.grid(row=3, column=0, columnspan=2, padx=10, pady=(10, 20), sticky="nsew")

    def format_message(self, name):
        return f"Nama anda adalah {name}!\n"

    def show_message(self):
        name = self.entry.get()
        self.text_area.config(state="normal")
        self.text_area.delete("1.0", t.END)
        if not name:
            self.text_area.insert(t.END, "Nama tidak boleh kosong!\n")
        else:
            message = self.format_message(name)
            self.text_area.insert(t.END, message)
        self.text_area.config(state="disabled")

    def reset(self):
        self.entry.delete(0, 'end')
        self.text_area.config(state="normal")
        self.text_area.delete("1.0", t.END)
        self.text_area.config(state="disabled")