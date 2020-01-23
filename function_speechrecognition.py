import speech_recognition as sr
import webbrowser

def speechtotext(recoganiser,microphone):
    r = recoganiser
    with microphone as source:
        print('Start Speaking...')
        audio = r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        reply = r.recognize_google(audio)
        return reply
    except:
        print('Unable to recoganise')
        return 0

if __name__ == "__main__":

    print('SPEECH RECOGNITION - SEARCH THE YOUTUBE....')
    key = speechtotext(sr.Recognizer(),sr.Microphone())
    print('You said : {}.\nIs the word correct?Reply back (yes/no)'.format(key))
    reply = speechtotext(sr.Recognizer(),sr.Microphone())
    print('You said : {}'.format(reply))
    if(reply == 'yes'):
        print("----Opening Youtube page----")
        url = "https://www.youtube.com/results?search_query="
        webbrowser.open_new(url+key)
    else:
        print('Finish and end')
        exit