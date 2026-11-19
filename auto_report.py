import subprocess, re, datetime
from fpdf import FPDF

client = input("Client name: ")
network = input("Network (e.g. 10.195.132.0/24): ")

print(f"\n[*] Scanning {network}...")
result = subprocess.run(["nmap", "-sn", network], capture_output=True, text=True)
output = result.stdout

hosts = re.findall(r"Nmap scan report for (\S+)", output)
print(f"[+] Found {len(hosts)} hosts")

today = datetime.date.today().strftime("%d %b %Y")

# Write Markdown
md = f"""Client: {client}
Location: Hatfield, Harare
Date: {today}
Tested by: Courage / RGANG
Scope: Own lab only, with permission

## What I Tested
Network: {network}
Method: Nmap ping scan - auto generated

## What I Found
"""
for h in hosts:
    md += f"- {h} - Host Up\n"
md += f"\nHosts Found: {len(hosts)}\nRisk: LOW\n\n## Fix It Now\n1. Turn OFF SSH when not using it\n2. WiFi password 12+ chars\n3. Change router admin password\n4. Turn OFF WPS\n\nSigned: Courage\nTest done with permission only. No data accessed.\n"

open("RGANG-Report-002.md", "w").write(md)

# Make PDF
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=20)
pdf.add_page()
pdf.set_font("Helvetica", "B", 20)
pdf.cell(0, 12, "RGANG SECURITY CHECK", new_x="LMARGIN", new_y="NEXT")
pdf.set_font("Helvetica", "", 9)
pdf.set_text_color(100,100,100)
pdf.cell(0, 6, "WiFi / Network Report | Harare, Zimbabwe", new_x="LMARGIN", new_y="NEXT")
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
        pdf.set_font("Helvetica","",11); pdf.cell(0,7,"- "+line[2:], new_x="LMARGIN", new_y="NEXT")
    elif line.startswith("Client:") or line.startswith("Location:") or line.startswith("Date:") or line.startswith("Tested") or line.startswith("Scope:") or line.startswith("Hosts Found:") or line.startswith("Risk:") or line.startswith("Signed:") or line.startswith("Test done"):
        pdf.set_font("Helvetica","",11); pdf.cell(0,7,line, new_x="LMARGIN", new_y="NEXT")
    else:
        pdf.set_font("Helvetica","",11); pdf.set_x(10); pdf.multi_cell(0,7,line)

pdf.output("RGANG-Report-002.pdf")
print("PDF DONE - AUTO REPORT")
print(f"Hosts: {hosts}")
