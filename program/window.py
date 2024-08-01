import customtkinter, logger as l, objects as obj

def main_window():
    l.logger.info("start program...")

    app = customtkinter.CTk()
    app.geometry("390x395+700+200")
    app.resizable(False, False)
    app.title("Calculator")

    obj.init_objects(app)

    l.logger.info("gui is created")
    app.mainloop()

if (__name__ == "__main__"):
    main_window()