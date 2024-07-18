import re

class Greeter:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, {self.name}!")

def main():
    greeter = Greeter("World")
    greeter.greet()
    
    text = "WordCom-ProLang is awesome!"
    if re.search(".*awesome.*", text):
        print("Pattern found!")
    
    numbers = [1, 2, 3, 4, 5]
    for num in numbers:
        print(num)
    
    name = input("Enter your name: ")
    print(f"Welcome, {name}!")

def interpret_wcpl_code():
    open main

if __name__ == "__main__":
    interpret_wcpl_code()
