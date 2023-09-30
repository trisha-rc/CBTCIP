import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv

#Sampling frequency
freq=44100
#Duration of recording
duration=3
#Recording the audio
recording=sd.rec(int(duration*freq),samplerate=freq,channels=2)
sd.wait()

write("recording.wav",freq,recording)
wv.write("recording1.wav",recording,freq,sampwidth=2)
