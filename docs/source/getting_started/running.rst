Run PDFDataExtractor
====================
You can start to extract information from PDF files once the tool is correctly installed.

Import necessary modules
------------------------

	.. code-block:: python
	
		from pdfdataextractor import Reader

Pass a PDF file
---------------

	.. code-block:: python

		# Spefify the path to the PDF file 
		path = r'the path to the PDF file'

		# Create an instance
		file = Reader()

		# Read the file
		pdf = file.read_file(path)
		
		# Test if pdf is returned successfully
		pdf.test()

Use PDFDataExtractor to perform chemistry related extraction
------------------------------------------------------------

You can use the flag "chem=Ture" to instruct the function to carry out chemistry related information extraction at the same time when extracting metadata, using ChemDataExtractor

	.. code-block:: python
		
		# Path to the PDF file
		file = r'path to the file'

		# Create an instance
		reader = Reader()

		# Read the file
		pdf = reader.read_file(file)

		# Show extracted chemical information
		r = pdf.abstract(chem=True)
		r.records.serialize()
