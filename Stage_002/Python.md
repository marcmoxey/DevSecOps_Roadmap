
# Python — Journal (Stage 2)

Coming from C#/ASP.NET — most of chapters 1-10 will be new SYNTAX for concepts already known, not new concepts. For each entry, the useful question is: "Is this new, or is this just Python's way of writing something I already know from C#?" Slow down only where the answer is genuinely new.

Note: conda activate abspython - spyder

Same template as the Bash Scripting journal:

```
## Date:
**Topic:**

**Commands / code:**

**What happened:**
Problem: exact error message (if any)
Fix: what actually solved it

**Learned:**
one sentence takeaway — note the C# comparison if relevant
```

---

## Date: 06/17/2026

**Topic:** Python Basics (ch. 1)

**Code:**

```python
print(2 + 2)
print(2 + 3 * 6)
print((2 + 3) * 6)
print(2 ** 8)          # exponent
print(23 / 7)           # float division
print(23 // 7)          # integer (floor) division

# strings
print('Alice' + 'Bob')        # concatenation
print('Alice' * 5)             # repetition
#print('Alice' + 5)            # TypeError: can only concatenate str (not "int") to str — use str(5)
#print('Alice' * 'Bob')        # TypeError: can't multiply sequence by non-int of type 'str'
#print('Alice' * 5.0)          # TypeError: can't multiply sequence by non-int of type 'float'

spam = 40
spam = spam + 2
spam = 'hello'          # same variable, now holds a string instead of an int

print(len('hello'))
print(str(29))           # int -> str
print(int('42'))          # str -> int
print(int(1.99))          # float -> int, TRUNCATES (doesn't round) -> 1
print(float(10))          # int -> float

print(42 == '42')        # False — different types, no coercion for ==
print(42 == 42.0)        # True — int/float ARE compared by value
print(type(42))
print(type('forty two'))

print(round(7.7))         # 8
print(round(7.777777, 3)) # 7.778 — second arg = decimal places
print(abs(-25))           # 25
```

**What happened:** Worked through basic operators, the three core data types (int, float, str), and the type-conversion functions (`str()`, `int()`, `float()`). Tried several "wrong" combinations on purpose to see the actual errors (commented out, kept in the file as notes).

