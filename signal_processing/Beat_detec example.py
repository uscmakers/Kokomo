import wave
import numpy as np
import matplotlib.pyplot as plt
import requests
import json
import time
import pyaudio
import threading

import wave
import numpy as np
import matplotlib.pyplot as plt

from scipy.misc import electrocardiogram

from scipy.signal import find_peaks

from pytictoc import TicToc

# Read file to get buffer
ifile = wave.open("1q2e3triplet.wav")
samples = ifile.getnframes()
audio = ifile.readframes(samples)
beats = 0
timeSig = 4
newMeasure = []

# Convert buffer to float32 using NumPy
audio_as_np_int16 = np.frombuffer(audio, dtype=np.int16)
audio_as_np_float32 = audio_as_np_int16.astype(np.float32)

# Normalise float32 array so that values are between -1.0 and +1.0
max_int16 = 2**15
audio_normalised = audio_as_np_float32

t = TicToc()
t.tic()  # start clock
peaks, _ = find_peaks(audio_normalised, height=7000)
plt.plot(audio_normalised)
plt.plot(peaks, audio_normalised[peaks], "x")
plt.plot(np.zeros_like(audio_normalised), "--", color="gray")
plt.show()
t.toc()  # stop clock and print elapsed time

print(peaks)

# We need to find the peak per interval since it says one peak is multiple peaks
# By first looping through all potential peaks we can then filter out which one is indeed a PEAK
actualPeaks = []
pastPeak = -1
potentialPeaks = []

for i in peaks: # Loop thru all peaks
    currPeak = int(peaks[i])
    if pastPeak != -1: # if we are not the very first peak
        currDigitList = [int(a) for a in str(currPeak)]
        previousDigitList = [int(a) for a in str(pastPeak)]
        if len(currDigitList) != len(previousDigitList): # different number of digits, but check if it just passed over (9->0)
            firstCurrDigit = currDigitList[0]
            firstPreviousDigit = previousDigitList[0]
            if (firstCurrDigit == 1) and (currDigitList[1] == 0) and (firstPreviousDigit == 9) and (previousDigitList[1] == 9):
                # then we just passed over, BUT we could have like a giant length
                if (len(currDigitList) - len(previousDigitList)) == 1: # if we passed over it would differ by at most one
                    totalCurrDigits = len(currDigitList)
                    totalPrevDigits = totalCurrDigits - 1

                else: # different interval
                    maxIntervalPeak = max(potentialPeaks)
                    actualPeaks.append(maxIntervalPeak)
                    potentialPeaks = []

            else: # different interval
                maxIntervalPeak = max(potentialPeaks)
                actualPeaks.append(maxIntervalPeak)
                potentialPeaks = []

        else:
            print("here")
            # the lengths are the same, same number of digits, so now check if in same interval

    pastPeak = currPeak
    potentialPeaks.append(currPeak)




print(audio_normalised[peaks])
from scipy.signal import find_peaks

from pytictoc import TicToc

# We need to find the peak per interval since it says one peak is multiple peaks
# By first looping through all potential peaks we can then filter out which one is indeed a PEAK

