import speech_recognition as sr

# Initialize recognizer
recognizer = sr.Recognizer()

while True:
    try:
        with sr.Microphone() as mic:
            print("Adjusting for ambient noise... Please wait.")
            recognizer.adjust_for_ambient_noise(mic, duration=0.5)
            print("Listening... Speak now (say 'stop' to exit).")
            audio = recognizer.listen(mic)

            print("Recognizing...")
            text = recognizer.recognize_google(audio)
            text = text.lower()
            print(f"Recognized text: {text}")

            # Stop the program if the user says "stop"
            if text == "stop":
                print("Stopping the program...")
                break

    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio. Please try again.")

    except sr.RequestError as e:
        print(f"Could not request results from the recognition service; {e}")
        break

    except Exception as e:
        print(f"An error occurred: {e}")
        break
