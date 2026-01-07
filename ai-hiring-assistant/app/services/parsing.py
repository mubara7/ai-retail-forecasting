from io import BytesIO
from typing import Optional
from app.core.utils import clean_text


def parse_txt(file_bytes: bytes) -> str:
    try:
        return file_bytes.decode("utf-8", errors="ignore")
    except Exception:
        return ""

def parse_pdf(file_bytes: bytes) -> str:
    try:
        from PyPDF2 import PdfReader
        reader = PdfReader(BytesIO(file_bytes))
        pages_text = []
        for p in reader.pages:
            pages_text.append(p.extract_text() or "")
        return "\n".join(pages_text)
    except Exception:
        return ""

def parse_docx(file_bytes: bytes) -> str:
    try:
        import docx
        bio = BytesIO(file_bytes)
        doc = docx.Document(bio)
        return "\n".join([p.text for p in doc.paragraphs if p.text])
    except Exception:
        return ""

def parse_resume(filename: str, file_bytes: bytes) -> str:
    name = (filename or "").lower()
    if name.endswith(".pdf"):
        return parse_pdf(file_bytes)
    if name.endswith(".docx"):
        return parse_docx(file_bytes)
    # default
    return parse_txt(file_bytes)
