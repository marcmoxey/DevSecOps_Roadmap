```
## Date:
**Topic:**

**Commands:**

**What happened:**
Problem: exact error message (if any)
Fix: what actually solved it

**Learned:**
one sentence takeaway
```

wsl -d Ubuntu
---
 
## Date: 06/15/2026

**Topic:** Variables

**Commands:**

bash

```bash
variable_name="value"      # assign — NO SPACES around =
echo "$variable_name"       # use a variable

bash -x ./script.sh         # run a script with debug output
set -x                       # turn on debug output mid-script
set +x                        # turn off debug output
```

**What happened:** Learned how to create and assign variables, and how to debug a script by seeing each command as it executes.

`variable_name="value"` — declares and assigns a variable

`bash -x ./script.sh` — runs the whole script in debug mode, printing each command (prefixed with `+`) before it executes — useful for seeing exactly what a script is doing line by line.

`set -x` / `set +x` — turn debug mode on/off _from within_ a script, so only a specific section gets the verbose output instead of the whole script.


**Learned:** Variables make it easy to store data. `set -x`/`set +x` are useful for debugging a specific section of a longer script without drowning in debug output from the whole thing; `bash -x` is the blunt "show me everything" version for the whole script.

---

## Date: 06/15/2026

**Topic:** Parameters — user input with read

**Commands:**

bash

```bash
read variable_name             # wait for user input, store it
echo "$variable_name"           # use what they entered

read -p "Enter your name: " name   # show a prompt, then read
```

**What happened:** Learned how to get input from the user while a script is running, using `read`.

- `read variable_name` — pauses the script and waits for the user to type something, then stores whatever they typed into `variable_name`
- `read -p "prompt text" variable_name` — same thing, but displays a prompt message first so the user knows what to enter (without `-p`, the script just sits there waiting with no indication of what it's waiting for)

**Example:**

bash

```bash
read -p "Enter your name: " name
echo "Hello, $name"
```

**Learned:** `read <variable>` lets a script pause and accept input rather than only working with hardcoded values or arguments passed at launch — this is what makes a script _interactive_. The `-p` flag is effectively always worth using; without it the user has no idea the script is waiting for them to type something.

---

## Date: 06/15/2026

**Topic:** Arrays

**Commands:**

bash

```bash
array_name=('value1' 'value2' 'value3' 'value4')   # create an array
echo "${array_name[@]}"                             # print all elements
echo "${array_name[1]}"                             # print element at index 1
unset array_name[1]                                  # remove element at index 1
array_name[1]='new_value'                            # set/replace element at index 1
```

**What happened:** Learned how arrays work in bash — storing multiple values in one variable, accessed by index.

- An array is created by wrapping space-separated values in `()` — e.g. `transport=('car' 'train' 'bike' 'bus')`
- **Indexing starts at 0** — `car` is index 0, `train` is index 1, `bike` is index 2, `bus` is index 3
- `"${array_name[@]}"` — `@` means "all elements"; the `[]` specifies which index (or `@` for all)
- `"${array_name[1]}"` — prints just the element at index 1 (`train`)
- `unset array_name[1]` — removes that element entirely (the array now has a gap at index 1, rather than the remaining items shifting down)
- `array_name[1]='trainride'` — overwrites the element at index 1. Echoing the array afterward gives `car trainride bike bus`

**Learned:** Arrays are how bash stores a *list* in a single variable `array[@]‘(allelements)vs‘{array[@]}` (all elements) vs ` array[@]‘(allelements)vs‘{array[N]}` (one element by index) is the core distinction, same pattern as indexing in most languages but with bash's `${}` syntax wrapper. `unset` removes by index without renumbering the rest

---

## Date: 06/15/2026

**Topic:** If statements & comparisons

**Commands:**

bash

```bash
if [ "$count" -eq 10 ]; then
    echo "true"
else
    echo "false"
fi

# Comparing a script parameter ($1) to a fixed value
if [ "$1" = "guessme" ]; then
    echo "They are equal"
else
    echo "They are not equal"
fi

# File test operators
if [ -f "$1" ] && [ -w "$1" ]; then
    echo "hello" >> "$1"
else
    rm -f "$1"
    touch "$1"
    echo "hello" >> "$1"
fi
```

**What happened:** Learned the basic syntax of `if` statements, comparison operators, and file test operators.

**Syntax basics:**

- An `if` statement uses `[ ]` (single brackets) around the condition — bash requires a **space on both sides** of the brackets and of any operator inside them (`[ "$count" -eq 10 ]`, not `["$count"-eq 10]`)
- Every `if` must be closed with `fi`
- `then` follows the condition, `else` is optional, `fi` ends it

**Comparison operators (for numbers):**

|Operator|Meaning|
|---|---|
|`-eq`|equal to|
|`-ne`|not equal to|
|`-gt`|greater than|
|`-lt`|less than|
|`-ge`|greater than or equal to|

`-eq` and `=` can both check equality — `-eq` is for numeric comparison, `=` is more commonly used for string comparison.

**Example 1 — comparing a variable to a fixed number:** `count=10`, then `if [ "$count" -eq 10 ]` → true, since 10 equals 10.

**Example 2 — a guessing game using a script parameter ($1):**

bash

```bash
./example.sh guessme   →  "They are equal"
./example.sh hi        →  "They are not equal"
```

`$1` is the first argument passed to the script when run — comparing it with `=` checks if the input matches the expected string.

**File test operators:**

|Operator|Checks|
|---|---|
|`-f`|file exists|
|`-w`|file is writable|

Combined with `&&` (AND), `[ -f "$1" ] && [ -w "$1" ]` checks both conditions are true. If the file exists _and_ is writable, append "hello" to it. If either check fails (doesn't exist, or exists but isn't writable), delete it (if present) and create a fresh one, then write "hello" to it.

**Side project (from this module):** Extend the previous biography maker script — use `read` to ask for someone's age, then `if`/`else` to check if it's under 18 (print a "not eligible for work" message) or 18+ (use `read` again to ask for their job).

Topic: if/else syntax errors

Problem: syntax error near 'else' —
         missing `then` after the if condition, 
         and `else` had its own [ ] condition 
         (not valid — else takes no condition)

Fix: added `then` after `if [ ... ]`
     removed the condition from `else`

Learned: if/then/else/fi each have a specific 
         role — `then` marks the start of the 
         "if true" block, `else` is just "otherwise" 
         with no condition of its own. For a second 
         condition, use `elif [ condition ]; then` 
         instead.
Learned: The space requirements around `[ ]` and operators inside an `if` are strict and easy to get wrong silently — a missing space often gives a confusing syntax error rather than an obvious one. `$1` (and `$2`, `$3`, etc.) are how a script receives arguments from the command line — this is the actual "parameters" concept, distinct from `read` (which gets input _during_ execution rather than at launch). Combining `-f` and `-w` with `&&` is a pattern that will come up constantly — checking a precondition before acting, and having a fallback (create the file) if the precondition fails.
---
