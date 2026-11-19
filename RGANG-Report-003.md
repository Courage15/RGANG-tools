Client: CTM Corps
Location: Hatfield, Harare
Date: 19 Nov 2026
Tested by: Courage / RGANG
Scope: Own lab only, with permission
Target: 10.195.132.73

## What I Tested
Target: 10.195.132.73
Method: Nmap service scan - top risky ports

## What I Found
- Port 22/tcp - ssh - MEDIUM - Check if needed

Open Ports: 1

## Fix It Now
1. Close port 23 Telnet - NEVER use it, use SSH instead
2. Close port 21 FTP - use SFTP instead
3. If SSH (22) is open, use strong password + change port
4. Turn OFF router remote management
5. WiFi password 12+ chars

Signed: Courage
Test done with permission only. No data accessed.
