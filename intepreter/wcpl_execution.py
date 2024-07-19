import subprocess

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
