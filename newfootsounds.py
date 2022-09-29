import serial
import time
import csv
from pygame import mixer
import pydub
# import required libraries
from pydub import AudioSegment 
from pydub.playback import play 

walksound = r"/home/pi/Documents/sounds/walktalk_01_16bit.wav"
#r"/home/pi/Desktop/regtest2.wav"
#r"/home/pi/Documents/sounds/walktalk.wav"
#r"/home/pi/Desktop/footsounds.wav"
runsound = walksound #r"/home/pi/Desktop/testrun1.wav"
wav_file_walk = AudioSegment.from_file(file= walksound, format="wav") 
wav_file_run = AudioSegment.from_file(file= runsound, format="wav") # data type fo the file
max_volume = 1

# Serial Input Ranges
pedal_min = 460 #455
pedal_max = 1005
pedal_range = pedal_max - pedal_min
pedal_in_75 = (pedal_range * .75) + pedal_min
pedal_in_50 = (pedal_range * .5) + pedal_min
pedal_in_25 = (pedal_range * .25) + pedal_min
audible_range = pedal_range

#for PyDub
def turnvolumedown(infile, db):
    outfile = infile - db
    return outfile

#for PyDub
def turnvolumeup(infile, db):
    outfile = infile + db
    return outfile

#for PyDub
def speed_change(sound, speed=1.0):
    # Manually override the frame_rate. This tells the computer how many
    # samples to play per second
    sound_with_altered_frame_rate = sound._spawn(sound.raw_data, overrides={
         "frame_rate": int(sound.frame_rate * speed)
      })
     # convert the sound with altered frame rate to a standard frame rate
     # so that regular playback programs will work right. They often only
     # know how to play audio at standard frame rate (like 44.1k)
    return sound_with_altered_frame_rate.set_frame_rate(sound.frame_rate)

#for PyGame
def soundchange(thistrack):
    #initialize pygame mixer
    mixer.init()
    # Loading the audio
    mixer.music.load(thistrack)
    # Setting the volume
    mixer.music.set_volume(0)
    # Playing the audio on infinite loop
    mixer.music.play(loops=-1)
    return

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.flush()
    time.sleep(0.5)
    ser.write(b'at\r\n')
    
    soundchange(walksound)

    #Create State Machine
    last = cur = None
    direction_up = True
    direction_down = False
    # curtrack = r"C:\Users\char6728\Desktop\danfeet\regtest1.wav"
    while True:
        h1 = ser.readline().strip()
        # convert analog reading to float
        g3 = float(h1)
        cur = g3
        print(cur)

        # Level set g3 based minimum ambient reading (pedal_min)
        pedal_in_zero_base = cur - pedal_min + 1

        # if this has already run at least once
        if last != None:
            # if there has been no change
            if last == cur:
                continue

        # remove reading below ambient (pedal_min) from While loop
        if cur < pedal_min:
            mixer.music.set_volume(0)
            mixer.pause()
            continue

        # you have to start somewhere!!!
        if last == None:
            last = cur
        starttime = time.perf_counter()
        nowtime = time.perf_counter()

        dif = cur - last
        if dif > 0 and not direction_up:
            starttime = nowtime
        elif dif < 0 and direction_up:
            starttime = nowtime
        elif last == None:
            starttime = nowtime

        if dif > 0:
            direction_up = True
            direction_down = False
        elif dif < 0:
            direction_up = False
            direction_down = True

        if cur >= last:
            #pedal is pressing down more than before
            time_pressed_down = nowtime - starttime
            print('Pressing Down')
            print('start time is: {}'.format(str(starttime)))
            print('time elapsed is {}'.format(str(time_pressed_down)))

            if time_pressed_down == 0:
                soundchange(walksound)
                mixer.unpause()
                mixer.music.set_volume(0)
                continue

            if cur <= pedal_in_25:
                volume = (pedal_in_zero_base / pedal_range) * .25

            if cur > pedal_in_25 and cur <= pedal_in_50:
                volume = (pedal_in_zero_base / pedal_range) * .5

            if cur > pedal_in_50 and cur <= pedal_in_75:
                volume = (pedal_in_zero_base / pedal_range) * .5
                print('my pydub db = {}'.format(int((pedal_in_zero_base / pedal_range) *45)))                
                #soundchange(runsound)

            if cur > pedal_in_75:
                volume = (pedal_in_zero_base / pedal_range) + .05
                print('my pydub db = {}'.format(int((pedal_in_zero_base / pedal_range) *45)))
                #soundchange(runsound)

            # Playing the track
            mixer.unpause()
            print(volume)
            # Setting the volume
            mixer.music.set_volume(volume)

        if cur < last:
            # pedal is being released
            time_released = nowtime - starttime
            print('Releasing Pedal')
            print('start time is: {}'.format(str(starttime)))
            print('time elapsed is {}'.format(str(time_pressed_down)))

            if cur <= pedal_in_25:
                volume = 1 - (pedal_in_zero_base / pedal_range)

            if cur > pedal_in_25 and cur <= pedal_in_50:
                volume = (1 - (pedal_in_zero_base / pedal_range)) * .75

            if cur > pedal_in_50 and cur <= pedal_in_75:
                volume = (1 - (pedal_in_zero_base / pedal_range)) * .5
                # soundchange(runsound)

            if cur > pedal_in_75:
                volume = ((1 - (pedal_in_zero_base / pedal_range)) * .25) + .05
                # soundchange(runsound)

            # Playing the track
            mixer.unpause()
            print(volume)
            # Setting the volume
            mixer.music.set_volume(volume)
