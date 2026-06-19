# Linux Fundamentals — 001
Journal template (for reference):

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

---

## Date: 06/13/2026

**Topic:** Basic commands — echo & whoami

**Commands:**

```bash
echo "Hello Friend"
whoami
```

**What happened:** Wanted to print a message to the terminal and check which user I was logged in as. Both worked first try.

- `echo` — outputs whatever text I give it
- `whoami` — prints the current logged in user

**Learned:** `echo` and `whoami` are simple but used constantly — `echo` especially for printing status messages inside scripts.

---

## Date: 06/13/2026

**Topic:** Interacting with the filesystem

**Commands:**

```bash
ls
cd <directory>
cat <file>
pwd
```

**What happened:** Practiced listing directory contents, moving between directories, viewing a file's contents, and checking my current location in the filesystem.

- `ls` — lists files and folders in the current directory
- `cd <directory>` — changes into that directory
- `cat <file>` — prints the contents of a file
- `pwd` — prints the full path of the current working directory

**Learned:** `pwd` is useful any time I'm not sure where I am after a few `cd` commands — good habit to run it often when starting out.

---

## Date: 06/13/2026

**Topic:** Searching for files

**Commands:**

```bash
find -name <filename>
find -name "*.<extension>"
grep "<value>" <filename>
grep -R "<value>" <directory>
```

