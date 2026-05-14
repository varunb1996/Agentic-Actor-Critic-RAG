import os

from rag.ingest import ingest_pdf

DATA_FOLDER = "data"

pdf_files = [
    file
    for file in os.listdir(DATA_FOLDER)
    if file.endswith(".pdf")
]

for pdf in pdf_files:

    pdf_path = os.path.join(
        DATA_FOLDER,
        pdf
    )

    print(f"Ingesting: {pdf}")

    ingest_pdf(pdf_path)

print("All PDFs ingested successfully.")