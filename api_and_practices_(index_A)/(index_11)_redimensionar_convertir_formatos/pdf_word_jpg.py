import os
import docx

folder = r"C:\Users\ASUS\Downloads\Photos"

for filename in os.listdir(folder):
    if filename.endswith(".pdf"):
        pdf_path = os.path.join(folder, filename)
        docx_filename = filename.split(".pdf")[0] + ".docx"
        docx_path = os.path.join(folder, docx_filename)
        
        doc = docx.Document()
        doc.add_page_break()
        doc.save(docx_path)
        
