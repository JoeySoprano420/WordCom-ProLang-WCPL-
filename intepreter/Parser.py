class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.next_token()
    
    def parse(self):
        self.program()
    
    def program(self):
        while self.current_token is not None:
            if self.current_token[0] == 'KEYWORD':
                keyword = self.current_token[1]
                
                if keyword == 'start':
                    self.match('KEYWORD', 'start')
                    self.block()
                    self.match('KEYWORD', 'stop')
                elif keyword == 'dynamic_print':
                    self.dynamic_print_statement()
                elif keyword == 'if':
                    self.if_statement()
                elif keyword == 'for':
                    self.for_loop()
                elif keyword == 'input':
                    self.input_statement()
                elif keyword == 'print':
                    self.print_statement()
                else:
                    self.error('Unknown keyword')
            else:
                self.error('Expected keyword')
            
            self.current_token = self.lexer.next_token()
    
    def block(self):
        while self.current_token is not None and self.current_token[1] != 'stop':
            self.statement()
            self.current_token = self.lexer.next_token()
    
    def statement(self):
        if self.current_token[0] == 'KEYWORD':
            keyword = self.current_token[1]
            if keyword == 'dynamic_print':
                self.dynamic_print_statement()
            elif keyword == 'if':
                self.if_statement()
            elif keyword == 'else':
                self.else_statement()
            elif keyword == 'for':
                self.for_loop()
            elif keyword == 'input':
                self.input_statement()
            elif keyword == 'print':
                self.print_statement()
            else:
                self.error('Unknown statement')
        else:
            self.error('Expected statement')
    
    def dynamic_print_statement(self):
        self.match('KEYWORD', 'dynamic_print')
        self.match('OPEN', 'open')
        message = self.current_token[1]
        self.match('STRING', message)
        self.match('CLOSE', 'close')
    
    def if_statement(self):
        self.match('KEYWORD', 'if')
        self.match('OPEN', 'open')
        # Implement conditional parsing
        # Example: if condition:
        self.match('CLOSE', 'close')
        self.block()
        if self.current_token[1] == 'else':
            self.else_statement()
    
    def else_statement(self):
        self.match('KEYWORD', 'else')
        self.block()
    
    def for_loop(self):
        self.match('KEYWORD', 'for')
        self.match('OPEN', 'open')
        # Implement for loop parsing
        # Example: for i in range(10):
        self.match('CLOSE', 'close')
        self.block()
    
    def input_statement(self):
        self.match('KEYWORD', 'input')
        self.match('OPEN', 'open')
        prompt = self.current_token[1]
        self.match('STRING', prompt)
        self.match('CLOSE', 'close')
    
    def print_statement(self):
        self.match('KEYWORD', 'print')
        self.match('OPEN', 'open')
        message = self.current_token[1]
        self.match('STRING', message)
        self.match('CLOSE', 'close')
    
    def match(self, expected_type, expected_value):
        if self.current_token[0] == expected_type and self.current_token[1] == expected_value:
            self.current_token = self.lexer.next_token()
        else:
            self.error(f'Expected {expected_type}: {expected_value}')
    
    def error(self, message):
        raise SyntaxError(message)
