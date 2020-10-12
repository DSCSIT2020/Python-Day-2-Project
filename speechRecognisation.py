import speech_recognition as sp
a = sp.Recognizer()
with sp.Microphone() as source:
    audio = a.listen(source)
    text = a.recognize_google(audio)
print(text)
print("Result : " +str(eval(text)))