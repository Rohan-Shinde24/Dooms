import pytest
from dooms.lexer.lexer import Lexer
from dooms.lexer.token_type import TokenType

def test_lexer_typed_declarations():
    source = 'int a = 1; str b = "hi"; any c = true;'
    lexer = Lexer(source)
    
    tokens = []
    token = lexer.next_token()
    while token.type != TokenType.EOF:
        tokens.append(token)
        token = lexer.next_token()
        
    assert tokens[0].type == TokenType.INT_TYPE
    assert tokens[5].type == TokenType.STRING_TYPE
    assert tokens[10].type == TokenType.ANY_TYPE

def test_lexer_comma():
    source = 'a, b'
    lexer = Lexer(source)
    assert lexer.next_token().type == TokenType.IDENTIFIER
    assert lexer.next_token().type == TokenType.COMMA
    assert lexer.next_token().type == TokenType.IDENTIFIER
