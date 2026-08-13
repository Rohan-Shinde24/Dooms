from dooms.interpreter.errors import DoomsRuntimeError
import pytest
from dooms.lexer.lexer import Lexer
from dooms.parser.parser import Parser
from dooms.interpreter.interpreter import Interpreter

def test_basic_arrays(capsys):
    source = """
        int a = [1, 2, 3]
        print(a)
    """
    interpreter = Interpreter()
    interpreter.interpret(Parser(Lexer(source)).parse())
    
    captured = capsys.readouterr()
    assert captured.out.strip() == "[1, 2, 3]"

def test_tuple_arrays(capsys):
    source = """
        [int, str] user = [1, "Alice"]
        print(user)
    """
    interpreter = Interpreter()
    interpreter.interpret(Parser(Lexer(source)).parse())
    
    captured = capsys.readouterr()
    assert captured.out.strip() == "[1, Alice]"

def test_array_methods(capsys):
    source = """
        any items = []
        items.push(1)
        items.push("two")
        items.insert(0, true)
        print(items)
        items.pop()
        print(items)
    """
    interpreter = Interpreter()
    interpreter.interpret(Parser(Lexer(source)).parse())
    
    captured = capsys.readouterr()
    outputs = captured.out.strip().split('\n')
    assert outputs[0] == "[true, 1, two]"
    assert outputs[1] == "[true, 1]"

def test_fixed_size_arrays():
    source = """
        any limited = [(2)]
        limited.push(1)
        limited.push(2)
        limited.push(3)
    """
    interpreter = Interpreter()
    with pytest.raises(DoomsRuntimeError):
        interpreter.interpret(Parser(Lexer(source)).parse())

def test_strict_typing():
    source = """
        int a = [1, "two"]
    """
    interpreter = Interpreter()
    with pytest.raises(DoomsRuntimeError):
        interpreter.interpret(Parser(Lexer(source)).parse())
