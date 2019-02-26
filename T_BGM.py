# NHẠC NỀN

from winsound import *
from _SETTINGS_ import BGMfile

def PlayBGM():
    PlaySound(BGMfile, SND_LOOP | SND_ASYNC)