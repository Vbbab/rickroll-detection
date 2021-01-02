#  Copyright (c) 2021 by Frank Huang. You may edit this code and distribute the software freely.

import moviepy.editor as mp

def extract(inpath, outpath):
    my_clip = mp.VideoFileClip(inpath)
    my_clip.audio.write_audiofile(outpath)
