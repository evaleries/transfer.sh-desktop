import wx
from TransferShMainFrame import TransferShMainFrame

class MainApp(wx.App):
    def OnInit(self):
        self.frame = TransferShMainFrame(None)
        self.frame.Show(True)
        self.SetTopWindow(self.frame)
        return True

if __name__ == '__main__':
    app = MainApp(0)
    app.MainLoop()
