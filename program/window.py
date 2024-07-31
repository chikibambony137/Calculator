import customtkinter, logger as l, actions

def init_objects(app):
    label1 = customtkinter.CTkLabel(app, text="My Calculator")
    label1.grid(row=0, column=0, padx=0, pady=0, sticky="EW", columnspan=3)

    textbox1 = customtkinter.CTkTextbox(app, width=100, height=10)
    textbox1.grid(row=1, column=0, padx=0, pady=1, sticky="NSEW", columnspan=3)
    
    button1 = customtkinter.CTkButton(app, text="1", width=130, command=lambda: actions.print_to_textbox("1", textbox1))
    button1.grid(row=2, column=0, padx=0, pady=0, sticky="ew")

    button2 = customtkinter.CTkButton(app, text="2", width=130, command=lambda: actions.print_to_textbox("2", textbox1))
    button2.grid(row=2, column=1, padx=0, pady=0, sticky="ew")

    button3 = customtkinter.CTkButton(app, text="3", width=130, command=lambda: actions.print_to_textbox("3", textbox1))
    button3.grid(row=2, column=2, padx=0, pady=0, sticky="ew")

    button4 = customtkinter.CTkButton(app, text="4", width=130, command=lambda: actions.print_to_textbox("4", textbox1))
    button4.grid(row=3, column=0, padx=0, pady=0, sticky="ew")

    button5 = customtkinter.CTkButton(app, text="5", width=130, command=lambda: actions.print_to_textbox("5", textbox1))
    button5.grid(row=3, column=1, padx=0, pady=0, sticky="ew")

    button6 = customtkinter.CTkButton(app, text="6", width=130, command=lambda: actions.print_to_textbox("6", textbox1))
    button6.grid(row=3, column=2, padx=0, pady=0, sticky="ew")

    button7 = customtkinter.CTkButton(app, text="7", width=130, command=lambda: actions.print_to_textbox("7", textbox1))
    button7.grid(row=4, column=0, padx=0, pady=0, sticky="ew")

    button8 = customtkinter.CTkButton(app, text="8", width=130, command=lambda: actions.print_to_textbox("8", textbox1))
    button8.grid(row=4, column=1, padx=0, pady=0, sticky="ew")

    button9 = customtkinter.CTkButton(app, text="9", width=130, command=lambda: actions.print_to_textbox("9", textbox1))
    button9.grid(row=4, column=2, padx=0, pady=0, sticky="ew")

    button0 = customtkinter.CTkButton(app, text="0", width=130, command=lambda: actions.print_to_textbox("0", textbox1))
    button0.grid(row=5, column=1, padx=0, pady=0, sticky="ew")

    buttonSum = customtkinter.CTkButton(app, text="+", width=130, command=lambda: actions.print_to_textbox("+", textbox1))
    buttonSum.grid(row=5, column=0, padx=0, pady=0, sticky="ew")

    buttonEq = customtkinter.CTkButton(app, text="=", width=130, command=lambda: actions.buttonEq_Click(textbox1))
    buttonEq.grid(row=5, column=2, padx=0, pady=0, sticky="ew")

    buttonClear = customtkinter.CTkButton(app, text="C", width=130, command=lambda: actions.clear_textbox(textbox1))
    buttonClear.grid(row=6, column=1, columnspan=2, padx=0, pady=0, sticky="ew")

def main_window():
    l.logger.info("start program...")

    app = customtkinter.CTk()
    app.geometry("390x500+700+200")
    app.resizable(False, False)
    app.title("Calculator")

    app.grid_columnconfigure(0, weight=1)
    init_objects(app)

    l.logger.info("gui is created")
    app.mainloop()

if (__name__ == "__main__"):
    main_window()