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


Pass a folder
-------------


	.. code-block:: python
	
		from pdfdataextractor import Reader
		import glob

	.. code-block:: python
	
		def read_single(file):
		    reader = Reader()
		    pdf = reader.read_file(file)
		    print(pdf.abstract())

		def read_single(file):
		    for pdf in path:
		        read_single(pdf)
		        print('-------------------', '\n')


	.. code-block:: python

		read_multiple(glob.glob(r'path_to_the_folder/*.pdf'))



