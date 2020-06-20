from pydub import AudioSegment
import matplotlib.pyplot as plt
from scipy.io import wavfile
from tempfile import mktemp

no_bassed_audio = 'attention.mp3'
bassed_audio = 'attention.mp3bass_boost.mp3'

print('plotting')
nb_mp3_audio = AudioSegment.from_file(no_bassed_audio, format="mp3")  # read mp3
b_mp3_audio = AudioSegment.from_file(bassed_audio, format="mp3")
wname_nb = mktemp('.wav')  # use temporary file
wname_b = mktemp('.wav')

nb_mp3_audio.export(wname_nb, format="wav")  # convert to wav
b_mp3_audio.export(wname_b, format="wav")

FS_nb, data_nb = wavfile.read(wname_nb) # read wav file
FS_b, data_b = wavfile.read(wname_b) # read wav file

transformed_nb = data_nb[:,1]
transformed_b = data_b[:,1]

#plt.specgram(transformed_nb, Fs=FS_nb, NFFT=128, noverlap=0)  # plot
#plt.specgram(transformed_b, Fs=FS_b, NFFT=128, noverlap=0)

plt.subplot(1, 2, 1)
plt.specgram(transformed_nb, Fs=FS_nb, NFFT=128, noverlap=0)
plt.title('MP3 songs')
plt.xlabel('unbassed mp3')


plt.subplot(1, 2, 2)
plt.specgram(transformed_b, Fs=FS_b, NFFT=128, noverlap=0)
plt.xlabel('bassed mp3')

plt.show()