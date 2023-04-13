class RPNCalculator:
    def __init__(self):
        self.stack = []
    
    def calculate(self, filename):
        with open(filename, "r") as f:
            content = f.read()
        
        tokens = content.split()
        token_types = []
        
        for token in tokens:
            if token.isnumeric():
                self.stack.append(float(token))
                token_types.append(("number", float(token)))
            elif token == "+":
                op2 = self.stack.pop()
                op1 = self.stack.pop()
                self.stack.append(op1 + op2)
                token_types.append(("plus(op)", "+"))
            elif token == "-":
                op2 = self.stack.pop()
                op1 = self.stack.pop()
                self.stack.append(op1 - op2)
                token_types.append(("minus(op)", "-"))
            elif token == "*":
                op2 = self.stack.pop()
                op1 = self.stack.pop()
                self.stack.append(op1 * op2)
                token_types.append(("multi(op)", "*"))
            elif token == "/":
                op2 = self.stack.pop()
                op1 = self.stack.pop()
                self.stack.append(op1 / op2)
                token_types.append(("div(op)", "/"))
            else:
                raise ValueError("Unknown operator: " + token)
        
        if len(self.stack) == 1:
            result = self.stack[0]
        else:
            raise ValueError("Invalid expression")
        
        for token_type in token_types:
            print(token_type[0], token_type[1])
        
        return result

calculator = RPNCalculator()
result = calculator.calculate(r'C:\Users\caio_\Downloads\Calc1.stk')
print(result) 
