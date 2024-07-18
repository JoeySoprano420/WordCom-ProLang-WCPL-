import re

class Lexer:
    def __init__(self, code):
        self.code = code
        self.tokens = []
        self.current_token = None
        self.current_position = 0
    
    def tokenize(self):
        # Define token patterns
        token_specification = [
            ('KEYWORD', r'(start|stop|open|close|dynamic_print|if|else|for|input|print)'),  # Keywords
            ('IDENTIFIER', r'[a-zA-Z_][a-zA-Z0-9_]*'),  # Identifiers
            ('NUMBER', r'\d+(\.\d*)?'),  # Numbers
            ('STRING', r'\"([^\\\"]|\\.)*\"'),  # Strings
            ('BOOLEAN', r'(True|False)'),  # Booleans
            ('NEWLINE', r'\n'),  # Newlines
            ('SKIP', r'[ \t]+'),  # Skip spaces and tabs
            ('UNKNOWN', r'.')  # Any other character
        ]
        
        tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
        line_num = 1
        
        for mo in re.finditer(tok_regex, self.code):
            kind = mo.lastgroup
            value = mo.group()
            
            if kind == 'NEWLINE':
                line_num += 1
                continue
            elif kind == 'SKIP':
                continue
            elif kind == 'UNKNOWN':
                raise SyntaxError(f'Unexpected character {value} on line {line_num}')
            
            if kind == 'IDENTIFIER' and value in ('if', 'else', 'for'):
                kind = 'KEYWORD'
            elif kind == 'BOOLEAN':
                value = True if value == 'True' else False
            
            token = (kind, value, line_num)
            self.tokens.append(token)
    
    def next_token(self):
        if self.current_position >= len(self.tokens):
            return None
        token = self.tokens[self.current_position]
        self.current_token = token
        self.current_position += 1
        return token
