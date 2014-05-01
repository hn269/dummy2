#!/usr/bin/env python
#
# \Dropbox\Reasearch_Nguyen\Dummy2\dummy2\
# Hoang Long Nguyen (hn269@cornell.edu)
# 2014/04/21
#
# 

"""
The Python Documentation and Release Project
============================================

The dummy2a program
--------------------

This program is to test the functioning and compatibility of ReadTheDocs and Git 
with executables generated from Python codes.

This program is an example of coding for a simple text editor with GUI by wxPython.

"""

import wx
import os.path

class MainWindow(wx.Frame):
    """ We simply derive a new class of Frame. """
    def __init__(self, filename='untitled.txt'):
        # A "-1" in the size parameter instructs wxWidgets to use the default size.
        # In this case, we select 200px width and the default height.
        super(MainWindow, self).__init__(None, size=(-1,-1))
        self.filename = filename
        self.dirname = '.'
        """ Create "interior" window components. In this case it is just a
            simple multiline text control."""
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        """ Create "exterior" window components, such as menu and status bar."""
        self.CreateStatusBar() # A Statusbar in the bottom of the window
        self.CreateMenu()
        self.SetTitle()
        
        favicon = wx.Icon('Dummy_icon.ico', wx.BITMAP_TYPE_ICO)
        self.SetIcon(favicon)
        
        # Create sizer(s)
        self.sizer2 = wx.BoxSizer(wx.HORIZONTAL)
        self.buttons = []
        i = 0
        for buttonid, buttonname, buttonhandler in [(wx.ID_ABOUT, 'About', self.OnAbout),
             (wx.ID_OPEN, 'Open', self.OnOpen),(wx.ID_SAVE, 'Save', self.OnSave),
             (wx.ID_SAVEAS, 'Save As', self.OnSaveAs),
             (wx.ID_EXIT, 'Exit', self.OnExit)]:
            self.buttons.append(wx.Button(self, -1, buttonname))
            self.Bind(wx.EVT_BUTTON, buttonhandler, self.buttons[i])
            self.sizer2.Add(self.buttons[i], 1, wx.EXPAND)
            i = i+1
            
        self.sizer3 = wx.BoxSizer(wx.HORIZONTAL)
        ClearButton = wx.Button(self,-1,'Clear')
        self.Bind(wx.EVT_BUTTON, self.OnClear, ClearButton)
        self.sizer3.Add(ClearButton,1,wx.EXPAND)
                                
        # Use some sizers to see layout options
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.control, 10, wx.EXPAND)
        self.sizer.Add(self.sizer3,1,wx.EXPAND)
        self.sizer.Add(self.sizer2,0,wx.EXPAND)

        #Layout sizers
        self.SetSizer(self.sizer)
        self.SetAutoLayout(True)
        self.sizer.Fit(self)
        
        self.Show(True)
        
    def CreateMenu(self):
        # Setting up the menu.
        fileMenu = wx.Menu()
        # wx.ID_ABOUT and wx.ID_EXIT are standard IDs provided by wxWidgets.
        for id, label, helpText, handler in \
            [(wx.ID_ABOUT, '&About', 'Information about this program',
                self.OnAbout),
             (wx.ID_OPEN, '&Open', 'Open a new file', self.OnOpen),
             (wx.ID_SAVE, '&Save', 'Save the current file', self.OnSave),
             (wx.ID_SAVEAS, 'Save &As', 'Save the file under a different name',
                self.OnSaveAs),
             (None, None, None, None),
             (wx.ID_EXIT, 'E&xit', 'Terminate the program', self.OnExit)]:
            if id == None:
                fileMenu.AppendSeparator()
            else:
                item = fileMenu.Append(id, label, helpText)
                #Set events
                self.Bind(wx.EVT_MENU, handler, item)
        # Creating the menubar.
        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, '&File') # Add the fileMenu to the MenuBar
        self.SetMenuBar(menuBar)  # Add the menuBar to the Frame

    def defaultFileDialogOptions(self):
        ''' Return a dictionary with file dialog options that can be
            used in both the save file dialog as well as in the open
            file dialog. '''
        return dict(message='Choose a file', defaultDir=self.dirname,
                    wildcard='*.*')

    def SetTitle(self):
        # MainWindow.SetTitle overrides wx.Frame.SetTitle, so we have to
        # call it using super:
        super(MainWindow, self).SetTitle('Editor %s'%self.filename)
    
    def askUserForFilename(self, **dialogOptions):
        dialog = wx.FileDialog(self, **dialogOptions)
        if dialog.ShowModal() == wx.ID_OK:
            userProvidedFilename = True
            self.filename = dialog.GetFilename()
            self.dirname = dialog.GetDirectory()
            self.SetTitle() # Update the window title with the new filename
        else:
            userProvidedFilename = False
        dialog.Destroy()
        return userProvidedFilename

    """Event handlers"""

    def OnAbout(self,event):
        # A message dialog box with an OK button. wx.OK is a standard ID in wxWidgets.
        dlg = wx.MessageDialog( self, "A small text editor", "About Sample Editor", wx.OK)
        dlg.ShowModal() # Show it
        dlg.Destroy() # finally destroy it when finished.
        
    def OnExit(self,event):
        dlg = wx.MessageDialog( self, "Are you sure you want to quit editor?", "Exit Confirmation")
        if dlg.ShowModal()==wx.ID_OK:
            self.Close(True)  # Close the frame.
        dlg.Destroy()

    def OnOpen(self,event):
        """ Open a file"""
        if self.askUserForFilename(style=wx.OPEN,**self.defaultFileDialogOptions()):
            f = open(os.path.join(self.dirname, self.filename), 'r')
            self.control.SetValue(f.read())
            f.close()
        
    def OnSave(self,event):
	""" Save a file"""
	textfile = open(os.path.join(self.dirname, self.filename), 'w')
        textfile.write(self.control.GetValue())
        textfile.close()
        
    def OnSaveAs(self, event):
        if self.askUserForFilename(defaultFile=self.filename, style=wx.SAVE,
                                   **self.defaultFileDialogOptions()):
            self.OnSave(event)
    
    def OnClear(self, event):
        dlg = wx.MessageDialog( self, "Are you sure you want to clear your editor?", "Clear Confirmation")
        if dlg.ShowModal()==wx.ID_OK:
            self.control.Clear()
        dlg.Destroy() # finally destroy it when finished.

app = wx.App(False)
frame = MainWindow()
app.MainLoop()