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
    - For inputs like ["ABC", "DEF", "GHJ"], this will interpreted in the following (Premises must be a conjunctive antecedent):
        - (A ∧ B ∧ C) |- ? 
        - (D ∧ E ∧ F) |- ?
        - (G ∧ H ∧ I) |- ?
    - For inputs like "pqr", this will be read as "P, Q, R |- ?" (i.e., "? -> (P ∧ Q ∧ R)")
    """
    def resolve_query(self, query:list) -> bool:
        print(f"Solving query: {query}")
        is_matching = self.verify_type(input = query, expected_type = list)
        if is_matching == False:   
            # Convert string into list of strings if possible
            if self.verify_type(input = query, expected_type = str) == True: # Transforms e.g., "pqr" = [p, q, r]
                query = [[char for char in query]]
            else:
                raise TypeError("The 'query' should be a list of strings")
            
        else: 
            """
            ["abc", "def", "ghi"] converted to [["abc"], ["def"], ["ghi"]]

            This will be treated as 3 separate queries passed to the solver i.e:
            - ?A, B, C  (Which is equivalent to (A ∧ B ∧ C))
            - ?D, E, F
            - ?G, H, I
            """
            query = [[q] for q in query]
        
        # For each query
        for q in query:
            # Resolve the query
            satisfied = self.__resolve_query(q)

            # Create a more readable representation of the query
            formula = q[0] # As q is currently e.g., ["ab"] or ["a"]
            if len(formula) == 1:
                readable_query = formula[0]
            else:
                readable_query = "({})".format(' ∧ '.join(formula))
            
            print(f"{readable_query} follows" if satisfied else f"{readable_query} does not follow")
        print("\n")

    # Private method for resolving queries
    """
    - The method takes in a query and see if it follows logically from the data contained in the logic program (resolution)
    """
    def __resolve_query(self, query:list) -> bool:
        
        # If the query is empty, then the initial query was satisfied
        if query[0] == "":
            return True
        
        # Check the current query against all of the formulas in the solver
        current_query = query[0]
        for formula in self.formulas:
            # Found a formula such that formula.tail -> current_query
            if formula.head == current_query:
                # Construct new query, replacing the current query with the tail of the formula
                new_query = [formula.tail] + query[1:]
                if self.__resolve_query(new_query) == True:
                    return True
        
        return False