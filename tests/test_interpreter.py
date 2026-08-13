import pytest
from dooms.interpreter.interpreter import Interpreter
from dooms.interpreter.errors import DoomsRuntimeError
from dooms.tree.statements import Program, VariableDeclaration
from dooms.tree.expressions import Identifier, Literal
from dooms.lexer.token_type import TokenType

def test_interpreter_type_enforcement(capsys):
    # int a = 1;
    program = Program([
        VariableDeclaration(Identifier('a'), Literal(1), TokenType.INT_TYPE)
    ])
    interpreter = Interpreter()
    interpreter.interpret(program)
    
    assert interpreter.environment.get('a') == 1

    # string error
    bad_program = Program([
        VariableDeclaration(Identifier('str'), Literal("hello"), TokenType.INT_TYPE)
    ])
    
    with pytest.raises(DoomsRuntimeError) as exc_info:
        interpreter.interpret(bad_program)

    assert "Type mismatch" in str(exc_info.value)