**Learned (vs C#):** No semicolons, no curly braces — indentation IS the block structure. `42 == '42'` is `False` (no implicit string/number coercion for `==`), but `42 == 42.0` is `True` — Python compares int and float **by value**, not by type, which is different from languages that might treat them as needing explicit comparison/casting. `int(1.99)` **truncates** toward zero rather than rounding — `int(1.99)` is `1`, not `2`; use `round()` if rounding is actually wanted. String `+` concatenates, but only with other strings — mixing types (`'Alice' + 5`) throws `TypeError` and requires an explicit `str()` conversion, similar to needing `.ToString()` in C# but Python is stricter about refusing the silent coercion C# sometimes allows.

---

## Date: 06/17/2026

**Topic:** if-else and Flow Control (ch. 2)

**Code:**

```python
# Comparison operators
print(42 == 42)
print(2 != 3)
print(42 < 100)
print(42 <= 42)

# Boolean operators
print(True and True)
print(False or True)
print(not True)
print(not not not not True)   # odd number of `not`s flips it; even number cancels out

# mixing boolean + comparison
print((4 < 5) and (5 < 6))

# if / elif / else
name = 'Marc'
age = 11
if name == 'Alice':
    print('Hi, Alice')
elif age < 12:
    print('You are not Alice, kiddo')
# no else — if neither condition is true, nothing prints at all

spam = 2
if spam == 1:
    print('Hello')
elif spam == 2:
    print('Howdy')
else:
    print('Greetings')
```

**What happened:** Practiced comparison operators, boolean operators (`and`/`or`/`not`), and chaining conditions with `if`/`elif`/`else`. Also built three small standalone scripts using this — `littleKid.py`, `vampire.py` (chained `elif`s checking age ranges), and `oppositeday.py` (toggling a boolean based on another boolean).

**Learned (vs C#):** `and`/`or`/`not` are spelled-out words in Python instead of `&&`/`||`/`!` in C# — takes a moment to retrain muscle memory. An `if`/`elif` chain with **no `else`** is completely valid — if no condition matches, the program just continues with no output and no error, which is different from expecting some kind of fallback to always fire. This came back to bite a separate script (`dishonestcapacity.py` — see entry below) where a missing `else` left a variable undefined later in the script, causing a crash several lines down rather than at the `if` itself — the error shows up far from its actual cause.

---

## Date: 06/17/2026

**Topic:** ⚠️ Real bug — missing else branch causes NameError (dishonestcapacity.py)

**Code:**

```python
print('Enter TB or GB for the advertised unit:')
unit = input('>')

if unit == 'TB' or unit == 'tb':
    discrepancy = 1000000000000 / 1099511627776
elif unit == 'GB' or unit == 'gb':
    discrepancy = 1000000000 / 1073741824
# no else!

advertised_capacity = float(input('>'))
real_capacity = str(round(advertised_capacity * discrepancy, 2))  # crashes here if discrepancy was never set
```

**What happened:** Problem: if the user types anything other than exactly `TB`, `tb`, `GB`, or `gb` (a typo, different case, anything else), **neither** branch of the `if`/`elif` runs, so `discrepancy` is never created. The crash (`NameError: name 'discrepancy' is not defined`) happens several lines later, at the point `discrepancy` is finally used — not at the `if` statement itself, which makes it confusing to trace back.

Fix: add an `else` to handle the "none of the above" case:

```python
else:
    print('Invalid unit entered.')
    import sys
    sys.exit()
```

**Learned:** General rule worth remembering: **any `if`/`elif` chain that assigns a variable should have an `else`** that handles the unexpected case — otherwise there's a real risk of a variable that simply doesn't exist later in the script. The error message points to where the missing variable is _used_, not where it _should have been created_ — so when debugging a `NameError`, the real fix is often several lines above where the error actually appears.

---

## Date: 06/17/2026

**Topic:** Loops (ch. 3)

**Code:**

```python
# while loop
spam = 0
while spam < 5:
    print('Hello, world.')
    spam = spam + 1

# for loop with range()
for i in range(12, 16):       # 12, 13, 14, 15 (end is EXCLUSIVE)
    print(i)

for i in range(0, 10, 2):     # start, end, step -> 0, 2, 4, 6, 8
    print(i)

for i in range(5, -1, -1):    # counting DOWN -> 5, 4, 3, 2, 1, 0
    print(i)

# loop variable still accessible AFTER the loop
for guesses_taken in range(1, 7):
    guess = int(input('>'))
    if guess == secret_number:
        break
if guess == secret_number:        # guess and guesses_taken still exist here
    print('Got it in ' + str(guesses_taken) + ' guesses!')

# break vs continue
while True:
    name = input('>')
    if name != 'Joe':
        continue          # skip the rest of this iteration, loop again
    password = input('>')
    if password == 'swordfish':
        break              # exit the loop entirely
```

**What happened:** Built several small programs using loops: `fiveTimes.py` (for vs while doing the same thing), `Loops.py` (range() variations including negative step), `guessTheNumber.py` (a number-guessing game using `break` on a correct guess), and `swordfish.py` (a login-style loop using both `continue` and `break`).

**Learned (vs C#):** `range(start, end, step)` — the `end` value is always **exclusive** (never reached), which trips people up constantly; `range(5, -1, -1)` has to go one PAST the actual target (`0`) to include `0`, since the step is negative and `end` is exclusive. **Loop variables are NOT block-scoped** to the loop in Python — `guess` and `guesses_taken` from inside a `for` loop are still readable after the loop ends, which is different from C#'s `for` loop variable being scoped only to the loop body. `continue` skips to the next iteration; `break` exits the loop completely — same concepts as C#, just confirmed they work identically.

---

## Date: 06/17/2026

**Topic:** Functions (ch. 4)

**Code:**

```python
# Basic function with no parameters
def hello():
    print('Good morning!')
    print('Good afternoon!')
    print('Good evening!')

hello()
hello()

# Function with a parameter
def say_hello_to(name):
    print('Good morning, ' + name)

say_hello_to('Alice')
say_hello_to('Bob')

# return values
def get_answer(answer_number):
    if answer_number == 1:
        return 'It is certain'
    elif answer_number == 2:
        return 'It is decidedly so'
    # ... etc

import random
r = random.randint(1, 9)
fortune = get_answer(r)
print(fortune)

# None — what a function returns if it has no explicit return
spam = print('Hello!')
print(spam)            # None
print(None == spam)     # True

# named/keyword arguments
print('Hello', end='')          # suppress the newline
print('cats', 'dogs', sep=',')   # change the separator between args

# Local vs global scope
def spam():
    global eggs
    eggs = 'spam'          # this modifies the GLOBAL eggs

def bacon():
    eggs = 'bacon'          # this creates a totally separate 
                              # LOCAL eggs — does NOT touch global, 
                              # even though same name

def ham():
    print(eggs)              # reads the global eggs (fine — reading 
                               # doesn't require the `global` keyword, 
                               # only modifying does)

eggs = 'global'
spam()
print(eggs)    # 'spam' — global was changed

# Exception handling
def spam(divide_by):
    try:
        return 42 / divide_by
    except ZeroDivisionError:
        print('Error: invalid argument')

print(spam(2))    # 21.0
print(spam(0))    # prints "Error: invalid argument", then 
                    # the function falls through with no 
                    # explicit return -> prints None afterward
```

**What happened:** Worked through function basics (defining, calling, parameters), return values vs. functions with no return (`None`), keyword arguments (`end=`, `sep=`), local vs. global scope including the `global` keyword, and `try`/`except` exception handling. Built several small scripts: `helloFunc.py`/`helloFunc2.py` (basic functions and parameters), `magic8Ball.py` (return values based on a random input), `sameNameLocalGlobal.py` (a same-named local variable NOT touching the global), `abcdStack.py` (tracing call order/return order through nested function calls by hand), and `coinFlip.py` (using `end=' '` to print 100 results on one line instead of 100 separate lines).

**Learned (vs C#):** A function with no explicit `return` statement doesn't error or do nothing — it implicitly returns `None`, Python's "no value" placeholder (similar in spirit to C#'s `void`, but `None` is an actual value you can check against, e.g. `print(spam(0))` after the `except` block prints `None` since there's no `return` inside it). **Local vs global scope is stricter than expected**: a variable assigned inside a function is local by default, even if a global variable with the exact same name exists — they don't interact at all unless the `global` keyword is explicitly used inside the function to say "modify the outer one, don't create a local one." This is different from just "scoping rules" in C# — it's specifically that _assignment_ inside a function defaults to creating a new local, full stop, unless told otherwise. Reading a global from inside a function works fine without any keyword — only _writing_ to it needs `global`. `try`/`except` matches C#'s `try`/`catch` conceptually, but the specific exception type (`ZeroDivisionError`) is caught by name, similar to catching a specific exception class in C#.

---

## Date: 06/17/2026

**Topic:** ⚠️ Real bug — nested loop indentation (spike.py)

**Code:**

```python
# BUGGY — second for loop is nested INSIDE the first
for i in range(1, 9):
    print('-' * (i * 1))
    time.sleep(0.1)

    for i in range(7, 1, -1):      # indented one level too deep
        print('-' * (i * 1))
        time.sleep(0.1)
```

**What happened:** Problem: the comment said "Draw lines with decreasing length" as if it were a separate step after the increasing-length loop — but the second `for` loop is indented to be INSIDE the first loop's body, not after it. This means for every single iteration of the increasing loop (8 times), the entire decreasing loop runs all over again inside it — producing a tangled, repeated pattern instead of "increase once, then decrease once."

Fix: dedent the second `for` loop so it's a sibling of the first, not a child:

```python
for i in range(1, 9):
    print('-' * (i * 1))
    time.sleep(0.1)

for i in range(7, 1, -1):          # now at the same level as the first loop
    print('-' * (i * 1))
    time.sleep(0.1)
```

**Learned:** Same root cause as the `rpsGame.py` indentation bug from Chapter 3 — indentation level determines what's nested inside what, and Python won't complain about it being "wrong" if it's still syntactically valid, even if it doesn't match the intended logic. Two blocks of code that are meant to run **sequentially** (one after another) need to be at the **same** indentation level; if one is indented further than the other, it becomes nested inside it instead. Worth a habit: whenever pairing two loops or blocks that are meant to be parallel steps, double-check they line up at the exact same indentation.

---

## Date: 06/18/2026

**Topic:** Debugging (ch. 5)

**Code:**

```python
# Raising exceptions manually
def box_print(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('Symbol must be a single character string.')
    if width <= 2:
        raise Exception('Width must be greater than 2.')
    if height <= 2:
        raise Exception('Height must be greater than 2.')

try:
    box_print('*', 4, 4)     # works
    box_print('x', 1, 3)     # raises "Width must be greater than 2"
    box_print('ZZ', 3, 3)    # raises "Symbol must be a single character string"
except Exception as err:
    print('An exception happened: ' + str(err))

# Assertions
ages = [26, 57, 92, 54, 22, 15, 17, 80, 47, 73]
ages.reverse()
assert ages[0] <= ages[-1]   # triggers AssertionError — reverse() puts largest first

# Logging
import logging
logging.basicConfig(level=logging.DEBUG,
    format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Some minor code and debugging details.')
logging.info('An event happened.')
logging.warning('Something could go wrong.')
logging.error('An error has occurred.')
logging.critical('The program is unable to recover!')

# disable logging
logging.disable(logging.CRITICAL)   # silences all logging at or below CRITICAL
logging.critical('This is silenced')

# Using logging inside a function to trace execution
def factorial(n):
    logging.debug('Start of factorial(' + str(n) + ')')
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(' + str(n) + ')')
    return total

print(factorial(5))
```

**What happened:** Worked through three debugging tools — `raise Exception()`, `assert`, and the `logging` module. Built `boxPrint.py` (validate inputs with raise, catch with try/except), `factorialLog.py` (trace every step of a factorial calculation using `logging.debug()` inside the loop), and practiced assertions on a reversed list. Also hit the Spyder-specific `basicConfig()` gotcha: calling it multiple times in the same kernel session silently ignores all calls after the first — only the very first `basicConfig()` in the session takes effect.

**Learned:** `raise Exception('message')` is how you manually signal an error in a function — useful for input validation at the top of a function before doing any work. `assert condition` triggers `AssertionError` when the condition is `False` — easy to get the direction backwards (assert fires on False, not True). `logging.basicConfig()` is a one-time-per-process setup call — calling it multiple times silently ignores all but the first, which explains why the `filename=` log file parameter didn't work when called second. `logging.disable(logging.CRITICAL)` silences everything at CRITICAL and below, which is effectively all levels since CRITICAL is the highest. Using `logging.debug()` inside a loop (like `factorialLog.py`) is much better than `print()` for debugging because you can silence all debug output with one line change before shipping, instead of hunting for every print statement.

---

## Date: 06/19/2026

**Topic:** Lists (ch. 6)

**Code:**

```python
# Indexing and slicing
spam = ['cat', 'bat', 'rat', 'elephant']
print(spam[0])          # 'cat'
print(spam[-1])          # 'elephant' — negative indexes from the end
print(spam[1:3])         # ['bat', 'rat'] — end is exclusive
print(spam[:2])          # ['cat', 'bat']
print(spam[:])           # full copy of the list

# Nested lists
spam = [['cat', 'bat'], [10, 20, 30, 40, 50]]
print(spam[0][1])        # 'bat' — first list, second item

# Modifying
spam = ['cat', 'bat', 'rat', 'elephant']
spam[1] = 'aardvark'    # update by index
del spam[2]              # delete by index

# in / not in
print('cat' in spam)
print('dog' not in spam)

# Multiple assignment (unpacking)
cat = ['fat', 'gray', 'loud']
size, color, disposition = cat    # unpacks all three at once

# enumerate()
for index, item in enumerate(['pens', 'staplers', 'binders']):
    print('Index ' + str(index) + ': ' + item)

# random.choice() and random.shuffle()
import random
pets = ['Dog', 'Cat', 'Mouse']
print(random.choice(pets))       # random single item
random.shuffle(pets)              # shuffles in-place

# List methods
spam = ['cat', 'dog', 'bat']
spam.append('moose')              # add to end
spam.insert(1, 'chicken')         # add at index
spam.remove('bat')                # remove first occurrence
spam.sort()                       # sort in-place
spam.reverse()                    # reverse in-place
print(spam.index('dog'))          # find index of value

# copy vs reference
import copy
spam = ['A', 'B', 'C']
cheese = copy.copy(spam)   # independent copy
cheese[1] = 42              # only affects cheese, NOT spam

eggs = spam                 # this is a REFERENCE, not a copy
eggs[1] = 'Hello'           # changes BOTH eggs AND spam!

# Coin flip streak project — list slicing for pattern detection
coins = ['H', 'T', 'H', 'H', 'H', 'H', 'H', 'T']
if coins[2:8] == ['H','H','H','H','H','H']:
    print('streak found')
```

**What happened:** Worked through the full list chapter — indexing, slicing, negative indexes, nested lists, `in`/`not in`, multiple assignment unpacking, `enumerate()`, `random.choice()`/`shuffle()`, all major list methods (append, insert, remove, sort, reverse, index), and the critical difference between copying a list vs copying a reference. Built `allMyCats1.py` vs `allMyCats2.py` (showing why a list is better than individual variables), `myPets.py` (using `in` to search a list), `magic8Ball2.py` (random list indexing instead of chained `elif`), `CoinFlipStreaks.py` (list slicing for pattern detection across 10,000 experiments), `CommaCode.py` (joining list items into a comma-separated string with "and" before the last item), and `matrixscreensaver.py` (a list tracking per-column counters for a Matrix-style screensaver).

**Learned (vs C#):** List slicing (`list[start:end]`) is Python-specific — C# doesn't have this syntax natively (you'd use LINQ `.Skip().Take()` or `Array.Copy()`). The slice end is always exclusive, same as `range()`. Negative indexes (`spam[-1]`) are also not in C# — Python maps them to `len(list) - n`. `list.sort()` sorts IN-PLACE and returns `None` — common bug in C# muscle memory is to do `spam = spam.sort()`, which sets spam to None (sort doesn't return the list). `copy.copy()` vs plain assignment is the most important distinction: `eggs = spam` makes both variables point to the SAME list in memory — modifying `eggs` modifies `spam` too. This is different from C# value types (ints, structs) but similar to C# reference types (objects) — Python lists are always reference types. `enumerate()` is cleaner than C#'s `for (int i = 0; i < list.Count; i++)` when you need both index and value — concise and Pythonic.

---

## Date: 06/19/2026

**Topic:** Dictionaries and Structuring Data (ch. 7)

**Code:**

```python
# Basic dictionary
my_cat = {'size': 'fat', 'color': 'gray', 'age': 17}
print(my_cat['size'])          # access by key
# print(my_cat['weight'])      # KeyError — key doesn't exist

# Order doesn't matter for equality
eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'}
print(eggs == ham)              # True — dicts compare by content not order
                                 # (opposite of lists where order matters)

# Iterating
spam = {'color': 'red', 'age': 42}
for k in spam.keys():    print(k)
for v in spam.values():  print(v)
for k, v in spam.items(): print('Key: ' + k + ' Value: ' + str(v))

# Checking key existence
print('color' in spam)           # True — shorthand for 'color' in spam.keys()
print('color' in spam.keys())    # same thing, explicit

# .get() — safe access with a default
picnic_items = {'apples': 5, 'cups': 2}
print(picnic_items.get('cups', 0))    # 5 (key exists)
print(picnic_items.get('eggs', 0))    # 0 (key missing, returns default)

# .setdefault() — set a key only if it doesn't already exist
spam = {'name': 'Pooka', 'age': 5}
spam.setdefault('color', 'black')    # adds 'color': 'black'
spam.setdefault('color', 'white')    # does NOTHING (key already exists)
print(spam)                            # {'name': 'Pooka', 'age': 5, 'color': 'black'}

# Character counter — a great dict pattern
message = 'It was a bright cold day in April...'
count = {}
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

# Nested dictionaries
all_guests = {
    'Alice': {'apples': 5, 'pretzels': 12},
    'Bob': {'ham sandwiches': 3, 'apples': 2}
}

def total_brought(guests, item):
    num_brought = 0
    for k, v in guests.items():
        num_brought += v.get(item, 0)
    return num_brought

# Chessboard — dict as a data structure for a board game
board = {'a1': 'wR', 'e1': 'wK', 'a8': 'bR'}
if 'e4' in board:
    print(board['e4'])
else:
    print('empty square')
```

**What happened:** Worked through the full dictionary chapter — basic access, key/value iteration with `.keys()`/`.values()`/`.items()`, safe access with `.get()`, `.setdefault()` for building up a dict incrementally, and nested dictionaries. Built `birthdays.py` (a dict that gets added to at runtime as user enters new birthdays), `characterCount.py` (counting character frequency using `setdefault()` — a clean pattern for building a tally dict), `Dictionaries.py` (all the core examples from the chapter), and `chessboard.py` (a full interactive chessboard using a dict as the board data structure — key is the square name like `'e4'`, value is the piece like `'wK'`).

**Learned (vs C#):** Python dictionaries are equivalent to C#'s `Dictionary<string, object>`, but with much cleaner syntax — `dict['key']` vs `dict["key"]` is the same idea, but Python allows mixed-type values naturally without generics. The key difference: `dict['missing_key']` throws `KeyError` (same as C# `KeyNotFoundException`), but `.get('missing_key', default)` is the safe version that returns a default instead of crashing — much cleaner than C#'s `.TryGetValue()` pattern. `.setdefault()` has no direct C# equivalent — it's a combined "check if key exists, if not add it" in one call. Dict ordering: since Python 3.7+, dicts maintain insertion order — but equality comparison (`==`) ignores order and compares by content, opposite of lists. `characterCount.py` is a good example of a recurring Python pattern: use `setdefault(key, 0)` to initialize a counter, then increment it — this shows up constantly in data processing/automation work.

---

## Date: 06/20/2026

**Topic:** Strings and Text Editing (ch. 8)

**Code:**

```python
# Escape characters and raw strings
print("Hello there!\nHow are you?\nI\'m doing fine")
print(r'The file is in C:\Users\Alice\Desktop')   # raw string — \n is literal, not a newline

# Indexing and slicing (same rules as lists)
greeting = 'Hello, world!'
print(greeting[0])        # 'H'
print(greeting[-1])        # '!'
print(greeting[7:])         # 'world!'

# in / not in
print('Hello' in 'Hello, world!')     # True
print('cats' not in 'cats and dogs')  # False

# f-strings (the modern way to build strings)
name = 'Ai'
age = 4000
print(f'My name is {name}. I am {age} years old')
print(f'In 10 years I will be {age + 10}')     # expressions work inside {}
print(f'{{name}}')                                # literal {name} — double braces escape

# Useful string methods
spam = 'Hello, world!'
print(spam.upper())             # 'HELLO, WORLD!'
print(spam.lower())              # 'hello, world!'
print('hello123'.isalpha())      # False — has digits
print('hello'.isalnum())          # True — letters and/or numbers only
print('  '.isspace())              # True
print('Hello, world1'.startswith('Hello'))   # True

# Joining and splitting
print(', '.join(['cats', 'rats', 'bats']))           # 'cats, rats, bats'
print('MyABCnameABCisABCSimon'.split('ABC'))          # ['My', 'name', 'is', 'Simon']

multiline = '''Dear Alice,
There is a milk bottle in the fridge.
Sincerely,
Bob'''
print(multiline.split('\n'))     # splits into a list, one item per line

# Justify and pad
print('Hello'.rjust(10))           # right-aligned, padded with spaces
print('Hello'.rjust(20, '*'))      # padded with '*' instead
print('Hello'.center(20, '='))     # centered

# Whitespace removal
spam = '       Hello, World             '
print(spam.strip())    # removes leading AND trailing whitespace
print(spam.lstrip())   # left only
print(spam.rstrip())   # right only

spam = 'SpamSpamBaconSpamEggsSpamSpam'
print(spam.strip('ampS'))   # strips any of those CHARACTERS from both ends, not the literal substring

# ord() and chr() — character <-> numeric code point
print(ord('A'))      # 65
print(chr(65))         # 'A'

# Clipboard (pyperclip)
import pyperclip
text = pyperclip.paste()   # read clipboard
pyperclip.copy(result)      # write to clipboard
```

**What happened:** Worked through the full string chapter — escape characters, raw strings, f-strings (and the `{{ }}` escape for literal braces), the major string methods (`upper`/`lower`/`isalpha`/`isalnum`/`startswith`/`endswith`), joining/splitting, justify/pad (`rjust`/`ljust`/`center`), whitespace stripping, and `ord()`/`chr()`. Also completed end-of-chapter projects without initially realizing that's what they were: `pigLatin.py` (full English-to-Pig-Latin translator — the hardest exercise in the chapter), `bulletPointAdder.py` (reads clipboard text, adds `*` to the start of every line, copies back), and `alternatingText.py` (aLtErNaTiNg CaSe converter using clipboard). Also built `feedcat.py` (multiline strings with triple quotes) and `validateInput.py` (using `.isdecimal()` and `.isalnum()` for input validation loops).

**Learned (vs C#):** F-strings (`f'{name}'`) are the direct equivalent of C#'s string interpolation (`$"{name}"`) — same idea, different prefix letter. Raw strings (`r'...'`) have no real C# equivalent for normal strings, but are similar in spirit to C#'s verbatim strings (`@"..."`) — both stop escape sequences from being interpreted. `strip('ampS')` was a genuine surprise: it doesn't strip the literal substring `"ampS"` — it strips any _characters_ found in that set from both ends, which is different from how `.Trim()` works with a substring in some other languages. String slicing uses the exact same `[start:end]` rules as list slicing from ch. 6 — confirms strings and lists share the same "sequence type" behavior in Python, which is a unifying concept C# doesn't really have (strings and arrays are more separate there).

---

---

## Date: 06/21/2026 - 06/22/2026

**Topic:** Text Pattern Matching with Regular Expressions (ch. 9) — pair with TryHackMe Regex room

**Code:**

```python
import re

# Basic compile + search
phone_num_pattern_obj = re.compile(r'\d{3}-\d{3}-\d{4}')
match_obj = phone_num_pattern_obj.search('My number is 415-555-4242')
print(match_obj.group())   # '415-555-4242'

# Grouping with parentheses
phone_re = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phone_re.search('My number is 415-555-4242')
print(mo.group(1))    # '415'       — first group
print(mo.group(2))    # '555-4242'  — second group
print(mo.group(0))    # '415-555-4242' — full match
area_code, main_number = mo.groups()   # unpack all groups at once

# Escape characters inside regex (literal parentheses need escaping)
pattern = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = pattern.search('My phone number is (415) 555-4242')
print(mo.group(1))    # '(415)'

# Alternation with |
pattern = re.compile(r'Cat(cerpiler|astrophe|ch|egory)')
match = pattern.search('Catch me if you can')
print(match.group())    # 'Catch'
print(match.group(1))   # 'ch'

# findall() — returns all matches
pattern = re.compile(r'\d{3}-\d{3}-\d{4}')  # no groups
result = pattern.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(result)    # ['415-555-9999', '212-555-0000']

pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')  # with groups
result = pattern.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(result)    # [('415', '555', '9999'), ('212', '555', '0000')]
# findall with groups → list of TUPLES, not list of strings

# Character classes
vowel_pattern = re.compile(r'[aeiouAEIOU]')
result = vowel_pattern.findall('RoboCop eats BABY FOOD')

consonant_pattern = re.compile(r'[^aeiouAEIOU]')  # ^ inside [] = NOT
result = consonant_pattern.findall('RoboCop eats BABY FOOD')

# Shorthand classes
pattern = re.compile(r'\d+\s\w+')
result = pattern.findall('12 drummers, 11 pipers, 10 lords')

# Dot — matches any character EXCEPT newline
at_re = re.compile(r'.at')
result = at_re.findall('The cat in the hat sat on the flat mat.')
print(result)    # ['cat', 'hat', 'sat', 'lat', 'mat'] — 'flat' gives 'lat'

# ? optional, * zero or more, + one or more
pattern = re.compile(r'(\d{3}-)?\d{3}-\d{4}')
print(pattern.search('415-555-4242').group())   # area code present
print(pattern.search('555-4242').group())         # area code absent — both work

# {n,m} specific repetition
haRegex = re.compile(r'(Ha){3}')
print(haRegex.search('HaHaHa').group())    # 'HaHaHa' ✅
print(haRegex.search('Haha') == None)       # True — case sensitive, only 1 'Ha'

# Greedy vs non-greedy
greedy_pattern = re.compile(r'(Ha){3,5}')
print(greedy_pattern.search('HaHaHaHaHa').group())   # 'HaHaHaHaHa' — grabs max (5)

lazy_pattern = re.compile(r'(Ha){3,5}?')
print(lazy_pattern.search('HaHaHaHaHa').group())     # 'HaHaHa' — grabs min (3)

# .* vs .*? (greedy vs non-greedy with dot)
greedy_re = re.compile(r'<.*>')
print(greedy_re.search('<To serve man> for dinner.>').group())
# '<To serve man> for dinner.>' — grabs as much as possible

lazy_re = re.compile(r'<.*?>')
print(lazy_re.search('<To serve man> for dinner.>').group())
# '<To serve man>' — stops at first > found

# re.DOTALL — make . match newlines too
newline_re = re.compile('.*', re.DOTALL)
result = newline_re.search('Serve the public trust.\nProtect the innocent.').group()

# Anchors
begins_with_hello = re.compile(r'^Hello')
print(begins_with_hello.search('Hello, world!'))          # match
print(begins_with_hello.search('He said "Hello."') == None)  # True — ^ anchors to start

ends_with_number = re.compile(r'\d$')
print(ends_with_number.search('Your number is 42'))         # match
print(ends_with_number.search('Your number is forty two.') == None)  # True

# Word boundaries
pattern = re.compile(r'\bcat.*?\b')
result = pattern.findall('The cat found a catapult')
# \b = word boundary — matches 'cat ' but not 'cat' inside 'catapult'

# re.IGNORECASE
pattern = re.compile(r'robocop', re.I)
print(pattern.search('Robocop is part man, part machine, all cop.').group())
print(pattern.search('ROBOCOP protects the innocent').group())

# Substitution with sub()
agent_pattern = re.compile(r'Agent \w+')
print(agent_pattern.sub('CENSORED', 'Agent Alice contacted Agent Bob'))
# 'CENSORED contacted CENSORED'

agent_pattern = re.compile(r'Agent (\w)\w*')
print(agent_pattern.sub(r'\1****', 'Agent Alice contacted Agent Bob'))
# 'A**** contacted B****' — \1 refers back to first group in replacement

# Verbose mode — re.VERBOSE allows comments inside the pattern
pattern = re.compile(r'''(
    (\d{3}|\(\d{3}\))?  # Area code
    (\s|-|\.)?           # Separator
    \d{3}                # First three digits
    (\s|-|\.)            # Separator
    \d{4}                # Last four digits
    (\s*(ext|x|ext\.)\s*\d{2,5})?  # Extension
    )''', re.VERBOSE)

# Combining flags
some_regex = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)

# humre — human-readable regex (third-party module)
from humre import *
phone_regex = exactly(3, DIGIT) + '-' + exactly(3, DIGIT) + '-' + exactly(4, DIGIT)
pattern = re.compile(phone_regex)
```

**What happened:** Worked through the complete regex chapter — `re.compile()` + `search()` + `group()`, grouping with parentheses, `findall()` returning strings vs tuples depending on whether groups exist, character classes `[...]` and negation `[^...]`, shorthand classes (`\d`, `\w`, `\s`), the dot `.`, all quantifiers (`?`, `*`, `+`, `{n}`, `{n,m}`), greedy vs non-greedy (`{3,5}` vs `{3,5}?`), anchors (`^` and `$`), word boundaries (`\b`), `re.DOTALL`, `re.IGNORECASE`, `sub()` for substitution with back-references, and `re.VERBOSE` for commenting complex patterns. Also built `isPhoneNumber.py` (the manual approach showing why regex exists — 18 lines of manual character checks vs one regex line) and the big end-of-chapter project `project_003.py` (phone + email finder that reads from clipboard and writes back to clipboard).

Real issue caught: `begins_with_hello = re.compile(r'Hello')` (missing `^`) vs `re.compile(r'^Hello')` — without `^`, pattern matches `Hello` anywhere in the string, returning a Match object, not `None`. `== None` then returns `False` instead of `True`. One character difference, completely different behavior — always check anchors first when a regex returns unexpected results.

**Learned (vs C#):** `re.compile()` + `.search()` + `.group()` is Python's equivalent of C#'s `Regex.Match()` — conceptually the same, different syntax. `findall()` has no direct C# equivalent; it returns either a list of strings (no groups) or a list of tuples (with groups) — this switch in return type based on whether groups exist is a genuine gotcha with no C# parallel to anchor onto. Greedy vs non-greedy matching (`{3,5}` vs `{3,5}?`) — the `?` after a quantifier makes it lazy/non-greedy, grabbing as few characters as possible; without it, Python grabs as many as possible (greedy default). `re.VERBOSE` makes complex regex maintainable — lets you spread a pattern across multiple lines with `#` comments, same readability benefit as well-commented code. `re.IGNORECASE | re.DOTALL | re.VERBOSE` — combining flags with `|` (bitwise OR) is the standard pattern for passing multiple options. `sub()` with a back-reference (`r'\1****'`) in the replacement string — `\1` refers to the first captured group in the match, letting you partially preserve what you matched while replacing the rest.

---

## Date: 06/22/2026

**Topic:** Project — Phone & Email Address Finder (project_003.py, end-of-ch.9 project)

**Code:**

```python
import pyperclip, re

# Phone number regex — handles multiple formats:
# 415-555-4242, (415) 555-4242, 415.555.4242, with optional extension
phone_re = re.compile(r'''(
    (\d{3}|\(\d{3}\))?  # Area code (optional, plain or parenthesized)
    (\s|-|\.)?           # Separator (optional)
    (\d{3})              # First three digits
    (\s|-|\.)            # Separator (required here)
    (\d{4})              # Last four digits
    (\s*(ext|x|ext\.)\s*(\d{2,5}))?  # Extension (optional)
    )''', re.VERBOSE)

# Email address regex
email_re = re.compile(r'''(
    [a-zA-Z0-9._%+-]+    # Username
    @                     # @ symbol
    [a-zA-Z0-9.-]+        # Domain name
    (\.[a-zA-Z]{2,4})     # Top-level domain (.com, .org, .io etc.)
    )''', re.VERBOSE)

# Read clipboard, search for matches
text = str(pyperclip.paste())
matches = []

for groups in phone_re.findall(text):
    phone_num = '-'.join([groups[1], groups[3], groups[5]])
    if groups[6] != '':
        phone_num += ' x' + groups[6]
    matches.append(phone_num)

for groups in email_re.findall(text):
    matches.append(groups[0])

# Copy results back to clipboard or report no matches
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard')
    print('\n'.join(matches))
else:
    print('No phone number or email address found')
```

**What happened:** This project combines everything from ch. 9 into one real, usable tool — copy any block of text (a webpage, email, document) to the clipboard, run the script, and it finds every phone number and email address and copies them back to the clipboard, ready to paste. Used `re.VERBOSE` to make the complex phone regex readable with inline comments. The phone regex handles multiple formats by making the area code and separators optional (`?`). Used `findall()` which returns tuples (since groups exist), then indexed into specific tuple positions to reconstruct a standardized `NNN-NNN-NNNN` format regardless of what format the original was in.

**Learned:** `re.VERBOSE` is genuinely worth using for any regex longer than ~10 characters — the inline comments make what would be an unreadable symbol string into something you can actually maintain and explain. The `isPhoneNumber.py` manual approach (18 lines, checks each character position individually) vs the one-line regex approach is a direct demonstration of WHY regex exists — the comparison makes the value obvious rather than abstract. Indexing specific tuple positions from `findall()` (`groups[1]`, `groups[3]`, `groups[5]`) to reconstruct a standardized output format is a common real-world pattern: match flexibly, output consistently.

**Code:**

**What happened:**

**Learned (vs C#):**

---

## Date: 06/24/2026

**Topic:** Reading and Writing Files (ch. 10)

**Code:**

```python
from pathlib import Path
import os, time, shelve

# Path basics — joining paths
Path('spam', 'bacon', 'eggs')              # join with comma
Path('spam') / 'bacon' / 'eggs'           # join with / operator
Path('spam') / Path('bacon/eggs')          # mix of styles — all equivalent

# 'spam' / 'bacon' → TypeError — must have a Path object on the LEFT side of /

# Current working directory and home
print(Path.cwd())     # where Python is currently running from
print(Path.home())    # C:\Users\moxey

# Create directories
Path(r'C:\Users\moxey\Desktop\newfolder').mkdir()   # creates one folder
os.makedirs(r'C:\path\to\deep\folder')               # creates all missing parent folders too

# Absolute vs relative paths
Path.cwd().is_absolute()                   # True
Path('spam/bacon/eggs').is_absolute()      # False
Path('my/relative/path').absolute()        # converts to absolute using cwd

# Parts of a filepath
p = Path('C:/Users/Al/spam.txt')
print(p.anchor)     # 'C:\\'
print(p.parent)     # C:/Users/Al
print(p.name)       # 'spam.txt'
print(p.stem)       # 'spam'
print(p.suffix)     # '.txt'
print(p.drive)      # 'C:'
print(p.parts)      # ('C:\\', 'Users', 'Al', 'spam.txt')
print(p.parts[0:2]) # ('C:\\', 'Users')

# Parent directories
print(Path.cwd().parents[0])   # one level up
print(Path.cwd().parents[1])   # two levels up

# File size and timestamps
calc_file = Path('C:/Windows/System32/calc.exe')
print(calc_file.stat().st_size)    # size in bytes
print(calc_file.stat().st_mtime)   # last modified (Unix timestamp)
print(time.asctime(time.localtime(calc_file.stat().st_mtime)))  # human readable

# Glob — find files matching a pattern
p = Path('C:/Users/moxey/Desktop')
for name in p.glob('*'):      # * = all files/folders
    print(name)
for name in p.glob('*.py'):   # only .py files
    print(name)
for name in p.glob('**/*.py'): # ** = recursive search into subfolders
    print(name)

# Checking path validity
print(Path('C:/Windows').exists())          # True
print(Path('C:/Windows').is_dir())          # True
print(Path('C:/Windows/calc.exe').is_file()) # False (wrong location)
print(Path('C:/NoSuchFolder').exists())      # False

# Simple file read/write with pathlib
p = Path('spam.txt')
p.write_text('Hello, world!')    # writes and closes automatically
print(p.read_text())              # reads and closes automatically

# Traditional open() — read mode
hello_file = open(r'C:\Users\moxey\Desktop\DevSecOps_Roadmap\Stage_002\Ch_010\hello.txt', encoding='UTF-8')
hello_content = hello_file.read()    # reads entire file as one string
print(hello_content)
hello_file.close()                    # must close manually

# readlines() — reads into a list, one line per item
sonnet_file = open(r'C:\Users\moxey\Desktop\DevSecOps_Roadmap\Stage_002\Ch_010\sonnet29.txt')
lines = sonnet_file.readlines()
print(lines)     # ['When, in disgrace...\n', 'With Fortune...\n', ...]
sonnet_file.close()

# Write mode ('w') — creates or OVERWRITES the file
bacon_file = open('bacon.txt', 'w', encoding='UTF-8')
bacon_file.write('Hello, world\n')
bacon_file.close()

# Append mode ('a') — adds to end of file without overwriting
bacon_file = open('bacon.txt', 'a', encoding='UTF-8')
bacon_file.write('Bacon is not a vegetable')
bacon_file.close()

# with statement — automatically closes file even if an error occurs
with open('data.txt', 'w', encoding='UTF-8') as file_obj:
    file_obj.write('This was written with a with statement')
with open('data.txt', encoding='UTF-8') as file_obj:
    content = file_obj.read()
print(content)

# shelve — saves Python objects to a binary file (like a persistent dict)
shelf_file = shelve.open('mydata')
shelf_file['cats'] = ['Zophie', 'Pooka', 'Simon']   # store a list
shelf_file.close()

shelf_file = shelve.open('mydata')
print(shelf_file['cats'])           # ['Zophie', 'Pooka', 'Simon']
print(list(shelf_file.keys()))
print(list(shelf_file.values()))
shelf_file.close()
```

**What happened:** Worked through the full file I/O chapter — `pathlib` for path manipulation (joining, checking existence, glob), `open()` for reading/writing, three file modes (`'r'` read, `'w'` write/overwrite, `'a'` append), `.read()` vs `.readlines()`, the `with` statement for automatic file closing, and `shelve` for persisting Python objects across script runs. Hit two real errors: (1) `PermissionError` — tried to `open()` a folder path (`Ch_010`) instead of a file — fixed by adding a filename at the end. (2) `FileNotFoundError` — tried to open `hello.txt` before it existed — fixed by creating it with `Path.write_text()` first.

**Learned (vs C#):** `Path` / operator for joining paths is unique to Python — no equivalent in C# (you'd use `Path.Combine()`). `pathlib`'s `.write_text()` and `.read_text()` are the simplest way to read/write a file in one line — much cleaner than C#'s `File.WriteAllText()` / `File.ReadAllText()` though conceptually the same. Three file modes (`'r'`, `'w'`, `'a'`) match C#'s `FileMode.Open`, `FileMode.Create`, `FileMode.Append` — same concepts, different syntax. The `with` statement for file handling is Python's equivalent of C#'s `using` statement — both automatically dispose/close the resource when the block exits, even if an exception occurs. `open()` without `with` requires a manual `.close()` call — forgetting it can cause file lock issues or data loss, same risk as forgetting `.Dispose()` in C# without `using`. `shelve` has no clean C# equivalent — it's like a persistent dictionary backed by a binary file, useful for caching Python objects between script runs without needing a full database.

---

## Date: 06/24/2026

**Topic:** Project — Random Quiz Generator (randomQuizGenerator.py, end-of-ch.10 project)

**Code:**

```python
import random

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', ...}  # 50 states

for quiz_num in range(35):
    # Open both files at once — quiz sheet and answer key
    quiz_file = open(f'capitalsquiz{quiz_num + 1}.txt', 'w', encoding='UTF-8')
    answer_file = open(f'capitalsquiz_answers{quiz_num + 1}.txt', 'w', encoding='UTF-8')

    # Write header
    quiz_file.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quiz_file.write((' ' * 20) + f'State Capitals Quiz (Form{quiz_num + 1})\n\n')

    # Shuffle states so each quiz has different question order
    states = list(capitals.keys())
    random.shuffle(states)

    for num in range(50):
        correct_answer = capitals[states[num]]

        # Build 3 wrong answers from remaining capitals
        wrong_answers = list(capitals.values())
        del wrong_answers[wrong_answers.index(correct_answer)]
        wrong_answers = random.sample(wrong_answers, 3)

        # Combine and shuffle all 4 answer options
        answer_options = wrong_answers + [correct_answer]
        random.shuffle(answer_options)

        # Write question + 4 options (A/B/C/D)
        quiz_file.write(f'{num + 1}. Capital of {states[num]}:\n')
        for i in range(4):
            quiz_file.write(f"    {'ABCD'[i]}. {answer_options[i]}\n")
        quiz_file.write('\n')

        # Write answer key — find which letter the correct answer landed on
        answer_file.write(f"{num + 1}.{'ABCD'[answer_options.index(correct_answer)]}\n")

    quiz_file.close()
    answer_file.close()
```

**What happened:** Generates 35 different quiz files plus their answer keys, all with shuffled question and answer order so no two quizzes are identical. One real bug spotted in the uploaded version: the question line was written twice (`quiz_file.write(f'{num + 1}. Capital of {states[num]}:\n')` appeared twice in a row) — a copy-paste duplication that would print every question heading twice on the actual quiz file.

**Learned:** Opening multiple files simultaneously (quiz file + answer key file) and writing to both inside the same loop is a real pattern — each file gets its corresponding content in lock-step as the loop runs. `'ABCD'[i]` is a clean Python idiom for converting a 0-3 index into a letter label — indexing directly into a string rather than needing a lookup dict or if/elif chain. `answer_options.index(correct_answer)` finds where the correct answer ended up after shuffling, so the answer key letter is always accurate regardless of what random order the options landed in — the logic is correct even without knowing in advance where the correct answer will be placed.

---

## Date: 06/28/2026

**Topic:** Designing and Deploying Command Line Programs (ch. 12) — directly feeds the Stage 2 build (labcheck CLI tool)

**Code:**

```python
# Color text with bext
import bext
bext.fg('red')
print('This text is red')
bext.bg('blue')
print('Red text on a blue background')
bext.fg('reset')
bext.bg('reset')
print('The text is normal again.')

# Sound notification with playsound3
import playsound3
from pathlib import Path
path = Path('C:/Users/moxey/Desktop/DevSecOps_Roadmap/Stage_002/Ch_012/hello.mp3')
playsound3.playsound(path)   # must call playsound3.playsound(), not playsound3() directly

# ccwd.py — copy current working directory to clipboard
import pyperclip, os, sys
if len(sys.argv) > 1:       # check if a path argument was passed
    os.chdir(sys.argv[1])   # change to that directory first
pyperclip.copy(os.getcwd()) # copy the current dir to clipboard

# cliprec.py — clipboard recorder
import pyperclip, time
print('Recording clipboard... (Ctrl-C to stop)')
previous_content = ''
try:
    while True:
        content = pyperclip.paste()
        if content != previous_content:
            print(content)
            previous_content = content
        time.sleep(0.01)
except KeyboardInterrupt:
    pass

# snowstorm.py — terminal animation using command line args
import os, random, time, sys
TOP    = chr(9600)   # ▀
BOTTOM = chr(9604)   # ▄
FULL   = chr(9608)   # █

DENSITY = 4           # default snow density
if len(sys.argv) > 1:
    DENSITY = int(sys.argv[1])   # override with CLI arg

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    clear()
    for y in range(20):
        for x in range(40):
            if random.randint(0, 99) < DENSITY:
                print(random.choice([TOP, BOTTOM]), end='')
            else:
                print('', end='')
        print()
    print(FULL * 40 + '\n' + FULL * 40)
    print('(Ctrl-C to stop.)')
    time.sleep(0.2)
```

**What happened:** Worked through the chapter covering: terminal color/styling with `bext`, sound notifications with `playsound3`, reading command line arguments via `sys.argv`, the `ccwd` deployment pattern (Python script + `.bat` file + Scripts folder in PATH = runnable from anywhere in the terminal), and the clipboard recorder. Built four programs: `CLIPrograms.py` (bext colors + playsound3), `ccwd.py` (copy working directory to clipboard with optional path argument), `cliprec.py` (monitors clipboard for changes), `snowstorm.py` (terminal animation with configurable density via CLI argument).

Real issues hit and fixed:

- `playsound3('path')` → `TypeError: module is not callable` — fixed by calling `playsound3.playsound(path)` (the function inside the module, not the module itself)
- `(sys.argv) > 1` → comparing a list to a number — fixed to `len(sys.argv) > 1`
- `bext` not in conda channels → installed via `pip install bext` instead
- `pip install bext` downgraded colorama (0.4.6 → 0.4.5) which broke Spyder/Sphinx → fixed with `pip install --upgrade colorama`
- `ccwd` not recognized in terminal → Scripts folder not in PATH yet → added `C:\Users\moxey\Scripts` to User environment variables
- pyperclip not found when running via `.bat` → had to install it specifically into the Scripts `.venv` (separate from conda environment)

**Learned (vs C#):** `sys.argv` is Python's equivalent of C#'s `string[] args` in `Main(string[] args)` — same concept (command line arguments as a list/array), different syntax. `sys.argv[0]` is always the script name itself, so `sys.argv[1]` is the first actual argument — that's why the check is `len(sys.argv) > 1` not `> 0`. The deployment pattern (`.py` script + `.bat` launcher + Scripts folder in PATH) is the Windows equivalent of installing a CLI tool globally — the `.bat` activates the right virtual environment and passes arguments through with `%*`. This directly maps to what the labcheck tool needs to do: run from anywhere in the terminal with `labcheck --host 192.168.0.52` rather than `python C:\full\path\to\labcheck.py --host ...`. Dependency conflicts between packages (bext downgrading colorama breaking Spyder) is a real production problem — this is exactly what SCA tools like Dependabot catch in Stage 6 of the roadmap.

---

## Date: 06/28/2026

**Topic:** argparse deep dive (Python docs tutorial — supplements ch. 12)

**Code:**

```python
import argparse

# 1. Positional arguments
parser = argparse.ArgumentParser()
parser.add_argument("square", help="display a square of a given number", type=int)
args = parser.parse_args()
print(args.square**2)
# python prog.py 4 → 16

# 2. Optional arguments with store_true
parser.add_argument("-v", "--verbosity", help="increase output verbosity", action='store_true')
# store_true: flag is True if present, False if absent — no value needed after -v

# 3. Combining positional + optional with action="count"
parser.add_argument("square", type=int)
parser.add_argument("-v", "--verbosity", action="count", default=0)
# default=0 critical — without it verbosity is None, and None >= 2 raises TypeError

# 4. nargs — number of values an argument consumes
parser.add_argument('-n', nargs='+')   # one or more values (greedy)
parser.add_argument('args', nargs='*') # zero or more values (positional)

# -- separator: forces everything after it to be treated as positional, not a flag
parser.parse_args(['--', '-f'])        # -f treated as value, not unknown flag
parser.parse_args(['-n', '1', '--', '2', '3'])  # n gets ['1'], args gets ['2','3']

# 5. Mutually exclusive group
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true")
# python prog.py 4 2 -vq → error: not allowed with argument

# 6. Custom type converters with lambda
parser = argparse.ArgumentParser(prefix_chars="-+")
parser.add_argument('-a', metavar='<value>', action="append",
                    type=lambda x: ('-', x))
parser.add_argument('+a', metavar='<value>', action="append",
                    type=lambda x: ('+', x))
# lambda x: ('-', x) converts each value into a tuple (sign, value)
# action="append" builds a list of tuples as -a/+a flags are repeated
```

**What happened:** Worked through the full argparse docs tutorial — positional arguments, optional arguments, `action='store_true'` vs `action='count'`, combining positional and optional, `nargs` for multi-value arguments, the `--` separator for ambiguous arguments, mutually exclusive groups, and custom type converters with lambda. Built one `prog.py` file with all examples staged as commented-out sections, progressively building up complexity.

Real issue documented: `action="count"` without `default=0` sets verbosity to `None` when the flag isn't passed → `None >= 2` raises `TypeError: '>=' not supported between instances of 'NoneType' and 'int'`. Fixed by always setting `default=0` on count arguments used in numeric comparisons.

**Learned (vs C#):** `action='store_true'` is Python's equivalent of a boolean flag — no value needed after the flag, just its presence/absence sets True/False (similar to nullable bool in C# but cleaner). `action='count'` has no direct C# CLI equivalent — it counts repetitions of the same flag (`-vvv` = 3), used for verbosity levels. `nargs='+'` (greedy, one or more) and `nargs='*'` (zero or more) map to `params` arrays in C# but with more explicit control. The `--` separator is a Unix convention with no C# equivalent — tells the parser to stop treating arguments as flags and treat everything after as literal values. `mutually_exclusive_group` handles the "either/or" constraint automatically with a built-in error message — in C# you'd write that validation logic yourself. `lambda` as `type=` converter is a concise way to transform argument values on parse — same as a one-line Func<string, T> in C#.

---

## Date: 07/01/2026

**Topic:** CSV, JSON, and XML Files (ch. 18) — important, used everywhere in cloud/AWS work

**Code:**

```python
import csv, json, xml.etree.ElementTree as ET

# ── CSV READING ──────────────────────────────────────────────
# Basic csv.reader
example_file = open('example3.csv')
example_reader = csv.reader(example_file)
example_data = list(example_reader)
print(example_data[0][0])   # row 0, col 0
print(example_data[1][1])   # row 1, col 1
example_file.close()

# Iterating with line_num
for row in example_reader:
    print('Row #' + str(example_reader.line_num) + ' ' + str(row))

# ── CSV WRITING ──────────────────────────────────────────────
output_file = open('output.csv', 'w', newline='')  # newline='' prevents double newlines on Windows
output_writer = csv.writer(output_file)
output_writer.writerow(['spam', 'eggs', 'bacon', 'ham'])
output_writer.writerow(['Hello, world!', 'eggs', 'bacon', 'ham'])
output_writer.writerow([1, 2, 3.141592, 4])
output_file.close()

# Tab-separated (TSV) with custom delimiter and line terminator
output_file = open('output.tsv', 'w', newline='')
output_writer = csv.writer(output_file, delimiter='\t', lineterminator='\n\n')
output_writer.writerow(['spam', 'eggs', 'bacon', 'ham'])
output_file.close()

# ── DICTREADER / DICTWRITER ──────────────────────────────────
# DictReader — uses header row as keys
example_file = open('exampleWithHeader3.csv')
example_dict_reader = csv.DictReader(example_file)
for row in example_dict_reader:
    print(row['Timestamp'], row['Fruit'], row['Quantity'])
example_file.close()

# DictReader — supply your own column names (no header in file)
example_file = open('example3.csv')
example_dict_reader = csv.DictReader(example_file, ['time', 'name', 'amount'])
for row in example_dict_reader:
    print(row['time'], row['name'], row['amount'])
example_file.close()

# DictWriter — write dicts as rows (order doesn't matter)
output_file = open('output2.csv', 'w', newline='')
output_dict_writer = csv.DictWriter(output_file, ['Name', 'Pet', 'Phone'])
output_dict_writer.writeheader()
output_dict_writer.writerow({'Name': 'Alice', 'Pet': 'cat', 'Phone': '555-1234'})
output_dict_writer.writerow({'Name': 'Bob', 'Phone': '555-9999'})  # missing Pet → blank
output_dict_writer.writerow({'Phone': '555-5555', 'Name': 'Carol', 'Pet': 'dog'})
output_file.close()

# ── JSON ─────────────────────────────────────────────────────
# json.loads — parse JSON string → Python dict
json_string = '{"name": "Alice", "age": 30, "car": null, "programmer": true}'
python_data = json.loads(json_string)
print(python_data)              # {'name': 'Alice', 'age': 30, 'car': None, 'programmer': True}
print(type(python_data))        # <class 'dict'>

# json.dumps — Python dict → JSON string
json_string = json.dumps(python_data, indent=2)
print(json_string)

# ── XML ──────────────────────────────────────────────────────
# Parsing XML with ElementTree
xml_string = """<person>
<name>Alice Doe</name>
<age>30</age>
<address>
    <street>100 Larkin St.</street>
    <city>San Francisco</city>
</address>
</person>"""

root = ET.fromstring(xml_string)
print(root.tag)         # 'person'
print(root[0].tag)      # 'name'
print(root[0].text)     # 'Alice Doe'

# Iterate immediate children
for elem in root:
    print(elem.tag, '--', elem.text)

# Iterate ALL descendants recursively
for elem in root.iter():
    print(elem.tag, '--', elem.text)

# Find specific tags
for elem in root.iter('number'):
    print(elem.tag, '--', elem.text)

# Writing XML with ElementTree
person = ET.Element('person')
name = ET.SubElement(person, 'name')
name.text = 'Alice Doe'
age = ET.SubElement(person, 'age')
age.text = '30'
result = ET.tostring(person, encoding='UTF-8')
print(result)

# xmltodict — parse XML directly to a Python dict (third party)
import xmltodict
python_data = xmltodict.parse(xml_string)
print(python_data)   # OrderedDict — same structure as JSON equivalent
```

**What happened:** Worked through the full ch. 18 — CSV reading with `csv.reader` and `DictReader`, writing with `csv.writer` and `DictWriter`, custom delimiters (TSV), JSON parsing with `json.loads`/`json.dumps`, XML parsing with `xml.etree.ElementTree`, and `xmltodict` for converting XML directly to Python dicts. Built two programs: `CSV_JSON_XML_Files.py` (all chapter examples) and `removeCsvHeader.py` (end-of-chapter project — loops through all CSV files in a directory, strips the header row, writes the result to a `headerRemoved/` subfolder).


**Learned (vs C#):** `json.loads()` / `json.dumps()` map directly to C#'s `JsonSerializer.Deserialize<T>()` / `JsonSerializer.Serialize()` — same concept (JSON string ↔ object), just dynamic typing means no generic type parameter needed in Python. JSON `null` → Python `None`, JSON `true`/`false` → Python `True`/`False` — the casing difference is a real gotcha when switching between languages. `DictReader` is more useful than plain `csv.reader` for real-world CSV files that have headers — accessing `row['Timestamp']` is much cleaner than `row[0]`. `DictWriter` handles column ordering automatically — you define the field names once in the constructor and it doesn't matter what order you pass keys in the dict, which is genuinely cleaner than managing column indices manually. XML is significantly more verbose than JSON for the same data — `json.loads()` one-lines what takes multiple `ET.fromstring()` + indexing calls to navigate. `newline=''` on `open()` for CSV writing prevents Windows from adding double newlines — Python's text mode adds `\r\n` and csv.writer also adds `\r\n`, causing blank lines between every row without it.

---

## Date:

**Topic:** Keeping Time, Scheduling Tasks, and Launching Programs (ch. 19)

**Code:**

**What happened:**

**Learned:**

---

## Date:

**Topic:** Paramiko — SSH from Python (Stage 2 build target)

**Code:**

**What happened:**

**Learned:**

---

## Date:

**Topic:** Putting it together — the SSH lab-check tool (Stage 2 build)

**Final script:**

**What happened:**

**Learned:**

---