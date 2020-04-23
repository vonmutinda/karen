import speech_recognition as sr 
from app import karen

if __name__ == "__main__":
    print("Starting . . .")

    app = karen.Karen(sr) 

    while True: 
        app.run(app.command()) 
