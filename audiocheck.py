import csv
import os
import pyaudio
import wave
import uuid

from database import*


# Set the recording parameters
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"

# Initialize PyAudio
audio = pyaudio.PyAudio()

# Open the audio stream
stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)

print("Recording...")

# Record the audio
frames = []
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("Done recording.")

# Stop and close the audio stream
stream.stop_stream()
stream.close()
audio.terminate()

# Save the recorded audio to a WAV file
wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(audio.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()



# # sng=request.files['song']
# sng.save("output.wav")
import librosa
import numpy as np
y, sr = librosa.load("output.wav", mono=True)
chroma_stft = librosa.feature.chroma_stft(y=y, sr=sr)
spec_cent = librosa.feature.spectral_centroid(y=y, sr=sr)
S, phase = librosa.magphase(librosa.stft(y))
spec_bw = librosa.feature.spectral_bandwidth(y=y, sr=sr)
rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr)
zcr = librosa.feature.zero_crossing_rate(y)
mfcc = librosa.feature.mfcc(y=y, sr=sr)
toappend=[]
toappend.append(np.mean(chroma_stft))
toappend.append(np.mean(spec_cent))
toappend.append(np.mean(spec_bw))
toappend.append(np.mean(rolloff))
toappend.append(np.mean(zcr))
for e in mfcc:
    toappend.append( np.mean(e))
aatest= np.array([toappend])
import pandas as pd
a=pd.read_csv('data.csv')
attributes= a.values[:,0:25]

labels=a.values[:,25]

print("aaa",attributes)

print("bbb",labels)

from sklearn.ensemble import RandomForestClassifier

rnd=RandomForestClassifier()

rnd.fit(attributes,labels)

c=rnd.predict(np.array(aatest))
print("predicted",c)

if c[0]=='Violence':
    q="insert into emergency values(null,'1','Weaponn/Violenecedetect','0','0','pending')"
    insert(q)
    path="static/audio/"+str(uuid.uuid4())+".wav"
    # Save the recorded audio to a WAV file
    wf = wave.open(path, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    
    q="insert into request values(null,'1','request','%s','0','pending','Audio')"%(path)
    insert(q)



    





