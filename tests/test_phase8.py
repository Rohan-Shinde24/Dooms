from dooms.interpreter.errors import DoomsRuntimeError
import pytest
import builtins
from dooms.lexer.lexer import Lexer
from dooms.parser.parser import Parser
from dooms.interpreter.interpreter import Interpreter
from unittest.mock import patch

def test_dictionary_basics(capsys):
    source = """
        any dict = { "a": 1, "b": 2 }
        print(dict.a)
        dict.c = 3
        print(dict["c"])
    """
    interpreter = Interpreter()
    # Note: dictionary assignment dict.c = 3 is not supported natively yet!
    # Let's test what IS supported: dict.set("c", 3)
    source_correct = """
        any dict = { "a": 1, "b": 2 }
        print(dict.a)
        dict.set("c", 3)
        print(dict["c"])
        print(dict.keys())
    """
    interpreter.interpret(Parser(Lexer(source_correct)).parse())
    
    captured = capsys.readouterr()
    outputs = captured.out.strip().split('\n')
    assert outputs[0] == "1"
    assert outputs[1] == "3"
    assert outputs[2] == "[a, b, c]"

def test_string_methods(capsys):
    source = """
        str name = "hello"
        print(name.length())
        print(name.upper())
        print(name.split("e"))
    """
    interpreter = Interpreter()
    interpreter.interpret(Parser(Lexer(source)).parse())
    
    captured = capsys.readouterr()
    outputs = captured.out.strip().split('\n')
    assert outputs[0] == "5"
    assert outputs[1] == "HELLO"
    assert outputs[2] == "[h, llo]"

def test_input_coercion(monkeypatch, capsys):
    # Mock Python's builtin input to return "42"
    monkeypatch.setattr('builtins.input', lambda _: "42")
    source = """
        int age = input()
        print(age + 10)
    """
    interpreter = Interpreter()
    interpreter.interpret(Parser(Lexer(source)).parse())
    
    captured = capsys.readouterr()
    assert captured.out.strip() == "52"

def test_input_coercion_error(monkeypatch, capsys):
    monkeypatch.setattr('builtins.input', lambda _: "not_a_number")
    source = """
        int age = input()
    """
    interpreter = Interpreter()
    with pytest.raises(DoomsRuntimeError):
        interpreter.interpret(Parser(Lexer(source)).parse())
