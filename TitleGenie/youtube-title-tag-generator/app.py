import os
import re

os.environ["HF_HOME"] = "/tmp"
os.environ["HF_HOME"] = "/tmp/huggingface"
os.environ["TRANSFORMERS_CACHE"] = "/tmp/huggingface"
os.environ["HF_DATASETS_CACHE"] = "/tmp/huggingface"
os.environ["HF_MODULES_CACHE"] = "/tmp/huggingface"
os.environ["HF_TRANSFORMERS_CACHE"] = "/tmp/huggingface"

from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
from keybert import KeyBERT

# Initialize Flask app
app = Flask(__name__, template_folder="templates", static_folder="static")
CORS(app)

# Load model with cache
model_name = "google/flan-t5-small"
cache_dir = "/tmp/huggingface"

tokenizer = AutoTokenizer.from_pretrained(model_name, cache_dir=cache_dir)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name, cache_dir=cache_dir)

# Text generation pipeline
generator = pipeline(
    "text2text-generation",
    model=model,
    tokenizer=tokenizer,
    device=-1
)

# Initialize KeyBERT
kw_model = KeyBERT()

# Routes
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/terms")
def terms():
    return render_template("terms.html")

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok", "message": "Server is running fine"}), 200

# Generate route 
@app.route("/generate", methods=["POST"])
def generate():
    try:
        data = request.get_json()
        description = data.get("description", "").strip()

        if not description:
            return jsonify({"error": "No description provided"}), 400

        # Improved prompt
        title_prompt = f"Write a short, catchy, and click-worthy YouTube video title about: {description}"

        # Generate title with sampling to avoid repetition
        title_output = generator(
            title_prompt,
            max_length=20,       
            num_return_sequences=1,
            do_sample=True,
            top_k=50,
            top_p=0.95,
            temperature=0.7
        )

        title = title_output[0]["generated_text"]

        
        title = re.sub(r'\b(\w+)( \1\b)+', r'\1', title)

        # Generate tags
        tags = kw_model.extract_keywords(description, top_n=8)
        tags = [tag[0] for tag in tags]

        return jsonify({
            "title": title,
            "tags": tags
        })

    except Exception as e:
        return jsonify({"error": f"Error generating output: {str(e)}"}), 500

# Run app
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 7860)) 
    app.run(host="0.0.0.0", port=port)
