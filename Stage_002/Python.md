# Python — Journal (Stage 2)

Resource: Automate the Boring Stuff with Python (3rd edition) — [https://automatetheboringstuff.com/](https://automatetheboringstuff.com/)

Coming from C#/ASP.NET most of chapters 1-10 will be new SYNTAX for concepts already known, not new concepts. For each entry, the useful question is: "Is this new, or is this just Python's way of writing something I already know from C#?" Slow down only where the answer is genuinely new.



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

python

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

**Learned (vs C#):** No semicolons, no curly braces  indentation IS the block structure. `42 == '42'` is `False` (no implicit string/number coercion for `==`), but `42 == 42.0` is `True`  Python compares int and float **by value**, not by type, which is different from languages that might treat them as needing explicit comparison/casting. `int(1.99)` **truncates** toward zero rather than rounding `int(1.99)` is `1`, not `2`; use `round()` if rounding is actually wanted. String `+` concatenates, but only with other strings  mixing types (`'Alice' + 5`) throws `TypeError` and requires an explicit `str()` conversion, similar to needing `.ToString()` in C# but Python is stricter about refusing the silent coercion C# sometimes allows.

---

## Date: 06/17/2026

**Topic:** if-else and Flow Control (ch. 2)

**Code:**

python

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

**Learned (vs C#):** `and`/`or`/`not` are spelled-out words in Python instead of `&&`/`||`/`!` in C# takes a moment to retrain muscle memory. An `if`/`elif` chain with **no `else`** is completely valid — if no condition matches, the program just continues with no output and no error, which is different from expecting some kind of fallback to always fire. This came back to bite a separate script (`dishonestcapacity.py`  see entry below) where a missing `else` left a variable undefined later in the script, causing a crash several lines down rather than at the `if` itself — the error shows up far from its actual cause.

---

## Date: 06/17/2026

**Topic:** ⚠️ Real bug  missing else branch causes NameError (dishonestcapacity.py)

**Code:**

python

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

**What happened:** Problem: if the user types anything other than exactly `TB`, `tb`, `GB`, or `gb` (a typo, different case, anything else), **neither** branch of the `if`/`elif` runs, so `discrepancy` is never created. The crash (`NameError: name 'discrepancy' is not defined`) happens several lines later, at the point `discrepancy` is finally used  not at the `if` statement itself, which makes it confusing to trace back.

Fix: add an `else` to handle the "none of the above" case:

python

```python
else:
    print('Invalid unit entered.')
    import sys
    sys.exit()
```

**Learned:** General rule worth remembering: **any `if`/`elif` chain that assigns a variable should have an `else`** that handles the unexpected case  otherwise there's a real risk of a variable that simply doesn't exist later in the script. The error message points to where the missing variable is _used_, not where it _should have been created_  so when debugging a `NameError`, the real fix is often several lines above where the error actually appears.

---

## Date: 06/17/2026

**Topic:** Loops (ch. 3)

**Code:**

python

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

**Learned (vs C#):** `range(start, end, step)`  the `end` value is always **exclusive** (never reached), which trips people up constantly; `range(5, -1, -1)` has to go one PAST the actual target (`0`) to include `0`, since the step is negative and `end` is exclusive. **Loop variables are NOT block-scoped** to the loop in Python  `guess` and `guesses_taken` from inside a `for` loop are still readable after the loop ends, which is different from C#'s `for` loop variable being scoped only to the loop body. `continue` skips to the next iteration; `break` exits the loop completely  same concepts as C#, just confirmed they work identically.

---

## Date: 06/17/2026

**Topic:** Functions (ch. 4)

**Code:**

python

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

**Learned (vs C#):** A function with no explicit `return` statement doesn't error or do nothing it implicitly returns `None`, Python's "no value" placeholder (similar in spirit to C#'s `void`, but `None` is an actual value you can check against, e.g. `print(spam(0))` after the `except` block prints `None` since there's no `return` inside it). **Local vs global scope is stricter than expected**: a variable assigned inside a function is local by default, even if a global variable with the exact same name exists they don't interact at all unless the `global` keyword is explicitly used inside the function to say "modify the outer one, don't create a local one." This is different from just "scoping rules" in C#  it's specifically that _assignment_ inside a function defaults to creating a new local, full stop, unless told otherwise. Reading a global from inside a function works fine without any keyword only _writing_ to it needs `global`. `try`/`except` matches C#'s `try`/`catch` conceptually, but the specific exception type (`ZeroDivisionError`) is caught by name, similar to catching a specific exception class in C#.

---

## Date: 06/17/2026

**Topic:** ⚠️ Real bug nested loop indentation (spike.py)

**Code:**

python

```python
# BUGGY — second for loop is nested INSIDE the first
for i in range(1, 9):
    print('-' * (i * 1))
    time.sleep(0.1)

    for i in range(7, 1, -1):      # indented one level too deep
        print('-' * (i * 1))
        time.sleep(0.1)
```

**What happened:** Problem: the comment said "Draw lines with decreasing length" as if it were a separate step after the increasing-length loop  but the second `for` loop is indented to be INSIDE the first loop's body, not after it. This means for every single iteration of the increasing loop (8 times), the entire decreasing loop runs all over again inside it  producing a tangled, repeated pattern instead of "increase once, then decrease once."

Fix: dedent the second `for` loop so it's a sibling of the first, not a child:

python

```python
for i in range(1, 9):
    print('-' * (i * 1))
    time.sleep(0.1)

for i in range(7, 1, -1):          # now at the same level as the first loop
    print('-' * (i * 1))
    time.sleep(0.1)
```

**Learned:** Same root cause as the `rpsGame.py` indentation bug from Chapter 3 indentation level determines what's nested inside what, and Python won't complain about it being "wrong" if it's still syntactically valid, even if it doesn't match the intended logic. Two blocks of code that are meant to run **sequentially** (one after another) need to be at the **same** indentation level; if one is indented further than the other, it becomes nested inside it instead. Worth a habit: whenever pairing two loops or blocks that are meant to be parallel steps, double-check they line up at the exact same indentation.

## Date:

**Topic:** Debugging (ch. 5)  

**Code:**

**What happened:**

**Learned:**

---

## Date:

**Topic:** Lists (ch. 6)

**Code:**

**What happened:**

**Learned (vs C#):**

---

## Date:

**Topic:** Dictionaries and Structuring Data (ch. 7)

**Code:**

**What happened:**

**Learned (vs C#):**

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