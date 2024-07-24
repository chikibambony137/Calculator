import actions

operations: dict = {
        "+": actions.Add,
        "-": actions.Sub,
        "*": actions.Mult,
        "/": actions.Div
}

if (__name__ == "__main__"):
    term: str = input("Введите выражение: ")
    
    for op, func in operations.items():
        if (op in term):
            term_list = term.split(op)
            x1: int = int(term_list[0])
            x2: int = int(term_list[1])
            func(x1, x2)
