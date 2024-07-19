class WCPLInterpreter:
    def __init__(self, code):
        self.lexer = Lexer(code)
        self.parser = Parser(self.lexer.tokenize())
        self.engine = ExecutionEngine()

    def run(self):
        parsed_code = self.parser.parse()
        self.engine.execute(parsed_code)

# Example usage of WCPLInterpreter
code = '''
start
    open
        dynamic_print("Hello, WCPL!")
    close
stop
'''

interpreter = WCPLInterpreter(code)
interpreter.run()
