# Mini-alexa
## Like Alexa, you can give input to the system via voice. Similarly, in this you can give the command via voice and it will perform several tasks based on your command.
In this python file, I have imported some libraries: 
  
[ speech_recognition, pyttsx3, pywhatkit (for access youtube functions), datetime, wikipedia, pyjokes, cv2, time ]

First of all, it will take command via listen the source and then recognize that source. After that if 'alexa' word will found in the command then it will perform the several tasks otherwise it will again listen the command.
The following are the tasks:
## **Task 1:** 
**Play the youtube song:** If 'play' will present in command then it will play the song on youtube. Suppose that when I will run the code and I will speak " Alexa play Where are you now " , then with the help of pywhatkit.playonyt() it will play that song on youtube.

**output:**
![image](https://user-images.githubusercontent.com/74066657/140491484-6030b251-843e-4543-9ee4-a272c0c79d86.png)

## **Task 2:**
**Show the present time:** If 'time' will present in the voice command then it will speak and show the time using datetime.datetime.now() fucntion. For Example: I will ask in the command "Alexa what is the time now ", so when the code recognize my voice then it will show me the current time.

**Output:**

![image](https://user-images.githubusercontent.com/74066657/140496065-986b1f4a-4bc2-413a-a764-f9e33966e8dc.png)

## **Task 3:** 
**Tell about someone:** In this task, if there will be sentence "tell me about" prsent in the voice command then it will show me the summary of lines of that person using wikipedia module. For Example, the command is "Alexa, tell me about Narendra Modi", then it will give me the summary of two lines about Narendra Modi. You can change the lines of the summary as per your own wish.

**output:**

![image](https://user-images.githubusercontent.com/74066657/140496307-d71f845b-43f5-4ab8-9ffa-031411bea33e.png)

## **Task 4:**
**Tell you joke:** If 'joke' will present in the voice command while recognizing, then it will show you a random joke using pyjokes.get_joke(). For Example: The command is "Alexa tell me some joke". So the output will be in any random joke and display you the joke.

**Output:**

![image](https://user-images.githubusercontent.com/74066657/140496199-cfe7f537-a2ca-4966-b3b9-07e5e8deaea8.png)

## **Task 5:**
**Open smile detection program:** if "Smile detection will present in the command then it will open the program of smile detection in which it will show a message whenever you will smile using opencv. In this program we use two harcascade file which automatically detect smile and face. After that we use vediocapture() method to access the default webcam. we read the images of the camera by using cap.read() and store in a img variable and we convert the image into gray color using cvtColor(). After that read the face detected in image and place x-y coordinates with width and height and draw a rectangle and with color code and its width. Lastly, we we specify now our reigion of interest i.e our face stored in a gray and initialise the smile cascade And when you will smile then it will show a message 'You are smiling'. 
## **Task 6:**
**Exit the program:** If 'Exit' will present in the command then it will close the program using exit() command.

**output:**

![image](https://user-images.githubusercontent.com/74066657/140495851-fe73d01e-1603-42f8-a63b-c134603ca4a6.png)

## **Task 7:**
**Give brief Introducion about the program:** In this task, if "Who are you" will present in the voice command, then it will tell you about the program with small introduction.

**Output:**
![image](https://user-images.githubusercontent.com/74066657/140496974-940b4bd1-3557-42c2-973f-1b138a7d64d9.png)

So these are the various tasks which will perform by this program.

**Summary:**
So basically, this program takes input via voice as command perform various operations based on the command and if there will be no Alexa present in the command then it will not perform any task.

I hope you like this

