import tkinter as tk

class ShowNameApp:
    def __init__(self, master):
        self.master = master
        master.title("Menampilkan nama : ")

        frmLabelAndNameEntry = tk.Frame(self.master)
        frmLabelAndNameEntry.config(bg="lightblue")
        frmLabelAndNameEntry.pack(fill=tk.BOTH, expand=True)

        frmButton = tk.Frame(self.master)
        frmButton.config(bg="yellow")
        frmButton.pack(fill=tk.BOTH, expand=True)

        self.lblOutputNama = tk.Label(frmLabelAndNameEntry, text="")
        self.lblOutputNama.pack(pady=10)

        self.entryNama = tk.Entry(frmLabelAndNameEntry)
        self.entryNama.pack(pady=10)

        self.btnTampil = tk.Button(frmButton, text="Show Name", command=self.show_name)
        self.btnTampil.grid(row=0, column=0, padx=10, pady=1)

        self.btnTampilOutputBox = tk.Button(frmButton, text="Show Output Box", command=self.show_output_box)
        self.btnTampilOutputBox.grid(row=0, column=1, padx=10, pady=1)

        self.btnReset = tk.Button(frmButton, text="Reset", command=self.reset)
        self.btnReset.grid(row=0, column=2, padx=10, pady=1)

    def show_name(self):
        self.name = self.entryNama.get()
        self.lblOutputNama.config(text=f"Nama anda adalah : {self.name}")

    def show_output_box(self):
        self.name = self.entryNama.get()
        output_window = tk.Toplevel(self.master)
        output_window.title("Output")
        output_window.geometry("300x200")
        
        text_widget = tk.Text(output_window, wrap=tk.WORD)
        text_widget.insert(tk.END, f"Nama anda adalah : {self.name}\n")
        text_widget.pack(expand=True, fill=tk.BOTH)
        
        close_button = tk.Button(output_window, text="Tutup", command=output_window.destroy)
        close_button.pack(pady=10)
        
    def reset(self):
        self.entryNama.delete(0, tk.END)
        self.lblOutputNama.config(text="")   

if __name__ == "__main__":
    root = tk.Tk()
    app = ShowNameApp(root)
    root.mainloop()