
| Data Type    | Example Code | Explanation | Purpose & Use Case |  
|-------------|-------------|-------------|---------------------|  
| **str** (String) | `x = str("Hello World")` | Stores a sequence of characters | Used for textual data like names, messages, etc. |  
| **int** (Integer) | `x = int(20)` | Stores whole numbers (positive, negative, or zero) | Used for counting, indexing, arithmetic operations, etc. |  
| **float** (Floating Point) | `x = float(20.5)` | Stores decimal numbers | Used in calculations requiring precision, like scientific computations or financial applications |  
| **complex** (Complex Number) | `x = complex(1j)` | Represents a number with a real and imaginary part | Used in advanced mathematical and engineering calculations |  
| **list** (List) | `x = list(("apple", "banana", "cherry"))` | Ordered, mutable collection | Used when you need a flexible, ordered collection of elements |  
| **tuple** (Tuple) | `x = tuple(("apple", "banana", "cherry"))` | Ordered, immutable collection | Used for fixed data structures like coordinates, database records |  
| **range** (Range) | `x = range(6)` | Represents a sequence of numbers | Used in loops for iteration (`for i in range(6)`) |  
| **dict** (Dictionary) | `x = dict(name="John", age=36)` | Key-value pairs (unordered) | Used for storing structured data like JSON, configurations |  
| **set** (Set) | `x = set(("apple", "banana", "cherry"))` | Unordered, unique elements | Used to store unique items and perform set operations |  
| **frozenset** (Frozen Set) | `x = frozenset(("apple", "banana", "cherry"))` | Immutable version of a set | Used when a set should not be modified |  
| **bool** (Boolean) | `x = bool(5)` | Represents `True` or `False` | Used for conditional checks (`if`, `while` loops) |  
| **bytes** (Bytes) | `x = bytes(5)` | Immutable sequence of bytes | Used for handling binary data like images, files |  
| **bytearray** (Byte Array) | `x = bytearray(5)` | Mutable sequence of bytes | Used when you need to modify binary data |  
| **memoryview** (Memory View) | `x = memoryview(bytes(5))` | Provides a view of a memory buffer | Used for handling large binary data efficiently without copying |  


Examples

| Data Type      | Representation Example                  | Explanation & Use Case |  
|---------------|-----------------------------------------|------------------------|  
| **str** (String) | `"Hello World"` | Used for textual data like names, messages, etc. |  
| **int** (Integer) | `20`, `-5`, `1000` | Used for counting, indexing, arithmetic operations, etc. |  
| **float** (Floating Point) | `20.5`, `-3.14`, `0.001` | Used in calculations requiring precision, like scientific computations or financial applications. |  
| **complex** (Complex Number) | `3 + 5j`, `-2j`, `1.5 + 2.5j` | Used in advanced mathematical and engineering calculations. |  
| **list** (List) | `["apple", "banana", "cherry"]` | Ordered, mutable collection. Used when you need a flexible, ordered collection of elements. |  
| **tuple** (Tuple) | `("apple", "banana", "cherry")` | Ordered, immutable collection. Used for fixed data structures like coordinates, database records. |  
| **range** (Range) | `range(0, 6)` → `[0, 1, 2, 3, 4, 5]` | Represents a sequence of numbers, mostly used in loops (`for i in range(6)`). |  
| **dict** (Dictionary) | `{"name": "John", "age": 36}` | Key-value pairs (unordered). Used for storing structured data like JSON, configurations. |  
| **set** (Set) | `{"apple", "banana", "cherry"}` | Unordered, unique elements. Used to store unique items and perform set operations. |  
| **frozenset** (Frozen Set) | `frozenset({"apple", "banana", "cherry"})` | Immutable version of a set. Used when a set should not be modified. |  
| **bool** (Boolean) | `True`, `False` | Represents `True` or `False`. Used for conditional checks (`if`, `while` loops). |  
| **bytes** (Bytes) | `b'hello'`, `b'\x00\x01\x02\x03\x04'` | Immutable sequence of bytes. Used for handling binary data like images, files. |  
| **bytearray** (Byte Array) | `bytearray([72, 101, 108, 108, 111])` → `b'Hello'` | Mutable sequence of bytes. Used when you need to modify binary data. |  
| **memoryview** (Memory View) | `memoryview(b'hello')` | Provides a view of a memory buffer. Used for handling large binary data efficiently without copying. |  


Table of escape characters in Python along with their descriptions and examples:  

