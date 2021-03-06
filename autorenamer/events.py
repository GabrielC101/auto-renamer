#!/usr/bin/env python

from __future__ import absolute_import, print_function

import datetime

from twisted.python.filepath import FilePath

from autorenamer.masks import InotifyMask


class InotifyEvent(object):
    def __init__(self, mask, file_changed, watch_path):
        self.mask = InotifyMask(mask)
        self.file_changed = FilePath(file_changed)
        self.watch_path = FilePath(watch_path)
        self.time = datetime.datetime.now()