# def getPeaks(wavFile):
#     # Read file to get buffer
#     print(wavFile)
#     ifile = wave.open(wavFile)
#     #ifile = wave.open("1q2e3triplet.wav")
#     samples = ifile.getnframes()
#     audio = ifile.readframes(samples)
#
#     # Convert buffer to float32 using NumPy
#     audio_as_np_int16 = np.frombuffer(audio, dtype=np.int16)
#     audio_as_np_float32 = audio_as_np_int16.astype(np.float32)
#
#     # Normalise float32 array so that values are between -1.0 and +1.0
#     max_int16 = 2 ** 15
#     audio_normalised = audio_as_np_float32
#
#     peaks, _ = find_peaks(audio_normalised, height=7000)
#
#     actualPeaks = []
#     pastPeak = -1
#     potentialPeaks = []
#     pastActualPeak = -1
#     for i in range(len(peaks)): # Loop thru all peaks
#         # print("Iteration: ",i)
#         currPeak = int(peaks[i])
#         if pastPeak != -1: # if we are not the very first peak
#             currDigitList = [int(a) for a in str(currPeak)]
#             previousDigitList = [int(a) for a in str(pastPeak)]
#             if len(currDigitList) != len(previousDigitList): # different number of digits, but check if it just passed over (9->0)
#                 firstCurrDigit = currDigitList[0]
#                 firstPreviousDigit = previousDigitList[0]
#                 if (firstCurrDigit == 1) and (currDigitList[1] == 0) and (firstPreviousDigit == 9) and (previousDigitList[1] == 9):
#                     # then we just passed over, BUT we could have like a giant length
#                     if (len(currDigitList) - len(previousDigitList)) == 1: # if we passed over it would differ by at most one
#                         totalCurrDigits = len(currDigitList)
#                         totalPrevDigits = totalCurrDigits - 1
#                         checkIfPassed = False
#                         for i in range(0,totalPrevDigits - 2):
#                             if previousDigitList[i] != 9:
#                                 checkIfPassed = True
#                         if checkIfPassed == True:
#                             # then this is different, we did not pass over
#                             maxIntervalPeak = max(potentialPeaks)
#                             if pastActualPeak != -1:
#                                 if maxIntervalPeak - pastActualPeak < 95:
#                                     actualPeaks.remove(pastActualPeak)
#                             pastActualPeak = maxIntervalPeak
#                             actualPeaks.append(maxIntervalPeak)
#                             potentialPeaks = []
#
#                     else: # different interval
#                         maxIntervalPeak = max(potentialPeaks)
#                         if pastActualPeak != -1:
#                             if maxIntervalPeak - pastActualPeak < 95:
#                                 actualPeaks.remove(pastActualPeak)
#                         pastActualPeak = maxIntervalPeak
#                         actualPeaks.append(maxIntervalPeak)
#                         potentialPeaks = []
#
#                 else: # different interval
#                     maxIntervalPeak = max(potentialPeaks)
#                     if pastActualPeak != -1:
#                         if maxIntervalPeak - pastActualPeak < 95:
#                             actualPeaks.remove(pastActualPeak)
#                     pastActualPeak = maxIntervalPeak
#                     actualPeaks.append(maxIntervalPeak)
#                     potentialPeaks = []
#
#             else: # the lengths are the same, same number of digits, so now check if in same interval
#                 totalDigits = len(currDigitList)
#                 checkIfPassed = False
#                 for i in range(0, totalDigits - 2):
#                     if previousDigitList[i] != currDigitList[i]:
#                         checkIfPassed = True
#                 # check the rounding case
#                 # ("Past: ", previousDigitList, "Curr: ", currDigitList)
#                 pastDigitRounded = int(previousDigitList[totalDigits-3])
#                 currDigitRounded = int(currDigitList[totalDigits - 2])
#                 # print("Last d prev: ", pastDigitRounded, "Curr d prev: ", currDigitRounded)
#                 if pastDigitRounded == currDigitRounded + 1:
#                     # print("Rounded case!")
#                     checkIfPassed = False
#                 #if currPeak - pastPeak < 90:
#                  #   checkIfPassed = False
#                 if checkIfPassed == True: # if the bool stays false then we're still in the same range
#                     maxIntervalPeak = max(potentialPeaks)
#                     if pastActualPeak != -1:
#                         if maxIntervalPeak - pastActualPeak < 95:
#                             actualPeaks.remove(pastActualPeak)
#                     pastActualPeak = maxIntervalPeak
#                     actualPeaks.append(maxIntervalPeak)
#                     potentialPeaks = []
#
#         pastPeak = currPeak
#         potentialPeaks.append(currPeak)
#
#     return actualPeaks
#
# def convertPeaksToTime(peaks):
#     hitTimes = []
#     for i in range(len(peaks)):
#         scaledPeak = peaks[i] / 100000
#         peaksTime = scaledPeak * (2.074074074074) + 0.016317037037037
#         hitTimes.append(peaksTime)
#     return hitTimes
#
# def postHitProcessing(hitTimes):
#     currTimes = hitTimes
#     print("Hit times!", hitTimes)
#     if hitTimes is not None:
#         goneThrough = False
#         flag = True
#         while goneThrough == False:
#             if len(currTimes) > 1:
#                 flag = True
#                 for i in range(1, len(currTimes)):
#                     # print("Curr i", i)
#                     # if i != len(hitTimes) - 1:
#                     hitOne = currTimes[i-1]
#                     hitTwo = currTimes[i]
#                     if float(hitTwo - hitOne) < 0.03:
#                         currTimes.remove(hitOne)
#                         flag = False
#                         break
#             if (len(currTimes) == 1) or (flag == True):
#                 goneThrough = True
#     if len(currTimes) > 1:
#         currTimes.pop(0)
#     return currTimes
#
#
# def postRequestDrumify(hitTimes):
#     if hitTimes is None:
#         return
#     original_ns = {}
#     notes = [] # list of dictionaries
#     for i in range(len(hitTimes)):
#         currNote = {}
#         currNote["pitch"] = 50
#         currNote["velocity"] = 46
#         currNote["program"] = 26
#         currNote["startTime"] = hitTimes[i]
#         currNote["endTime"] = hitTimes[i] + 0.001
#         notes.append(currNote)
#
#     original_ns["notes"] = notes
#
#     tempos = []
#     oneTempo = {}
#     oneTempo["qpm"] = 120
#     tempos.append(oneTempo)
#
#     original_ns["tempos"] = tempos
#     original_ns["totalTime"] = 4
#     original_ns["temperature"] = 1
#
#     headers = {'Content-Type': 'application/json'}
#
#     r = requests.post('https://experiments.devinmui.com/drumify', data=json.dumps(original_ns), headers=headers)
#     if r.ok:
#         return r.json()
#     return None
#
#
# def main():
#     global newMeasure
#     global beats
#     currMeasure = []
#     threads = []
#     # in seconds
#     currTime = time.perf_counter()
#     prevMeasureLastBeatTime = currTime
#     bpm = 120
#     timeSig = 4  # assume time signatures are in x/4
#     lock = threading.Lock()
#     while True:
#         newTime = time.perf_counter()
#         dt = newTime - currTime
#         currTime = newTime
#
#         # beats per second
#         newBeats = beats + bpm * dt / 60
#
#         #if int(newBeats) != int(beats):
#             #print(newBeats)
#
#         beats = newBeats
#
#         relativeMeasureCurrTime = currTime - prevMeasureLastBeatTime
#         # play
#         if len(currMeasure) > 0 and relativeMeasureCurrTime > currMeasure[0]["startTime"]:
#             currMeasure.pop(0)
#             # TODO: send MIDI
#
#         if beats > timeSig:
#             beats = 0
#             currMeasure = newMeasure
#             try:
#                 if len(threads) > 0:
#                     threads[-1].stop = True
#                 threads.append(Thread(lock))
#                 threads[-1].start()
#             except:
#                 print("ded hehe")
#             print('new measure!')
#             prevMeasureLastBeatTime = currTime
#
# class Thread(threading.Thread):
#     def __init__(self, lock):
#         threading.Thread.__init__(self)
#         self.lock = lock
#         self.stop = False
#
#     def recordAudio(self, wavOutputFileName):
#         self.lock.acquire()
#         CHUNK = 1024
#         FORMAT = pyaudio.paInt16
#         CHANNELS = 2
#         RATE = 44100
#         WAVE_OUTPUT_FILENAME = wavOutputFileName
#
#         p = pyaudio.PyAudio()
#
#         stream = p.open(format=FORMAT,
#                         channels=CHANNELS,
#                         rate=RATE,
#                         input=True,
#                         frames_per_buffer=CHUNK)
#
#         print("* recording")
#
#         frames = []
#
#         while not self.stop:
#             data = stream.read(CHUNK)
#             frames.append(data)
#
#         print("* done recording")
#
#         stream.stop_stream()
#         stream.close()
#         p.terminate()
#
#         wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
#         wf.setnchannels(CHANNELS)
#         wf.setsampwidth(p.get_sample_size(FORMAT))
#         wf.setframerate(RATE)
#         wf.writeframes(b''.join(frames))
#         wf.close()
#         self.lock.release()
#
#     def run(self):
#         # do recording
#         global newMeasure
#         wavFile = "output.wav"
#         self.recordAudio(wavFile)
#         waveFormPeaks = getPeaks(wavFile)
#         hitTimes = convertPeaksToTime(waveFormPeaks)
#         print("Pre-process", hitTimes)
#         hitTimes = postHitProcessing(hitTimes)
#         print("post-process", hitTimes)
#         if hitTimes is None:
#             return
#         grooVAEData = postRequestDrumify(hitTimes)
#         if grooVAEData is None or len(grooVAEData) == 0:
#             return
#         newMeasure = grooVAEData["notes"]
#         print("newM", grooVAEData)
#
#
# main()


