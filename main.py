import PyPDF2

pdfiles = [""]
merger = PyPDF2.PdfMerger()
for filename in pdfiles:
    pdfile = open(filename, 'rb')
    pdfReader = PyPDF2.PdfReader(pdfile)
    merger.append(pdfReader)
pdfile.close()
merger.write("merged.pdf")
