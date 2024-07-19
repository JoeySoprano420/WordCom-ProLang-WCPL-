import re

# Token types
TOKENS = {
    'START': r'\bstart\b',
    'STOP': r'\bstop\b',
    'OPEN': r'\bopen\b',
    'CLOSE': r'\bclose\b',
    'PRINT': r'dynamic_print',
    'IDENTIFIER': r'[a-zA-Z_][a-zA-Z_0-9]*',
    'STRING': r'\".*?\"',
    'NUMBER': r'\b\d+\b',
    'WHITESPACE': r'\s+',
    'NEWLINE': r'\n',
    'COMMENT': r'#.*',
}

class Lexer:
    def __init__(self, code):
        self.code = code
        self.tokens = []
        self.pos = 0

    def tokenize(self):
        while self.pos < len(self.code):
            match = None
            for token_type, pattern in TOKENS.items():
                regex = re.compile(pattern)
                match = regex.match(self.code, self.pos)
                if match:
                    token = (token_type, match.group(0))
                    if token_type not in ['WHITESPACE', 'COMMENT']:  # Ignore whitespace and comments
                        self.tokens.append(token)
                    self.pos = match.end(0)
                    break
            if not match:
                raise SyntaxError(f"Unexpected character: {self.code[self.pos]}")
        return self.tokens

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def parse(self):
        parsed_code = []
        while self.pos < len(self.tokens):
            token_type, value = self.tokens[self.pos]
            if token_type == 'START':
                parsed_code.append({'action': 'start'})
            elif token_type == 'STOP':
                parsed_code.append({'action': 'stop'})
            elif token_type == 'OPEN':
                parsed_code.append({'action': 'open'})
            elif token_type == 'CLOSE':
                parsed_code.append({'action': 'close'})
            elif token_type == 'PRINT':
                self.pos += 1  # Move past the 'dynamic_print' token
                if self.tokens[self.pos][0] == 'STRING':
                    message = self.tokens[self.pos][1]
                    parsed_code.append({'action': 'print', 'message': message})
            self.pos += 1
        return parsed_code

class ExecutionEngine:
    def __init__(self):
        self.context = {}

    def execute(self, parsed_code):
        for command in parsed_code:
            action = command['action']
            if action == 'print':
                self.execute_print(command['message'])
            elif action == 'start':
                print("Starting execution block...")
            elif action == 'stop':
                print("Stopping execution block...")
            elif action == 'open':
                print("Opening execution block...")
            elif action == 'close':
                print("Closing execution block...")

    def execute_print(self, message):
        print(f"Dynamic print: {message}")

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
