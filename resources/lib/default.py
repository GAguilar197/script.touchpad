import xbmcgui
import xbmc
import xbmcaddon

addon = xbmcaddon.Addon()
addon_path = addon.getAddonInfo('path')

class TouchOverlay(xbmcgui.WindowXMLDialog):
    def onInit(self):
        xbmc.log("TouchOverlay initialized", xbmc.LOGINFO)

    def onClick(self, controlId):
        xbmc.log(f"Button clicked: {controlId}", xbmc.LOGINFO)

        actions = {
            1001: "Action(Up)",
            1002: "Action(Down)",
            1003: "Action(Left)",
            1004: "Action(Right)",
            1005: "Action(Select)",
            1006: "Action(Back)"
        }

        if controlId in actions:
            xbmc.executebuiltin(actions[controlId])
        elif controlId == 9999:
            self.close()
        else:
            xbmc.log(f"Unknown button ID: {controlId}", xbmc.LOGWARNING)

dialog = TouchOverlay('touchpad.xml', addon_path)
dialog.doModal()
del dialog
