import speech_recognition as sr
import pyttsx3
import pywhatkit# for access youtube functions
import datetime
import wikipedia
import pyjokes
import cv2
import time as t

listener=sr.Recognizer()#to reconize voice
engine=pyttsx3.init()# to initialize the package which will use to speak
engine.say("Hi, I am your mini Alexa")
engine.say("What can I do for you")
engine.runAndWait()
def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
    with sr.Microphone() as source:#make our microphone as resource
        engine.say('Listening')
        engine.runAndWait()
        print('Listening.........')
        voice = listener.listen(source)#listen the source
        command=listener.recognize_google(voice)#recognize that source
        command=command.lower()
        if 'alexa' not in command:#if there is a alexa then only the command will show otherwise not show
            print(command)
            run_alexa()
        elif 'alexa' in command:#if there is a alexa then only the command will show otherwise not show
            command=command.replace('alexa','')
            print(command)
        return command
def run_alexa():
    command=take_command()
    if 'play' in command:
        song=command.replace('play','')
        talk('Playing '+ song)
        talk('I will wait for 20 sec for next command')
        pywhatkit.playonyt(song)
        t.sleep(20)
        run_alexa()#play the song on youtube
    elif 'time' in command:
        time=datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('The current time is '+ time)
    elif 'tell me about' in command:
        person=command.replace('tell me about','')
        try:
            info=wikipedia.summary(person,2) # we will get summary of that topic upto 2 lines
            talk('Two lines for ' + person)
            print(info)
            talk(info)
        except:
            pass
    elif 'joke' in command:
        j=pyjokes.get_joke()
        print(j)
        talk(j)
    elif 'smile detection' in command:
        faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        smileCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')
        # opening the webcam to access the default webcam
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        while True:
            ret, img = cap.read()
            # here we read the images of the camera by using cap.read() and store in a img variable and ret is a falg which specifies that our camera is properly working or not
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            # we convert the image into gray color using cvtColor()
            faces = faceCascade.detectMultiScale(  # it will read the image and detect an object in image
                gray,  # Initialise the face cascade
                scaleFactor=1.3,  # size of the image
                minNeighbors=5,  # minimum number of object for detection in image
                minSize=(30, 30)  # minimum size of the face in an image
            )
            for (
            x, y, w, h) in faces:  # read the face detected in image and place x-y coordinates with width and height
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                # draw a rectangle and with color code and its width
                roi_gray = gray[y:y + h, x:x + w]
                # we specify now our reigion of interest i.e our face stored in a gray
                smile = smileCascade.detectMultiScale(
                    roi_gray,  # initialise the smile cascade
                    scaleFactor=1.5,
                    minNeighbors=15,
                    minSize=(25, 25),
                )
                for i in smile:
                    if len(smile) > 1:
                        cv2.putText(img, "You're Smiling", (x, y - 30), cv2.FONT_HERSHEY_SIMPLEX,
                                    2, (0, 0, 255), 3, cv2.LINE_AA)
            cv2.imshow('video', img)
            k = cv2.waitKey(30) & 0xff
            if k == 27:  # press 'ESC' to quit
                break
        cap.release()
        cv2.destroyAllWindows()

    elif 'exit' in command:
        talk('See you again, By')
        exit()

    elif 'how are you' in command:
        talk('I am gud, you say')

    elif 'love you' in command:
        print('Shut Up! I am virtual dear, not real . hahahaha')
        talk('Shut Up! I am virtual dear, not real . hahahaha')

    elif 'good' in command:
        print('great, so what can I do for you')
        talk('great, so what can I do for you')

    elif 'who are you' in command:
        talk('I am mini alexa who can perform small tasks by listen the command, like open the song on youtube, tell about something, show you the current time, also tell you a joke and many more things. you can explore me by giving me some command also. Thank you.')

    else:
        print("please tell me the command again")
        talk('please tell me the command again')


while True:
   run_alexa()
