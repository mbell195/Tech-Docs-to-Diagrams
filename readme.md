# Hybrid Documentation: Precision & Visuals

**Maintained by:** Marc Bell

This repository demonstrates a "Hybrid Diagramming" workflow designed for modern technical documentation. It bridges the gap between **Engineering Precision** (Version-controlled diagram code) and **Visual Impact** (Generative AI assets).

## 📂 Project Structure

```text
.
├── .github/workflows/      # CI/CD Automation (Renderers & AI Bots)
├── .vscode/                # Editor Configuration
├── assets/
│   └── diagrams-generated/ # FINAL OUTPUTS (Auto-generated SVGs & PNGs)
├── content/                # The actual documentation (Markdown/DITA)
├── prompts/                # AI INSTRUCTIONS (System prompts)
├── scripts/                # PYTHON AUTOMATION (AI API Logic)
├── source/
│   ├── drafts/             # WORKFLOW A INPUT: Rough text (.txt)
│   ├── mermaid/            # WORKFLOW A OUTPUT: Source Code (.mmd)
│   ├── generative/         # WORKFLOW B INPUT: Pure AI Prompts (.json)
│   └── polished/           # WORKFLOW C INPUT: Mermaid -> AI Polish (.json)
├── LICENSE                 # MIT License
└── README.md
```

---

## 🤖 AI Automation (Server-Side)

This project is equipped with a **Self-Orchestrating AI Engine**. You do not need to run AI tools locally. The GitHub Action (`ai-automation.yml`) handles generation for you.

### 1. Setup

To enable the AI features, you must provide an API Key.

1. Go to your GitHub Repo **Settings > Secrets and variables > Actions**.
2. Click **New repository secret**.
3. **Name:** `AI_API_KEY`
   **Value:** Your OpenAI API Key (or compatible provider).

### 2. How to Trigger the Bots

| Workflow | Action Required | What happens? |
|----------|----------------|---------------|
| **A: Text-to-Mermaid** | Create/Push a file to `source/drafts/my-note.txt` | 1. AI reads text.<br>2. AI generates `source/mermaid/my-note.mmd`.<br>3. Render Bot detects `.mmd` and creates SVG/PNG. |
| **B: Text-to-Image** | Create/Push a file to `source/generative/hero.json` | 1. AI reads JSON prompt.<br>2. AI generates DALL-E 3 image.<br>3. Bot saves `assets/diagrams-generated/hero.png`. |
| **C: Polished Logic** | Create/Push a file to `source/polished/style.json` | 1. AI reads linked Mermaid code.<br>2. AI "draws" the logic in requested style.<br>3. Bot saves `assets/diagrams-generated/style.png`. |

---

## 📐 Workflow A: The Precision Path

**Best for:** API flows, sequence diagrams, database schemas, and logic trees.

1. **Draft:** Upload rough notes to `source/drafts/`.
2. **Wait:** The bot will commit a `.mmd` file to `source/mermaid/` automatically.
3. **Refine:** Pull the changes. Open the `.mmd` file in VS Code (using the Mermaid Editor extension) to fix any logic errors manually.
4. **Publish:** The Render Bot automatically maintains the SVG/PNG versions in `assets/`.

---

## 🎨 Workflow B & C: The Visual Paths

**Best for:** High-level architecture, executive summaries, marketing assets.

- **Workflow B (Pure Generation):** Used for "vibes" and general illustrations.
- **Workflow C (Logic Enhancement):** Used when you need a specific flow (defined in Mermaid) but want it to look like a whiteboard sketch, a blueprint, or a 3D render.

**Tip:** If you delete a generated image from `assets/`, the bot will regenerate it on the next run (costing API credits). If the image exists, the bot skips it to save money.

---

## 🛠️ Local Development

To run the AI scripts locally (for testing without committing):

```bash
# 1. Install Python requirements
pip install -r requirements.txt

# 2. Set API Key
export AI_API_KEY="sk-..."

# 3. Run Engine
python scripts/ai_engine.py
```

To run the mermaid compiler locally:

```bash
npm install -g @mermaid-js/mermaid-cli
mmdc -i source/mermaid/input.mmd -o assets/diagrams-generated/output.svg
```

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

Copyright (c) 2025 Marc Bell

