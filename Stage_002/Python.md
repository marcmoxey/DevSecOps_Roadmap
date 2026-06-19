# Python — Journal (Stage 2)

Resource: Automate the Boring Stuff with Python (3rd edition) — https://automatetheboringstuff.com/

Coming from C#/ASP.NET  most of chapters 1-10 will be new SYNTAX for concepts already known, not new concepts. For each entry, the useful question is: "Is this new, or is this just Python's way of writing something I already know from C#?" Slow down only where the answer is genuinely new.



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

## Date:

**Topic:** Strings and Text Editing (ch. 8)

**Code:**

**What happened:**

**Learned (vs C#):**

---

## Date:

**Topic:** Text Pattern Matching with Regular Expressions (ch. 9) — pair with TryHackMe Regex room

**Code:**

**What happened:**

**Learned:**

---

## Date:

**Topic:** Reading and Writing Files (ch. 10)

**Code:**

**What happened:**

**Learned (vs C#):**

---

## Date:

**Topic:** Designing and Deploying Command Line Programs (ch. 12) — directly feeds the Stage 2 build (labcheck CLI tool)

**Code:**

**What happened:**

**Learned:**

---

## Date:

**Topic:** CSV, JSON, and XML Files (ch. 18) — important, used everywhere in cloud/AWS work

**Code:**

**What happened:**

**Learned:**

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

## Notes / things to revisit later

- Chapters skipped on purpose (office/desktop automation, not infra-relevant): 11 (Organizing Files), 13 (Web Scraping — optional skim), 14 (Excel), 15 (Google Sheets), 16 (SQLite — optional later for local DB work), 17 (PDF/Word), 20 (Email/Texts — optional later for alerting), 21-24 (graphs/images/keyboard-mouse/speech)