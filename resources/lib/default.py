import xbmcgui
import xbmc
import xbmcaddon

addon = xbmcaddon.Addon()
addon_path = addon.getAddonInfo('path')

class TouchOverlay(xbmcgui.WindowXMLDialog):
    def onInit(self):
        xbmc.log("TouchOverlay initialized", xbmc.LOGINFO)

    def onClick(self, controlId):
        if controlId == 1001:
            xbmc.executebuiltin("Action(Up)")
        elif controlId == 1002:
            xbmc.executebuiltin("Action(Down)")
        elif controlId == 1003:
            xbmc.executebuiltin("Action(Left)")
        elif controlId == 1004:
            xbmc.executebuiltin("Action(Right)")
        elif controlId == 1005:
            xbmc.executebuiltin("Action(Select)")
        elif controlId == 1006:
            xbmc.executebuiltin("Action(Back)")
        elif controlId == 9999:
            self.close()
        else:
            xbmc.log(f"Unknown button clicked: {controlId}", xbmc.LOGINFO)

# Launch the overlay
dialog = TouchOverlay('touchpad.xml', addon_path)
dialog.doModal()
del dialog
