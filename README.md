# Title-genie
# ✨ TitleGenie > **AI-Powered YouTube Title &amp; Tag Generator** TitleGenie is a web application designed to help content creators optimize their YouTube videos. By leveraging advanced Natural Language Processing (NLP) models, it generates catchy, click-worthy titles and relevant, SEO-friendly tags based on a simple video description.
## 🚀 Features
*   **Smart Title Generation:** Uses the `google/flan-t5` model to create engaging titles.
*   **Keyword Extraction:** Uses `KeyBERT` to extract relevant tags for better SEO.
*   **Modern UI:** A clean, responsive interface with a glassmorphism aesthetic.
*   **Instant Results:** Get suggestions in seconds.
## 🛠️ Tech Stack
*   **Backend:** Python, Flask
*   **ML/AI:** Hugging Face Transformers, KeyBERT, PyTorch
*   **Frontend:** HTML5, CSS3, Vanilla JavaScript
*   **Deployment:** Docker (Ready)
## ⚙️ Installation & Setup
1.  **Clone the repository**
    ```bash
    git clone https://github.com/yourusername/TitleGenie.git
    cd TitleGenie
    ```
2.  **Create a virtual environment**
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate
    ```
3.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Run the application**
    ```bash
    python app.py
    ```
    *Note: The first run will download the ML models (~1GB), which may take a few minutes.*
5.  **Access the app**
    Open your browser and go to `http://127.0.0.1:5000`
## 🤝 Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.
