# AI-Powered Technical Documentation to Image Generator

**Created and maintained by:** Marc Bell

Automatically generates Mermaid diagrams from written drafts using OpenAI GPT-4o or Google Gemini. Fine-tune diagrams with precision using a visual editor, then beautify them with DALL-E 3 or Imagen 3 AI. This hybrid workflow combines version-controlled code with professional design aesthetics, fully automated via GitHub Actions.

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

To enable the AI features, you must configure API Keys. You can choose to use **OpenAI** (GPT-4o + DALL-E 3) or **Google AI** (Gemini + Imagen 3), or both.

1. Go to your GitHub Repo **Settings > Secrets and variables > Actions**.
2. Click **New repository secret**.
3. **Configure at least one of the following:**

   **For OpenAI:**
   - **Name:** `OPENAI_API_KEY`
   - **Value:** Your OpenAI API Key

   **For Google AI:**
   - **Name:** `GOOGLE_API_KEY`
   - **Value:** Your Google AI API Key

4. **Optional - Choose your LLM provider for text-to-Mermaid generation:**
   - **Name:** `LLM_PROVIDER`
   - **Value:** `openai` (default) or `gemini`

### 2. How to Trigger the Bots

| Workflow | Action Required | What happens? |
|----------|----------------|---------------|
| **A: Text-to-Mermaid** | Create/Push a file to `source/drafts/my-note.txt` | 1. AI (GPT-4o or Gemini) reads text.<br>2. AI generates `source/mermaid/my-note.mmd`.<br>3. Render Bot detects `.mmd` and creates SVG/PNG. |
| **B: Text-to-Image** | Create/Push a file to `source/generative/hero.json` | 1. AI reads JSON prompt.<br>2. AI generates image using specified model (DALL-E 3 or Imagen 3).<br>3. Bot saves `assets/diagrams-generated/hero.png`. |
| **C: Polished Logic** | Create/Push a file to `source/polished/style.json` | 1. AI reads linked Mermaid code.<br>2. AI "draws" the logic in requested style using specified model.<br>3. Bot saves `assets/diagrams-generated/style.png`. |

---

## 🔧 AI Provider Options

This project supports both major AI ecosystems:

### Text Generation (Workflow A - Mermaid Diagrams)
- **OpenAI GPT-4o**: Excellent at understanding complex technical descriptions and generating precise Mermaid diagrams
- **Google Gemini 2.0 Flash**: Fast, cost-effective alternative with strong diagram generation capabilities

Set `LLM_PROVIDER` to choose which one to use (defaults to `openai` if not specified).

### Image Generation (Workflows B & C - Visual Diagrams)
- **OpenAI DALL-E 3**: High-quality image generation with excellent prompt following
- **Google Imagen 3**: Latest Google image generation model with strong artistic capabilities

Specify `image_model` in your JSON files to choose which image generator to use.

### Provider Combinations

You can mix and match providers:
- Use Gemini for text-to-Mermaid (faster/cheaper) + DALL-E 3 for images (high quality)
- Use GPT-4o for text-to-Mermaid (precise) + Imagen 3 for images (artistic)
- Use all Google AI (Gemini + Imagen 3) or all OpenAI (GPT-4o + DALL-E 3)

---

## 📐 Workflow A: The Precision Path

**Best for:** API flows, sequence diagrams, database schemas, and logic trees.

**LLM Options:**
- **GPT-4o** (OpenAI) - Default, excellent at understanding complex technical descriptions
- **Gemini 2.0 Flash** (Google) - Fast and cost-effective alternative

1. **Draft:** Upload rough notes to `source/drafts/`.
2. **Wait:** The bot will commit a `.mmd` file to `source/mermaid/` automatically.
3. **Refine:** Pull the changes. Open the `.mmd` file in VS Code (using the Mermaid Editor extension) to fix any logic errors manually.
4. **Publish:** The Render Bot automatically maintains the SVG/PNG versions in `assets/`.

---

## 🎨 Workflow B & C: The Visual Paths

**Best for:** High-level architecture, executive summaries, marketing assets.

- **Workflow B (Pure Generation):** Used for "vibes" and general illustrations.
- **Workflow C (Logic Enhancement):** Used when you need a specific flow (defined in Mermaid) but want it to look like a whiteboard sketch, a blueprint, or a 3D render.

### Image Model Selection

You can choose between two AI image generation models:

- **DALL-E 3** (default): OpenAI's image generation model
- **Imagen 3**: Google's latest image generation model

To specify a model, add the `image_model` field to your JSON file:

```json
{
  "prompt": "Your image prompt here",
  "image_model": "dall-e-3"
}
```

Or for Imagen 3:

```json
{
  "prompt": "Your image prompt here",
  "image_model": "imagen-3.0-generate-001"
}
```

If no `image_model` is specified, DALL-E 3 is used by default.

**Tip:** If you delete a generated image from `assets/`, the bot will regenerate it on the next run (costing API credits). If the image exists, the bot skips it to save money.

---

## 📝 Configuration Examples

### Example 1: All OpenAI
```bash
export OPENAI_API_KEY="sk-..."
export LLM_PROVIDER="openai"
```
JSON files: `"image_model": "dall-e-3"` (or omit for default)

### Example 2: All Google AI
```bash
export GOOGLE_API_KEY="..."
export LLM_PROVIDER="gemini"
```
JSON files: `"image_model": "imagen-3.0-generate-001"`

### Example 3: Mixed (Gemini for text, DALL-E for images)
```bash
export OPENAI_API_KEY="sk-..."
export GOOGLE_API_KEY="..."
export LLM_PROVIDER="gemini"
```
JSON files: `"image_model": "dall-e-3"`

---

## 🛠️ Local Development

To run the AI scripts locally (for testing without committing):

```bash
# 1. Install Python requirements
pip install -r requirements.txt

# 2. Set API Keys (at least one required)
export OPENAI_API_KEY="sk-..."          # For GPT-4o and DALL-E 3
export GOOGLE_API_KEY="..."             # For Gemini and Imagen 3

# 3. (Optional) Choose LLM provider for text-to-Mermaid
export LLM_PROVIDER="openai"            # or "gemini" (default: openai)

# 4. Run Engine
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

