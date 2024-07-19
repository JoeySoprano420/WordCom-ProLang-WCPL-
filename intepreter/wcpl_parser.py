class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.macros = {}

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
            elif token_type == 'SCRIPT':
                self.pos += 1  # Move past the 'script' token
                if self.tokens[self.pos][0] == 'STRING':
                    script_file = self.tokens[self.pos][1].strip('"')
                    parsed_code.append({'action': 'script', 'file': script_file})
            elif token_type == 'QUANTUM':
                self.pos += 1  # Move past the 'quantum' token
                if self.tokens[self.pos][0] == 'STRING':
                    quantum_code = self.tokens[self.pos][1].strip('"')
                    parsed_code.append({'action': 'quantum', 'code': quantum_code})
            elif token_type == 'IDENTIFIER' and value == 'macro':
                self.pos += 1
                macro_name = self.tokens[self.pos][1]
                macro_body = self.parse_macro()
                self.macros[macro_name] = macro_body
            elif token_type == 'IDENTIFIER' and value in self.macros:
                parsed_code.extend(self.macros[value])
            self.pos += 1
        return parsed_code

    def parse_macro(self):
        macro_body = []
        self.pos += 1  # Move past the macro name
        while self.tokens[self.pos][0] != 'STOP':
            token_type, value = self.tokens[self.pos]
            if token_type == 'PRINT':
                self.pos += 1
                if self.tokens[self.pos][0] == 'STRING':
                    message = self.tokens[self.pos][1]
                    macro_body.append({'action': 'print', 'message': message})
            self.pos += 1
        return macro_body
