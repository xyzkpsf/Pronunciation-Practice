# Pronunciation-Practice
A speech recognition application for kids to practice pronunciation when learing new language.

![console](https://github.com/xyzkpsf/Pronunciation-Practice/blob/master/img/img1.JPG?raw=true)
![console](https://github.com/xyzkpsf/Pronunciation-Practice/blob/master/img/img2.JPG?raw=true)

This application uses Python's speech_recognition package, which supports many different languages, just set the language parameter as your prefer language when you call it.
For me, I mainly use on Chinese and English, I just hard code it as language='cmn-Hans-CN'.

When the program runs, it will first search all the supported voices in the current system, please make sure to select a language consistent with the one on speech recognition. 
For Windows 10, the system's voice will clearly indicate the supported languages, but I haven't tested it on Mac or other systems.

Then it takes in a txt file and display the content on a simple UI.
The Listen button will make the system read out the content, while the Speak button will trigger the voice input 
and display the content recognized by the system to test the user's pronunciation.
