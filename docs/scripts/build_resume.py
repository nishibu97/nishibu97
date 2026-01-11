import json
import os
from jinja2 import Environment, FileSystemLoader

# パス設定
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, 'data', 'career.json')
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
OUTPUT_PATH = os.path.join(BASE_DIR, 'README.md')

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
        template = env.get_template('resume_template.md')
    except Exception as e:
        print(f"Error: Failed to load template: {e}")
        return

    # レンダリング
    try:
        output = template.render(companies=career_data)
    except Exception as e:
        print(f"Error: Failed to render template: {e}")
        return

    # 書き出し
    try:
        with open(OUTPUT_PATH, 'w', encoding='utf-8') as f:
            f.write(output)
        print(f"Successfully generated resume at: {OUTPUT_PATH}")
    except Exception as e:
        print(f"Error: Failed to write output file: {e}")

if __name__ == "__main__":
    main()
