from google import genai

client = genai.Client(api_key="AIzaSyCPQA-Xqojv3JgLPTSDkyI0BPXwnJusMfU")
                      
response = client.models.generate_content(
    model="gemini-2.0-flash", 
    
        contents="What is AI" )
print(response.text)