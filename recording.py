import pyaudio
import wave
import keyboard
from os import listdir

chunk = 1024  # Record in chunks of 1024 samples
sample_format = pyaudio.paInt16  # 16 bits per sample
channels = 2
fs = 44100  # Record at 44100 samples per second
filename = ""

p = pyaudio.PyAudio()  # Create an interface to PortAudio

def Recording():
    stream = p.open(format=sample_format,
                channels=channels,
                rate=fs,
                frames_per_buffer=chunk,
                input=True)

    # Store data in chunks for n seconds
    frames = []  # Initialize array to store frames
    print('Start recording until press q')
    while True:
        try:  # used try so that if user pressed other than the given key error will not be shown
            data = stream.read(chunk)
            frames.append(data)
            if keyboard.is_pressed('q'):  # if key 'q' is pressed
                print('Finished recording')
                break  # finishing the loop
        except:
            break  # if user pressed a key other than the given key the loop will break

    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    # Terminate the PortAudio interface
    p.terminate()

    # Save the recorded data as a WAV file
    wf = wave.open('Wav/thoi su/'+filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()

def FileName(dir):
    all_item = listdir(dir)
    if(len(all_item)==0):
        return "1.wav"
    else:
        max = 0
        id = 0
        for i in all_item:
            if(len(i)>=max):
                max = len(i)
                last_item = int(i[0:-4]) + 1
        return str(last_item)+ ".wav"


filename = FileName('Wav/thoi su/')
print(filename)
Recording()