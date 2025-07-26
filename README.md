## AI Chatbot Interface (Streamlit + Ollama/OpenAI)

A chatbot built with **Streamlit**, supporting both **OpenAI's GPT models** and **Ollama's local LLMs** like `llama3.2`. This app provides seamless switching between cloud and local AI models, making it versatile for both offline and API-driven use cases.

---

### Features

* Conversational memory with chat history
* Toggle between **Ollama (local)** and **OpenAI (cloud)**
* Context-aware replies with limited memory span
* Simple, minimalistic UI using **Streamlit**

---

### 🗂️ Project Structure

```
📁 ai-chatbot
├── gui.py           # Streamlit-based frontend with model switch
├── main.py          # Backend logic for generating chatbot responses
```

---

### Requirements

#### Python Packages

Install them using pip:

```bash
pip install streamlit openai ollama
```

#### Optional: Ollama (for local LLMs)

To use `ollama` (e.g., `llama3.2`) locally:

1. Install from [https://ollama.com](https://ollama.com)
2. Run Ollama server:

   ```bash
   ollama serve
   ```
3. Pull a model:

   ```bash
   ollama pull llama3
   ```

#### OpenAI API Key

Create a `.streamlit/secrets.toml` file:

```toml
OPENAI_API_KEY = "your-api-key-here"
```

---

### How to Run

Run the Streamlit app:

```bash
streamlit run gui.py
```

---

### Switching Between Models

In the sidebar:

* Click **“Switch Model”** to toggle between:

  * `ollama`: uses local `llama3.2` via `ollama` client
  * `openai`: uses `gpt-4` or `gpt-3.5` via OpenAI API

Chat memory is handled independently for both models.

---

### Author

GitHub: [@ridazfr](https://github.com/ridazfr)

---

### License

This project is licensed under the MIT License.

---
