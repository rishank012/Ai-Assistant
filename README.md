# 🤖 Friday AI Assistant

Friday is a powerful, multi-modal AI assistant designed to handle everything from writing code and generating images to automating local computer tasks via voice commands. 

Powered by the Google Gemini API for advanced language and image generation, and backed by custom Python automation scripts, Friday acts as a complete personal assistant.

## ✨ Features

* **🧠 Advanced LLM Capabilities:** Powered by the Gemini API, Friday can write code, draft applications, answer complex queries, or just have a friendly, natural conversation.
* **🎨 Image Generation:** Integrated with a dedicated Gemini-compatible image generation model to create high-quality images directly from text prompts.
* **🎙️ Custom Voice Assistant:** A fully integrated voice module built with Python that can listen to your commands and speak back.
* **⚙️ System Automation:** Friday can automate local tasks, including creating files, writing documents, and interacting with your operating system to save you time.

## 🛠️ Tech Stack

* **Language:** Python 3.x
* **AI APIs:** Google Gemini API (Text & Image)
* **Voice Integration:** `SpeechRecognition`, `pyttsx3`, `playsound`,etc
* **Other Libraries:** `os`, `threading`, `tkinter`, `pyautogui`, etc

## 🚀 Installation & Setup

**1. Clone the repository:**
```bash
git clone [https://github.com/](https://github.com/)[rishank012/Ai-Assistant.git]
cd Ai-Assistant
```

**2. Install dependencies:**
```bash
pip install -r requirements.txt
```

**3. Set up your API Keys:**
* Create a `.env` file in the root directory.
* Add your Gemini API key and any other necessary keys:
```env
GEMINI_API_KEY=your_api_key_here
```

**4. Run Friday:**
```bash
python main.py
```

## 🎯 Usage

Once the application is running, you can interact with Friday by:
1. **Text Interface:** Type your prompts for code generation, chat, or image creation.
2. **Voice Commands:** Speak directly to your microphone by clicking mic button to trigger automations (e.g., "Friday, create a new text file and write a to-do list").

## 🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/[Your-Username]/friday-ai-assistant/issues).

## 📝 License
This project is [MIT](https://choosealicense.com/licenses/mit/) licensed.
