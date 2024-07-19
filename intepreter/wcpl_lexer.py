import re

# Token types
TOKENS = {
    'START': r'\bstart\b',
    'STOP': r'\bstop\b',
    'OPEN': r'\bopen\b',
    'CLOSE': r'\bclose\b',
    'PRINT': r'dynamic_print',
    'SCRIPT': r'\bscript\b',
    'QUANTUM': r'\bquantum\b',
    'GAME': r'\bgame\b',
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

# Example usage of Lexer
code = '''
start
    open
        dynamic_print("Hello, WCPL!")
    close
stop
'''

lexer = Lexer(code)
tokens = lexer.tokenize()
print(tokens)
