

# Copyright 2015 TODO:
# TODO:Backup id3 tags into id3.bcpk file



#{u'art': True, u'lyrics': None, u'albumstatus': None, u'disctitle': None, u'month': None, u'channels': 2, u'genre': u'Pop', u'original_day': None, u'disc': None, u'mb_trackid': None, u'composer': None, u'year': None, u'albumdisambig': None, u'samplerate': 44100, u'tracktotal': 8, u'album': u'2 - 4am', u'asin': None, u'genres': [u'Pop'], u'albumartist_sort': None, u'date': None, u'disctotal': None, u'title': u'Never Be Another', u'media': None, u'artist_sort': None, u'mb_albumid': None, u'comments': None, u'acoustid_fingerprint': None, u'rg_album_gain': None, u'script': None, u'mb_releasegroupid': None, u'acoustid_id': None, u'rg_album_peak': None, u'albumartist_credit': None, u'catalognum': None, u'original_month': None, u'mb_artistid': None, u'track': 1, u'comp': None, u'encoder': None, u'initial_key': None, u'rg_track_gain': None, u'bitdepth': 0, u'bitrate': 320000, u'day': None, u'original_year': None, u'language': None, u'artist': u'Delilah', u'country': None, u'mb_albumartistid': None, u'bpm': None, u'label': None, 'path': u'/mnt/nfs4/storage/beets/music/Delilah/0000 - 2 - 4am [MP3-44kHz]/0001 Never Be Another.mp3', u'length': 185.159125, u'albumartist': None, u'albumtype': None, u'artist_credit': None, u'format': u'MP3', u'rg_track_peak': None, u'original_date': None, u'grouping': None}

#ajl.write('{artist}l{album}l{title}\n'.format(audiofile).encode('utf-8'))

import subprocess
from os import path
from os.path import dirname
from glob import glob

from beets.util import command_output, displayable_path, syspath
from beets.plugins import BeetsPlugin
from beets import mediafile


PLUGIN = 'id3backup'

class Id3backupPlugin(BeetsPlugin):

    def __init__(self):
        super(Id3backupPlugin, self).__init__()

        # Listeners.
        self.register_listener('write', self.write_event)

    def emitter(self, path):
        fields = list(mediafile.MediaFile.readable_fields())
        fields.remove('images')
        mf = mediafile.MediaFile(syspath(path))
        tags = {}
        for field in fields:
           tags[field] = getattr(mf, field)
        tags['art'] = mf.art is not None
        tags['path'] = displayable_path(path)
        #print tags
        return tags

    def write_event(self, item, path, tags):
        audiofile = self.emitter(path)

        destDir = dirname(item.destination()) + "/"

        with open(destDir + "id3.bcpk", "a") as fajl:
            fajl.write(audiofile['artist'].encode('utf-8')+";"+audiofile['album'].encode('utf-8')+";"+audiofile['title'].encode('utf-8')+'\n')

