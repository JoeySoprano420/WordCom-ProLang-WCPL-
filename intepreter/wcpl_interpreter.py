import re
import subprocess
import qiskit
import pygame
from pydub import AudioSegment
from midiutil import MIDIFile
import manim

# Lexer for WCPL
class Lexer:
    TOKENS = {
        'START': r'\bstart\b',
        'STOP': r'\bstop\b',
        'OPEN': r'\bopen\b',
        'CLOSE': r'\bclose\b',
        'PRINT': r'dynamic_print',
        'SCRIPT': r'\bscript\b',
        'QUANTUM': r'\bquantum\b',
        'GAME': r'\bgame\b',
        'MUSIC': r'\bmusic\b',
        'ANIMATION': r'\banimation\b',
        'IDENTIFIER': r'[a-zA-Z_][a-zA-Z_0-9]*',
        'STRING': r'\".*?\"',
        'NUMBER': r'\b\d+\b',
        'WHITESPACE': r'\s+',
        'NEWLINE': r'\n',
        'COMMENT': r'#.*',
    }

    def __init__(self, code):
        self.code = code
        self.tokens = self.tokenize()
    
    def tokenize(self):
        tokens = []
        for token_type, pattern in self.TOKENS.items():
            regex = re.compile(pattern)
            for match in regex.finditer(self.code):
                tokens.append((token_type, match.group()))
        tokens.sort(key=lambda x: x[1])
        return tokens

# Parser for WCPL
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
                self.pos += 1
                if self.tokens[self.pos][0] == 'STRING':
                    message = self.tokens[self.pos][1]
                    parsed_code.append({'action': 'print', 'message': message})
            elif token_type == 'SCRIPT':
                self.pos += 1
                if self.tokens[self.pos][0] == 'STRING':
                    script_file = self.tokens[self.pos][1].strip('"')
                    parsed_code.append({'action': 'script', 'file': script_file})
            elif token_type == 'QUANTUM':
                self.pos += 1
                if self.tokens[self.pos][0] == 'STRING':
                    quantum_code = self.tokens[self.pos][1].strip('"')
                    parsed_code.append({'action': 'quantum', 'code': quantum_code})
            elif token_type == 'GAME':
                self.pos += 1
                if self.tokens[self.pos][0] == 'STRING':
                    game_code = self.tokens[self.pos][1].strip('"')
                    parsed_code.append({'action': 'game', 'code': game_code})
            elif token_type == 'MUSIC':
                self.pos += 1
                if self.tokens[self.pos][0] == 'STRING':
                    music_code = self.tokens[self.pos][1].strip('"')
                    parsed_code.append({'action': 'music', 'code': music_code})
            elif token_type == 'ANIMATION':
                self.pos += 1
                if self.tokens[self.pos][0] == 'STRING':
                    animation_code = self.tokens[self.pos][1].strip('"')
                    parsed_code.append({'action': 'animation', 'code': animation_code})
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
        self.pos += 1
        while self.tokens[self.pos][0] != 'STOP':
            token_type, value = self.tokens[self.pos]
            if token_type == 'PRINT':
                self.pos += 1
                if self.tokens[self.pos][0] == 'STRING':
                    message = self.tokens[self.pos][1]
                    macro_body.append({'action': 'print', 'message': message})
            self.pos += 1
        return macro_body

# Execution Engine for WCPL
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
            elif action == 'script':
                self.execute_script(command['file'])
            elif action == 'quantum':
                self.execute_quantum(command['code'])
            elif action == 'game':
                self.execute_game(command['code'])
            elif action == 'music':
                self.execute_music(command['code'])
            elif action == 'animation':
                self.execute_animation(command['code'])

    def execute_print(self, message):
        print(f"Dynamic print: {message}")

    def execute_script(self, script_file):
        try:
            result = subprocess.run(['python', script_file], capture_output=True, text=True)
            print(f"Script output:\n{result.stdout}")
            if result.stderr:
                print(f"Script error:\n{result.stderr}")
        except Exception as e:
            print(f"Failed to execute script {script_file}: {e}")

    def execute_quantum(self, quantum_code):
        print(f"Executing quantum code: {quantum_code}")
        from qiskit import QuantumCircuit, Aer, execute
        circuit = QuantumCircuit(1, 1)
        circuit.h(0)
        circuit.measure(0, 0)
        simulator = Aer.get_backend('qasm_simulator')
        result = execute(circuit, simulator).result()
        counts = result.get_counts()
        print(f"Quantum result: {counts}")

    def execute_game(self, game_code):
        print(f"Executing game code: {game_code}")
        pygame.init()
        screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption('WCPL Game Example')
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            screen.fill((0, 0, 0))
            pygame.display.flip()
        pygame.quit()

    def execute_music(self, music_code):
        print(f"Executing music code: {music_code}")
        midi = MIDIFile(1)
        midi.addTempo(0, 0, 120)
        midi.addNote(0, 0, 60, 0, 1, 100)
        with open("output.mid", "wb") as output_file:
            midi.writeFile(output_file)
        print("Music created: output.mid")

    def execute_animation(self, animation_code):
        print(f"Executing animation code: {animation_code}")
        from manim import Scene, Square
        class ExampleScene(Scene):
            def construct(self):
                square = Square()
                self.play(square.animate.scale(2))
        ExampleScene().render()

# WCPL Interpreter
class WCPLInterpreter:
    def __init__(self, code):
        lexer = Lexer(code)
        parser = Parser(lexer.tokens)
        self.parsed_code = parser.parse()
        self.engine = ExecutionEngine()

    def run(self):
        self.engine.execute(self.parsed_code)

if __name__ == "__main__":
    code = '''
    start
        open
            dynamic_print("Running a quantum script...")
            quantum "test_quantum.py"
            dynamic_print("Quantum script finished.")
            dynamic_print("Running a game script...")
            game "test_game.py"
            dynamic_print("Game script finished.")
            dynamic_print("Running a music script...")
            music "test_music.py"
            dynamic_print("Music script finished.")
            dynamic_print("Running an animation script...")
            animation "test_animation.py"
            dynamic_print("Animation script finished.")
        close
    stop
    '''

    interpreter = WCPLInterpreter(code)
    interpreter.run()
