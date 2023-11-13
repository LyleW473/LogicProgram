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
        - (A ∧ B ∧ C) |- ? [or in other words: A, B, C |- ?]
        - (D ∧ E ∧ F) |- ?
        - (G ∧ H ∧ I) |- ?
    - For inputs like "pqr" or ["pqr"], this will be read as "P, Q, R |- ?" (i.e., "? -> (P ∧ Q ∧ R)")
    """
    def resolve_query(self, query:list, depth_limit: int) -> bool:
        print(f"Solving query: {query}")
        is_matching = self.verify_type(input = query, expected_type = list)
        if is_matching == False:   
            # Convert string into list of strings if possible
            if self.verify_type(input = query, expected_type = str) == True: # Transforms e.g., "pqr" = [p, q, r] and places it inside of a queries list
                queries = [[char for char in query]]
            else:
                raise TypeError("The 'query' should be a list of strings")
            
        else: 
            """
            query = ["ABC", "DEF", "GHI"] converted to [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]]
            query = "ABC" will also be converted to [["A", "B", "C"]]
            query = ["A", "B", "C"] will be treated as 3 separate queries (i.e., ?A, ?B, ?C)

            This will be treated as 3 separate queries passed to the solver i.e:
            - ?A, B, C  (Which is equivalent to (A ∧ B ∧ C))
            - ?D, E, F
            - ?G, H, I
            """
            queries = [[q] if len(q) == 1 else [char for char in q] for q in query]
        
        # For each query
        for q in queries:
            # Resolve the query
            satisfied = self.__resolve_query(query = q, current_depth = 0, depth_limit = depth_limit)

            # Create a more readable representation of the query
            if len(q) == 1:
                readable_query = q[0]
            else:
                readable_query = "({})".format(' ∧ '.join(q))
            
            print(f"{readable_query} follows" if satisfied else f"{readable_query} does not follow")
        print("\n")

    # Private method for resolving queries
    """
    - The method takes in a query and see if it follows logically from the data contained in the logic program (resolution)
    """
    def __resolve_query(self, query:list, current_depth: int, depth_limit: int) -> bool:
        
        # If the query is empty, then the initial query was satisfied
        if not query:
            return True
        
        # Avoid maximum recursion depth (large computations)
        if current_depth > depth_limit:
            print("Exited call due to exceeding depth limit")
            return False
        
        # Check the current query against all of the formulas in the solver
        current_query = query[0]
        for formula in self.formulas:
            # Found a formula such that formula.tail -> current_query
            if formula.head == current_query:
                # Construct new query, replacing the current query with the tail of the formula
                new_query = formula.tail + query[1:]
                if self.__resolve_query(new_query, current_depth = current_depth + 1, depth_limit = depth_limit) == True:
                    return True
        
        return False