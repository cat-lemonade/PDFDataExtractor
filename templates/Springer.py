# -*- coding: utf-8 -*-
from .methods import Methods
import re

class Springer(Methods):
    #Becasue variable is passed to ELSEVIER, so need to pass pdf to __init__
    #pdf is the key-value pair representation of the article

    def __init__(self, pdf, func):
        Methods.__init__(self)#initiate extraction methods
        self.pdf = pdf
        self.func = func #save for future development
        self.metadata = self.get_MetaData(pdf)#TODO: inject special characters here？

    def author(self):#add affiliation atm
        pass

    def reference(self):
        return self.get_Reference(self.get_Section(self.pdf))

    def section(self):#TODO: inject special characters here
        return self.get_Section(self.pdf)

    def test(self):
        print('PDF returned successfully')

    def plaintext(self):
        return self.get_Puretext(self.pdf)

    def journal(self, info_type=None):
        journal = {}
        for key, value in self.pdf.items():
            if key[0] == 0:
                if value['universal_sequence'] == 1:
                    text = re.findall('\d+', value['text'])
                    journal['name'] = value['text']
                    journal['volume'] = text[0]
                    journal['year'] = text[1]
                    journal['page'] = text[2]
        if info_type == None:
            return journal
        else:
            return journal[info_type]

    def doi(self):
        return self.metadata['doi']

    def title(self):
        return self.metadata['title']

    def keywords(self):
        return self.metadata['keywords']

    def abstract(self):
        return self.metadata['abstract']

    def caption(self):
        return self.metadata['figure']





