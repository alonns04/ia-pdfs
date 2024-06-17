import fitz  # PyMuPDF
from transformers import pipeline
import os
import glob

carpeta = r'c:\UNI\Materias\Desarrollo de SW\pptx-machine-learning\pdfs' # RUTA DE LA CARPETA CON PDFS

archivos_pdf = glob.glob(os.path.join(carpeta, '*.pdf'))

pdf_paths = []

for archivo in archivos_pdf:
    pdf_paths.append(archivo)


# Ejemplo de pregunta
question = input("Ingrese su pregunta: ")

def extract_text_from_pdf(pdf_paths):
    all_text = []
    for pdf_path in pdf_paths:
        text = ""
        pdf_document = fitz.open(pdf_path)
        for page_num in range(len(pdf_document)):
            page = pdf_document.load_page(page_num)
            text += page.get_text()
        all_text.append(text)
    return all_text

def answer_question_from_pdf(pdf_texts, question):
    qa_pipeline = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")
    answers = []
    for pdf_text in pdf_texts:
        result = qa_pipeline(question=question, context=pdf_text)
        answers.append(result['answer'])
    return answers

# Extraer texto de todos los archivos PDF
all_texts = extract_text_from_pdf(pdf_paths)

# Obtener respuestas para todas las PDFs
answers = answer_question_from_pdf(all_texts, question)

# Imprimir las respuestas
for idx, answer in enumerate(answers):
    print(f"Respuesta del archivo {pdf_paths[idx]}:")
    print(answer)
    print("=" * 50)  # Separador para facilitar la lectura

