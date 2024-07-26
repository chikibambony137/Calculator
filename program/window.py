import customtkinter

def button1_Click():
    print("Ughhh...")

if (__name__ == "__main__"):
    app = customtkinter.CTk()
    app.geometry("390x500+700+200")
    app.resizable(False, False)
    app.title("Calculator")

    app.grid_columnconfigure(0, weight=1)
    
    label1 = customtkinter.CTkLabel(app, text="Calculator228")
    label1.grid(row=0, column=0, padx=0, pady=0, sticky="EW", columnspan=3)

    textbox1 = customtkinter.CTkTextbox(app, width=100, height=10)
    textbox1.grid(row=1, column=0, padx=0, pady=1, sticky="NSEW", columnspan=3)
    
    button1 = customtkinter.CTkButton(app, text="1", width=130, command=button1_Click)
    button1.grid(row=2, column=0, padx=0, pady=0, sticky="ew")

    button2 = customtkinter.CTkButton(app, text="2", width=130, command=button1_Click)
    button2.grid(row=2, column=1, padx=0, pady=0, sticky="ew")

    button3 = customtkinter.CTkButton(app, text="3", width=130, command=button1_Click)
    button3.grid(row=2, column=2, padx=0, pady=0, sticky="ew")

    button4 = customtkinter.CTkButton(app, text="4", width=130, command=button1_Click)
    button4.grid(row=3, column=0, padx=0, pady=0, sticky="ew")

    button5 = customtkinter.CTkButton(app, text="5", width=130, command=button1_Click)
    button5.grid(row=3, column=1, padx=0, pady=0, sticky="ew")

    button6 = customtkinter.CTkButton(app, text="6", width=130, command=button1_Click)
    button6.grid(row=3, column=2, padx=0, pady=0, sticky="ew")

    button7 = customtkinter.CTkButton(app, text="7", width=130, command=button1_Click)
    button7.grid(row=4, column=0, padx=0, pady=0, sticky="ew")

    button8 = customtkinter.CTkButton(app, text="8", width=130, command=button1_Click)
    button8.grid(row=4, column=1, padx=0, pady=0, sticky="ew")

    button9 = customtkinter.CTkButton(app, text="9", width=130, command=button1_Click)
    button9.grid(row=4, column=2, padx=0, pady=0, sticky="ew")

    button0 = customtkinter.CTkButton(app, text="0", width=130, command=button1_Click)
    button0.grid(row=5, column=1, padx=0, pady=0, sticky="ew")


    app.mainloop()