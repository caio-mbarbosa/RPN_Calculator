class RPNCalculator:
    def __init__(self):
        self.stack = []
    
    def calculate(self, filename):
        with open(filename, "r") as f:
            content = f.read()
        
        tokens = content.split()
        
        for token in tokens:
            if token.isnumeric():
                self.stack.append(float(token))
            elif token == "+":
                op2 = self.stack.pop()
                op1 = self.stack.pop()
                self.stack.append(op1 + op2)
            elif token == "-":
                op2 = self.stack.pop()
                op1 = self.stack.pop()
                self.stack.append(op1 - op2)
            elif token == "*":
                op2 = self.stack.pop()
                op1 = self.stack.pop()
                self.stack.append(op1 * op2)
            elif token == "/":
                op2 = self.stack.pop()
                op1 = self.stack.pop()
                self.stack.append(op1 / op2)
            else:
                raise ValueError("Unknown operator: " + token)
        
        if len(self.stack) == 1:
            return self.stack[0]
        else:
            raise ValueError("Invalid expression")

calculator = RPNCalculator()
result = calculator.calculate(r'C:\Users\caio_\Downloads\Calc1.stk')
print(result) 
