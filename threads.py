import wx
import ctypes
import requests
import threading
import mimetypes

class StoppableThread(threading.Thread):

    def __init__(self,  *args, **kwargs):
        super(StoppableThread, self).__init__(*args, **kwargs)

    def stop(self):
        self.raise_exception()

    def get_id(self):
        if hasattr(self, '_thread_id'):
            return self._thread_id
        for id, thread in threading._active.items():
            if thread is self:
                return id

    def raise_exception(self):
        thread_id = self.get_id()
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, ctypes.py_object(SystemExit))
        if res > 1:
            ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0)


class UploadThread(StoppableThread):

    def __init__(self, requestsEvent, frame, serverUrl, filePath, options, fileName):
        super(UploadThread, self).__init__()
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
            mime = mimetypes.MimeTypes().guess_type(self.filePath)[0]
            if not mime:
                mime = 'text/plain'
            self.options['Content-Type'] = mime
            response = requests.put(f'{self.serverUrl}/{self.fileName}', files={'file': (self.fileName, open(self.filePath, 'rb'), mime)}, headers=self.options, timeout=None)
        except Exception as err:
            exception = err

        wx.PostEvent(self.frame, self.requestsEvent(data=(response, exception, self.filePath), thread=threading.current_thread()))


class DeleteThread(StoppableThread):

    def __init__(self, requestsEvent, frame, deleteUrl):
        super(DeleteThread, self).__init__()
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
