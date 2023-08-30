from pdfminer.high_level import extract_text

filename = 'resources/pdf_files/Die_vier_Jahreszeiten.pdf'

# is broken in the repo see
# https://github.com/pdfminer/pdfminer.six/issues/770
text = extract_text(filename)

print(text)
