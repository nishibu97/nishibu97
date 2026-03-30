import os
from weasyprint import HTML

# パス設定
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INPUT_HTML_PATH = os.path.join(BASE_DIR, 'resume.html')
OUTPUT_PDF_PATH = os.path.join(BASE_DIR, 'resume.pdf')


def main():
    if not os.path.exists(INPUT_HTML_PATH):
        print(f"Error: HTML file not found at {INPUT_HTML_PATH}")
        return

    HTML(filename=INPUT_HTML_PATH).write_pdf(OUTPUT_PDF_PATH)
    print(f"Successfully generated PDF at: {OUTPUT_PDF_PATH}")


if __name__ == "__main__":
    main()
