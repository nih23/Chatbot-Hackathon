import os
from langchain.llms import HuggingFaceTextGenInference, OpenAI
from dotenv import load_dotenv
load_dotenv()


def getLLM_openai(): #openai API key kommt aus der .env Datei
    return OpenAI(request_timeout=10, model_name="gpt-4-turbo-preview")


def getLLM_TGI(): 
     llm = HuggingFaceTextGenInference(inference_server_url=os.environ['TGI_URL'], max_new_tokens=2048, top_k=10, top_p=0.95, typical_p=0.95, temperature=0.01, repetition_penalty=1.03) 
     return llm