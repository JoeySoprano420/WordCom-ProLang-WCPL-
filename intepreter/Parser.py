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
                elif keyword == 'else':
                    self.else_statement()
                elif keyword == 'for':
                    self.for_loop()
                elif keyword == 'input':
                    self.input_statement()
                elif keyword == 'print':
                    self.print_statement()
                else:
                    self.error('Unknown keyword')
            elif self.current_token[0] == 'IDENTIFIER':
                self.function_call()
            else:
                self.error('Expected keyword or function call')
            
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
        elif self.current_token[0] == 'IDENTIFIER':
            self.function_call()
        else:
            self.error('Expected statement or function call')
    
    def dynamic_print_statement(self):
        self.match('KEYWORD', 'dynamic_print')
        self.match('OPEN', '(')
        message = self.current_token[1]
        self.match('STRING', message)
        self.match('CLOSE', ')')
        self.match('SEMICOLON', ';')
    
    def if_statement(self):
        self.match('KEYWORD', 'if')
        self.match('OPEN', '(')
        self.condition()
        self.match('CLOSE', ')')
        self.block()
        if self.current_token is not None and self.current_token[1] == 'else':
            self.else_statement()
    
    def else_statement(self):
        self.match('KEYWORD', 'else')
        self.block()
    
    def for_loop(self):
        self.match('KEYWORD', 'for')
        self.match('OPEN', '(')
        self.match('IDENTIFIER', 'var')
        self.match('IDENTIFIER', 'i')
        self.match('ASSIGN', '=')
        self.match('NUMBER', '0')
        self.match('SEMICOLON', ';')
        self.match('IDENTIFIER', 'i')
        self.match('OPERATOR', '<')
        self.match('NUMBER', '10')
        self.match('SEMICOLON', ';')
        self.match('IDENTIFIER', 'i')
        self.match('OPERATOR', '++')
        self.match('CLOSE', ')')
        self
