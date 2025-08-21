from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage
import os
import httpx

# Only for local dev or self-hosted endpoints
client = httpx.Client(verify=False)
# NEW api key   9b5ad71b2ce5302211f9c61530b329a4922fc6a4
# Model "azure/genailab-maas-DeepSeek-V3-0324"
# Set your Azure OpenAI config (replace with your actual values)
AZURE_API_KEY = os.getenv("AZURE_API_KEY", "sk-h4SzToxOqOneSAXq191PXA")
AZURE_API_BASE = "https://genailab.tcs.in/"
AZURE_MODEL_NAME =  "azure/genailab-maas-gpt-4o"

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

if __name__ == "__main__":
    location = input("Enter your city: ")
    cuisines = input("Enter preferred cuisines (comma-separated): ").split(",")
    recommendation = ai_recommend_restaurants(location.strip(), [c.strip() for c in cuisines])
    print("\nAI Recommendations:\n", recommendation)
