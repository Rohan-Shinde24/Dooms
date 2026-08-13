import pytest
from dooms.lexer.lexer import Lexer
from dooms.parser.parser import Parser
from dooms.tree.statements import Program, VariableDeclaration
from dooms.tree.expressions import Identifier, BinaryExpression
from dooms.lexer.token_type import TokenType

def test_parser_typed_variable():
    source = 'int a = 1 + 2;'
    lexer = Lexer(source)
    parser = Parser(lexer)
    program = parser.parse()

    assert isinstance(program, Program)
    assert len(program.body) == 1
    
    stmt = program.body[0]
    assert isinstance(stmt, VariableDeclaration)
    assert stmt.var_type == TokenType.INT_TYPE
    assert isinstance(stmt.name, Identifier)
    assert stmt.name.name == 'a'
    
    expr = stmt.initializer
    assert isinstance(expr, BinaryExpression)
