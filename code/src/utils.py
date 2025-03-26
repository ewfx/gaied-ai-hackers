import mailparser
import fitz  # PyMuPDF
import docx

def parse_eml(file_path):
    """Parse an .eml file."""
    mail = mailparser.parse_from_file(file_path)
    return {
        "body": mail.body,
        "subject": mail.subject,
        "from": mail.from_,
        "attachments": [att["filename"] for att in mail.attachments]
    }

def parse_pdf(file_path):
    """Extract text from a PDF."""
    with fitz.open(file_path) as doc:
        return {"text": " ".join([page.get_text() for page in doc])}

def parse_docx(file_path):
    """Extract text from a DOCX file."""
    doc = docx.Document(file_path)
    return {"text": "\n".join([p.text for p in doc.paragraphs])}
