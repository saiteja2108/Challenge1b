Here’s a clean, complete `README.md` tailored for your **Challenge 1b: Multi-Collection PDF Analysis** solution. It follows the submission guidelines, reflects your actual code, and is structured for Docker-based evaluation.

---

### ✅ `README.md`

```markdown
# Challenge 1b: Multi-Collection PDF Analysis

This solution performs persona-based content extraction from PDF collections. It processes one collection at a time based on a JSON configuration file and outputs structured analysis.

---

## 🚀 Features

- Processes all PDFs listed in `challenge1b_input.json`
- Embeds persona and task to guide relevance scoring
- Ranks extracted sections by semantic similarity
- Outputs `challenge1b_output.json` with:
  - Top 10 relevant sections
  - Full subsection analysis
- Fully offline execution (no internet calls)

---

## 🗂️ Expected Directory Structure

```

Challenge\_1b/
├── Collection 1/
│   ├── PDFs/
│   ├── challenge1b\_input.json
│   └── challenge1b\_output.json  ← (Generated)
├── Collection 2/
│   ├── PDFs/
│   ├── challenge1b\_input.json
│   └── challenge1b\_output.json
├── Collection 3/
│   ├── PDFs/
│   ├── challenge1b\_input.json
│   └── challenge1b\_output.json
├── process\_collection.py
├── requirements.txt
├── Dockerfile
└── README.md

````

---

## 🐳 Docker Instructions

### 🔧 Build the Image

```bash
docker build --platform linux/amd64 -t challenge1b .
````

### ▶️ Run the Container (Example: Collection 1)

```bash
docker run --rm \
  -v "$(pwd)/Collection 1":/app/collection \
  --network none \
  challenge1b /app/collection
```

