import tabula

file1 = "note.pdf"
table = tabula.read_pdf(file1,pages=1)
print(table[0])

tabula.convert_into("note.pdf","Name_of_csv_file.csv")
