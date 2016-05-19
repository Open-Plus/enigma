# Embedded file name: /usr/lib/enigma2/python/Components/Renderer/Picon.py
import os, re, unicodedata
from Renderer import Renderer
from enigma import ePixmap, ePicLoad
from Tools.Alternatives import GetWithAlternative
from Tools.Directories import pathExists, SCOPE_SKIN_IMAGE, SCOPE_ACTIVE_SKIN, resolveFilename
from Components.Harddisk import harddiskmanager
from ServiceReference import ServiceReference
from Components.config import config, ConfigBoolean
searchPaths = []
lastPiconPath = None

def initPiconPaths():
    global searchPaths
    searchPaths = []
    for mp in ('/usr/share/enigma2/', '/'):
        onMountpointAdded(mp)

    for part in harddiskmanager.getMountedPartitions():
        mp = path = os.path.join(part.mountpoint, 'usr/share/enigma2')
        onMountpointAdded(part.mountpoint)
        onMountpointAdded(mp)


def onMountpointAdded(mountpoint):
    try:
        path = os.path.join(mountpoint, 'picon') + '/'
        if os.path.isdir(path) and path not in searchPaths:
            for fn in os.listdir(path):
                if fn.endswith('.png'):
                    print '[Picon] adding path:', path
                    searchPaths.append(path)
                    break

    except Exception as ex:
        print '[Picon] Failed to investigate %s:' % mountpoint, ex


def onMountpointRemoved(mountpoint):
    path = os.path.join(mountpoint, 'picon') + '/'
    try:
        searchPaths.remove(path)
        print '[Picon] removed path:', path
    except:
        pass


def onPartitionChange(why, part):
    if why == 'add':
        onMountpointAdded(part.mountpoint)
    elif why == 'remove':
        onMountpointRemoved(part.mountpoint)


def findPicon(serviceName):
    global lastPiconPath
    if lastPiconPath is not None:
        pngname = lastPiconPath + serviceName + '.png'
        if pathExists(pngname):
            return pngname
        else:
            return ''
    else:
        pngname = ''
        for path in searchPaths:
            if pathExists(path) and not path.startswith('/media/net'):
                pngname = path + serviceName + '.png'
                if pathExists(pngname):
                    lastPiconPath = path
                    break
            elif pathExists(path):
                pngname = path + serviceName + '.png'
                if pathExists(pngname):
                    lastPiconPath = path
                    break

        if pathExists(pngname):
            return pngname
        return ''
    return


def getPiconName(serviceName):
    sname = '_'.join(GetWithAlternative(serviceName).split(':', 10)[:10])
    pngname = findPicon(sname)
    if not pngname:
        fields = sname.split('_', 3)
        if len(fields) > 2 and fields[2] != '2':
            fields[2] = '1'
        if len(fields) > 0 and fields[0] == '4097':
            fields[0] = '1'
        pngname = findPicon('_'.join(fields))
    if not pngname:
        name = ServiceReference(serviceName).getServiceName()
        name = unicodedata.normalize('NFKD', unicode(name, 'utf_8')).encode('ASCII', 'ignore')
        name = re.sub('[^a-z0-9]', '', name.replace('&', 'and').replace('+', 'plus').replace('*', 'star').lower())
        if len(name) > 0:
            pngname = findPicon(name)
    return pngname


class MCmPicon(Renderer):

    def __init__(self):
        Renderer.__init__(self)
        self.PicLoad = ePicLoad()
        self.PicLoad.PictureData.get().append(self.updatePicon)
        self.piconsize = (0, 0)
        self.pngname = ''
        self.lastPath = None
        pngname = findPicon('picon_default')
        self.defaultpngname = None
        if not pngname:
            tmp = resolveFilename(SCOPE_ACTIVE_SKIN, 'piconmediam.png')
            if pathExists(tmp):
                pngname = tmp
            else:
                pngname = resolveFilename(SCOPE_SKIN_IMAGE, 'skin_default/piconmediam.png')
        self.nopicon = resolveFilename(SCOPE_SKIN_IMAGE, 'skin_default/piconmediam.png')
        if os.path.getsize(pngname):
            self.defaultpngname = pngname
            self.nopicon = pngname
        return

    def addPath(self, value):
        if pathExists(value):
            if not value.endswith('/'):
                value += '/'
            if value not in searchPaths:
                searchPaths.append(value)

    def applySkin(self, desktop, parent):
        attribs = self.skinAttributes[:]
        for attrib, value in self.skinAttributes:
            if attrib == 'path':
                self.addPath(value)
                attribs.remove((attrib, value))
            elif attrib == 'size':
                self.piconsize = value

        self.skinAttributes = attribs
        return Renderer.applySkin(self, desktop, parent)

    GUI_WIDGET = ePixmap

    def postWidgetCreate(self, instance):
        self.changed((self.CHANGED_DEFAULT,))

    def updatePicon(self, picInfo = None):
        ptr = self.PicLoad.getData()
        if ptr is not None:
            self.instance.setPixmap(ptr.__deref__())
            self.instance.show()
        return

    def changed(self, what):
        if self.instance:
            pngname = ''
            if what[0] == 1 or what[0] == 3:
                pngname = getPiconName(self.source.text)
                if not pathExists(pngname):
                    pngname = self.defaultpngname
                if not config.usage.showpicon.value:
                    pngname = self.nopicon
                if self.pngname != pngname:
                    if pngname:
                        self.instance.setScale(1)
                        self.instance.setPixmapFromFile(pngname)
                        self.instance.show()
                    else:
                        self.instance.hide()
                    self.pngname = pngname


harddiskmanager.on_partition_list_change.append(onPartitionChange)
initPiconPaths()