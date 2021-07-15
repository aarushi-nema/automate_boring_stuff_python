import PyPDF2 
import os 
# Open the files that have to be merged one by one


def merge_file(file1, file2, merged_file):
	pdf1File = open(file1, 'rb')
	pdf2File = open(file2, 'rb')
	 
	# Read the files that you have opened
	pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
	pdf2Reader = PyPDF2.PdfFileReader(pdf2File)
	 
	# Create a new PdfFileWriter object which represents a blank PDF document
	pdfWriter = PyPDF2.PdfFileWriter()
	 
	# Loop through all the pagenumbers for the first document
	for pageNum in range(pdf1Reader.numPages):
	    pageObj = pdf1Reader.getPage(pageNum)
	    pdfWriter.addPage(pageObj)
	 
	# Loop through all the pagenumbers for the second document
	for pageNum in range(pdf2Reader.numPages):
	    pageObj = pdf2Reader.getPage(pageNum)
	    pdfWriter.addPage(pageObj)
	 
	# Now that you have copied all the pages in both the documents, write them into the a new document
	pdfOutputFile = open(merged_file, 'wb')
	pdfWriter.write(pdfOutputFile)
	 
	# Close all the files - Created as well as opened
	pdfOutputFile.close()
	pdf1File.close()
	pdf2File.close()

files = ["Chapter1.pdf","Chapter2.pdf","Chapter3.pdf"]
for index in range(0,len(files)-1):
	merge_file(files[index],files[index+1],"merged_file"+str(index)+".pdf")
	if (index > 0) :
		print("deleting " +  files[index])
		os.remove(files[index])
	files[index+1] = "merged_file"+str(index)+".pdf"
	print("generated file" + "merged_file"+str(index)+".pdf")
