import speech_recognition as sr

# Crear reconocedor
recognizer = sr.Recognizer()

# Usar el micrófono
with sr.Microphone() as source:
    print("Habla algo...")
    audio = recognizer.listen(source)

try:
    # Convertir audio a texto (usa modelo de Google)
    texto = recognizer.recognize_google(audio, language="es-ES")
    print("Dijiste:", texto)

except sr.UnknownValueError:
    print("No se pudo entender el audio")

except sr.RequestError:
    print("Error en el servicio")