import json
import os
from jinja2 import Environment, FileSystemLoader

# パス設定
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, 'data', 'career.json')
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
OUTPUT_PATH = os.path.join(BASE_DIR, 'README.md')
OUTPUT_HTML_PATH = os.path.join(BASE_DIR, 'resume.html')

def main():
    # データの読み込み
    try:
        with open(DATA_PATH, 'r', encoding='utf-8') as f:
            career_data = json.load(f)
    except FileNotFoundError:
        print(f"Error: Data file not found at {DATA_PATH}")
        return
    except json.JSONDecodeError as e:
        print(f"Error: Failed to decode JSON from {DATA_PATH}: {e}")
        return

    # テンプレート環境の設定
    try:
        env = Environment(loader=FileSystemLoader(TEMPLATE_DIR), trim_blocks=True, lstrip_blocks=True)
        md_template = env.get_template('resume_template.md')
        html_template = env.get_template('resume_template.html')
    except Exception as e:
        print(f"Error: Failed to load template: {e}")
        return

    # Markdownレンダリングと書き出し
    try:
        md_output = md_template.render(companies=career_data)
        with open(OUTPUT_PATH, 'w', encoding='utf-8') as f:
            f.write(md_output)
        print(f"Successfully generated Markdown resume at: {OUTPUT_PATH}")
    except Exception as e:
        print(f"Error: Failed to generate Markdown: {e}")

    # HTMLレンダリングと書き出し
    try:
        html_output = html_template.render(companies=career_data)
        with open(OUTPUT_HTML_PATH, 'w', encoding='utf-8') as f:
            f.write(html_output)
        print(f"Successfully generated HTML resume at: {OUTPUT_HTML_PATH}")
    except Exception as e:
        print(f"Error: Failed to generate HTML: {e}")

if __name__ == "__main__":
    main()
