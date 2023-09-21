# Question-Answering-App-Development

**Set up your environment**

Make sure you have Python installed. Create a virtual environment and install the necessary packages:
```
python -m venv question_answering_env
source question_answering_env/bin/activate
pip install Flask transformers
```

**Rationale behind the chosen model:**

The chosen model, DistilBERT, is a lightweight version of the popular BERT (Bidirectional Encoder Representations from Transformers) model. DistilBERT is designed to be computationally efficient while retaining much of the performance of BERT. It achieves this by reducing the number of parameters and layers in the model, making it faster to train and deploy, which is particularly useful in web applications where latency matters.

In this specific use case, the model is fine-tuned for question-answering tasks using the SQuAD (Stanford Question Answering Dataset) dataset, which makes it well-suited for extracting answers from a given context based on user-provided questions.

**Preprocessing and Post-processing Steps:**

1. **Preprocessing:** The following preprocessing steps are implemented in the application:

   - The DistilBERT tokenizer is used to tokenize both the question and context. Tokenization involves breaking down text into smaller units (tokens) suitable for input to the model.
   - The tokenized inputs are then passed to the question-answering pipeline.

2. **Post-processing:** After obtaining the answer from the model, the following post-processing step is implemented:

   - The answer is extracted from the pipeline result, specifically from the `"answer"` field of the result dictionary.

**Instructions for Setting Up and Running the Application:**

To set up and run the Flask web application for question answering using DistilBERT, follow these steps:

1. **Install Required Libraries:**
   Make sure you have the necessary libraries installed. You can install them using pip:
   ```
   pip install transformers
   pip install flask
   ```

2. **Download and Import the Model:**
   The code imports the DistilBERT tokenizer and pre-trained question-answering model from the Hugging Face Transformers library.

3. **Create a Flask App:**
   The Flask web application is created with a single route, "/" (the root URL). This route serves both GET and POST requests.

4. **Handle POST Requests:**
   - When a POST request is received (usually when the user submits a form), the application extracts the question and context provided by the user.
   - It then calls the `get_answer` function to obtain an answer.
   - The answer is returned along with the question to be displayed on the web page.

5. **Create the `get_answer` Function:**
   - This function sets up a Question Answering pipeline using the DistilBERT model and tokenizer.
   - It takes the user's question and context, passes them to the pipeline, and extracts the answer from the result.

6. **Run the Application:**
   - If the script is executed directly (i.e., `__name__` is `"__main__"`), the Flask application is run with debugging enabled.
   - You can start the application by running the script.

7. **Access the Web Application:**
   - Open a web browser and navigate to `http://localhost:5000` to access the application.
   - Enter a question and context in the provided form and submit it to get the answer.

Remember to replace `"distilbert-base-cased-distilled-squad"` with a different pre-trained model if needed, and ensure that you have the required model files downloaded or cached.
