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

    solver.add_formula(tail = "AB", head = "R")
    solver.add_formula(tail = "CD", head = "A")
    solver.add_formula(tail = ["C", "D", "E", "F"], head = "P")
    solver.add_formula(tail = "GHIJ", head = "Z")

    # The following formulas should cause errors
    ## solver.add_formula(tail = ["CD", "D", "E", "F"], head = "A")
    ## solver.add_formula(tail = "", head = "AB")
    
    solver.resolve_query("P")
    solver.resolve_query("T")
    solver.resolve_query("Q")
    solver.resolve_query("ABC")
    solver.resolve_query(["ABC"])
    solver.resolve_query(["ABC", "DEF", "GHI"])
    solver.resolve_query(["A", "B", "C"])
    solver.resolve_query(["A"])
    solver.resolve_query(["AB", "B", "C"])

    # 2
    # solver.add_formula(tail = "", head = "P")
    # solver.add_formula(tail = "", head = "R")
    # solver.add_formula(tail = "P", head = "Q")
    # solver.add_formula(tail = "Q", head = "Q")
    # solver.add_formula(tail = "B", head = "Q")
    # solver.add_formula(tail = "C", head = "Q")
