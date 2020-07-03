from pydub import AudioSegment
import numpy as np


class BassBooster():
    # can change accentuate_db
    def __init__(self,filepath,bass=True, accentuate_db = 2, attenuate_db = 0):
        self.attenuate_db = attenuate_db
        self.accentuate_db = accentuate_db
        self.filepath = filepath
        self.bass =bass # if bass boosting then true; if treble boosting then False
        
    def bass_line_freq(self,track):
        sample_track = list(track)
        # c-value
        est_mean = np.mean(sample_track)
        # a-value
        est_std = 3 * np.std(sample_track) / (np.sqrt(2))
        bass_factor = int(round((est_std - est_mean) * 0.005))
        return bass_factor

    def bass_boost(self):
        print('Sampling the Audio')
        sample = AudioSegment.from_mp3(self.filepath)
        print('Filtering the Audio')
        if self.bass:
            filtered = sample.low_pass_filter(self.bass_line_freq(sample.get_array_of_samples()))
        else:
            filtered = sample.high_pass_filter(self.bass_line_freq(sample.get_array_of_samples()))
        print('Boosting')
        boosted = (sample - self.attenuate_db).overlay(filtered + self.accentuate_db)
        print('Writing the file')
        if self.bass:
            boosted.export(self.filepath + 'bass_boost.mp3',format = 'mp3')
        else:
            boosted.export(self.filepath + 'treble_boost.mp3',format = 'mp3')
            

b=BassBooster('attention.mp3', accentuate_db = 2,attenuate_db = 0)
b.bass_boost()
