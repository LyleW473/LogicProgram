if __name__ == "__main__":
    from solver import Solver
    solver = Solver()

    # 1
    solver.add_formula(tail = "", head = "P")
    solver.add_formula(tail = "A", head = "P")
    solver.add_formula(tail = "R", head = "P")
    solver.add_formula(tail = "A", head = "Q")
    solver.add_formula(tail = "B", head = "Q")
    solver.add_formula(tail = "C", head = "Q")
    solver.resolve_query("P")
    solver.resolve_query("T")
    #solver.resolve_query("Q")

    # 2
    # solver.add_formula(tail = "", head = "P")
    # solver.add_formula(tail = "", head = "R")
    # solver.add_formula(tail = "P", head = "Q")
    # solver.add_formula(tail = "Q", head = "Q")
    # solver.add_formula(tail = "B", head = "Q")
    # solver.add_formula(tail = "C", head = "Q")
