import uvicorn
from fastapi import FastAPI, UploadFile, File
from classifiers import classify_email
from extractors import extract_data
from duplicate_detector import check_duplicate
from utils import parse_eml

app = FastAPI()

@app.post("/process-email/")
async def process_email(file: UploadFile = File(...)):
    contents = await file.read()
    email_data = parse_eml(contents)
    
    request_type, confidence, reasoning = classify_email(email_data["body"])
    extracted_data = extract_data(email_data, request_type)
    is_duplicate, duplicate_reason = check_duplicate(email_data)

    return {
        "request_type": request_type,
        "confidence": confidence,
        "reasoning": reasoning,
        "extracted_data": extracted_data,
        "is_duplicate": is_duplicate,
        "duplicate_reason": duplicate_reason
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
