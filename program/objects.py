import customtkinter, actions

def init_objects(app):
    app.grid_columnconfigure(0, weight=1)

    label1 = customtkinter.CTkLabel(app, text="My Calculator", text_color="dark gray", font=('Arial Black', 44))
    label1.grid(row=0, column=0, padx=0, pady=40, sticky="EW", columnspan=4)

    textbox1 = customtkinter.CTkTextbox(app, height=45, text_color="blue", fg_color="dark gray", font=('Arial Black', 30), corner_radius=0)
    textbox1.grid(row=1, column=0, padx=0, pady=0, sticky="EW", columnspan=4)

    buttonClear = customtkinter.CTkButton(app, text="C", text_color="blue", fg_color="gray", font=("Arial Black", 20), corner_radius=0,
                                        hover_color="red", height=40, width=98, command=lambda: actions.clear_textbox(textbox1))
    buttonClear.grid(row=2, column=0, padx=0, pady=0, sticky="ew")

    buttonDel = customtkinter.CTkButton(app, text="<-", text_color="blue", fg_color="gray", font=("Arial Black", 20), corner_radius=0,
                                         hover_color="red", height=40, width=98, command=lambda: actions.buttonDelete(textbox1))
    buttonDel.grid(row=2, column=1, padx=0, pady=0, sticky="ew")

    buttonDegree = customtkinter.CTkButton(app, text="^", text_color="blue", fg_color="gray", font=("Arial Black", 20), corner_radius=0,
                                        height=40, width=98, command=lambda: actions.print_to_textbox("^", textbox1))
    buttonDegree.grid(row=2, column=2, padx=0, pady=0, sticky="ew")

    buttonSum = customtkinter.CTkButton(app, text="+", text_color="blue", fg_color="gray", font=("Arial Black", 20), corner_radius=0,
                                         height=40, width=98, command=lambda: actions.print_to_textbox("+", textbox1))
    buttonSum.grid(row=2, column=3, padx=0, pady=0, sticky="ew")

    button7 = customtkinter.CTkButton(app, text="7", text_color="black", fg_color="dark gray", corner_radius=0,
                                       height=40, width=98, command=lambda: actions.print_to_textbox("7", textbox1))
    button7.grid(row=3, column=0, padx=0, pady=0, sticky="ew")

    button8 = customtkinter.CTkButton(app, text="8", text_color="black", fg_color="dark gray", corner_radius=0,
                                       height=40, width=98, command=lambda: actions.print_to_textbox("8", textbox1))
    button8.grid(row=3, column=1, padx=0, pady=0, sticky="ew")

    button9 = customtkinter.CTkButton(app, text="9", text_color="black", fg_color="dark gray", corner_radius=0,
                                       height=40, width=98, command=lambda: actions.print_to_textbox("9", textbox1))
    button9.grid(row=3, column=2, padx=0, pady=0, sticky="ew")

    buttonSub = customtkinter.CTkButton(app, text="-", text_color="black", fg_color="gray", corner_radius=0,
                                         height=40, width=98, command=lambda: actions.print_to_textbox("-", textbox1))
    buttonSub.grid(row=3, column=3, padx=0, pady=0, sticky="ew")

    button4 = customtkinter.CTkButton(app, text="4", text_color="black", fg_color="dark gray", corner_radius=0,
                                       height=40, width=98, command=lambda: actions.print_to_textbox("4", textbox1))
    button4.grid(row=4, column=0, padx=0, pady=0, sticky="ew")

    button5 = customtkinter.CTkButton(app, text="5", text_color="black", fg_color="dark gray", corner_radius=0,
                                       height=40, width=98, command=lambda: actions.print_to_textbox("5", textbox1))
    button5.grid(row=4, column=1, padx=0, pady=0, sticky="ew")

    button6 = customtkinter.CTkButton(app, text="6", text_color="black", fg_color="dark gray", corner_radius=0,
                                       height=40, width=98, command=lambda: actions.print_to_textbox("6", textbox1))
    button6.grid(row=4, column=2, padx=0, pady=0, sticky="ew")

    buttonMult = customtkinter.CTkButton(app, text="*", text_color="black", fg_color="gray", corner_radius=0,
                                          height=40, width=98, command=lambda: actions.print_to_textbox("*", textbox1))
    buttonMult.grid(row=4, column=3, padx=0, pady=0, sticky="ew")

    button1 = customtkinter.CTkButton(app, text="1", text_color="black", fg_color="dark gray", corner_radius=0,
                                       height=40, width=98, command=lambda: actions.print_to_textbox("1", textbox1))
    button1.grid(row=5, column=0, padx=0, pady=0, sticky="ew")

    button2 = customtkinter.CTkButton(app, text="2", text_color="black", fg_color="dark gray", corner_radius=0,
                                       height=40, width=98, command=lambda: actions.print_to_textbox("2", textbox1))
    button2.grid(row=5, column=1, padx=0, pady=0, sticky="ew")

    button3 = customtkinter.CTkButton(app, text="3", text_color="black", fg_color="dark gray", corner_radius=0,
                                       height=40, width=98, command=lambda: actions.print_to_textbox("3", textbox1))
    button3.grid(row=5, column=2, padx=0, pady=0, sticky="ew")

    buttonDiv = customtkinter.CTkButton(app, text="/", text_color="black", fg_color="gray", corner_radius=0,
                                         height=40, width=98, command=lambda: actions.print_to_textbox("/", textbox1))
    buttonDiv.grid(row=5, column=3, padx=0, pady=0, sticky="ew")

    buttonPoint = customtkinter.CTkButton(app, text=".", text_color="black", fg_color="gray", corner_radius=0,
                                           height=40, width=98, command=lambda: actions.print_to_textbox(".", textbox1))
    buttonPoint.grid(row=6, column=0, padx=0, pady=0, sticky="ew")

    button0 = customtkinter.CTkButton(app, text="0", text_color="black", fg_color="dark gray", corner_radius=0,
                                       height=40, width=98, command=lambda: actions.print_to_textbox("0", textbox1))
    button0.grid(row=6, column=1, padx=0, pady=0, sticky="ew")

    buttonEq = customtkinter.CTkButton(app, text="=", text_color="blue", fg_color="gray", font=("Arial Black", 20), corner_radius=0,
                                    hover_color="red", height=40, width=98, command=lambda: actions.buttonEq_Click(textbox1))
    buttonEq.grid(row=6, column=2, columnspan=2, padx=0, pady=0, sticky="ew")
