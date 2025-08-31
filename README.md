# 🔐 VIT Auto-CAPTCHA Extension

An intelligent browser extension that automates the CAPTCHA solving process on the VIT login page. It leverages a secure, local Flask backend powered by a fine-tuned machine learning model to provide a seamless login experience.

---

## ✨ Key Features

- 🚀 **Automated CAPTCHA Solving**: Instantly detects and solves CAPTCHAs, eliminating the need for manual entry.  
- 🖥 **Local Flask Backend**: A high-performance, local server handles complex machine learning inference.  
- 🌍 **Multi-Environment Support**: Easily switch between development and production modes with a clear configuration system.  
- 🤓 **Easy-to-Use**: Simple setup process designed to get you running in minutes.  

---

## 🛠 Tech Stack

| Component | Technology       | Description                                                        |
|----------|------------------|--------------------------------------------------------------------|
| Client   | Browser Extension | Built with JavaScript, HTML, and CSS for a lightweight, native feel. |
| Server   | Flask             | A Python micro-framework for the backend API.                     |
| Model    | TrOCR             | A Transformer-based model from Hugging Face for Optical Character Recognition (OCR). |

---

## ⚙️ Installation

1. **Clone the repository**

  *first...*
   ```bash
   git clone https://github.com/MetalFingerDev/VIT-CAPTCHA-extension.git
   ```
  *...then after everthing gets installed*
   ```bash
   cd VIT-CAPTCHA-extension
   ```

2. **Start the Flask Server**  
   Run the appropriate script for your operating system to set up the Python environment and start the Flask server.

   - **Windows**:  
     ```bash
     start_server.bat
     ```

   - **macOS / Linux**:  
     ```bash
     bash start_server.sh
     ```

3. **Load the Extension**  
   - Open your browser's extensions page (`chrome://extensions/`)  
   - Enable Developer Mode in the top-right corner  
   - Click **Load unpacked** and select the `extension/` directory from the cloned repository  

---

## 📡 API Reference

Our backend exposes a single, simple API endpoint to handle the CAPTCHA solving.

### 🔹 Solve CAPTCHA

**POST** `/api/solve`

**Request Body**:
```json
{
  "image": "base64-encoded CAPTCHA image"
}
```

**Success Response**:
```json
{
  "solution": "SOLVEDTEXT"
}
```

**Error Response**:
```json
{
  "error": "Reason for failure"
}
```

---

## 🌐 Environment Configuration

The server's behavior is controlled by environment variables. You can set these in a `.env` file in the root directory.

| Variable         | Description                                      | Example                                           |
|------------------|--------------------------------------------------|---------------------------------------------------|
| `FLASK_ENV`      | Sets the environment (development or production) | `development`                                     |
| `ALLOWED_ORIGINS`| Comma-separated list of permitted request origins| `http://localhost:3000` |

---

## 🎥 Demo

[▶️ WATCH ME](WATCHME.mp4), a live demonstration of the extension in action.  
>This video shows the automatic CAPTCHA solving process in real time.

![CAPTCHA GIF](src/static/demo.gif)
> This GIF shows the automatic CAPTCHA solving process in real time.

---

## 🗺 Roadmap

### ✅ Short-term Goals

- Implement a proper testing framework (`pytest`) for the backend API  
- Refactor the extension to use a secure messaging channel between `content.js` and `background.js`  
- Containerize the backend using Docker  
- Fine-tune the TrOCR model on a custom dataset of VIT CAPTCHAs  

### ☑️ Mid-term Goals

- Migrate from Flask's development server to Gunicorn  
- Add support for Firefox and Edge via WebExtension API  
- Implement structured logging for API and model performance  

### ✔️ Long-term Goals

- Develop algorithms for distorted/animated CAPTCHAs  
- Build a dashboard to monitor and manage extension behavior  
- Explore a plugin ecosystem for community CAPTCHA contributions  

---

## ✍️ Author

[@MetalFingerDev](https://github.com/MetalFingerDev)

---

## 🏷 References

[![TrOCR Model by anuashok](https://img.shields.io/badge/Model-TrOCR-blueviolet?style=for-the-badge&logo=huggingface)](https://huggingface.co/anuashok/ocr-captcha-v3)
[![Flask](https://img.shields.io/badge/Backend-Flask-lightgrey?style=for-the-badge&logo=flask)](https://flask.palletsprojects.com/)
[![Hugging Face](https://img.shields.io/badge/AI%20Platform-Hugging%20Face-yellow?style=for-the-badge&logo=huggingface)](https://huggingface.co/)
