# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.richtext

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Transfer.sh", pos = wx.DefaultPosition, size = wx.Size( 432,574 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )

		mainSizer = wx.BoxSizer( wx.VERTICAL )

		self.mainPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.mainPanel.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )

		uploadSizer = wx.BoxSizer( wx.VERTICAL )

		uploadSizer.SetMinSize( wx.Size( 1,-1 ) )
		self.topLabel = wx.StaticText( self.mainPanel, wx.ID_ANY, u"Transfer.sh - Transfer your files to the cloud", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.topLabel.Wrap( -1 )

		self.topLabel.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		uploadSizer.Add( self.topLabel, 0, wx.ALL|wx.EXPAND, 5 )

		optionDurationSizer = wx.BoxSizer( wx.HORIZONTAL )

		self.labelMaxDays = wx.StaticText( self.mainPanel, wx.ID_ANY, u"Keep for X days (Max 14 days)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelMaxDays.Wrap( -1 )

		self.labelMaxDays.SetMinSize( wx.Size( 200,-1 ) )

		optionDurationSizer.Add( self.labelMaxDays, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.optionSliderDays = wx.Slider( self.mainPanel, wx.ID_ANY, 14, 1, 14, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL|wx.SL_MIN_MAX_LABELS|wx.SL_VALUE_LABEL )
		optionDurationSizer.Add( self.optionSliderDays, 1, wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, 5 )


		uploadSizer.Add( optionDurationSizer, 0, wx.ALL|wx.EXPAND, 5 )

		optionDownloadSizer = wx.BoxSizer( wx.HORIZONTAL )

		self.labelMaxDays1 = wx.StaticText( self.mainPanel, wx.ID_ANY, u"Limit Downloads ( Unlimited: 0 )", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelMaxDays1.Wrap( -1 )

		self.labelMaxDays1.SetMinSize( wx.Size( 200,-1 ) )

		optionDownloadSizer.Add( self.labelMaxDays1, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.optionMaxDownload = wx.TextCtrl( self.mainPanel, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		optionDownloadSizer.Add( self.optionMaxDownload, 1, wx.ALL|wx.EXPAND, 5 )


		uploadSizer.Add( optionDownloadSizer, 0, wx.EXPAND|wx.ALL, 5 )

		actionUploadSizer = wx.BoxSizer( wx.HORIZONTAL )

		actionUploadSizer.SetMinSize( wx.Size( -1,1 ) )
		self.labelChooseFile = wx.StaticText( self.mainPanel, wx.ID_ANY, u"Choose File", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelChooseFile.Wrap( -1 )

		actionUploadSizer.Add( self.labelChooseFile, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.filePicker = wx.FilePickerCtrl( self.mainPanel, wx.ID_ANY, wx.EmptyString, u"Choose file to upload", u"*.*", wx.DefaultPosition, wx.Size( 150,-1 ), wx.FLP_FILE_MUST_EXIST )
		self.filePicker.SetHelpText( u"Browse your file" )

		actionUploadSizer.Add( self.filePicker, 0, wx.ALL|wx.EXPAND, 5 )

		self.btnUpload = wx.Button( self.mainPanel, wx.ID_ANY, u"UPLOAD", wx.DefaultPosition, wx.DefaultSize, wx.BU_NOTEXT )

		self.btnUpload.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_GO_UP, wx.ART_TOOLBAR ) )
		self.btnUpload.SetBitmapMargins( wx.Size( 15,1 ) )
		self.btnUpload.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, True, "Arial Black" ) )
		self.btnUpload.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.btnUpload.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		self.btnUpload.SetToolTip( u"Upload file" )
		self.btnUpload.SetHelpText( u"Upload now" )

		actionUploadSizer.Add( self.btnUpload, 1, wx.ALL, 5 )


		uploadSizer.Add( actionUploadSizer, 0, wx.EXPAND|wx.RIGHT|wx.LEFT, 1 )

		actionDeleteSizer = wx.BoxSizer( wx.HORIZONTAL )

		self.labelDeleteUrl = wx.StaticText( self.mainPanel, wx.ID_ANY, u"URL Delete", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelDeleteUrl.Wrap( -1 )

		actionDeleteSizer.Add( self.labelDeleteUrl, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.deleteUrl = wx.TextCtrl( self.mainPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_AUTO_URL )
		self.deleteUrl.SetHelpText( u"Your delete url" )

		actionDeleteSizer.Add( self.deleteUrl, 1, wx.ALL|wx.EXPAND, 5 )

		self.btnDelete = wx.Button( self.mainPanel, wx.ID_ANY, u"DELETE", wx.DefaultPosition, wx.DefaultSize, wx.BU_NOTEXT )

		self.btnDelete.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_DELETE, wx.ART_BUTTON ) )
		self.btnDelete.SetBitmapMargins( wx.Size( 15,-1 ) )
		self.btnDelete.SetHelpText( u"Delete File From URL" )

		actionDeleteSizer.Add( self.btnDelete, 0, wx.ALL|wx.EXPAND, 5 )


		uploadSizer.Add( actionDeleteSizer, 0, wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )

		self.resultBox = wx.richtext.RichTextCtrl( self.mainPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_AUTO_URL|wx.TE_READONLY|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
		self.resultBox.SetMinSize( wx.Size( -1,160 ) )

		uploadSizer.Add( self.resultBox, 0, wx.ALL|wx.EXPAND, 10 )

		bSizer9 = wx.BoxSizer( wx.VERTICAL )

		self.btnClearLog = wx.Button( self.mainPanel, wx.ID_ANY, u"Clear Log", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.btnClearLog.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_MISSING_IMAGE, wx.ART_BUTTON ) )
		bSizer9.Add( self.btnClearLog, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		uploadSizer.Add( bSizer9, 0, wx.ALIGN_RIGHT, 5 )


		self.mainPanel.SetSizer( uploadSizer )
		self.mainPanel.Layout()
		uploadSizer.Fit( self.mainPanel )
		mainSizer.Add( self.mainPanel, 0, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( mainSizer )
		self.Layout()
		self.menuBar = wx.MenuBar( 0 )
		self.menuFile = wx.Menu()
		self.menuItemOpen = wx.MenuItem( self.menuFile, wx.ID_ANY, u"Open..."+ u"\t" + u"Ctrl+O", u"Open to upload file", wx.ITEM_NORMAL )
		self.menuFile.Append( self.menuItemOpen )

		self.menuFile.AppendSeparator()

		self.menuItemExit = wx.MenuItem( self.menuFile, wx.ID_ANY, u"Exit"+ u"\t" + u"Alt+F4", u"Quit the program", wx.ITEM_NORMAL )
		self.menuFile.Append( self.menuItemExit )

		self.menuBar.Append( self.menuFile, u"&File" )

		self.menuProcess = wx.Menu()
		self.menuItemUpload = wx.MenuItem( self.menuProcess, wx.ID_ANY, u"Upload"+ u"\t" + u"CTRL+U", u"Upload selected file", wx.ITEM_NORMAL )
		self.menuProcess.Append( self.menuItemUpload )

		self.menuItemDelete = wx.MenuItem( self.menuProcess, wx.ID_ANY, u"Delete"+ u"\t" + u"CTRL+D", u"Delete file from a given url in textbox", wx.ITEM_NORMAL )
		self.menuProcess.Append( self.menuItemDelete )

		self.menuProcess.AppendSeparator()

		self.menuItemCancelAllUploads = wx.MenuItem( self.menuProcess, wx.ID_ANY, u"Cancel All Uploads"+ u"\t" + u"CTRL+SHIFT+X", u"Cancel all uploads threads", wx.ITEM_NORMAL )
		self.menuProcess.Append( self.menuItemCancelAllUploads )

		self.menuProcess.AppendSeparator()

		self.menuItemClearLog = wx.MenuItem( self.menuProcess, wx.ID_ANY, u"Clear Log"+ u"\t" + u"CTRL+L", u"Clear the result log", wx.ITEM_NORMAL )
		self.menuProcess.Append( self.menuItemClearLog )

		self.menuBar.Append( self.menuProcess, u"&Process" )

		self.menuHelp = wx.Menu()
		self.menuItemAbout = wx.MenuItem( self.menuHelp, wx.ID_ANY, u"About", u"About transfer.sh desktop client", wx.ITEM_NORMAL )
		self.menuHelp.Append( self.menuItemAbout )

		self.menuItemReportProblems = wx.MenuItem( self.menuHelp, wx.ID_ANY, u"Report Problems", u"Create a new issue on repository.", wx.ITEM_NORMAL )
		self.menuHelp.Append( self.menuItemReportProblems )

		self.menuItemVersion = wx.MenuItem( self.menuHelp, wx.ID_ANY, u"Desktop Client Version", u"Your transfer.sh desktop client version", wx.ITEM_NORMAL )
		self.menuHelp.Append( self.menuItemVersion )

		self.menuBar.Append( self.menuHelp, u"&Help" )

		self.SetMenuBar( self.menuBar )

		self.statusBar = self.CreateStatusBar( 1, wx.STB_DEFAULT_STYLE|wx.STB_SHOW_TIPS|wx.STB_SIZEGRIP, wx.ID_ANY )
		self.statusBar.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )


		self.Centre( wx.BOTH )

		# Connect Events
		self.optionSliderDays.Bind( wx.EVT_SCROLL_CHANGED, self.updateOptions )
		self.filePicker.Bind( wx.EVT_FILEPICKER_CHANGED, self.fileChangeHandler )
		self.btnUpload.Bind( wx.EVT_BUTTON, self.handleBtnUpload )
		self.btnDelete.Bind( wx.EVT_BUTTON, self.handleBtnDelete )
		self.btnClearLog.Bind( wx.EVT_BUTTON, self.handleBtnClearLog )
		self.Bind( wx.EVT_MENU, self.handleMenuItemOpen, id = self.menuItemOpen.GetId() )
		self.Bind( wx.EVT_MENU, self.handleMenuItemExit, id = self.menuItemExit.GetId() )
		self.Bind( wx.EVT_MENU, self.handleMenuItemUpload, id = self.menuItemUpload.GetId() )
		self.Bind( wx.EVT_MENU, self.handleMenuItemDelete, id = self.menuItemDelete.GetId() )
		self.Bind( wx.EVT_MENU, self.handleMenuItemCancelAllUploads, id = self.menuItemCancelAllUploads.GetId() )
		self.Bind( wx.EVT_MENU, self.handleMenuItemClearLog, id = self.menuItemClearLog.GetId() )
		self.Bind( wx.EVT_MENU, self.handleMenuItemAbout, id = self.menuItemAbout.GetId() )
		self.Bind( wx.EVT_MENU, self.handleMenuItemReportProblems, id = self.menuItemReportProblems.GetId() )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def updateOptions( self, event ):
		event.Skip()

	def fileChangeHandler( self, event ):
		event.Skip()

	def handleBtnUpload( self, event ):
		event.Skip()

	def handleBtnDelete( self, event ):
		event.Skip()

	def handleBtnClearLog( self, event ):
		event.Skip()

	def handleMenuItemOpen( self, event ):
		event.Skip()

	def handleMenuItemExit( self, event ):
		event.Skip()

	def handleMenuItemUpload( self, event ):
		event.Skip()

	def handleMenuItemDelete( self, event ):
		event.Skip()

	def handleMenuItemCancelAllUploads( self, event ):
		event.Skip()

	def handleMenuItemClearLog( self, event ):
		event.Skip()

	def handleMenuItemAbout( self, event ):
		event.Skip()

	def handleMenuItemReportProblems( self, event ):
		event.Skip()


