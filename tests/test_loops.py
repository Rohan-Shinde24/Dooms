import pytest
from dooms.lexer.lexer import Lexer
from dooms.parser.parser import Parser
from dooms.interpreter.interpreter import Interpreter
from dooms.interpreter.errors import DoomsRuntimeError

def test_while_loop(capsys):
    source = """
        int i = 0;
        while (i < 3) {
            print(i);
            i = i + 1;
        }
    """
    
    lexer = Lexer(source)
    parser = Parser(lexer)
    program = parser.parse()
    
    interpreter = Interpreter()
    interpreter.interpret(program)
    
    captured = capsys.readouterr()
    outputs = captured.out.strip().split('\n')
    assert outputs == ["0", "1", "2"]

def test_block_scope():
    source = """
        {
            int secret = 42;
        }
        print(secret);
    """
    
    lexer = Lexer(source)
    parser = Parser(lexer)
    program = parser.parse()
    
    interpreter = Interpreter()
    with pytest.raises(DoomsRuntimeError):
        interpreter.interpret(program)
