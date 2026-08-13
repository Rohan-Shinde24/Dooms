import pytest
from dooms.lexer.lexer import Lexer
from dooms.parser.parser import Parser
from dooms.interpreter.interpreter import Interpreter

def test_custom_functions(capsys):
    source = """
        func add(int a, int b) {
            return a + b;
        }
        
        int result = add(5, 10);
        print(result);
        
        func recursive(int n) {
            if (n < 2) {
                return n;
            }
            return recursive(n - 1) + recursive(n - 2);
        }
        
        print(recursive(6));
    """
    
    lexer = Lexer(source)
    parser = Parser(lexer)
    program = parser.parse()
    
    interpreter = Interpreter()
    interpreter.interpret(program)
    
    captured = capsys.readouterr()
    outputs = captured.out.strip().split('\n')
    assert outputs[0] == "15"
    assert outputs[1] == "8"
