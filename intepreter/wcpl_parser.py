class Interpreter:
    def __init__(self, code):
        self.lexer = Lexer(code)
        self.parser = Parser(self.lexer)
    
    def interpret(self):
        self.lexer.tokenize()
        self.parser.parse()

# Example WCPL code to interpret
wcpl_code = """
start
    open
        dynamic_print("Hello, World!")
        
        if
            open
                print("Condition met")
            close
        else
            open
                print("Condition not met")
            close
        
        for
            open
                print("Loop iteration")
            close
        close
        
        input("Enter your name: ")
        open
            print(f"Welcome, {name}!")
        close
        
    close
stop
"""

interpreter = Interpreter(wcpl_code)
interpreter.interpret()
