class Formula:
    def __init__(self, tail: str, head: str):
        """ Notes:
        - The head of a formula should contain at most one literal (Even though 0 is valid, decided not to consider this since it is pointless)
        - The tail of a formula can contain zero or more literals
        """
        if type(tail) == str:
            self.tail = [char for char in tail]
        elif type(tail) == list:
            # Ensure that all literals in the list have a length of at most 1 (if 0, remove the item)
            items_to_remove = []
            for char in tail:
                if len(char) == 0:
                    items_to_remove.append(char)
                elif len(char) > 1:
                    raise ValueError("Too many characters, only one positive literal at most is allowed!")
            for item in items_to_remove:
                tail.remove(item)

            self.tail = tail
        else:
            raise ValueError("'tail' must be either be of type 'str' or of type 'list'.")
        
        if type(head) == list:
            # E.g., []
            if len(head) == 0:
                head = ""
            # E.g., ["P"] or [""] or ["PQ"]
            elif len(head) == 1:
                if len(head[0]) <= 1:
                    head = head[0]
                else:
                    raise ValueError("Head should contain at most one positive literal.")
        elif type(head) == str:
            if len(head) > 1:
                raise ValueError("Head should contain at most one positive literal.")
        else:
            raise ValueError("'head' must be either be of type 'str' or of type 'list'.")
        self.head = head

        print(f"Added formula:\nTail: {self.tail}\nHead: {self.head}\n")