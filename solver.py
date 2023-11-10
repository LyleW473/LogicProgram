from formula import Formula

class Solver:

    def __init__(self):
        self.formulas = set()

    # Adds formulas to the 
    def add_formula(self, tail: str, head: str):
        self.formulas.add(Formula(tail = tail, head = head))

    # Checks whether the input matches the passed in expected type
    def verify_type(self, input, expected_type):
        return type(input) == expected_type
    
    # Public method that users should use to check if a query is satisfied
    """
    - Used to verify that the input is correct on the very first resolve_query call
    - For inputs like ["ABC", "DEF", "GHJ"], this will be read as "(A # B # C), (D # E # F), (G # H # J) |- ?" (Where # can represent a conjunction or disjunction at any time)
    - For inputs like "pqr", this will be read as "P, Q, R |- ?"
    - 
    """
    def resolve_query(self, clause:list) -> bool:
        is_matching = self.verify_type(input = clause, expected_type = list)
        if is_matching == False:   
            # Convert string into list of strings if possible
            if self.verify_type(input = clause, expected_type = str) == True: # Transforms e.g., "pqr" = [p, q, r]
                clause = [char for char in clause]
            else:
                raise TypeError("The 'clause' should be a list of strings")

        # Continue to resolve the query
        satisfied = self.__resolve_query(clause)
        # print(satisfied, clause , "here")
        print(f"{clause} follows" if satisfied else f"{clause} does not follow")


    # Private method for resolving queries
    """
    - The method takes in a query and see if it follows logically from the data contained in the logic program (resolution)
    """
    def __resolve_query(self, clause:list) -> bool:
        
        # If the clause is empty, then the initial query was satisfied
        
        if clause[0] == "":
            return True
        
        # Check if 
        query = clause[0]
        for formula in self.formulas:
            # print(formula, formula.tail, formula.head, query)
            if formula.head == query:
                new_query = [formula.tail] + clause[1:] # Construct new query
                # print("new query", new_query)
                if self.__resolve_query(new_query) == True:
                    return True
        
        return False