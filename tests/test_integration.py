import pytest
from dooms.lexer.lexer import Lexer
from dooms.parser.parser import Parser
from dooms.interpreter.interpreter import Interpreter

def test_integration(capsys):
    source = """
        int a = 1;
        any b = 2;
        print(a + b);
        
        boo active = true;
        str name = "DOOMS";
        print(name, active);
    """
    
    lexer = Lexer(source)
    parser = Parser(lexer)
    program = parser.parse()
    
    interpreter = Interpreter()
    interpreter.interpret(program)
    
    captured = capsys.readouterr()
    outputs = captured.out.strip().split('\n')
    assert outputs[0] == "3"
    assert outputs[1] == "DOOMS true"
