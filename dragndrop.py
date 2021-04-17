import wx

class DragnDrop(wx.FileDropTarget):

    def __init__(self, target):
        wx.FileDropTarget.__init__(self)
        self.target = target

    def OnDropFiles(self, x, y, files):
        if not self.__confirm(len(files)):
            return False

        for file in files:
            self.target.doUpload(file)

        return True

    def __confirm(self, totalFiles):
        word = f'These {totalFiles} files' if totalFiles > 1 else 'This file'
        r = wx.MessageDialog(None, f'{word} will be uploaded? Are you sure?','Upload Confirmation', wx.YES_NO | wx.NO_DEFAULT | wx.ICON_WARNING).ShowModal()
        return r == wx.ID_YES
