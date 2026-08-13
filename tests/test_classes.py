import pytest
from dooms.lexer.lexer import Lexer
from dooms.parser.parser import Parser
from dooms.interpreter.interpreter import Interpreter

def test_class_declaration_and_instantiation(capsys):
    source = """
        class Person {
            func init(str name) {
                this.name = name;
            }
            
            func greet() {
                print("Hello", this.name);
            }
        }
        
        any p = Person("Alice");
        p.greet();
    """
    interpreter = Interpreter()
    interpreter.interpret(Parser(Lexer(source)).parse())
    
    captured = capsys.readouterr()
    outputs = captured.out.strip().split('\n')
    assert outputs[0] == "Hello Alice"

def test_class_property_assignment(capsys):
    source = """
        class Math {
            func init() {}
            func square(int x) { return x * x; }
        }
        any m = Math();
        m.value = 10;
        print(m.square(m.value));
    """
    interpreter = Interpreter()
    interpreter.interpret(Parser(Lexer(source)).parse())
    
    captured = capsys.readouterr()
    assert captured.out.strip() == "100"
