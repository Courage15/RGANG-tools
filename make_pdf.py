from fpdf import FPDF
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.set_margins(15, 15, 15)
pdf.add_page()
pdf.set_font("Helvetica", size=11)
text = open("RGANG-Report-001.md", errors="ignore").read()
for line in text.splitlines():
    line = line.encode("latin-1", "replace").decode("latin-1")
    if not line.strip():
        pdf.ln(4)
        continue
    # break super long words so fpdf doesn't crash
    if len(line) > 90:
        line = " ".join([line[i:i+90] for i in range(0, len(line), 90)])
    pdf.multi_cell(0, 6, line, new_x="LMARGIN", new_y="NEXT")
pdf.output("RGANG-Report-001.pdf")
print("PDF DONE")
