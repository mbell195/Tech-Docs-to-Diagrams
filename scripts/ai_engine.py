import os
import glob
import json
import re
from openai import OpenAI

# Initialize Client
client = OpenAI(api_key=os.environ.get("AI_API_KEY"))

def generate_mermaid_from_text():
    """Workflow A: Watches source/drafts/*.txt -> Creates source/mermaid/*.mmd"""
    drafts = glob.glob("source/drafts/*.txt")

    try:
        system_prompt = open("prompts/mermaid-generator.md", "r").read()
    except FileNotFoundError:
        print("Error: prompts/mermaid-generator.md not found.")
        return

    for draft_path in drafts:
        base_name = os.path.basename(draft_path).replace(".txt", "")
        output_path = f"source/mermaid/{base_name}.mmd"

        # Idempotency check
        if os.path.exists(output_path):
            print(f"Skipping {base_name} (Exists)")
            continue

        print(f"Generating Mermaid for: {base_name}...")
        user_content = open(draft_path, "r").read()

        try:
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_content}
                ]
            )
            content = response.choices[0].message.content
            mermaid_code = re.search(r"```mermaid\n(.*?)\n```", content, re.DOTALL)

            if mermaid_code:
                with open(output_path, "w") as f:
                    f.write(mermaid_code.group(1))
                print(f"Saved {output_path}")
            else:
                print(f"Failed to parse Mermaid code for {base_name}")
        except Exception as e:
            print(f"API Error for {base_name}: {e}")

def generate_images():
    """Workflow B & C: Watches source/generative & polished -> Creates assets/diagrams-generated/*.png"""
    json_files = glob.glob("source/generative/*.json") + glob.glob("source/polished/*.json")

    for json_path in json_files:
        try:
            with open(json_path, "r") as f:
                meta = json.load(f)
        except json.JSONDecodeError:
            print(f"Error decoding JSON: {json_path}")
            continue

        if "output_image" in meta:
            output_path = meta["output_image"]
        else:
            base_name = os.path.basename(json_path).replace(".json", ".png")
            output_path = f"assets/diagrams-generated/{base_name}"

        if os.path.exists(output_path):
            print(f"Skipping Image {output_path} (Exists)")
            continue

        print(f"Generating Image for: {json_path}...")
        final_prompt = meta.get("prompt", "")

        # Handle Workflow C (Polished)
        if "source_logic" in meta:
            try:
                with open(meta["source_logic"], "r") as mmd:
                    mermaid_content = mmd.read()
                style_prompt = meta.get("style_prompt", "")
                final_prompt = f"Create a diagram based on this logic:\n{mermaid_content}\n\nStyle Guide:\n{style_prompt}"
            except FileNotFoundError:
                print(f"Error: Source logic file {meta['source_logic']} not found.")
                continue

        try:
            response = client.images.generate(
                model="dall-e-3",
                prompt=final_prompt,
                size="1024x1024",
                quality="hd",
                n=1,
            )
            image_url = response.data[0].url

            import requests
            img_data = requests.get(image_url).content
            with open(output_path, "wb") as handler:
                handler.write(img_data)
            print(f"Saved Image: {output_path}")

        except Exception as e:
            print(f"Failed to generate image for {json_path}: {e}")

if __name__ == "__main__":
    if not os.environ.get("AI_API_KEY"):
        print("Skipping AI generation: No AI_API_KEY found.")
    else:
        generate_mermaid_from_text()
        generate_images()
