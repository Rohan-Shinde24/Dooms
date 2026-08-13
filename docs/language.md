# DOOMS Language Documentation

Welcome to the DOOMS programming language documentation! This guide outlines the syntax, rules, and features currently supported by the interpreter.

## 1. Variables and Explicit Types
DOOMS is strongly typed. You must declare variables using one of the core types (`int`, `str`, `boo`) or `any`.
```dooms
int age = 10;
str name = "DOOMS";
boo active = true;
```

**The `any` Keyword:**
If you want a variable that can store any type and change types later (like dynamic typing), use `any`:
```dooms
any mystery = 22;
mystery = "hi"; // Perfectly valid
```

**Runtime Type Checking:**
DOOMS strictly enforces your declared types. If you try to assign the wrong type to a strict variable, DOOMS throws a `RuntimeError`:
```dooms
int count = "hello"; // DOOMS Runtime Error: Type mismatch
```

## 2. Arithmetic and Comparisons
You can use standard math operators on integers:
- Addition: `+`
- Subtraction: `-`
- Multiplication: `*`
- Division: `/` (Note: Division floors the result to remain an integer).

You can also compare values to return a `boo` (boolean):
- Less Than: `<`
- Greater Than: `>`
- Equal To: `==`

## 3. Control Flow (If / Else)
You can write branching logic using `if` and `else` blocks:
```dooms
int health = 50;

if (health < 20) {
    print("Low Health!");
} else {
    print("Looking good.");
}
```

## 4. Loops (`while`)
DOOMS supports `while` loops to repeat logic as long as a condition is true:
```dooms
int i = 0;
while (i < 3) {
    print(i);
    i = i + 1;
}
```

## 5. Block Scoping
DOOMS manages memory using block scope (`{ ... }`). Any typed variables declared inside a block are safely destroyed when the block finishes executing:
```dooms
{
    int secret = 42;
    print("Inside:", secret);
}
// print(secret); // This will crash! The variable 'secret' no longer exists.
```

## 6. Built-in Functions
- `print(a, b, c, ...)`: Prints any number of values to the standard output, separated by spaces.

## 7. Custom Functions
You can define your own functions using the `func` keyword. Because DOOMS is strictly typed, you must declare the types of your function parameters:
```dooms
func add(int a, int b) {
    return a + b;
}

int result = add(5, 10);
print(result); // Outputs: 15
```

DOOMS supports recursion! A function can call itself to calculate complex values:
```dooms
func factorial(int n) {
    if (n < 2) {
        return 1;
    }
    return n * factorial(n - 1);
}

print(factorial(5)); // Outputs: 120
```

## 8. Arrays, Tuples, and Constraints
Arrays use square brackets `[]`. 

### Simple Typing
If you define an array with a basic type (`int`, `str`, `boo`), it means every element in the array must match that type:
```dooms
int a = [1, 2, 3] // Valid
int b = [1, "two"] // ERROR! Array expects int only.
```

### Tuple Types
You can enforce strict structures by passing a list of types. This creates a Tuple Type:
```dooms
[int, str] user = [1, "Alice"] // Valid! Exactly one int and one str.
[int, str] bad = ["Alice", 1] // ERROR! Sequence must match exactly.
```

### Fixed Size Constraints
You can create an empty array locked to a maximum size using `[(size)]`. Attempting to add items beyond this limit will throw a runtime error.
```dooms
any a = [(3)]
a.push(1)
a.push(2)
a.push(3)
a.push(4) // ERROR! Cannot push: array is fixed to size 3
```

### Array Methods
Arrays have built-in methods that you can invoke using the `.` operator:
- `.push(val)` or `.append(val)`: Adds an item to the end of the array.
- `.insert(index, val)`: Inserts an item at a specific index.
- `.pop()`: Removes and returns the last item in the array.

## 9. Dictionaries
Dictionaries allow you to store key-value pairs using `{}` and `:`. 
```dooms
any person = {
    "name": "Alice",
    "age": 25
}
```

### Dictionary Operations
You can access keys using bracket notation (`person["name"]`) or dot notation (`person.name`).
Dictionaries also have methods:
- `.set("key", value)`: Adds or updates a key.
- `.get("key")`: Returns the value of a key.
- `.keys()`: Returns an array of keys.
- `.values()`: Returns an array of values.

## 10. Strings & Input
DOOMS supports built-in interactive input using `input("Prompt: ")`.

### Type Coercion
If you assign the result of `input()` to a strictly typed variable like `int` or `boo`, DOOMS will attempt to coerce the value automatically:
```dooms
int age = input("Enter age: ") // If you type 25, age becomes an integer 25!
```

### String Methods
Strings support methods just like arrays and dictionaries:
- `.length()`: Returns the number of characters.
- `.upper()`: Returns uppercase text.
- `.lower()`: Returns lowercase text.
- `.split("delimiter")`: Returns an array of string chunks.

## 11. Modules and Imports
DOOMS supports splitting code across multiple files! You can use the `import` keyword to run external `.dooms` files.

### Global Inclusion
To execute a file and dump all its variables/functions directly into your current scope, just provide the filepath as a string:
```dooms
import "math_utils.dooms";

int result = add(5, 5); // Assuming `add` was defined inside math_utils.dooms
```

### Namespaced Imports
To prevent scope pollution, you can import a file under a specific namespace using the `as` keyword:
```dooms
import "math_utils.dooms" as math;

int result = math.add(5, 5); // The file's variables/functions become properties!
```

## 12. Classes and OOP
DOOMS supports Object-Oriented Programming using the `class` keyword. You can define properties using the `this` keyword.

### Class Declaration
```dooms
class Person {
    // The 'init' method runs automatically upon creation!
    func init(str name, int age) {
        this.name = name;
        this.age = age;
    }

    func greet() {
        print("Hello, my name is", this.name);
    }
}
```

### Instantiation
To create an instance of a class, you just call the class name like a function (no `new` keyword required).
```dooms
any my_person = Person("DOOMS", 1);
my_person.greet();
```
