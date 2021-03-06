import os
import wx
import wx.adv
import requests
import transfersh
import wx.lib.newevent
from dragndrop import DragnDrop
from threads import UploadThread, DeleteThread
from utils import Utils

RequestsEvent, EVT_REQUESTS = wx.lib.newevent.NewEvent()

# Implementing MainFrame
class TransferShMainFrame( transfersh.MainFrame ):
	def __init__( self, parent ):
		transfersh.MainFrame.__init__( self, parent )
		self.__version = '1.1.2'
		self.__githubRepo = 'https://github.com/evaleries/transfer.sh-desktop'

		self.serverUrl = 'http://transfer.sh'
		self.options = {
			'Max-Days': '14'
		}
		self.jobs = []
		self.idle()
		self.logOutput('Output Log: \nStart upload your files to transfer.sh')
		self.setupEventBindings()
		self.setAppIcon()
		self.setupDragnDrop()
		self.setupShortcuts()
		self.menuItemVersion.SetItemLabel(f'Version: {self.__version}')

	def setAppIcon(self):
		if not os.path.exists(Utils.resource_path('res/icon.ico')):
			return
		icon = wx.Icon()
		icon.CopyFromBitmap(wx.Bitmap(Utils.resource_path('res/icon.ico'), wx.BITMAP_TYPE_ICO))
		self.SetIcon(icon)

	def setupEventBindings(self):
		self.Bind(EVT_REQUESTS, self.requestsEventListener)
		self.Bind(wx.EVT_CLOSE, self.OnExit)

	def setupDragnDrop(self):
		dragndrop = DragnDrop(self)
		self.SetDropTarget(dragndrop)

	def setupShortcuts(self):
		self.SetAcceleratorTable(wx.AcceleratorTable([
			(wx.ACCEL_ALT, wx.WXK_F4, self.menuItemExit.GetId()),
			(wx.ACCEL_CTRL, wx.WXK_CONTROL_O, self.menuItemOpen.GetId()),
			(wx.ACCEL_SHIFT, wx.WXK_CONTROL_X, self.menuItemCancelAllUploads.GetId()),
			(wx.ACCEL_CTRL, wx.WXK_CONTROL_L, self.menuItemClearLog.GetId()),
			(wx.ACCEL_CTRL, wx.WXK_CONTROL_U, self.menuItemUpload.GetId()),
			(wx.ACCEL_CTRL, wx.WXK_CONTROL_D, self.menuItemDelete.GetId()),
			]))

	def requestsEventListener(self, event):
		if isinstance(event.thread, UploadThread):
			return self.handleEventUpload(event)
		elif isinstance(event.thread, DeleteThread):
			return self.handleEventDelete(event)

	def updateOptions(self, event=None):
		self.options['Max-Days'] = str(self.optionSliderDays.GetValue())
		if (isinstance(self.optionMaxDownload.GetValue(), int)) and self.optionMaxDownload.GetValue() > 0:
			self.options['Max-Downloads'] = str(self.optionMaxDownload.GetValue())

	def doUpload(self, filePath):
		workerThread = UploadThread(requestsEvent=RequestsEvent, frame=self, serverUrl=self.serverUrl, filePath=filePath, options=self.options, fileName=Utils.normalize_filename(filePath))
		workerThread.start()
		self.statusBar.SetStatusText(f'Uploading {filePath} ...')
		self.logOutput(f'Upload Processed with Thread ID {workerThread.ident}')
		self.jobs.append(workerThread)
		self.filePicker.SetPath('')

		return workerThread

	def doDelete(self, deleteUrl):
		workerThread = DeleteThread(requestsEvent=RequestsEvent, frame=self, deleteUrl=deleteUrl)
		workerThread.start()
		self.statusBar.SetStatusText(f'Deleting file from {deleteUrl} ...')
		self.logOutput(f'Delete Processed with Thread ID {workerThread.ident}')
		self.jobs.append(workerThread)

		return workerThread

	def handleBtnUpload(self, event):

		filePath = self.filePicker.GetPath().strip()
		if filePath == '':
			return self.logOutput("File can't be empty!").idle()
		elif not os.path.exists(filePath):
			return self.logOutput("The selected file doesn't exists on the system.").idle()

		self.updateOptions()
		self.doUpload(filePath)

	def handleEventUpload(self, event):
		try:
			response, exception, filePath = event.data

			if isinstance(response, requests.Response):
				if response.ok:
					self.logOutput(f'=============[Upload Done - {event.thread.ident}]=============')
					self.logOutput(f'File Path: {filePath}')
					if os.path.exists(filePath): self.logOutput(f'File Size: {Utils.human_readable_size(os.path.getsize(filePath))}')
					self.logOutput(f'Url Download: {response.text}')
					self.logOutput(f'Url Delete: {response.headers["X-Url-Delete"]}')
				else:
					self.logOutput(f'[{event.thread.ident}] Upload failed, got {response.status_code} response code')

			if exception:
				raise Exception(exception)

		except Exception as err:
			self.logOutput(f'Error occured: {err}')

		finally:
			self.jobs.remove(event.thread)
			self.filePicker.SetPath('')
			self.idle()

	def handleBtnDelete(self, event):
		deleteUrl = self.deleteUrl.GetValue().strip()
		if deleteUrl == '':
			return event.Skip()

		r = wx.MessageDialog(None, 'This file will be deleted. Are you sure?', 'Delete Confirmation', wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION).ShowModal()
		if r != wx.ID_YES: return

		self.doDelete(deleteUrl)

	def handleEventDelete(self, event):
		try:
			response, exception, deleteUrl = event.data

			if isinstance(response, requests.Response):
				if response.ok:
					self.logOutput(f'=============[Delete Done - {event.thread.ident}]=============')
					self.logOutput(f'File successfully deleted, URL: {deleteUrl}.')
					self.deleteUrl.SetValue('')
				else:
					self.logOutput(f'Delete failed: {response.text}, Response Code: {response.status_code}')

			if exception:
				raise Exception(exception)

		except Exception as err:
			self.logOutput(f'Error occured: {err}')

		finally:
			self.jobs.remove(event.thread)
			self.idle()

	def handleBtnClearLog(self, event):
		self.resultBox.SetValue('')

	def idle(self):
		self.statusBar.SetStatusText('Idle')

	def logOutput(self, text):
		lastVal = self.resultBox.GetValue() + "\n" if self.resultBox.GetValue().strip() != '' else ''
		self.resultBox.SetValue(lastVal + text)
		self.resultBox.ShowPosition(self.resultBox.GetLastPosition())
		return self

	def fileChangeHandler( self, event ):
		self.statusBar.SetStatusText(f'Selected file: {os.path.basename(self.filePicker.GetPath())} ({Utils.human_readable_size(os.path.getsize(self.filePicker.GetPath()))})')

	def handleMenuItemOpen(self, event):
		dlg = wx.FileDialog(parent=self, message='Select file(s) to upload', style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
		if dlg.ShowModal() == wx.ID_CANCEL: return

		self.filePicker.SetPath(dlg.GetPath())
		self.fileChangeHandler(event)

	def handleMenuItemExit(self, event):
		self.OnExit(event)

	def handleMenuItemCancelAllUploads(self, event):
		if len(self.jobs) > 0:
			r = wx.MessageDialog(None, 'Are you sure want to cancel all uploads? This may cause an error', 'Cancel All Uploads Confirmation', wx.YES_NO | wx.NO_DEFAULT | wx.ICON_WARNING).ShowModal()
			if r != wx.ID_YES: return

			self.__killAllJobs()
			self.logOutput('All uploads progress were cancelled').idle()

	def handleMenuItemClearLog(self, event):
		self.handleBtnClearLog(event)

	def handleMenuItemAbout(self, event):
		info = wx.adv.AboutDialogInfo()
		info.SetIcon(wx.Icon(Utils.resource_path('res/icon.ico'), wx.BITMAP_TYPE_ICO))
		info.SetName('Transfer.sh Desktop Client')
		info.SetVersion(self.__version)
		info.SetDescription("Transfer.sh Desktop Client is a free file-sharing software. \nAllows you to upload files to transfer.sh with ease. \nYou can drag and drop files to upload multiple files\nDelete uploaded files")
		info.SetCopyright('(C) 2021 evaleries')
		info.SetWebSite(self.__githubRepo)
		info.SetLicence('Transfer.sh Desktop Client is a free software;\nyou can redistribute it and/or modify it under the terms of the MIT License.')
		info.AddDeveloper('evaleries')
		wx.adv.AboutBox(info)

	def handleMenuItemReportProblems(self, event):
		import webbrowser
		webbrowser.open_new_tab(f'{self.__githubRepo}/issues/new/choose')

	def handleMenuItemUpload(self, event):
		self.handleBtnUpload(event)

	def handleMenuItemDelete(self, event):
		self.handleBtnDelete(event)

	def __killAllJobs(self):
		for job in self.jobs:
			if job.is_alive():
				job.stop()
				self.jobs.remove(job)

	def OnExit(self, event):
		if len(self.jobs) > 0:
			r = wx.MessageDialog(None, 'You have upload in progress. Do you want to exit? This may cause an error', 'Exit Confirmation', wx.YES_NO | wx.NO_DEFAULT | wx.ICON_WARNING).ShowModal()
			if r != wx.ID_YES: return

			self.__killAllJobs()

		wx.Exit()
