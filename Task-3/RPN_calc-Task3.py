import re

class RPNCalculator:
    def __init__(self):
        self.stack = []
    
    def calculate(self, filename):
        with open(filename, "r") as f:
            content = f.read()
        
        #A expressão regular  (\d+\.\d+|\d+|[+\-*/])extrai tokens que correspondem a números decimais, números inteiros e operadores aritméticos. Cada token é armazenado na lista tokens
        tokens = re.findall(r'(\d+\.\d+|\d+|[+\-*/])', content)
        token_types = []
        
        for token in tokens:
            if re.match(r'\d+(\.\d+)?', token):
                self.stack.append(float(token))
                token_types.append(("number", float(token)))
            elif token in "+-*/":
                op2 = self.stack.pop()
                op1 = self.stack.pop()
                if token == "+":
                    result = op1 + op2
                elif token == "-":
                    result = op1 - op2
                elif token == "*":
                    result = op1 * op2
                elif token == "/":
                    result = op1 / op2
                self.stack.append(result)
                token_types.append(("operator", token))
            else:
                raise ValueError("Unknown token: " + token)
        
        if len(self.stack) == 1:
            result = self.stack[0]
        else:
            raise ValueError("Invalid expression")
        
        for token_type in token_types:
            print(token_type[0], token_type[1])
        
        return result

calculator = RPNCalculator()
#Aqui você coloca o diretório em que está o arquivo para ler
result = calculator.calculate(r'C:\Users\caio_\Downloads\Calc1.stk')
print(result) 
