from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import uvicorn
import importlib

# Import the refactored chatbot module
gemini_chatbot = importlib.import_module("gemini-chatbot")

app = FastAPI()

class ChatRequest(BaseModel):
    """
    Data model for the chat request.
    
    Attributes:
        message (str): The message sent by the user.
    """
    message: str

@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    """
    Endpoint to handle chat requests.
    
    Receives a message from the user, sends it to the Gemini chatbot,
    and returns the generated response.
    
    Args:
        request (ChatRequest): The request body containing the user's message.
        
    Returns:
        dict: A dictionary containing the chatbot's response.
    """
    response_text = gemini_chatbot.generate_response(request.message)
    return {"response": response_text}

app.mount("/", StaticFiles(directory="static", html=True), name="static")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
