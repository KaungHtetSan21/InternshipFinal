import speech_recognition as sr
r = sr.Recognizer()
with  sr.Microphone() as source:
    print("Talk")
    audio_text = r.listen(source)
    try:
       print("Text: "+r.recognize_google(audio_text, language='my-MM'))
    except:
 
        print("Sorry, I did not get that")
