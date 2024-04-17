import os
from docx2pdf import convert


def convert_docx_to_pdf(docx_file, pdf_file):
    try:
        convert(docx_file, pdf_file)
        print("Конвертация завершена успешно!")
    except Exception as e:
        print(f"Произошла ошибка при конвертации: {e}")


def get_project_folder():
    return os.path.dirname(os.path.abspath(__file__))


def get_file_paths(project_folder):
    docx_file = os.path.join(project_folder, "88.docx")
    pdf_file = os.path.join(project_folder, "output.pdf")
    return docx_file, pdf_file


def main():
    """
    Основная функция программы.
    """
    project_folder = get_project_folder()
    docx_file, pdf_file = get_file_paths(project_folder)
    convert_docx_to_pdf(docx_file, pdf_file)


if __name__ == "__main__":
    main()
