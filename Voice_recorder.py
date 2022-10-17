import sounddevice
from scipy.io.wavfile import write

# voice = open("(3) Voice_recorder.txt" , "w+")

def voice_recorder(seconds , file) :
    print("Recording started....")
    recording = sounddevice.rec((seconds * 44100) , samplerate= 44100 , channels=2)
    sounddevice.wait()
    write(file,44100,recording)
    print("Recording finishes")

voice_recorder(10 , "record.wav")
