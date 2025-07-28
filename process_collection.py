import os
import json
import fitz  # PyMuPDF
from datetime import datetime
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")  # <1GB, fast

def extract_pages_text(pdf_path):
    doc = fitz.open(pdf_path)
    return [page.get_text() for page in doc]

def embed(texts):
    return model.encode(texts, convert_to_tensor=True)

def process_collection(folder_path):
    # Load input config
    with open(os.path.join(folder_path, "challenge1b_input.json"), "r") as f:
        config = json.load(f)

    input_docs = [doc["filename"] for doc in config["documents"]]
    persona = config["persona"]["role"]
    task = config["job_to_be_done"]["task"]
    persona_task = f"{persona}: {task}"

    # Embed persona-task
    persona_embedding = embed([persona_task])[0]

    extracted_sections = []
    subsection_analysis = []

    for doc in config["documents"]:
        filename = doc["filename"]
        pdf_path = os.path.join(folder_path, "PDFs", filename)
        all_pages = extract_pages_text(pdf_path)

        for page_num, text in enumerate(all_pages):
            if not text.strip():
                continue
            score = util.cos_sim(embed([text])[0], persona_embedding).item()
            extracted_sections.append({
                "document": filename,
                "section_title": text.strip().split('\n')[0][:100],  # First line as section
                "importance_rank": 0,  # Temp, will sort later
                "page_number": page_num
            })
            subsection_analysis.append({
                "document": filename,
                "refined_text": text.strip(),
                "page_number": page_num
            })

    # Sort by score & assign importance rank
    scored_sections = sorted(extracted_sections, key=lambda sec: util.cos_sim(embed([sec["section_title"]])[0], persona_embedding).item(), reverse=True)
    for rank, sec in enumerate(scored_sections[:10]):  # Top 10
        sec["importance_rank"] = rank + 1

    output = {
        "metadata": {
            "input_documents": input_docs,
            "persona": persona,
            "job_to_be_done": task,
            "processing_timestamp": datetime.utcnow().isoformat()
        },
        "extracted_sections": scored_sections[:10],
        "subsection_analysis": subsection_analysis
    }

    # Write output
    with open(os.path.join(folder_path, "challenge1b1_output.json"), "w") as f:
        json.dump(output, f, indent=2)

if __name__ == "__main__":
    import sys
    folder = sys.argv[1] if len(sys.argv) > 1 else "./Collection 1"
    process_collection(folder)
