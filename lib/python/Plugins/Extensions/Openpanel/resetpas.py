import sys
import os
from Components.ActionMap import ActionMap
from Components.Pixmap import Pixmap
from Components.ConfigList import ConfigListScreen
from Components.Label import Label
from datetime import datetime
from time import strftime
from Screens.Screen import Screen
from Screens.MessageBox import MessageBox
from enigma import getDesktop

class resetpasScreen(Screen, ConfigListScreen):
    screenWidth = getDesktop(0).size().width()
    if screenWidth and screenWidth == 1920:
            skin = """<screen name="resetpasScreen" position="center,center" size="1920,1080" backgroundColor="transparent" flags="wfNoBorder">
  <ePixmap pixmap="Openpanel/icons/fpassword.png" position="363,447" size="250,250" alphatest="blend" zPosition="-11" />
  <widget name="data" position="645,318" zPosition="4" size="890,501" font="Regular; 22" foregroundColor="white" transparent="1" halign="left" valign="top" backgroundColor="background" />
  <widget source="Title" transparent="1" render="Label" zPosition="2" valign="center" halign="left" position="365,235" size="1125,50" font="Regular; 32" backgroundColor="background" foregroundColor="white" noWrap="1" />
  <eLabel position="center,center" size="1288,808" transparent="0" zPosition="-15" backgroundColor="background" />
  <eLabel position="640,312" size="901,514" transparent="0" foregroundColor="white" backgroundColor="black" zPosition="-10" />
  <eLabel position="887,847" size="36,36" transparent="0" foregroundColor="white" backgroundColor="green" zPosition="1" />
  <eLabel position="647,847" size="36,36" transparent="0" foregroundColor="white" backgroundColor="red" zPosition="1" />
  <widget name="key_red" render="Label" position="689,847" size="195,35" zPosition="1" font="Regular; 25" backgroundColor="background" transparent="1" foregroundColor="white" />
  <widget name="key_green" render="Label" position="929,847" size="195,35" zPosition="1" font="Regular; 25" backgroundColor="background" transparent="1" foregroundColor="white" />
</screen>"""
    else:
            skin = """<screen name="resetpasScreen" position="center,center" size="1280,720" backgroundColor="transparent" flags="wfNoBorder">
  <ePixmap alphatest="blend" pixmap="Openpanel/icons/setup1.png" position="920,230" size="256,256" transparent="1" zPosition="2" />
  <widget name="data" position="70,108" zPosition="4" size="800,415" font="Regular; 20" foregroundColor="white" transparent="1" halign="left" valign="top" backgroundColor="black" />
  <eLabel position="341,620" size="36,36" transparent="0" backgroundColor="green" zPosition="1" />
  <eLabel position="67,620" size="36,36" transparent="0" backgroundColor="red" zPosition="1" />
  <widget name="key_red" render="Label" position="109,620" size="195,35" zPosition="1" font="Regular; 25" transparent="1" />
  <widget name="key_green" render="Label" position="383,620" size="195,35" zPosition="1" font="Regular; 25" transparent="1" />
  <eLabel backgroundColor="background" position="40,25" size="1205,650" zPosition="-10" />
  <widget source="Title" transparent="1" render="Label" font="Regular; 28" zPosition="2" valign="center" halign="left" position="70,47" size="800,43" noWrap="1" />
</screen>"""
                
    def __init__(self, session):
        Screen.__init__(self, session)
        self['data'] = Label(_('To reset your password, press green button and please wait... or Exit'))
        self["key_red"] = Label(_("Exit"))
        self["key_green"] = Label(_("Reset"))
        self.setTitle(_("OpenPlus Reset Pass"))
        self['actions'] = ActionMap(['OkCancelActions','ColorActions'],{'cancel': self.exit, 'red': self.exit, 'green': self.reset,})
        
    def reset(self):
        numeros = datetime.now().strftime('%Y%m%d%H%M%S%f')
        otro = open('/var/volatile/tmp/systemop'+str(numeros),'w+')
        otro.write ( "reset_root_passwd ")
        otro.close()
        self.session.open(MessageBox, _("Password was reset to blank"), MessageBox.TYPE_INFO, timeout=4)
    
    def exit(self):
        self.close()
    
    def skintrad(self):
        self['data1'] = Label(_('PHOTO'))
        self['data2'] = Label(_('YouTube search'))
        self['data3'] = Label(_('MY MOVIE'))
        self['data4'] = Label(_(' Translation Plugins:'))
        self['data5'] = Label(_(' Translation of Enigma:'))
        self['data6'] = Label(_('CHOOSE THE CHANNEL TO RECORD , AND THEN PRESS BLUE BUTTON'))
        self['data7'] = Label(_('                                      RECORD PROGRAM'))
        self['data8'] = Label(_('       +MORE INFO '))
        self['data9'] = Label(_('MUSIC'))
        self['data11'] = Label(_('CHANNELS'))
        self['data12'] = Label(_('LIST'))
        self['data13'] = Label(_('MULTIGUID'))
        self['data14'] = Label(_('GUIDE'))
        self['data15'] = Label(_('DESCRIPTION'))
        self['data16'] = Label(_('PROGRAMS TV'))
        self['data17'] = Label(_('SEARCH'))
        self['data18'] = Label(_('CLICK      TO RECORD SELECTED PROGRAM'))
        self['data19'] = Label(_("You're watching..."))
        self['data20'] = Label(_('Program Duration:'))
        self['data21'] = Label(_('Playback Time:'))
        self['data22'] = Label(_('SYS-Temp: %s'))
        self['data23'] = Label(_('CPU-Speed: %s MHz'))
        self['data24'] = Label(_('CPU-Temp: %s'))
        self['data25'] = Label(_('CPU-Load: %s'))
        self['data26'] = Label(_('Flash Memory free: %s MByte'))
        self['data27'] = Label(_('Active video downloads'))
        self['data28'] = Label(_('First configure IP and port of the server and click save... Then Press the yellow button to configure channel list and sent to another receiver in your network. Press blue button to download the list m3u media/hdd.'))
        self['data29'] = Label(_('First configure Ip user and password of your receiver client and then press the green button to send channel list to another receiver of your network.'))
        self['data30'] = Label(_('Building server and clients in the background... \nOnce finished, you will see a message on the screen, and the configurations will already be created. \n\nYou can transfer the settings from: \netc/openvpn/client1-android \netc/openvpn/client2-ipad \netc/openvpn/client3-pc_lin \n\nYou should now configure your IP range in the server.conf eg: push route 192.168.1.0 255.255.255.0 in /etc/openvpn. Then on each generated client.ovpn remember to put the public ip or Dyndns where the server is hosted and the port if you want to change it, (remember to open it on the router for the IP of the server) eg: remote my.dyndns.org 1194. \n\nNote: Be sure to restart the OpenVPN Server after you make the changes. And to automatically start OpenVPN, choose the option in the OpenPlus graphical user interface!'))
        