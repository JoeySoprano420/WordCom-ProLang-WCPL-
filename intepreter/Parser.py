class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def parse(self):
        while self.pos < len(self.tokens):
            token_type, value = self.tokens[self.pos]
            if token_type == 'START':
                self.parse_start()
            elif token_type == 'STOP':
                self.parse_stop()
            elif token_type == 'OPEN':
                self.parse_open()
            elif token_type == 'CLOSE':
                self.parse_close()
            elif token_type == 'PRINT':
                self.parse_print()
            self.pos += 1

    def parse_start(self):
        print("Start block detected")
        self.pos += 1  # Move past the 'start' token

    def parse_stop(self):
        print("Stop block detected")
        self.pos += 1  # Move past the 'stop' token

    def parse_open(self):
        print("Open block detected")
        self.pos += 1  # Move past the 'open' token

    def parse_close(self):
        print("Close block detected")
        self.pos += 1  # Move past the 'close' token

    def parse_print(self):
        self.pos += 1  # Move past the 'dynamic_print' token
        if self.tokens[self.pos][0] == 'STRING':
            message = self.tokens[self.pos][1]
            print(f"Executing dynamic print with message: {message}")
            self.pos += 1  # Move past the string token

# Example usage of Parser
parser = Parser(tokens)
parser.parse()
