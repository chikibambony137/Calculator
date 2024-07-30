import actions, logger as l

def main(term):
    # action -> func
    operations: dict = {
            "+": actions.Add,
            "-": actions.Sub,
            "*": actions.Mult,
            "/": actions.Div
    }
    l.logger.info("dict \"operations\" created")
    
    l.logger.info("starting loop")
    for op, func in operations.items():
        if (op in term):

            l.logger.debug(f"operation is \"{op}\"")
            term_list = term.split(op)
            try:
                x1: float = float(term_list[0])
                x2: float = float(term_list[1])
                return func(x1, x2)
                #l.logger.info("end program...")
            except:
                l.logger.error("Incorrect term")
                return "Error!"

"""if (__name__ == "__main__"):
l.logger.info("start program...")
main()"""