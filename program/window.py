import customtkinter, logger as l, objects as obj

def main_window():
    l.logger.info("start program...")

    app = customtkinter.CTk()
    app.geometry("390x500+700+200")
    app.resizable(False, False)
    app.title("Calculator")

    app.grid_columnconfigure(0, weight=1)
    obj.init_objects(app)

    l.logger.info("gui is created")
    app.mainloop()

if (__name__ == "__main__"):
    main_window()