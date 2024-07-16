import actions

if (__name__ == "__main__"):
    term: str = input("Введите выражение: ")
    
    for i in term:
        if (i == "+"):
            term_list = term.split("+")
            x1: int = int(term_list[0])
            x2: int = int(term_list[1])
            actions.Add(x1, x2)
        elif (i == "-"):
            term_list = term.split("-")
            x1: int = int(term_list[0])
            x2: int = int(term_list[1])
            actions.Sub(x1, x2)
        elif (i == "*"):
            term_list = term.split("*")
            x1: int = int(term_list[0])
            x2: int = int(term_list[1])
            actions.Mult(x1, x2)
        elif (i == "/"):
            term_list = term.split("/")
            x1: int = int(term_list[0])
            x2: int = int(term_list[1])
            actions.Div(x1, x2)
