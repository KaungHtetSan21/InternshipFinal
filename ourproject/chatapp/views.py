from django.shortcuts import render
from google import genai

# Create your views here.
def sendmsg(request):
    msg = request.GET['chat1']
    client = genai.Client(api_key="AIzaSyCPQA-Xqojv3JgLPTSDkyI0BPXwnJusMfU")
                      
    response = client.models.generate_content(
    model="gemini-2.0-flash", content=msg
    
    )
    return render(request, 'testchatbot.html', {'ans':response.text})


