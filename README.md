🔐 VIT Auto-CAPTCHA Extension

Automatically solves and fills CAPTCHA on the VIT Bhopal login page using a Chrome Extension + Flask backend powered by a pretrained OCR model.

📌 Features

Injects directly into the VIT login page.

Detects and captures CAPTCHA images automatically.

Sends CAPTCHA to a local Flask backend.

Backend uses a Hugging Face OCR model (anuashok/ocr-captcha-v3) to solve it.

Auto-fills solution in the login form.

Watches for CAPTCHA refreshes and re-solves instantly.

📂 Repository Structure
.
├── app.py              # Flask backend entrypoint
├── test.py             # Local test script for model
├── requirements.txt    # Python dependencies
├── manifest.json       # Chrome extension manifest (v3)
├── background.js       # Background script (handles API calls)
├── content.js          # Content script (runs inside login page)
├── src/
│   ├── config.py       # Flask configuration (dev/prod)
│   ├── model.py        # OCR model (TrOCR) logic
│   ├── static/
│   │   └── image.png   # Sample CAPTCHA for testing

🔄 How It Works
Frontend (Chrome Extension)

manifest.json → Defines permissions and injects content.js only on the VIT login page.

content.js →

Waits for CAPTCHA image + input field.

Captures image (base64).

Sends it to background.js.

Fills returned solution into input.

Uses MutationObserver to detect and re-solve refreshed CAPTCHAs.

background.js →

Receives image data from content.js.

Sends POST request to Flask backend (/api/solve).

Returns solution to content.js.

Backend (Flask + Model)

app.py →

Runs Flask server (http://127.0.0.1:8008).

Defines /api/solve endpoint to accept base64 image.

Calls solve_captcha() from model.py.

Returns solution JSON.

config.py → Handles environment configs (dev vs production).

model.py →

Loads pretrained Hugging Face OCR model (anuashok/ocr-captcha-v3).

Converts image → tensor → text.

Returns solved CAPTCHA string.

test.py → Run locally to check model predictions before using extension.

⚙️ Installation
1. Backend Setup
git clone <this-repo>
cd <repo>
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt


Run Flask server:

python app.py


By default → runs at: http://127.0.0.1:8008

2. Extension Setup

Open Chrome → chrome://extensions/.

Enable Developer Mode.

Click Load Unpacked → select repo folder.

Navigate to VIT Login
.

CAPTCHA should auto-solve 🎉

🛠️ Tech Stack

Frontend: Chrome Extension (Manifest v3, JS).

Backend: Flask, Hugging Face Transformers, PyTorch.

Model: anuashok/ocr-captcha-v3
.

📊 Data Flow
sequenceDiagram
    participant User
    participant ContentJS
    participant BackgroundJS
    participant FlaskAPI
    participant Model

    User->>ContentJS: Open VIT Login Page
    ContentJS->>BackgroundJS: Send CAPTCHA (base64)
    BackgroundJS->>FlaskAPI: POST /api/solve { image }
    FlaskAPI->>Model: solve_captcha(image)
    Model-->>FlaskAPI: "ZLNQ52"
    FlaskAPI-->>BackgroundJS: { solution: "ZLNQ52" }
    BackgroundJS-->>ContentJS: Return solution
    ContentJS->>User: Autofills CAPTCHA input

🧪 Testing the Model

Run locally without extension:

python test.py


Output:

Solution from model: ZLNQ52

⚠️ Disclaimer

This project is for educational purposes only.

Use responsibly and ensure compliance with institutional policies.
