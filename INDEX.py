from transformers import DistilBertTokenizer, DistilBertForQuestionAnswering, pipeline
from flask import Flask, request, render_template

# Load the DistilBERT tokenizer and model
tokenizer = DistilBertTokenizer.from_pretrained("distilbert-base-cased-distilled-squad")
model = DistilBertForQuestionAnswering.from_pretrained("distilbert-base-cased-distilled-squad")

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        question = request.form["question"]
        context = request.form["context"]  # Get the context from the form
        answer = get_answer(question, context)
        return render_template("index.html", question=question, answer=answer)
    return render_template("index.html")

def get_answer(question, context):
    # Create a Question Answering pipeline
    qa_pipeline = pipeline("question-answering", model=model, tokenizer=tokenizer)
    
    # Provide the context and question to the pipeline
    result = qa_pipeline(question=question, context=context)
    
    # Return the answer from the pipeline result
    return result["answer"]

if __name__ == "__main__":
    app.run(debug=True)
