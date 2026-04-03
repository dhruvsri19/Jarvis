import os
import subprocess
import sounddevice as sd
import numpy as np
import time

def location():
    cmd = ['networksetup', '-getairportnetwork', 'en0'] #To Get Wifi's Name, en0- wificard
    result = subprocess.run(cmd, capture_output=True, text=True)
    wifi_name = result.stdout.lower()
    
    if "pesu" in wifi_name:
        return "in college"
    elif "hostel" in wifi_name:
        return "in hostel"
    else:
        return "doing sidequests"

def clap():
    threshold=0.05
    duration=0.2
    fs=44100
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    volume = np.max(np.abs(recording))
    if volume > threshold:
        return True
    return False

print("JARVIS is online and listening for a clap")

while True:
    if clap():
        print("Clap Detected, Running JARVIS Protocol")
        my_place=location()
        os.system(f"say Welcome Back Dhruv You are currently {my_place}")
        os.system("open -a 'Claude'")
        os.system("open -a 'Music'")
        os.system("open -n -a 'Antigravity'")
        time.sleep(54000)
        print("Listening for a clap again...")