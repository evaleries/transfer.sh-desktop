import wx
import requests
import threading

class UploadThread(threading.Thread):

    def __init__(self, requestsEvent, frame, serverUrl, filePath, options, fileName):
        threading.Thread.__init__(self)
        self.serverUrl = serverUrl
        self.filePath = filePath
        self.fileName = fileName
        self.options = options
        self.frame = frame
        self.requestsEvent = requestsEvent
        self.daemon = True

    def run(self):
        exception = None
        response = None

        try:
            response = requests.put(f'{self.serverUrl}/{self.fileName}', files={'file': open(self.filePath, 'rb')}, headers=self.options, timeout=None)
        except Exception as err:
            exception = err

        wx.PostEvent(self.frame, self.requestsEvent(data=(response, exception, self.filePath), thread=threading.current_thread()))


class DeleteThread(threading.Thread):

    def __init__(self, requestsEvent, frame, deleteUrl):
        threading.Thread.__init__(self)
        self.deleteUrl = deleteUrl
        self.frame = frame
        self.requestsEvent = requestsEvent
        self.daemon = True

    def run(self):
        exception = None
        response = None

        try:
            response = requests.delete(self.deleteUrl)
        except Exception as err:
            exception = err

        wx.PostEvent(self.frame, self.requestsEvent(data=(response, exception, self.deleteUrl), thread=threading.current_thread()))