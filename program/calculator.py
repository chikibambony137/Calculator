import actions, logger as l

def calculate(term: str) -> str:
    # action -> func
    operations: dict = {
            "+": actions.Add,
            "-": actions.Sub,
            "*": actions.Mult,
            "/": actions.Div,
            "^": actions.Degree
    }

    # delete "\n"
    term = term.strip()

    l.logger.info("calculating...")

    # check exist of operation in dict
    i: int = 0
    for op in operations:
        if (term.find(op) == -1):
            i+=1
            if (i == len(operations)):
                return "Error! Operation not found"

    # spliting string
    for op, func in operations.items():
        if (op in term):
            l.logger.debug(f"operation is \"{op}\"")
            term_list: list = term.split(op)      # split from str"2+2" to list["2", "2"]
            l.logger.debug(f"term_list = {term_list}")

            # calculating
            try:
                x1: float = float(term_list[0])
                x2: float = float(term_list[1])
                res = func(x1, x2)
                if (float(res) % 1 == 0):
                    res = int(float(res))
                return res
            except:
                l.logger.error("Incorrect term")
                return "Error! Incorrect term"
        