| Escape Character | Description | Example | Output |  
|-----------------|-------------|---------|--------|  
| `\'` | Single quote | `'It\'s a pen.'` | `It's a pen.` |  
| `\"` | Double quote | `"He said, \"Hello!\""` | `He said, "Hello!"` |  
| `\\` | Backslash | `"This is a backslash: \\"` | `This is a backslash: \` |  
| `\n` | New line | `"Hello\nWorld"` | `Hello`<br>`World` |  
| `\t` | Tab (horizontal) | `"Hello\tWorld"` | `Hello    World` |  
| `\r` | Carriage return | `"Hello\rWorld"` | `World` (Replaces "Hello") |  
| `\b` | Backspace | `"Hello\bWorld"` | `HellWorld` |  
| `\f` | Form feed (New page in some printers) | `"Hello\fWorld"` | `Hello` (New page effect) `World` |  
| `\v` | Vertical tab | `"Hello\vWorld"` | `Hello`<br>(Vertical space)`World` |  
| `\ooo` | Octal value | `"\101\102\103"` | `ABC` |  
| `\xhh` | Hexadecimal value | `"\x41\x42\x43"` | `ABC` |  


A table summarizing all the string methods in Python along with examples:  

| Method | Description | Example | Output |  
|--------|-------------|---------|--------|  
| `capitalize()` | Converts the first character to uppercase | `"hello".capitalize()` | `"Hello"` |  
| `casefold()` | Converts string into lowercase | `"HELLO".casefold()` | `"hello"` |  
| `center(width)` | Returns a centered string | `"hello".center(10)` | `"  hello   "` |  
| `count(value)` | Counts occurrences of a substring | `"banana".count("a")` | `3` |  
| `encode()` | Returns encoded version of string | `"hello".encode()` | `b'hello'` |  
| `endswith(value)` | Checks if string ends with value | `"hello".endswith("o")` | `True` |  
| `expandtabs(size)` | Sets tab size | `"H\te\tl\tl\to".expandtabs(2)` | `"H e l l o"` |  
| `find(value)` | Finds position of first occurrence | `"hello".find("l")` | `2` |  
| `format()` | Formats string | `"My name is {}".format("John")` | `"My name is John"` |  
| `format_map(mapping)` | Formats using a dictionary | `"My name is {name}".format_map({"name": "John"})` | `"My name is John"` |  
| `index(value)` | Finds position of first occurrence (error if not found) | `"hello".index("l")` | `2` |  
| `isalnum()` | Checks if all characters are alphanumeric | `"Hello123".isalnum()` | `True` |  
| `isalpha()` | Checks if all characters are letters | `"Hello".isalpha()` | `True` |  
| `isascii()` | Checks if all characters are ASCII | `"Hello".isascii()` | `True` |  
| `isdecimal()` | Checks if all characters are decimals | `"123".isdecimal()` | `True` |  
| `isdigit()` | Checks if all characters are digits | `"123".isdigit()` | `True` |  
| `isidentifier()` | Checks if valid Python identifier | `"hello".isidentifier()` | `True` |  
| `islower()` | Checks if all characters are lowercase | `"hello".islower()` | `True` |  
| `isnumeric()` | Checks if all characters are numeric | `"123".isnumeric()` | `True` |  
| `isprintable()` | Checks if all characters are printable | `"hello".isprintable()` | `True` |  
| `isspace()` | Checks if string contains only spaces | `"   ".isspace()` | `True` |  
| `istitle()` | Checks if string follows title case | `"Hello World".istitle()` | `True` |  
| `isupper()` | Checks if all characters are uppercase | `"HELLO".isupper()` | `True` |  
| `join(iterable)` | Joins iterable elements with string | `"-".join(["a", "b", "c"])` | `"a-b-c"` |  
| `ljust(width)` | Left justifies string | `"hello".ljust(10)` | `"hello     "` |  
| `lower()` | Converts to lowercase | `"Hello".lower()` | `"hello"` |  
| `lstrip()` | Trims leading spaces | `"  hello".lstrip()` | `"hello"` |  
| `maketrans()` | Creates a translation table | `"hello".maketrans("h", "H")` | `{104: 72}` |  
| `partition(value)` | Splits into three parts | `"hello world".partition(" ")` | `('hello', ' ', 'world')` |  
| `replace(old, new)` | Replaces a substring | `"hello".replace("l", "L")` | `"heLLo"` |  
| `rfind(value)` | Finds last occurrence of value | `"hello".rfind("l")` | `3` |  
| `rindex(value)` | Finds last occurrence (error if not found) | `"hello".rindex("l")` | `3` |  
| `rjust(width)` | Right justifies string | `"hello".rjust(10)` | `"     hello"` |  
| `rpartition(value)` | Splits into three parts from the right | `"hello world".rpartition(" ")` | `('hello', ' ', 'world')` |  
| `rsplit(separator)` | Splits string into list from right | `"a,b,c".rsplit(",")` | `['a', 'b', 'c']` |  
| `rstrip()` | Trims trailing spaces | `"hello   ".rstrip()` | `"hello"` |  
| `split(separator)` | Splits string into list | `"a,b,c".split(",")` | `['a', 'b', 'c']` |  
| `splitlines()` | Splits string at line breaks | `"Hello\nWorld".splitlines()` | `['Hello', 'World']` |  
| `startswith(value)` | Checks if string starts with value | `"hello".startswith("h")` | `True` |  
| `strip()` | Trims both leading and trailing spaces | `"  hello  ".strip()` | `"hello"` |  
| `swapcase()` | Swaps case of characters | `"Hello".swapcase()` | `"hELLO"` |  
| `title()` | Converts to title case | `"hello world".title()` | `"Hello World"` |  
| `translate(table)` | Translates characters using table | `"hello".translate({104: 72})` | `"Hello"` |  
| `upper()` | Converts to uppercase | `"hello".upper()` | `"HELLO"` |  
| `zfill(width)` | Fills with zeros from the left | `"42".zfill(5)` | `"00042"` |  
