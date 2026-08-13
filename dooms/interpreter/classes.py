from .errors import DoomsRuntimeError

class DoomsClass:
    def __init__(self, name, methods):
        self.name = name
        self.methods = methods
        
    def find_method(self, name):
        if name in self.methods:
            return self.methods[name]
        return None
        
    def __call__(self, interpreter, args):
        instance = DoomsInstance(self)
        initializer = self.find_method("init")
        if initializer:
            initializer.bind(instance)(interpreter, args)
        return instance

    def __str__(self):
        return f"<class {self.name}>"

class DoomsInstance:
    def __init__(self, dooms_class):
        self.dooms_class = dooms_class
        self.fields = {}
        
    def get_value(self, name):
        if name in self.fields:
            return self.fields[name]
            
        method = self.dooms_class.find_method(name)
        if method:
            return method.bind(self)
            
        raise DoomsRuntimeError(f"Undefined property '{name}'.")
        
    def set_value(self, name, value):
        self.fields[name] = value

    def __str__(self):
        return f"<{self.dooms_class.name} instance>"
