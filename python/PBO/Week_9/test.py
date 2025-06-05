import tkinter as t

def show_message():
    print("This is a message from the PBO test script.")

if __name__ == "__main__":
    root = t.Tk()
    root.title("PBO Test")

    label = t.Label(root, text="Hello, PBO!", bg="lightblue", font=("Arial", 16))

    button = t.Button(root, text="Click Me", command=show_message, bg="lightgreen", font=("Arial", 12))
    
    label.grid(row=0, column=0, padx=10, pady=10)
    button.grid(row=1, column=0, padx=10, pady=10)

    root.mainloop()