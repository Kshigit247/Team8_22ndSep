import tkinter as tk
from tkinter import messagebox
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage
import os
import httpx

# Only for local dev or self-hosted endpoints
client = httpx.Client(verify=False)

# Azure OpenAI Config
AZURE_API_KEY = os.getenv("AZURE_API_KEY", "sk-h4SzToxOqOneSAXq191PXA")
AZURE_API_BASE = "https://genailab.tcs.in/"
AZURE_MODEL_NAME = "azure/genailab-maas-gpt-4o"

def ai_recommend_restaurants(location, cuisines):
    llm = ChatOpenAI(
        base_url=AZURE_API_BASE,
        model=AZURE_MODEL_NAME,
        api_key=AZURE_API_KEY,
        http_client=client,
    )

    prompt = f"""
    You are a helpful assistant. Recommend some restaurants in {location} that serve {', '.join(cuisines)} cuisine.
    Provide restaurant names and some recommended dishes.
    """

    response = llm.invoke([HumanMessage(content=prompt)])
    return response.content

# GUI Functions
def submit_inputs():
    location = location_entry.get().strip()
    cuisines_input = cuisines_entry.get().strip()
    if not location or not cuisines_input:
        messagebox.showerror("Input Error", "Please fill in all fields.")
        return
    
    cuisines = [c.strip() for c in cuisines_input.split(",")]
    result = ai_recommend_restaurants(location, cuisines)
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, result)

def clear_inputs():
    location_entry.delete(0, tk.END)
    cuisines_entry.delete(0, tk.END)
    result_text.delete("1.0", tk.END)

# Create the window
root = tk.Tk()
root.title("AI Restaurant Recommender")
root.geometry("600x400")

# Location input
tk.Label(root, text="Enter your city:").pack(pady=5)
location_entry = tk.Entry(root, width=50)
location_entry.pack(pady=5)

# Cuisine input
tk.Label(root, text="Enter preferred cuisines (comma-separated):").pack(pady=5)
cuisines_entry = tk.Entry(root, width=50)
cuisines_entry.pack(pady=5)

# Button frame to hold buttons side by side
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# Submit button
submit_btn = tk.Button(button_frame, text="Submit", command=submit_inputs)
submit_btn.pack(side=tk.LEFT, padx=5)

# Clear button
clear_btn = tk.Button(button_frame, text="Clear", command=clear_inputs)
clear_btn.pack(side=tk.LEFT, padx=5)

# Result area
result_text = tk.Text(root, height=10, wrap=tk.WORD)
result_text.pack(pady=10, fill=tk.BOTH, expand=True)

# Run the GUI
root.mainloop()
