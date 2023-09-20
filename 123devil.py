import os
from PyPDF2 import PdfReader, PdfWriter
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO

def create_certificate(recipient_name,template_pdf_path,output_folder_path,font_name='Helvetica-Bold'):
    certificate_file = os.path.join(output_folder_path, f'{recipient_name}_certificate.pdf')
    with open(template_pdf_path, 'rb') as template_file:
        pdf_reader = PdfReader(template_file)
        pdf_writer = PdfWriter()
        
        for page in pdf_reader.pages:
            temp_buffer = BytesIO()
            c = canvas.Canvas(temp_buffer, pagesize=letter)
            c.setFont(font_name, 18)
            c.drawString(443, 250, recipient_name)
            c.save()
            temp_buffer.seek(0)
            temp_pdf_reader = PdfReader(temp_buffer)
            page.merge_page(temp_pdf_reader.pages[0])
            pdf_writer.add_page(page)
            with open(certificate_file, 'wb') as output_file:
                pdf_writer.write(output_file)
            
        

def generate_certificates(template_pdf_path, data_csv_path, output_folder_path):
    with open(data_csv_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            recipient_name = row[0]
            create_certificate(recipient_name, template_pdf_path, output_folder_path)


if __name__ == "__main__":
    template_pdf_path = "C:\\Users\\Bharath\\Downloads\\CERTIFICATE.pdf"
    data_csv_path = "C:\\Users\\Bharath\\Downloads\\1.csv"
    output_folder_path = "C:\\Users\\Bharath\\Downloads\\"
    generate_certificates(template_pdf_path, data_csv_path, output_folder_path)

    
                
