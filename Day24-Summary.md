# RGANG-TOOLS - Day 24 Summary
**Date:** 19 Nov 2026 | **Location:** Harare, ZW
**Repo:** github.com/Courage15/RGANG-tools
**Tool:** brute.sh | **Lab:** Own device only - 127.0.0.1 / u0_a447

## 1. The Goal
- Test if a weak SSH password can be cracked
- Learn attack -> fix -> re-test (ethical loop)
- ONLY on own Termux lab

## 2. What Failed (And Why)
- `hydra`: E: Unable to locate package hydra
  -> Removed from Termux repo. Not your fault.
- `paramiko`: Failed to build cryptography / Rust not found
  -> Python 3.14 on Termux cannot build it.
- First `brute.sh`: Said SECURE even with 123456
  -> Wrong port. Termux SSH is on 8022, not 22.

## 3. The Fix - Our Own Tool: brute.sh
- Installed: `pkg install openssh sshpass -y`
- Started SSH: `sshd` (port 8022)
- Script loops: 123456, password, admin, 12345, qwerty, letmein, courage, harare
- Command: `sshpass -p $pw ssh -p 8022 u0_a447@127.0.0.1`

## 4. Proof - Attack Worked
- Set weak password: `passwd -> 123456`
- Ran: `./brute.sh`
- Result:

## 5. Proof - Fix Worked
- Changed password: `passwd -> STRONG password`
- Ran again: `./brute.sh`
- Tried all 8 passwords -> none worked
- Result: `[-] No password found - SECURE!`

## 6. Pushed To GitHub
- `git add brute.sh`
- `git commit -m "Day 24 - SSH brute force own lab - CRACKED 123456 then FIXED to SECURE"`
- `git push` -> 5ce6baa..6775ae7 main -> main
- 1 file changed, 14 insertions(+) create mode 100755 brute.sh

## 7. Lesson Learned
- Weak passwords fall in <1 second.
- Strong passwords + correct port + re-testing = real security.
- Real hackers build their own tools when public ones fail.
- RGANG Toolkit now: auto_report.py, port_report.py, brute.sh

**Next:** Day 25 - WiFi Password Audit (Own WiFi Only)

*RGANG - Learn. Build. Secure. For education / own devices only.*
