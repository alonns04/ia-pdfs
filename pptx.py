import fitz  # PyMuPDF
from transformers import pipeline

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

# Lista de rutas de archivos PDF
pdf_paths = [
    r'c:\UNI\Materias\Desarrollo de SW\pptx-machine-learning\pdfs\ClaseI.pdf',
    r'c:\UNI\Materias\Desarrollo de SW\pptx-machine-learning\pdfs\ClaseII.pdf',
    r'c:\UNI\Materias\Desarrollo de SW\pptx-machine-learning\pdfs\ClaseIII.pdf',
    r'c:\UNI\Materias\Desarrollo de SW\pptx-machine-learning\pdfs\ClaseIV.pdf',
    r'c:\UNI\Materias\Desarrollo de SW\pptx-machine-learning\pdfs\ClaseV.pdf',
    r'c:\UNI\Materias\Desarrollo de SW\pptx-machine-learning\pdfs\ClaseVI.pdf',
    r'c:\UNI\Materias\Desarrollo de SW\pptx-machine-learning\pdfs\ClaseVII.pdf',
    r'c:\UNI\Materias\Desarrollo de SW\pptx-machine-learning\pdfs\ClaseVIII.pdf'
]

# Extraer texto de todos los archivos PDF
all_texts = extract_text_from_pdf(pdf_paths)

# Ejemplo de pregunta
question = " debe el diseño traducirse en una forma legible para la máquina?"

# Obtener respuestas para todas las PDFs
answers = answer_question_from_pdf(all_texts, question)

# Imprimir las respuestas
for idx, answer in enumerate(answers):
    print(f"Respuesta del archivo {pdf_paths[idx]}:")
    print(answer)
    print("=" * 50)  # Separador para facilitar la lectura

