import subprocess, re, datetime
from fpdf import FPDF

client = input("Client name: ")
target = input("Target IP (e.g. 10.195.132.73): ")

print(f"\n[*] Port scanning {target}... this takes ~30 sec")
result = subprocess.run(["nmap", "-sV", "-p", "21,22,23,80,443,445,3306,8080", target], capture_output=True, text=True)
output = result.stdout
print(output)

# Find open ports
ports = re.findall(r"(\d+/tcp)\s+open\s+(\S+)", output)
print(f"[+] Found {len(ports)} open ports")

today = datetime.date.today().strftime("%d %b %Y")

md = f"""Client: {client}
Location: Hatfield, Harare
Date: {today}
Tested by: Courage / RGANG
Scope: Own lab only, with permission
Target: {target}

## What I Tested
Target: {target}
Method: Nmap service scan - top risky ports

## What I Found
"""
for p, service in ports:
    risk = "HIGH - Change / Close this!" if p in ["21/tcp","23/tcp","445/tcp","3306/tcp"] else "MEDIUM - Check if needed" if p in ["22/tcp","8080/tcp"] else "LOW - Normal"
    md += f"- Port {p} - {service} - {risk}\n"

if not ports:
    md += "- No risky ports open - Good!\n"

md += f"\nOpen Ports: {len(ports)}\n\n## Fix It Now\n1. Close port 23 Telnet - NEVER use it, use SSH instead\n2. Close port 21 FTP - use SFTP instead\n3. If SSH (22) is open, use strong password + change port\n4. Turn OFF router remote management\n5. WiFi password 12+ chars\n\nSigned: Courage\nTest done with permission only. No data accessed.\n"

open("RGANG-Report-003.md", "w").write(md)

pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=20)
pdf.add_page()
pdf.set_font("Helvetica", "B", 20)
pdf.cell(0, 12, "RGANG SECURITY CHECK", new_x="LMARGIN", new_y="NEXT")
pdf.set_font("Helvetica", "", 9)
pdf.set_text_color(100,100,100)
pdf.cell(0, 6, "Port Scan Report | Harare, Zimbabwe", new_x="LMARGIN", new_y="NEXT")
pdf.set_draw_color(0,0,0)
pdf.line(10, 32, 200, 32)
pdf.ln(8)
pdf.set_text_color(0,0,0)

for line in md.splitlines():
    line=line.strip()
    if not line:
        pdf.ln(4); continue
    if line.startswith("## "):
        pdf.set_font("Helvetica","B",14); pdf.cell(0,10,line[3:], new_x="LMARGIN", new_y="NEXT"); pdf.ln(1)
    elif line.startswith("- "):
        pdf.set_font("Helvetica","",11); pdf.set_x(10); pdf.cell(0,7,"- "+line[2:], new_x="LMARGIN", new_y="NEXT")
    else:
        pdf.set_font("Helvetica","",11); pdf.set_x(10); pdf.multi_cell(0,7,line)

pdf.output("RGANG-Report-003.pdf")
print("PDF DONE - PORT REPORT")
print(f"Ports: {ports}")
