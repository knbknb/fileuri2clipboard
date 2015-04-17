# knb Apr 2015
#package python-gi is in /usr/lib/python2.7/dist-packages
#https://python-gtk-3-tutorial.readthedocs.org/en/latest/clipboard.html
from gi.repository import Nautilus, GObject, Gtk, Gdk
#import syslog 

class ColumnExtension(GObject.GObject, Nautilus.MenuProvider):
    def __init__(self):
        self.clipboard = None
        

    def menu_activate_cb(self, menu, file):
        print "menu_activate_cb",file
    
    def set_clipboard(self, str):
        self.clipboard = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)        
        self.clipboard.set_text(str, -1)
        self.clipboard.store()

    def get_file_items(self, window, files):
        if len(files) != 1:
            return
        
        file = files[0]
        text = file.get_uri()
    
        try:
            if text != None:
                #syslog.syslog(__name__)
                self.set_clipboard(text)
                
        except Exception as e:
 #           syslog.syslog( "{}: {}".format(__name__, e))
            pass
        finally:
            # don't need this anymore. Data is one clipboard
            self.clipboard = None
            


        item = Nautilus.MenuItem(
            name="SimpleMenuExtension::Copy_Uri_to_Clipb",
            #label="Copy uri %s" % file.get_name(),
            #
            label="Copy URI",
            
            tip="Showing %s" % text
        )
        #item.connect('activate', self.menu_activate_cb, file)
        
        return [item]
