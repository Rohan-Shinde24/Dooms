import pytest
from dooms.lexer.lexer import Lexer
from dooms.parser.parser import Parser
from dooms.interpreter.interpreter import Interpreter

def test_if_else(capsys):
    source = """
        int age = 20;
        if (age < 18) {
            print("young");
        } else {
            print("adult");
        }
        
        if (age == 20) {
            print("exact");
        }
    """
    
    lexer = Lexer(source)
    parser = Parser(lexer)
    program = parser.parse()
    
    interpreter = Interpreter()
    interpreter.interpret(program)
    
    captured = capsys.readouterr()
    outputs = captured.out.strip().split('\n')
    assert outputs == ["adult", "exact"]