**What happened:** Practiced finding a file by name (and by extension when I didn't know the exact name), and searching inside files for a specific value.

- `find -name <filename>` — finds a file if I know its name
- `find -name "*.txt"` — finds files by extension if I don't know the exact name
- `grep "<value>" <filename>` — searches for a value inside a specific file
- `grep -R "<value>" <directory>` — searches recursively:
    - checks every file in the current directory
    - checks all subdirectories too
    - shows where the value appears

**Learned:** `find` answers "where is this file?" and `grep` answers "what's inside this file?" — different tools for different questions, easy to mix up at first.

---

## Date: 06/13/2026

**Topic:** Shell operators

**Commands:**

```bash
command &
command1 && command2
command > file.txt
command >> file.txt
```

**What happened:** Learned how to control command execution and output.

- `&` — runs a command in the background, frees up the terminal
- `&&` — chains commands together; the second only runs if the first succeeds
- `>` — redirects output to a file, overwriting it
- `>>` — redirects output to a file, appending instead of overwriting

**Learned:** `>` vs `>>` is an easy mistake to make — `>` will silently wipe a file's existing content. Default to `>>` when logging, unless I specifically want to overwrite.

---
# Linux Fundamentals — 002

---

## Date: 06/14/2026

**Topic:** Secure Shell (SSH)

**Commands:**

```bash
ssh <username>@<ip-address>
```

**What happened:** Connected to another machine remotely. Prompted for a password, entered it, and was logged into the remote machine's shell.

**Learned:** SSH encrypts traffic between my machine and the remote one — data is unencrypted only once it arrives at the destination. This is the foundation for managing any remote server, including my Beelink.

---

## Date: 06/14/2026

**Topic:** Flags and switches

**Commands:**

```bash
man <command>
```

**What happened:** Learned that flags/switches extend or change the behavior of a command, and that `man <command>` shows the manual page listing all available flags for that command.

**Learned:** When I don't know what a flag does, `man` is the first place to check before searching online.

---

## Date: 06/14/2026

**Topic:** Filesystem interaction

**Commands:**

```bash
touch <file>
mkdir <folder>
cp <source> <destination>
mv <source> <destination>
rm <file>
rm -R <folder>
file <file>
```

**What happened:** Practiced creating, copying, moving, and removing files and folders, and checking what type a file is.

- `touch <file>` — creates an empty file
- `mkdir <folder>` — creates a new folder
- `cp <source> <destination>` — copies a file or folder
- `mv <source> <destination>` — moves (or renames) a file or folder
- `rm <file>` — removes a file
- `rm -R <folder>` — removes a folder and its contents recursively
- `file <file>` — shows what type of file something is

**Learned:** `rm -R` is permanent — no trash bin to recover from. Worth double-checking the path before running it, especially with wildcards.

---

### Deeper dive — copying and moving (06/15/2026)

**Commands:**

```bash
cp -r <source-folder> <destination-folder>
cp -i <source> <destination>

mv <old-name> <new-name>
mv -i <source> <destination>
```

- `cp -r <source-folder> <destination-folder>` — copies a folder and everything inside it (recursive). Without `-r`, copying a folder fails
- `cp -i <source> <destination>` — asks for confirmation before overwriting an existing file at the destination
- `mv <old-name> <new-name>` — renaming is just "moving" a file to a new name in the same directory
- `mv -i <source> <destination>` — asks for confirmation before overwriting

**Examples:**

```bash
# Copy a file into another directory
cp notes.txt ~/Documents/

# Copy a file and give it a new name in the destination
cp notes.txt ~/Documents/notes-backup.txt

# Copy an entire folder and its contents
cp -r project/ ~/Documents/project-backup/

# Move a file to another directory
mv notes.txt ~/Documents/

# Rename a file (move within the same directory)
mv notes.txt important-notes.txt

# Move and rename at the same time
mv notes.txt ~/Documents/important-notes.txt
```

**What happened (error encountered):** Problem: ran `cp project/ ~/Documents/` on a folder without `-r` —

```
cp: -r not specified; omitting directory 'project/'
```

Fix: added `-r` flag — `cp -r project/ ~/Documents/`

**Learned:** `cp` needs `-r` for folders but `mv` doesn't — because `mv` doesn't actually duplicate the contents, it just changes the file's location/reference. `cp` has to physically copy every file inside, which is why it needs to be told explicitly to do so recursively.

**Also learned:** Neither `cp` nor `mv` warn before overwriting a file by default — `-i` (interactive) is worth using as a habit when working with anything important, since an overwritten file can't be recovered.

---

## Date: 06/14/2026

**Topic:** Permissions 101

**Commands:**

```bash
ls -l
chmod
su <user>
su -l <user>
chmod 750 <file>
```

**What happened:** Learned how Linux represents file permissions and how ownership works between users and groups.

**Reading permission strings:** A permission string like `-rw-r--r--` breaks down into four parts:

```
-   rw-      r--      r--
|   |        |        |
|   owner    group    others
file type: indicates regular file; d indicates directory
```

- `r` = read
- `w` = write
- `x` = execute
- `-` = file type

Each file has three sets of these three permissions — one for the owner, one for the group, one for everyone else (others).

**Example:** `-rw-r--r--`

- Owner: `rw-` → read and write, no execute
- Group: `r--` → read only
- Others: `r--` → read only

**Users vs groups:** A file can belong to a group of users, and that group can have its own permission set — separate from the owner's permissions and separate from everyone else's. This means multiple people can share access to the same file with different levels of access, without changing the file itself for anyone else.

**Switching between users:**

- `su <user>` — switch to another user (su = "switch user")
- `su -l <user>` — switch to another user and load their environment as if logging in fresh (login shell)

**Converting symbolic permissions to numbers (octal notation):**

Each permission has a numeric value:

| Permission    | Value |
| ------------- | ----- |
| Read (`r`)    | 4     |
| Write (`w`)   | 2     |
| Execute (`x`) | 1     |

Add them together for each set (owner / group / others) to get a single digit 0–7:

|Permission set|Permissions|Calculation|Value|
|---|---|---|---|
|Owner|rwx|4+2+1|7|
|Group|rwx|4+2+1|7|
|Others|rwx|4+2+1|7|

So `rwxrwxrwx` = `777` — full permissions for everyone.

A more realistic example — `-rw-r--r--`:

|Permission set|Permissions|Calculation|Value|
|---|---|---|---|
|Owner|rw-|4+2+0|6|
|Group|r--|4+0+0|4|
|Others|r--|4+0+0|4|

→ `644` — owner can read/write, everyone else can only read. Common default for regular files.

**More common examples:**

|Symbolic|Numeric|Meaning|
|---|---|---|
|`rwxr-xr-x`|755|Owner can do everything, others can read and execute|
|`rw-r--r--`|644|Owner can read/write, others can only read|
|`rwx------`|700|Only the owner has access|
|`rwxr-x---`|750|Owner has full access, group can read/execute, others have no access|

This is the number used with `chmod`:

```bash
chmod 644 <file>   # sets rw-r--r--
chmod 755 <file>   # sets rwxr-xr-x — common for scripts/executables
chmod 750 <file>   # sets rwxr-x--- — owner + group only, no access for others
```

**Security note — `chmod 750`:** `750` is worth remembering specifically for sensitive files. It gives the owner full control, lets a trusted group read and execute, and locks everyone else out completely. Useful for identifying or fixing a security risk where a file is more open than it should be e.g. if `ls -l` shows a config file with secrets is `644` (world-readable), tightening it to `750` or even `700` removes that exposure.

**Learned:** The three-part owner/group/others structure means permissions aren't all-or-nothing a file can be fully open to its owner, readable by a team via group permissions, and locked down to everyone else, all at once. Octal notation (`644`, `755`, `750`, etc.) is just a compact way of writing all three permission sets as one number, and it's also a quick way to spot files that are more exposed than they should be.


## Date: 06/14/2026

**Topic:** Common directories

**Commands:**

```bash
cd /etc
cd /var
cd /root
cd /tmp
```

**What happened:** Learned the purpose of a few common top-level directories in the Linux filesystem.

- `/etc` — stores system-wide configuration files used by the OS and installed applications
- `/var` — stores data that changes frequently — logs, caches, and files written to by services or applications while running
- `/root` — the home directory for the `root` user (not to be confused with `/`, the root of the entire filesystem)
- `/tmp` — temporary storage for data only needed briefly; contents are typically cleared on reboot

**Learned:** Each of these directories signals _how_ the data inside it behaves — `/etc` is config (rarely changes), `/var` is runtime data (changes constantly), `/tmp` is disposable, and `/root` is just one user's home directory with the same structure as `/home/<user>` but reserved for root. Knowing this makes it easier to guess where to look when troubleshooting e.g. checking `/var/log` for logs, or `/etc` for a service's config file.


# Linux Fundamentals — 003

## Date: 06/14/2026

**Topic:** Terminal text editors

**Commands:**

bash

```bash
nano <filename>
```

**What happened:** Learned to use `nano` to open and edit a file directly in the terminal, and the key bindings for navigating and editing within it.

**nano key bindings:**

All `nano` shortcuts use `Ctrl` (shown as `^` at the bottom of the nano screen) or `Alt` (shown as `M-`, for "Meta").

|Action|Shortcut|
|---|---|
|Search for text|`Ctrl + W`|
|Find next occurrence|`Ctrl + W` then `Enter` again|
|Jump to a specific line number|`Ctrl + _` (then type the line number)|
|Show current line/column number|`Ctrl + C`|
|Cut a line (or selected text)|`Ctrl + K`|
|Paste cut text|`Ctrl + U`|
|Save the file|`Ctrl + O` (then `Enter` to confirm filename)|
|Exit|`Ctrl + X`|

**Copying and pasting a block of text:**

1. Move the cursor to the start of the text
2. Press `Alt + A` to set a selection mark
3. Move the cursor to the end of the text you want to select
4. Press `Ctrl + K` to cut the selection (this also copies it into nano's buffer)
5. Move the cursor to where you want it
6. Press `Ctrl + U` to paste

**Learned:** `Ctrl + K` / `Ctrl + U` (cut/paste) is how nano handles both cutting _and_ copying — there's no separate "copy" command. To copy without removing the original, cut it with `Ctrl + K` then immediately paste it back with `Ctrl + U` before pasting it again wherever it's needed. `Ctrl + _` for jumping to a line number is awkward to type but useful when an error message tells you exactly which line a problem is on (e.g. a config file syntax error).

## Date: 06/14/2026

**Topic:** General / useful utilities — wget & scp

**Commands:**

bash

```bash
wget <url>

# Copy a file from this machine TO a remote machine
scp <filename> <user>@<ip-address>:<destination-path>

# Copy a file FROM a remote machine TO this machine
scp <user>@<ip-address>:<remote-filename> <local-destination-path>
```

**What happened:** Learned `wget` for downloading files over HTTP, and `scp` for transferring files to/from a remote system over SSH.

- `wget <url>` — downloads a file from the web directly to the current directory
- `scp` — "secure copy"; works like `cp` but one side of the path can be a remote machine, connected over SSH

**Example using the variables below:**

|Variable|Value|
|---|---|
|IP address of the remote system|`192.168.1.30`|
|User on the remote system|`ubuntu`|
|Name of the file on the local system|`important.txt`|
|Name to store the file as on the remote system|`transferred.txt`|

bash

```bash
# Copy important.txt from this machine to the remote system,
# saving it as transferred.txt in ubuntu's home directory
scp important.txt ubuntu@192.168.1.30:transferred.txt

# Copy transferred.txt from the remote system back down
# to this machine, saving it in the current directory as a copy
scp ubuntu@192.168.1.30:transferred.txt ./transferred-copy.txt
```

**Learned:** `scp` is just `cp` with a `user@ip:path` prefix on whichever side is remote  the direction depends on which side of the command the `user@ip:` part is on. Both sides need a destination path; leaving one off (as in my first attempt) errors out because `scp` doesn't know what to name the file on the receiving end. `wget` is one-directional (download only) and doesn't need credentials for public URLs `scp` always authenticates over SSH like a normal login.

---

### Serving files from a host — Python's built-in web server (06/14/2026)

**Commands:**

bash

```bash
python3 -m http.server &   # run a simple HTTP server in the background
wget http://<ip-address>:<port>/<filename>   # download a file from it
```

**What happened:** Started a quick HTTP server to serve files from the current directory, then downloaded one of those files using `wget` from another machine.

- `python3 -m http.server` — starts a basic web server on port 8000 by default, serving the current directory's contents
- `&` — runs it in the background so the terminal is still usable
- `wget http://<ip>:8000/<filename>` — fetches a file from that server over HTTP

**What happened (error encountered):** Problem: ran `wget http://10.66.143.225:8000/.flag.txt` from my own machine, before being connected to the target system —

```
Connecting to 10.66.143.225:8000... failed: Connection refused.
```

The IP address belonged to the remote target machine, not my own machine, so `wget` couldn't reach it at all from where I was.

Fix: SSH into the remote machine first. Run `python3 -m http.server &` _on_ the remote machine, then open a second terminal/session (also on the remote machine, or anywhere that can route to it) and run `wget` against `localhost` or the remote's own address.

**Learned:** `python3 -m http.server` serves files from wherever it's _run_ it has to be running on the same machine as the files I want to share, not on my own machine while pointing at someone else's IP. "Unable to connect" almost always means I'm trying to reach an address from the wrong machine  first question to ask is "which machine am I actually on right now?"


## Date: 06/14/2026

**Topic:** Processes 101

**Commands:**

bash

```bash
ps aux
top
kill <PID>
kill -SIGTERM <PID>
kill -SIGKILL <PID>
kill -SIGSTOP <PID>
```

**What happened:** Learned how to view running processes and how to signal them to stop.

**Viewing processes:**

- `ps aux` — shows processes from all users, including ones not attached to a terminal session
- `top` — shows real-time, continuously updating process statistics (CPU, memory, etc.). Exit with `Ctrl + C`
- `kill <PID>` — sends a signal to a process by its Process ID, by default `SIGTERM`

**Managing processes — signals:**

|Signal|What it does|
|---|---|
|`SIGTERM`|Asks the process to terminate, but allows it to clean up first (close files, save state)|
|`SIGKILL`|Forces the process to stop immediately — no cleanup|
|`SIGSTOP`|Pauses/suspends the process without ending it|

**How processes start:**

- **Namespaces** — the OS slices up CPU, RAM, and priority between processes, like cutting a cake. Processes can only see others in the same namespace — this isolation is also the basis for how containers work (a container is a process in its own namespace).
- **PID 0 / PID 1** — PID 0 is the kernel scheduler (not directly manageable). PID 1 is `systemd` on Ubuntu, the first real process, started at boot. Everything else is a child (or descendant) of systemd.
- **fork & exec** — a process **forks** itself to create a copy (child), then that child **execs** — replaces itself with the program to actually run. This is why a shell shows as the parent (`PPID`) of any command you run.

**Learned:** Every process traces back through its PPID to systemd at PID 1 — one long parent/child chain. Namespaces are why a container's process can think it's PID 1 in its own world while the host sees it as just another process. Also: `kill <PID>` (SIGTERM) lets a program clean up before exiting; `kill -9 <PID>` (SIGKILL) forces it immediately — worth knowing the difference before reaching for `-9` by default.

---

## Date: 06/14/2026

**Topic:** Getting processes/services to start on boot 

**Commands:**

bash

```bash
systemctl start <service>
systemctl stop <service>
systemctl enable <service>
systemctl disable <service>
systemctl status <service>
```

**What happened:** Learned how to control services managed by systemd  the process from the previous entry that everything traces back to.

Critical software like web servers, databases, or file transfer servers often needs to start automatically when the system boots, without an administrator manually starting it every time. `systemctl` is the command used to interact with systemd to manage this.

**The five core options, using `apache2` as the example:**

|Command|What it does|
|---|---|
|`systemctl start apache2`|Starts the service right now|
|`systemctl stop apache2`|Stops the service right now|
|`systemctl enable apache2`|Sets the service to start automatically on every future boot (doesn't start it now)|
|`systemctl disable apache2`|Removes the service from starting automatically on boot (doesn't stop it now)|
|`systemctl status apache2`|Shows whether the service is currently running, plus recent log output|

**Learned:** `start`/`stop` and `enable`/`disable` are two separate, independent settings — one controls _right now_, the other controls _on next boot_. A service can be running but not enabled (it'll stop being available after a reboot), or enabled but not currently running (it'll come up on the next boot but isn't active now). `status` is the command to reach for first when something "isn't working" — it shows both the current state and recent errors in one place.

## Date: 06/14/2026

**Topic:** Foreground vs background processes

**Commands:**

bash

```bash
<command> &      # run a command in the background
Ctrl + Z          # suspend (background) the current foreground process
fg                # bring a backgrounded process back to the foreground
ps aux            # confirm a background process is still running
```

**What happened:** Learned that processes run in one of two states — foreground or background  and how to move a process between them.

- **Foreground** — the default. A command like `echo "Hi THM"` runs in the foreground, and its output returns directly to the terminal. The terminal is "busy" with it until it finishes.
- **Background** — adding `&` to a command (`echo "Hi THM" &`) runs it in the background. Instead of the output, the terminal immediately returns the process ID, and the terminal is free to take more commands. This is useful for things like copying large files — the copy runs in the background while other commands continue.
- **`Ctrl + Z`** — suspends/backgrounds a currently-running foreground process without starting it with `&` in the first place. A looping script printing output repeatedly can be silenced this way — the terminal stops filling with its output until it's brought back.
- **`fg`** — brings a backgrounded process back to the foreground, reconnecting its output to the terminal.

**Learned:** `&` and `Ctrl+Z` both result in a backgrounded process, just at different points  `&` backgrounds it from the start, `Ctrl+Z` backgrounds something already running in the foreground. Either way, `ps aux` can confirm the process is still alive in the background, and `fg` is the way back to interacting with it directly.

## Date: 06/14/2026

**Topic:** Maintaining your system: automation with cron / crontab

**Commands:**

bash

```bash
crontab -e   # open your crontab for editing (pick an editor, e.g. nano)
crontab -l   # list your current crontab entries
```

**What happened:** Learned how to schedule a task to run automatically — similar to Windows Task Scheduler. Users may want to run commands, back up files, or launch programs automatically after boot, on a schedule, without doing it manually each time.

`cron` is a process started at boot that manages scheduled tasks. `crontab` ("cron table") is the file format cron reads — each line is one scheduled job, executed step-by-step.

**The 6 fields of a crontab line:**

|Value|Description|
|---|---|
|MIN|What minute to execute at|
|HOUR|What hour to execute at|
|DOM|What day of the month to execute at|
|MON|What month of the year to execute at|
|DOW|What day of the week to execute at|
|CMD|The actual command that will be executed|

**Example — back up a folder every 12 hours:**

bash

```bash
0 */12 * * * cp -R /home/cmnatic/Documents /var/backups/
```

- `0` — at minute 0
- `*/12` — every 12 hours
- `* * *` — every day of the month, every month, every day of the week (don't care)
- `cp -R ...` — the command to run

**Wildcards:** `*` means "don't care / every" for that field. In the example above, the three trailing `*`s mean the job runs at the specified time regardless of date, month, or weekday  only the every-12-hours timing matters.

**Editing a crontab:** `crontab -e` opens your crontab in a chosen editor (e.g. nano) to add, edit, or remove scheduled jobs.

**Helpful tools:** "Crontab Generator" and "Cron Guru" are online tools that build the correct field syntax from a friendly interface useful while the format is still unfamiliar.

**Learned:** The 5 time fields read left to right as minute → hour → day-of-month → month → day-of-week, always followed by the command. `*/12` in the hour field specifically means "every 12 hours" (i.e. at hour 0 and hour 12), not "12 o'clock" — step values (`*/N`) are a different thing from a fixed number in that field. When in doubt, generate the line with a tool first and compare it field-by-field against this table rather than guessing.

## Date: 06/14/2026

**Topic:** Maintaining your system: package management & repositories

**Commands:**

bash

```bash
add-apt-repository <repo>          # add a repository
add-apt-repository --remove <repo> # remove a repository

apt update                          # refresh package lists from all repos
apt install <package>               # install software
apt remove <package>                # uninstall software
```

**What happened:** Learned how software gets distributed on Ubuntu, and how to add/remove sources for it.

**Packages and repositories:** Developers submit their software to an "apt" repository. Once approved, it becomes installable by anyone  this is the user-accessibility and open-source side of Linux. Ubuntu's own repositories are maintained by Canonical, but additional community/third-party repositories can be added to extend what's installable, either with `add-apt-repository` or by manually listing a provider (e.g. a vendor's repo hosted closer to your region).

**`apt` vs `dpkg`:** `apt` is the higher-level tool — it manages both the packages _and_ the list of repositories ("sources") they come from. Software installed via `apt` gets checked for updates automatically whenever the system updates, because apt already knows which repo it came from. `dpkg` installs individual package files directly but doesn't track a source repo for future updates.

**Adding a third-party repo manually — example (Sublime Text):**

Software not in Ubuntu's default repos (like Sublime Text) needs its repo added manually, trusted via a **GPG key** first.

1. Download and trust the developer's GPG key:

bash

```bash
   wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -
```

The GPG key is the integrity check — it confirms the software actually came from the developer it claims to, and if the key doesn't match, apt won't install it.

2. Create a dedicated file for this repo (good practice: one file per third-party repo) in `/etc/apt/sources.list.d/`, e.g. `sublime-text.list`, and add the repo's source line to it (using nano or any editor).
3. Refresh apt so it picks up the new repo:

bash

```bash
   apt update
```

4. Install the software:

bash

```bash
   apt install sublime-text
```

**Removing a repo and package:**

bash

```bash
add-apt-repository --remove ppa:PPA_Name/ppa   # or delete the .list file manually
apt remove sublime-text
```

**Learned:** The GPG key step exists _before_ the repo is even usable  it's a trust handshake, separate from actually installing anything. The reason `apt` is preferred over `dpkg` for ongoing use is that apt remembers _where_ a package came from (via the `.list` file in `/etc/apt/sources.list.d/`), so `apt update` + future upgrades automatically include it `dpkg` alone has no concept of "where did this come from, check there again later."

## Date: 06/14/2026

**Topic:** Maintaining Your System: Logs

**What happen:**  Learn services and logs to monitor the health of your system and protecting it.

**Command**

```bash
cd /var/logs/<service>
```

