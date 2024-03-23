class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def get_output(self):
        '''
        Print the output depending on the evaluated value.
        If the 0 <= value <= 999 the value is printed.
        If the value < 0, UNDERFLOW is printed.
        If the value > 999, OVERFLOW is printed.

        :return: None
        '''
        value = self.evaluate()
        if value > 999:
            print('OVERFLOW')
        elif value < 0:
            print('UNDERFLOW')
        else:
            print(value)

    
    def insert(self, data, bracketed):

        #Insert operators and operands into the binary tree.

        # If the data is an operator
        if data[0] == 'OPERATOR':
            if bracketed:
                # If the operator is bracketed, Get self.right part seperatly and add it to the left of the bracketed_Operator.(Make a new node called bracketed_Operator )
                # Then add bracketed_Operator to self.right (Root is not changing)
                # Nested brackets equations are also supported(Addition one)
                prev_right_child=self.right
                bracketed_Operator=Node(data)
                bracketed_Operator.left=prev_right_child
                self.right=bracketed_Operator
                
            else:
               # Make a new node for the new root and add the previous tree to the left of it(Root is changing)
               New_root=Node(data)
               New_root.left=self
               self=New_root
            
        # If the data is an operand(Root is not changing)
        else:
            if self.right==None:
                # If there's no right node, set the new operand as the right node
                self.right=Node(data)
            else:
                # If there's already a right node, go to the right end child recursively and insert the new operand to right
                self.right.insert(data,False)
        
        return self

    def evaluate(self):
        '''
        Process the expression stored in the binary tree and compute the final result.
        To do that, the function should be able to traverse the binary tree.

        Note that the evaluate function does not check for overflow or underflow.

        :return: the evaluated value
        '''
        # We need to go recursively to the left bottom and then we need to come to the top by calculating in each step
        # If the node is an operand, return its value
        if self.data[0] == 'OPERAND':
            return self.data[1]
        
        operator = self.data[1]
        # Evaluate the left and right subtrees by recursion
        left_operand = self.left.evaluate()
        right_operand = self.right.evaluate()

        # Perform the corresponding arithmetic operation based on the operator
        if operator == '+':
            return left_operand + right_operand
        elif operator == '^':
            return left_operand ** right_operand
        elif operator == '*':
            return left_operand * right_operand
        elif operator == '-':
           return left_operand - right_operand
        pass

# Use the insert method to add nodes
# Begin with forming the root node for the tree.
root = Node(('OPERAND', 1))
# Form the rest of the tree by inserting data to the root node.
root = root.insert(('OPERATOR', '+'), False)
root = root.insert(('OPERAND', 2), False)
root = root.insert(('OPERATOR', '*'), True)
root = root.insert(('OPERAND', 3), False)
root = root.insert(('OPERATOR', '+'), False)
root = root.insert(('OPERAND', 3), False)
root = root.insert(('OPERATOR', '^'), False)
root = root.insert(('OPERAND', 2), False)
# Get the output.
root.get_output()   