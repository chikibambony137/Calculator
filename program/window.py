import customtkinter

def button1_Click():
    print("Ughhh...")

if (__name__ == "__main__"):
    app = customtkinter.CTk()
    app.geometry("400x500")
    app.title("Calculator")

    app.grid_columnconfigure(0, weight=1)
    
    button1 = customtkinter.CTkButton(app, text="tap meeee", command=button1_Click)
    button1.grid(row=0, column=0, padx=0, pady=0, sticky="EW")

    textbox1 = customtkinter.CTkTextbox(app, width=100, height=10)
    textbox1.grid(row=1, column=0, padx=0, pady=1, sticky="NSEW")
    textbox1.size

    app.mainloop()