
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
