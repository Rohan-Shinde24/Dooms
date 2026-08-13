from dooms.interpreter.environment import Environment
from dooms.interpreter.errors import ReturnException

class DoomsFunction:
    def __init__(self, declaration, closure):
        self.declaration = declaration
        self.closure = closure

    def bind(self, instance):
        from .environment import Environment
        from dooms.lexer.token_type import TokenType
        env = Environment(self.closure)
        env.define("this", instance, TokenType.ANY_TYPE)
        return DoomsFunction(self.declaration, env)

    def __call__(self, interpreter, args):
        if len(args) != len(self.declaration.params):
            from .errors import DoomsRuntimeError
            raise DoomsRuntimeError(f"Expected {len(self.declaration.params)} arguments but got {len(args)}.")

        environment = Environment(self.closure)
        for i in range(len(self.declaration.params)):
            param = self.declaration.params[i]
            environment.define(param['name'].name, args[i], param['var_type'])

        try:
            interpreter.execute_block(self.declaration.body.statements, environment)
        except ReturnException as ret:
            return ret.value
            
        return None
