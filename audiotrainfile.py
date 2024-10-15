
import csv
import os
import pyaudio
import wave

def training():


    import librosa
    import pandas
    import numpy as np

    c=[]
    header = 'chroma_stft spectral_centroid spectral_bandwidth rolloff zero_crossing_rate'
    for i in range(1, 21):
        header += ' mfcc'+str(i)
    header += ' label'
    header = header.split()

    file = open('data.csv', 'w', newline='')
    with file:
        writer = csv.writer(file)
        writer.writerow(header)

    genres = 'NoViolence Violence'.split()

    for g in genres:
        for filename in os.listdir("static/data_set/"+g):
            songname = "static/data_set/"+g+"/"+filename

            aa=[]

            y, sr = librosa.load(songname, mono=True)
            chroma_stft = librosa.feature.chroma_stft(y=y, sr=sr)
            spec_cent = librosa.feature.spectral_centroid(y=y, sr=sr)

            S, phase = librosa.magphase(librosa.stft(y))

            spec_bw = librosa.feature.spectral_bandwidth(y=y, sr=sr)
            rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr)
            zcr = librosa.feature.zero_crossing_rate(y)
            mfcc = librosa.feature.mfcc(y=y, sr=sr)
            to_append = str(np.mean(chroma_stft)) +" "+str(np.mean(spec_cent)) +" "+ str(np.mean(spec_bw)) +" "+str(np.mean(rolloff)) +" "+str(np.mean(zcr))

            aa.append(np.mean(chroma_stft))
            aa.append(np.mean(spec_cent))
            aa.append(np.mean(spec_bw))
            aa.append(np.mean(rolloff))
            aa.append(np.mean(zcr))



            for e in mfcc:
                to_append += " "+str(np.mean(e))
                aa.append(np.mean(e))

            to_append +=  " "+g
            print(to_append)
            aa.append(g)

            file = open('data.csv', 'a', newline='')
            with file:
                writer = csv.writer(file)
                writer.writerow(to_append.split())


            c.append(aa)
training()