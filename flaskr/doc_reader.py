
import docx
import doc_analyzer
import pptxcreator

doc = docx.Document('report.docx')
print(len(doc.paragraphs))
paragraphs = []
title_headings = []
headings = []
for i,par in enumerate(doc.paragraphs):
    
    if len(par.text) >  60:    
        paragraphs.append(par)
for i,par in enumerate(paragraphs):
    
    
    a = doc_analyzer.summarize_heading(par.text)
    headings.append(a)
    title_headings.append(str(i))

pptxcreator.create_slides(1,"Report PPT",title_headings,headings)

