from src.lexer.lexer import Lexer
from src.lexer.token_type import TokenType

with open("examples/hello.dooms", "r") as f:
    source = f.read()

lexer = Lexer(source)
tok = lexer.next_token()
while tok.type != TokenType.EOF:
    print(tok.line, tok.type)
    tok = lexer.next_token()
