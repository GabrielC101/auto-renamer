#!/usr/bin/env python


#from /usr/src/linux/include/linux/inotify.h

IN_ACCESS = 0x00000001L         # File was accessed
IN_MODIFY = 0x00000002L         # File was modified
IN_ATTRIB = 0x00000004L         # Metadata changed
IN_CLOSE_WRITE = 0x00000008L    # Writeable file was closed
IN_CLOSE_NOWRITE = 0x00000010L  # Unwriteable file closed
IN_OPEN = 0x00000020L           # File was opened
IN_MOVED_FROM = 0x00000040L     # File was moved from X
IN_MOVED_TO = 0x00000080L       # File was moved to Y
IN_CREATE = 0x00000100L         # Subfile was created
IN_DELETE = 0x00000200L         # Subfile was delete
IN_DELETE_SELF = 0x00000400L    # Self was deleted
IN_MOVE_SELF = 0x00000800L      # Self was moved
IN_UNMOUNT = 0x00002000L        # Backing fs was unmounted
IN_Q_OVERFLOW = 0x00004000L     # Event queued overflowed
IN_IGNORED = 0x00008000L        # File was ignored

IN_ONLYDIR = 0x01000000         # only watch the path if it is a directory
IN_DONT_FOLLOW = 0x02000000     # don't follow a sym link
IN_MASK_ADD = 0x20000000        # add to the mask of an already existing watch
IN_ISDIR = 0x40000000           # event occurred against dir
IN_ONESHOT = 0x80000000         # only send event once

IN_CLOSE = IN_CLOSE_WRITE | IN_CLOSE_NOWRITE     # closes
IN_MOVED = IN_MOVED_FROM | IN_MOVED_TO           # moves
IN_CHANGED = IN_MODIFY | IN_ATTRIB               # changes

IN_WATCH_MASK = (IN_MODIFY | IN_ATTRIB |
                 IN_CREATE | IN_DELETE |
                 IN_DELETE_SELF | IN_MOVE_SELF |
                 IN_UNMOUNT | IN_MOVED_FROM | IN_MOVED_TO)


MASK_DICT = {0x00000001L:'IN_ACCESS',
             0x00000002L:'IN_MODIFY',
             0x00000004L:'IN_ATTRIB',
             0x00000008L:'IN_CLOSE_WRITE',
             0x00000010L:'IN_CLOSE_NOWRITE',
             0x00000020L:'IN_OPEN',
             0x00000040L:'IN_MOVED_FROM',
             0x00000080L:'IN_MOVED_TO',
             0x00000100L:'IN_CREATE',
             0x00000200L:'IN_DELETE',
             0x00000400L:'IN_DELETE_SELF',
             0x00000800L:'IN_MOVE_SELF',
             0x00002000L:'IN_UNMOUNT',
             0x00004000L:'IN_Q_OVERFLOW',
             0x00008000L:'IN_IGNORED',
             0x01000000:'IN_ONLYDIR',
             0x02000000:'IN_DONT_FOLLOW',
             0x20000000:'IN_MASK_ADD',
             0x40000000:'IN_ISDIR',
             0x80000000:'IN_ONESHOT'}

READABLE_DICT = {
    'IN_ACCESS': 'access',
    'IN_MODIFY': 'modify',
    'IN_ATTRIB': 'attrib',
    'IN_CLOSE_WRITE': 'close_write',
    'IN_CLOSE_NOWRITE': 'close_nowrite',
    'IN_OPEN': 'open',
    'IN_MOVED_FROM': 'moved_from',
    'IN_MOVED_TO': 'moved_to',
    'IN_CREATE': 'create',
    'IN_DELETE': 'delete',
    'IN_DELETE_SELF': 'delete_self',
    'IN_MOVE_SELF': 'move_self',
    'IN_UNMOUNT': 'unmount',
    'IN_Q_OVERFLOW': 'queue_overflow',
    'IN_IGNORED': 'ignored',
    'IN_ONLYDIR': 'only_dir',
    'IN_DONT_FOLLOW': 'dont_follow',
    'IN_MASK_ADD': 'mask_add',
    'IN_ISDIR': 'is_dir',
    'IN_ONESHOT': 'one_shot'
}

_FLAG_TO_HUMAN = [
    (IN_ACCESS, 'access'),
    (IN_MODIFY, 'modify'),
    (IN_ATTRIB, 'attrib'),
    (IN_CLOSE_WRITE, 'close_write'),
    (IN_CLOSE_NOWRITE, 'close_nowrite'),
    (IN_OPEN, 'open'),
    (IN_MOVED_FROM, 'moved_from'),
    (IN_MOVED_TO, 'moved_to'),
    (IN_CREATE, 'create'),
    (IN_DELETE, 'delete'),
    (IN_DELETE_SELF, 'delete_self'),
    (IN_MOVE_SELF, 'move_self'),
    (IN_UNMOUNT, 'unmount'),
    (IN_Q_OVERFLOW, 'queue_overflow'),
    (IN_IGNORED, 'ignored'),
    (IN_ONLYDIR, 'only_dir'),
    (IN_DONT_FOLLOW, 'dont_follow'),
    (IN_MASK_ADD, 'mask_add'),
    (IN_ISDIR, 'is_dir'),
    (IN_ONESHOT, 'one_shot')
]


class InotifyMask(object):

    def __init__(self, mask):
        self.mask = mask
        self.readable_mask = self.readable_mask(self.mask)
        self.human_readable_mask = self.human_readable_mask(self.mask)

    def human_readable_mask(self, mask):
        """
        Auxiliary function that converts an hexadecimal mask into a series
        of human readable flags.
        """
        s = []
        for k, v in _FLAG_TO_HUMAN:
            if k & mask:
                s.append(READABLE_DICT[MASK_DICT[k]])
        return s

    def readable_mask(self, mask):
        """
        Auxiliary function that converts an hexadecimal mask into a series
        of human readable flags.
        """
        s = []
        for k, v in _FLAG_TO_HUMAN:
            if k & mask:
                s.append(MASK_DICT[k])
        return s
