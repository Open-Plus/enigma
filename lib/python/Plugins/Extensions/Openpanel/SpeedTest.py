##by mfaraj57 https://www.tunisia-sat.com/
# 2016.09.18 10:47:13 Jerusalem Daylight Time
##MOD by openplus https://www.open-plus.es/
# 2017.02.22 17:28 Spain
TEST_PATH='/usr/lib/enigma2/python/Plugins/Extensions/Openpanel'
from Screens.Screen import Screen
from Screens.Standby import TryQuitMainloop
from Components.ConfigList import ConfigListScreen
from Components.Label import Label
from Components.ActionMap import ActionMap
from Components.ScrollLabel import ScrollLabel
from enigma import getDesktop
from enigma import eConsoleAppContainer
from Tools.Directories import copyfile, fileExists
from Plugins.Plugin import PluginDescriptor
import os




class SpeedTestScreen(Screen, ConfigListScreen):
    screenWidth = getDesktop(0).size().width()
    if screenWidth and screenWidth == 1920:
            skin = """<screen name="SpeedTestScreen" position="center,center" size="1237,769" title="Speed Test" backgroundColor="transparent" flags="wfNoBorder">
                <ePixmap position="0,0" size="1237,769" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Openpanel/icons/speed_test.png" zPosition="1" transparent="1" alphatest="blend" />
                <widget name="data" position="208,106" zPosition="4" size="824,337" font="Regular; 20" foregroundColor="white" transparent="1" halign="left" valign="top" backgroundColor="black" />
                <widget name="ping" position="313,36" zPosition="4" size="161,20" font="audiowide; 16" foregroundColor="white" transparent="1" halign="left" valign="center" backgroundColor="rds_text_bg" />
                <widget name="host" position="928,668" zPosition="4" size="254,80" font="audiowide; 21" foregroundColor="white" transparent="1" halign="left" valign="center" backgroundColor="rds_text_bg" />
                <widget name="ip" position="50,668" zPosition="4" size="254,80" font="audiowide; 21" foregroundColor="white" transparent="1" halign="left" valign="center" backgroundColor="rds_text_bg" />
                <widget name="download" position="543,58" zPosition="4" size="207,40" font="audiowide; 21" foregroundColor="white" transparent="1" halign="left" valign="center" backgroundColor="rds_text_bg" />
                <widget name="upload" position="821,58" zPosition="4" size="207,40" font="audiowide; 21" foregroundColor="white" transparent="1" halign="left" valign="center" backgroundColor="rds_text_bg" />
             </screen>"""
    else:
            skin = """<screen name="SpeedTestScreen" position="center,center" size="1237,720" title="Speed Test" backgroundColor="transparent" flags="wfNoBorder">
                <ePixmap position="0,0" size="1237,720" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Openpanel/icons/speed_test720.png" zPosition="1" transparent="1" alphatest="blend" />
                <widget name="data" position="208,106" zPosition="4" size="824,337" font="Regular; 20" foregroundColor="white" transparent="1" halign="left" valign="top" backgroundColor="black" />
                <widget name="ping" position="308,11" zPosition="4" size="161,20" font="audiowide; 16" foregroundColor="white" transparent="1" halign="left" valign="center" backgroundColor="rds_text_bg" />
                <widget name="host" position="918,636" zPosition="4" size="254,80" font="audiowide; 21" foregroundColor="white" transparent="1" halign="left" valign="center" backgroundColor="rds_text_bg" />
                <widget name="ip" position="40,636" zPosition="4" size="254,80" font="audiowide; 21" foregroundColor="white" transparent="1" halign="left" valign="center" backgroundColor="rds_text_bg" />
                <widget name="download" position="538,28" zPosition="4" size="207,40" font="audiowide; 21" foregroundColor="white" transparent="1" halign="left" valign="center" backgroundColor="rds_text_bg" />
                <widget name="upload" position="816,28" zPosition="4" size="207,40" font="audiowide; 21" foregroundColor="white" transparent="1" halign="left" valign="center" backgroundColor="rds_text_bg" />
             </screen>"""
    def __init__(self, session):
        Screen.__init__(self, session)
        self.color = '#800080'
        
        self['data'] = Label(_('Testing net speed,please wait......'))
        self['ping'] = Label(" ")
        self['host'] = Label(" ")
        self['ip'] = Label(" ")
        self['download'] = Label(" ")

        self['upload'] = Label(" ")
        self['actions'] = ActionMap(['OkCancelActions','ColorActions'],{'cancel': self.exit,'green': self.testagain}, -1)
        
        cmd="python "+TEST_PATH+"/speedtesting.pyo"
        self.finished=False
        self.data=''
        self.container = eConsoleAppContainer()
        self.container.appClosed.append(self.action)
        self.container.dataAvail.append(self.dataAvail)
        
        self.container.execute(cmd)
    def testagain(self):
        if  self.finished==False:
            return
        self['data'].setText(_("Testing net speed,please wait......"))
        self['ping'].setText("")
        cmd="python "+TEST_PATH+"/speedtesting.pyo"
        self.container.execute(cmd)
    def action(self, retval):
        print "retval",retval
        print _("finished test")
        self.finished=True
    def dataAvail(self, rstr):
            
            if rstr:
               
                self.data=self.data+rstr
                parts=rstr.split("\n")
                for part in parts:
                    if 'Alojado por' in part:
                        try:host=part.split("Alojado por")[1].split("[")[0].strip()
                        except:host=''
                        self['host'].setText(str(host))
                    if 'Test desde' in part:
                        ip=part.split("Test desde")[1].split(")")[0].replace("(","").strip()
                        self['ip'].setText(str(ip))                        
                if  "Ping" in rstr:
                    
                    try:ping =rstr.split("Ping")[1].split("\n")[0].strip()
                    except:ping=''
                    
                   
                    self['ping'].setText(str(ping))
                    
                if  "Descarga:" in rstr:
                    
                    try:download =rstr.split(":")[1].split("\n")[0].strip()
                    except:download =''
                    
                    self['download'].setText(str(download))
                    self.data=''
                    self.data=_('Testing upload speed....')    
                if  "Subida:" in rstr:
                   
                    try:upload =rstr.split(":")[1].split("\n")[0].strip()
                    except:upload =''
                    
                    self['upload'].setText(str(upload))
                    self['data'].setText(_(" Test completed,to test again press green"))
                    return
                       
                    
                self['data'].setText(self.data)
                
                                
               
                     
                     
                
    def exit(self):
        
            self.container.appClosed.remove(self.action)
            self.container.dataAvail.remove(self.dataAvail)
            self.close()


    def updateTitle(self):
        self.newtitle='speedtest'
        self.setTitle(self.newtitle)

