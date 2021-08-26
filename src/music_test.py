from pydub import AudioSegment
from pydub.playback import play

# Input an existing wav filename
wavFile = "C:\\Users\\natha\\Coding\\Projects\\Gigakoops.wav"
# load the file into pydub
sound = AudioSegment.from_file(wavFile)
print("Playing wav file...")
# play the file
play(sound)