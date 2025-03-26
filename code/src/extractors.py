import re
from utils import parse_pdf, parse_docx

def extract_data(email_data, request_type):
    """Extract structured data based on request type."""
    extracted = {}

    if request_type == "Billing Issue":
        extracted["Invoice Number"] = re.search(r"Invoice #: (\d+)", email_data["body"])
        extracted["Amount Due"] = re.search(r"Amount: \$(\d+\.\d+)", email_data["body"])
        extracted["Due Date"] = re.search(r"Due Date: (\d{2}/\d{2}/\d{4})", email_data["body"])

    for attachment in email_data["attachments"]:
        if attachment.endswith(".pdf"):
            extracted.update(parse_pdf(attachment))
        elif attachment.endswith(".docx"):
            extracted.update(parse_docx(attachment))

    return extracted
