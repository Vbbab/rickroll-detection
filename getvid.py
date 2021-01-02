#  Copyright (c) 2020 by Frank Huang. You may edit this code and distribute the software freely.
# Gets all videos on a webpage. If it's a youtube link then uses youtube-dl to download the main video.
import youtube_dl
import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urlparse
from utils import extractaudio
from utils.logging import write

def getvid(url):
    _u = urlparse(url)
    # If yt, we can directly get the audio file from the video
    if _u.netloc == 'www.youtube.com':
        write('getvid', 'Is YT', True)
        vidId = _u.query.split('v=')[1]
        os.chdir('temp')
        youtube_dl.main(['-x', vidId])
        os.chdir('..')
    elif _u.netloc == 'youtu.be':
        write('getvid', 'Is YT', True)
        vidId = _u.path[1:]
        os.chdir('temp')
        youtube_dl.main(['-x', vidId])
        os.chdir('..')
    else:
        # Oh boy
        resp = requests.get(url)
        page = BeautifulSoup(resp.text)
        vids = page.select('video')
        for i in vids:
            src = i.attrs['src']
            if src.startswith('blob:'):
                # Impossible to handle sadly
                pass
            else:
                _s = urlparse(src)
                filename = _s.path.split('/')[-1]
                os.chdir('temp')
                with open(filename, 'w+') as f:
                    f.write(requests.get(src).content)
                extractaudio.extract(filename, filename + '.mp3')
                os.chdir('..')
