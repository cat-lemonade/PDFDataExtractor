from pdfdataextractor import Reader
import glob

def read_single(file):
    reader = Reader()
    pdf = reader.read_file(file)
    try:
        # print(pdf.keywords())
        for i,j in pdf.reference().items():
            print(i)
            print(j)


        # from pdfminer.pdfparser import PDFParser
        # from pdfminer.pdfdocument import PDFDocument
        #
        # fp = open(file, 'rb')
        # parser = PDFParser(fp)
        # doc = PDFDocument(parser)
        #
        # print(doc.info)  # The "Info" metadata


    except:
        pass

def read_multiple(path):
    for seq, pdf in enumerate(path):
        print(seq)
        read_single(pdf)
        print('-------------------', '\n')





read_multiple(glob.glob(r'/Users/miao/Desktop/PDFDataExtractor/SI/Others/acs/*.pdf'))

# read_single(r'/Users/miao/Desktop/PDFDataExtractor/SI/Others/acs/acs.est.0c08390.pdf')