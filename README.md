# AG First Demo Project

A simple AI chatbot application built with Python, FastAPI, and Google's Gemini API. This project demonstrates how to integrate a Large Language Model (LLM) into a web application.

## Features

- **Chat Interface**: A clean, web-based chat interface.
- **Gemini Integration**: Powered by Google's `gemini-2.5-flash` model.
- **FastAPI Backend**: High-performance, easy-to-use Python web framework.
- **Interactive**: Real-time chat capabilities.

## Prerequisites

- Python 3.14 or higher
- A Google Cloud Project with the Gemini API enabled
- A Google API Key

## Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/kiran7kkbai/AG-First-Demo-Prj.git
    cd AG-First-Demo-Prj
    ```

2.  **Create and activate a virtual environment (optional but recommended):**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up Environment Variables:**
    Create a `.env` file in the root directory and add your Google API Key:
    ```env
    GOOGLE_API_KEY=your_google_api_key_here
    ```

## Usage

1.  **Start the server:**
    ```bash
    python app.py
    ```
    Or using uvicorn directly:
    ```bash
    uvicorn app:app --reload
    ```

2.  **Access the application:**
    Open your web browser and go to:
    [http://localhost:8000](http://localhost:8000)

## Project Structure

- `app.py`: The main FastAPI application file defining routes and serving the frontend.
- `gemini-chatbot.py`: Contains the logic for interacting with the Google Gemini API.
- `static/`: Directory containing frontend assets (HTML, CSS, JS).
- `requirements.txt`: List of Python dependencies.

## Technologies Used

- **FastAPI**: Web framework for building APIs.
- **Google GenAI SDK**: For accessing Gemini models.
- **HTML/CSS/JS**: For the frontend user interface.
