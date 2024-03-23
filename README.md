# Simple-symbolic-equation-solver


Implementation a simple symbolic equation solver. 

The equation should be stored in a binary tree. An equation consists of operands and operators.

Each operand or operator should be stored as a tuple of the form (TYPE, VALUE). Examples 
are (OPERAND, 5), (OPERAND, 7), (OPERAND, 34), (OPERATOR, ‘+’) or 
(OPERATOR, '*’').

Following operators should be supported: addition (+), subtraction (-), multiplication (*), and 
exponentiation (^). Grouping of terms in the equation using brackets should be supported. 
However, nested brackets need not be supported. For example, the expression “1 + (2 * 3) + 3 
^ 2” should be supported but the expression “1 + ((2 * 3) + 3) ^ 2” need not be supported. In
addition, the expressions will have a maximum of only one operator inside the brackets. For 
example, you do not have to consider expressions such as “1 + (2 * 3 + 7) + 3 ^ 2” which 
contains two operators ‘*’ and ‘+’ inside the brackets.

Evaluation of terms should be done left-to-right subjected to precedence given by brackets. 
(i.e. all the operators have equal precedence except the brackets). For example, the expression 
“1 + (2 * 3) + 3 ^ 2” will result in 100.

Explanation:
Total = 1
Total = 1 + (2*3) = 7 (2*3 is evaluated first since they are within brackets)
Total = 7 + 3 = 10
Total = 10 ^ 2 = 100

Note that these are not our usual arithmetic operations where we follow the BODMAS order.

Sample binary tree for the expression “1 + (2 * 3) + 3 ^ 2”

![image](https://github.com/AkinduH/Simple_symbolic_equation_solver/assets/164672047/653e150f-58aa-4be8-a54e-416facff85c8)

Expression: 1 + (2 * 3) + 3 ^ 2

Use the insert method to add nodes

Begin with forming the root node for the tree.

root = Node(('OPERAND', 1))

Form the rest of the tree by inserting data to the root node.

root = root.insert(('OPERATOR', '+'), False)

root = root.insert(('OPERAND', 2), False)

root = root.insert(('OPERATOR', '*'), True)

root = root.insert(('OPERAND', 3), False)

root = root.insert(('OPERATOR', '+'), False)

root = root.insert(('OPERAND', 3), False)

root = root.insert(('OPERATOR', '^'), False)

root = root.insert(('OPERAND', 2), False)

Get the output.

root.get_output() 

Should print 100


