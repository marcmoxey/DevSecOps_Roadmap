## Date: 06/15/2026

**Topic:** Putting it together — the disk-check script (Stage 1 build)

**Final script:**

bash

```bash
#!/bin/bash

threshold=80
logfile="$HOME/disk-check.log"

usage=$(df -h / | awk 'NR==2 {print $5}' | tr -d '%')

if [ "$usage" -gt "$threshold" ]; then
    echo "$(date): WARNING - Disk usage at ${usage}% (threshold: ${threshold}%)" >> "$logfile"
else
    echo "$(date): OK - Disk usage at ${usage}%" >> "$logfile"
fi
```

**Line-by-line — where each piece came from in this journal:**

| Line / piece                                              | What it does                                                                                                                   | Where I learned it                                                |
| --------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------- |
| `#!/bin/bash`                                             | Shebang — run this file with bash                                                                                              | "Missing slash" debugging session (`#!bin/bash` vs `#!/bin/bash`) |
| `threshold=0`                                             | Variable, no spaces around `=`                                                                                                 | Variables entry                                                   |
| `logfile="$HOME/disk-check.log"`                          | `$HOME` = built-in variable for home directory                                                                                 | Discussed when breaking down this script                          |
| `usage=$(df -h / \| awk 'NR==2 {print $5}' \| tr -d '%')` | `df` = disk usage table; `awk 'NR==2 {print $5}'` = line 2, column 5; `tr -d '%'` = strip `%`; `$(...)` = command substitution | Broken down separately — `awk`/`tr`/pipes entry                   |
| `if [ "$usage" -gt "$threshold" ]; then`                  | If statement, `-gt` = greater than, spacing rules around `[ ]`                                                                 | "If statements & comparisons" entry                               |
| `$(date)`                                                 | Command substitution again — same `$()` as the `usage=` line, different command                                                | Same as above                                                     |
| `${usage}%`                                               | `${}` makes the variable boundary explicit (`usage` vs `usage%`)                                                               | Discussed when breaking down this script                          |
| `>> "$logfile"`                                           | Append (not overwrite) to the log file                                                                                         | Very first journal entry — Shell Operators                        |
| `else` / `fi`                                             | `else` takes no condition; `fi` closes every `if`                                                                              | "If statements & comparisons" entry                               |

**The honest summary:** Every piece of this script is something I already debugged or had explained — `#!/bin/bash`, variables, `$HOME`, command substitution `$()`, the `df|awk|tr` pipeline, `if`/`-gt`/`fi`, `${}`, and `>>`. This script is a synthesis of the entire Stage 1 journal into one working tool.

---

**Resources for going forward — general pattern:**

```
man <command>     → official docs for any single 
                     command (df, awk, tr, date, test)

man bash          → the shell ITSELF — variables, 
                     $(), ${}, if/else syntax, 
                     redirects (>>)

man test          → [ ] is the `test` command — 
                     lists every operator 
                     (-gt, -eq, -f, -w, etc.)

explainshell.com  → paste any command/script, it 
                     highlights and explains each 
                     part — bookmark this

tldr <command>    → (if installed) short practical 
                     examples instead of the full 
                     man page

My own journal    → search "Learned" sections — 
                     most of this is already 
                     explained to myself
```

---

## Date: 06/15/2026

**Topic:** Cron — setting up the scheduled job (still need more practice)

**Commands:**

bash

```bash
crontab -e            # edit my crontab
crontab -l            # list current crontab entries
service cron status   # check if cron daemon is running
sudo service cron start  # start it if not running
```

**The crontab line — every minute (for testing):**

```
* * * * * "/full/path/to/disk-usage.sh"
```

**The crontab line — every hour (the real schedule):**

```
0 * * * * "/full/path/to/disk-usage.sh"
```

**What happened — errors along the way:**

**Error 1 — pointed at the folder, not the script**

```
crontab line:  * * * * * /path/to/scripts
                          ^^^^^^^^^^^^^^^^ 
                          this is the FOLDER, 
                          missing /disk-usage.sh
```

No new log entries appeared. Fix: add the actual filename to the end of the path.

**Error 2 — unquoted path with spaces** My path is `/mnt/c/Users/moxey/Desktop/Cloud infra roadmap/scripts/disk-usage.sh` — the spaces in "Cloud infra roadmap" break the path into multiple pieces unless quoted.

Fix:

```
* * * * * "/mnt/c/Users/moxey/Desktop/Cloud infra roadmap/scripts/disk-usage.sh"
```

**WSL-specific note — cron daemon may not run by default** On a real server (Beelink), cron runs automatically as a systemd service. On WSL, the cron daemon sometimes needs to be started manually each session:

bash

```bash
service cron status        # check
sudo service cron start    # start if not active
```

**Learned (and what's still fuzzy):**

- cron needs an **absolute path** to the script — no `~`, no `./`, because cron doesn't run with my interactive shell's context (no `$HOME` the same way, different working directory)
- Paths with spaces need quotes, same as any command
- `crontab -l` is how to verify what's actually saved — always check this after editing, don't assume the edit worked
- `* * * * *` = every minute (good for testing), `0 * * * *` = every hour at minute 0 (the real schedule)
- **Still need more practice with:** the 5-field syntax beyond `*` and `0` — e.g. what `*/15` means, how day-of-month vs day-of-week interact, and reading `crontab -l` output confidently without having to look up each field again. Revisit the "Maintaining Your System: Automation" entry in Linux Fundamentals for the field table, and consider doing a few more THM exercises specifically on cron syntax variations (not just hourly).

---

## Notes / things to revisit later

- Cron syntax beyond `* * * * *` and `0 * * * *` — step values (`*/15`), specific weekdays, etc. Want more reps here before feeling confident.
- `awk` — only learned the one pattern (`NR==2 {print $5}`) needed for this script. Don't need to master it now, but worth knowing it's a recurring tool.