import moviepy.editor as mp

def extract(inpath, outpath):
    my_clip = mp.VideoFileClip(inpath)
    my_clip.audio.write_audiofile(outpath)
