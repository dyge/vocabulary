import wx
import backend
import frontend

if __name__=='__main__':
    app=wx.App()
    frame=frontend.choice(parent=None,id=-1)
    frame.Show()
    app.MainLoop()
