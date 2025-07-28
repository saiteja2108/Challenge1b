

### `README.md` for Challenge 1b

````markdown
# Challenge 1b: Multi-Collection PDF Analysis

This solution performs persona-based content extraction from multiple PDF collections. Each collection is processed based on the configuration inside it (`challenge1b_input.json`), and the tool outputs structured insights into `challenge1b_output.json`.

---

## 🚀 Features

- Processes PDFs inside folders named like `Collection 1`, `Collection 2`, etc.
- Each folder must contain a `challenge1b_input.json` file
- Embeds persona and task prompts to guide relevance scoring
- Ranks extracted sections by semantic similarity
- Outputs:
  - Top 10 relevant sections
  - Full subsection analysis
- Fully offline (no internet access required)



## 🐳 Docker Instructions

### 🔧 Build the Image

```bash
docker build --platform linux/amd64 -t challenge1b .
```

### 🔁 Run for All Collections (Optional Bash Loop)

If you're on a Unix-like system (Linux/macOS/WLS):

```bash
for dir in Collection*/; do
  docker run --rm \
    -v "$(pwd)/$dir":/app/collection \
    --network none \
    challenge1b /app/collection
done
```

This will run the container once for each `Collection` folder in the current directory.

---

## 🔒 Notes

* Make sure `challenge1b_input.json` is present inside each collection folder
* No internet connection is required — works fully offline
* Compatible with `linux/amd64` platforms

---

