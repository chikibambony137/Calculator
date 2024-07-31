import actions, logger as l

def calculate(term: str) -> str:
    # action -> func
    operations: dict = {
            "+": actions.Add,
            "-": actions.Sub,
            "*": actions.Mult,
            "/": actions.Div
    }

    term = term.strip()     #delete "\n"

    l.logger.info("calculating...")
    for op, func in operations.items():
        if (op in term):
            l.logger.debug(f"operation is \"{op}\"")
            term_list: list = term.split(op)      #split from "2+2" to ["2", "2"]
            l.logger.debug(f"term_list = {term_list}")
            try:
                x1: float = float(term_list[0])
                x2: float = float(term_list[1])
                return func(x1, x2)
            except:
                l.logger.error("Incorrect term")
                return "Error!"
        else:
            l.logger.error("Incorrect term")
            return "Error!"
