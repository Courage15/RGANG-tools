from fpdf import FPDF
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.set_margins(15, 15, 15)
pdf.add_page()
# Header
pdf.set_font("Helvetica", "B", 18)
pdf.cell(0, 10, "RGANG SECURITY CHECK", new_x="LMARGIN", new_y="NEXT")
pdf.set_font("Helvetica", "", 10)
pdf.set_text_color(100,100,100)
pdf.cell(0, 6, "WiFi / Network Report  |  Harare, Zimbabwe", new_x="LMARGIN", new_y="NEXT")
pdf.line(15, pdf.get_y()+2, 195, pdf.get_y()+2)
pdf.ln(6)
pdf.set_text_color(0,0,0)

for line in open("RGANG-Report-001.md", errors="ignore").read().splitlines():
    line = line.encode("latin-1", "replace").decode("latin-1").strip()
    if not line: 
        pdf.ln(4); continue
    if line.startswith("# "):
        pdf.set_font("Helvetica", "B", 16)
        pdf.cell(0, 9, line[2:], new_x="LMARGIN", new_y="NEXT")
    elif line.startswith("## "):
        pdf.ln(3)
        pdf.set_font("Helvetica", "B", 13)
        pdf.cell(0, 8, line[3:], new_x="LMARGIN", new_y="NEXT")
    else:
        pdf.set_font("Helvetica", "", 11)
        pdf.multi_cell(0, 6, line, new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Helvetica", "", 11)

pdf.output("RGANG-Report-001.pdf")
print("PDF DONE - PRO VERSION")
