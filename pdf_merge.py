from PyPDF2 import PdfWriter
merger=PdfWriter()
pdfs=[]
n=int(input("Enter the no of PDF: \n"))
for i in range(0,n):
    name=input(f"Enter The name of the PDF{i+1}")
    pdfs.append(name)
for pdf in pdfs:
    merger.append(pdf)
merger.write("Merged_PDF.pdf")
merger.close()
