# Bass-Booster
Pythonic way to overlay another layer of bass in songs. (Recommended to try Attention by Charlie Puth)

## Installation
This will install the library `pydub` in a virtual environment.
Just copy and paste the below code in a terminal.
```
# clone the repo
git clone https://github.com/nsidn98/Bass-Booster.git
# change directory
cd Bass-Booster
# install stuff
sh install.sh
# activate virtualenv
source ~/pydub/bin/activate
# run the python file
python3 BassBooster.py
# deactivate virtualenv
deactivate pydub  
```

This above snippet will give a bass boosted version of Attention by Charlie Puth in the same folder. You will have to change the song filepath in `BassBooster.py`

To change the amount of bass to be overlaid change the `accentuate_db` variable. But do not increase it much as the headphones/speakers may not be able to produce such low frequencies.


## Reference

[Pydub Library](https://github.com/jiaaro/pydub) by [James Robert](https://github.com/jiaaro)
