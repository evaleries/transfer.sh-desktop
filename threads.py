import wx
import requests
import threading

class UploadThread(threading.Thread):

    def __init__(self, ItemActivated, frame, serverUrl, filePath, options, fileName):
        self.serverUrl = serverUrl
        self.filePath = filePath
        self.fileName = fileName
        self.options = options
        self.frame = frame
        self.ItemActivated = ItemActivated
        threading.Thread.__init__(self)

    def run(self):
        exception = None
        response = None

        try:
            response = requests.put(f'{self.serverUrl}/{self.fileName}', files={'file': open(self.filePath, 'rb')}, headers=self.options, timeout=None)
        except Exception as err:
            exception = err

        wx.PostEvent(self.frame, self.ItemActivated(data=(response, exception, self.filePath), thread=threading.current_thread()))


class DeleteThread(threading.Thread):

    def __init__(self, ItemActivated, frame, deleteUrl):
        self.deleteUrl = deleteUrl
        self.frame = frame
        self.ItemActivated = ItemActivated
        threading.Thread.__init__(self)

    def run(self):
        exception = None
        response = None

        try:
            response = requests.delete(self.deleteUrl)
        except Exception as err:
            exception = err

        wx.PostEvent(self.frame, self.ItemActivated(data=(response, exception, self.deleteUrl), thread=threading.current_thread()))
