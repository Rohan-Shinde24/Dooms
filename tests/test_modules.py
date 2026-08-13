import pytest
import os
from dooms.lexer.lexer import Lexer
from dooms.parser.parser import Parser
from dooms.interpreter.interpreter import Interpreter

def test_global_include(capsys):
    # Tests import "tests/math_utils.dooms";
    source = """
        import "tests/math_utils.dooms";
        print(add(5, 5));
        print(math_version);
    """
    interpreter = Interpreter()
    interpreter.interpret(Parser(Lexer(source)).parse())
    
    captured = capsys.readouterr()
    outputs = captured.out.strip().split('\n')
    assert outputs[0] == "10"
    assert outputs[1] == "1"

def test_namespace_import(capsys):
    # Tests import "tests/math_utils.dooms" as math;
    source = """
        import "tests/math_utils.dooms" as math;
        print(math.subtract(10, 5));
        print(math.math_version);
    """
    interpreter = Interpreter()
    interpreter.interpret(Parser(Lexer(source)).parse())
    
    captured = capsys.readouterr()
    outputs = captured.out.strip().split('\n')
    assert outputs[0] == "5"
    assert outputs[1] == "1"

def test_import_missing_file():
    source = """
        import "does_not_exist.dooms";
    """
    interpreter = Interpreter()
    from dooms.interpreter.errors import DoomsRuntimeError
    with pytest.raises(DoomsRuntimeError):
        interpreter.interpret(Parser(Lexer(source)).parse())
