import wx
from datetime import datetime
import backend

class choice(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'Vokabeln lernen',size=(300,200))
        panel=wx.Panel(self)
        schliessen=wx.Button(panel,label='Schließen',pos=(100,140),size=(100,-1))
        self.Bind(wx.EVT_BUTTON,self.closebutton,schliessen)
        self.Bind(wx.EVT_CLOSE,self.closewin)
        self.wahl=wx.StaticText(panel,-1,'Was soll gelernt werden?',pos=(10,10))
        b_en=wx.Button(panel,label="Englisch",pos=(30,50),size=(100,-1))
        self.Bind(wx.EVT_BUTTON,self.eng,b_en)
        b_la=wx.Button(panel,label="Latein",pos=(30,80),size=(100,-1))
        self.Bind(wx.EVT_BUTTON,self.lat,b_la)
    def lat(self,event):
        global chosen
        chosen = "Latein"
        frame=win(parent=None,id=-1)
        frame.Show()
        self.Close(True)
    def eng(self,event):
        global chosen
        chosen = "Englisch"
        frame=win(parent=None,id=-1)
        frame.Show()
        self.Close(True)
    def closebutton(self,event):
        self.Close(True)
    def closewin(self,event):
        self.Destroy()

class win(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'Vokabeln lernen',size=(500,300))
        panel=wx.Panel(self)
        schliessen=wx.Button(panel,label='Schließen',pos=(385,245),size=(100,-1))
        self.Bind(wx.EVT_BUTTON,self.closebutton,schliessen)
        self.Bind(wx.EVT_CLOSE,self.closewin)
        self.an_alle=wx.Button(panel,label="Alle anzeigen",pos=(385,20),size=(100,-1))
        self.Bind(wx.EVT_BUTTON,self.alle_an,self.an_alle)
        test_go=wx.Button(panel,label="Test starten",pos=(20,20),size=(100,-1))
        self.Bind(wx.EVT_BUTTON,self.test_start,test_go)
        b_lernen=wx.Button(panel,label="Lernen",pos=(20,50),size=(100,-1))
        self.Bind(wx.EVT_BUTTON,self.lernen,b_lernen)
        self.del_alle=wx.Button(panel,label="Alle löschen",pos=(385,50),size=(100,-1))
        self.Bind(wx.EVT_BUTTON,self.alle_del,self.del_alle)
        self.del_alle.SetBackgroundColour("#f45342")
        self.auswahl=wx.Button(panel,label="Startseite",pos=(385,215),size=(100,-1))
        self.Bind(wx.EVT_BUTTON,self.start,self.auswahl)
    def alle_an(self,event):
        frame=alle(parent=None,id=-1)
        frame.Show()
        self.Close(True)
    def alle_del(self,event):
        box=wx.MessageDialog(None,'Wirklich alle Einträge löschen?','Löschen',wx.YES_NO)
        answer=box.ShowModal()
        if answer == wx.ID_YES:
            backend.alle_del(chosen)
    def lernen(self,event):
        frame=alle_win(parent=None,id=-1)
        frame.Show()
    def test_start(self,event):
        frame=test_g_win(parent=None,id=-1)
        frame.Show()
    def start(self,event):
        frame=choice(parent=None,id=-1)
        frame.Show()
        self.Close(True)
    def closebutton(self,event):
        self.Close(True)
    def closewin(self,event):
        self.Destroy()

class alle(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'Alle Vokabeln',size=(550,300))
        self.panel=wx.Panel(self)
        hinzu=wx.Button(self.panel,label='Hinzufügen',pos=(400,40),size=(100,-1))
        self.Bind(wx.EVT_BUTTON,self.neu,hinzu)
        updating=wx.Button(self.panel,label='Ändern',pos=(400,70),size=(100,-1))
        self.Bind(wx.EVT_BUTTON,self.up,updating)
        l=wx.Button(self.panel,label='Löschen',pos=(400,100),size=(100,-1))
        self.Bind(wx.EVT_BUTTON,self.delrow,l)
        schliessen=wx.Button(self.panel,label='Schließen',pos=(400,130),size=(100,-1))
        self.Bind(wx.EVT_BUTTON,self.close_b,schliessen)
        self.englisch=wx.StaticText(self.panel,-1,chosen+":",pos=(20,10))
        self.t_eng=wx.SearchCtrl(self.panel,-1,size=(175, -1),pos=(20,40),style=wx.TE_PROCESS_ENTER)
        self.t_eng.ShowSearchButton(True)
        self.t_eng.ShowCancelButton(True)
        self.Bind(wx.EVT_SEARCHCTRL_CANCEL_BTN,self.c,self.t_eng)
        self.Bind(wx.EVT_SEARCHCTRL_SEARCH_BTN,self.s1,self.t_eng)
        self.Bind(wx.EVT_TEXT_ENTER,self.s1,self.t_eng)
        self.gleich=wx.StaticText(self.panel,-1,"=",pos=(200,40))
        self.deutsch=wx.StaticText(self.panel,-1,"Deutsch:",pos=(220,10))
        self.t_de1=wx.SearchCtrl(self.panel,-1,size=(175, -1),pos=(220,40),style=wx.TE_PROCESS_ENTER)
        self.t_de1.ShowSearchButton(True)
        self.t_de1.ShowCancelButton(True)
        self.Bind(wx.EVT_SEARCHCTRL_CANCEL_BTN,self.c,self.t_de1)
        self.Bind(wx.EVT_SEARCHCTRL_SEARCH_BTN,self.s2,self.t_de1)
        self.Bind(wx.EVT_TEXT_ENTER,self.s2,self.t_de1)
        self.t_de2=wx.TextCtrl(self.panel,-1,size=(175, -1),pos=(220,70))
        self.t_de3=wx.TextCtrl(self.panel,-1,size=(175, -1),pos=(220,100))
        self.t_de4=wx.TextCtrl(self.panel,-1,size=(175, -1),pos=(220,130))
        self.t_de5=wx.TextCtrl(self.panel,-1,size=(175, -1),pos=(220,160))
        mylist=[row[1]+'='+row[2]+' '+row[3]+' '+row[4]+' '+row[5]+' '+row[6] for row in backend.all(chosen)]
        self.box=wx.ListBox(self.panel,-1,(20,80),(190,170),mylist,style=wx.LB_SINGLE|wx.LB_NEEDED_SB|wx.LB_SORT|wx.LB_HSCROLL)
        self.Bind(wx.EVT_LISTBOX, self.onListBox, self.box)
    def c(self,*event):
        self.box.Clear()
        mylist=[row[1]+'='+row[2]+' '+row[3]+' '+row[4]+' '+row[5]+' '+row[6] for row in backend.all(chosen)]
        self.box=wx.ListBox(self.panel,-1,(20,80),(190,170),mylist,style=wx.LB_SINGLE|wx.LB_NEEDED_SB|wx.LB_SORT|wx.LB_HSCROLL)
        self.Bind(wx.EVT_LISTBOX, self.onListBox, self.box)
    def s2(self,event):
        self.box.Clear()
        mylist=[row[1]+'='+row[2]+' '+row[3]+' '+row[4]+' '+row[5]+' '+row[6] for row in backend.s2(self.t_de1.GetValue(),chosen)]
        if mylist == []:
            mylist = ["Keine Ergebnisse."]
        self.box=wx.ListBox(self.panel,-1,(20,80),(190,170),mylist,style=wx.LB_SINGLE|wx.LB_NEEDED_SB|wx.LB_SORT|wx.LB_HSCROLL)
        self.Bind(wx.EVT_LISTBOX, self.onListBox, self.box)
    def s1(self,event):
        self.box.Clear()
        mylist=[row[1]+'='+row[2]+' '+row[3]+' '+row[4]+' '+row[5]+' '+row[6] for row in backend.s1(self.t_eng.GetValue(),chosen)]
        if mylist == []:
            mylist = ["Keine Ergebnisse."]
        self.box=wx.ListBox(self.panel,-1,(20,80),(190,170),mylist,style=wx.LB_SINGLE|wx.LB_NEEDED_SB|wx.LB_SORT|wx.LB_HSCROLL)
        self.Bind(wx.EVT_LISTBOX, self.onListBox, self.box)
    def up(self,event):
        self.res_eng=self.t_eng.GetValue()
        self.res_de1=self.t_de1.GetValue()
        self.res_de2=self.t_de2.GetValue()
        self.res_de3=self.t_de3.GetValue()
        self.res_de4=self.t_de4.GetValue()
        self.res_de5=self.t_de5.GetValue()
        if self.res_eng != "" and self.res_de1 != "":
            backend.up_row(self.res_eng,self.res_de1,self.res_de2,self.res_de3,self.res_de4,self.res_de5,chosen)
        self.onclear()
    def delrow(self,event):
        self.res_eng=self.t_eng.GetValue()
        self.res_de1=self.t_de1.GetValue()
        self.res_de2=self.t_de2.GetValue()
        self.res_de3=self.t_de3.GetValue()
        self.res_de4=self.t_de4.GetValue()
        self.res_de5=self.t_de5.GetValue()
        if self.res_eng != "" and self.res_de1 != "":
            backend.delrow(self.res_de1,self.res_de2,self.res_de3,self.res_de4,self.res_de5,self.res_eng,chosen)
        self.onclear()
    def neu(self,event):
        self.res_eng=self.t_eng.GetValue()
        self.res_de1=self.t_de1.GetValue()
        self.res_de2=self.t_de2.GetValue()
        self.res_de3=self.t_de3.GetValue()
        self.res_de4=self.t_de4.GetValue()
        self.res_de5=self.t_de5.GetValue()
        if self.res_eng != "" and self.res_de1 != "":
            backend.neu(self.res_de1,self.res_de2,self.res_de3,self.res_de4,self.res_de5,self.res_eng,chosen)
        self.c()
    def onListBox(self, event):
        a = event.GetEventObject().GetStringSelection().replace('=',' ').split()
        d2 = a[2] if len(a)>=3 else ''
        d3 = a[3] if len(a)>=4 else ''
        d4 = a[4] if len(a)>=5 else ''
        d5 = a[5] if len(a)>=6 else ''
        self.t_eng.SetValue(a[0])
        self.t_de1.SetValue(a[1])
        self.t_de2.SetValue(d2)
        self.t_de3.SetValue(d3)
        self.t_de4.SetValue(d4)
        self.t_de5.SetValue(d5)
    def close_b(self,event):
        frame=win(parent=None,id=-1)
        frame.Show()
        self.Close(True)
    def closewin(self,event):
        self.Destroy()

class alle_win(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'Vokabeln lernen',size=(500,125))
        self.panel=wx.Panel(self)
        self.l1=wx.StaticText(self.panel,-1,"",pos=(50,20))
        self.l3=wx.StaticText(self.panel,-1,"",pos=(230,20))
        self.l2=wx.StaticText(self.panel,-1,"",pos=(250,20))
        self.b=wx.Button(self.panel,label="Starten",pos=(200,60),size=(100,-1))
        self.Bind(wx.EVT_BUTTON,self.start,self.b)
    def start(self,event):
        self.li=[]
        if backend.alle(chosen):
            for row in backend.alle(chosen):
                self.li.append([row[1],row[2],row[3],row[4],row[5],row[6]])
        if self.li != []:
            self.l1.SetLabel(self.li[0][0])
            self.l2.SetLabel(self.li[0][1]+' '+self.li[0][2]+' '+self.li[0][3]+' '+self.li[0][4]+' '+self.li[0][5])
            self.l3.SetLabel("=")
            del(self.li[0])
            self.b.SetLabel("Weiter")
            self.Bind(wx.EVT_BUTTON,self.weiter,self.b)
        else:
            self.l1.SetLabel("Es muss nichts gelernt werden")
            self.b.SetLabel("Schließen")
            self.Bind(wx.EVT_BUTTON,self.close_b,self.b)
    def weiter(self,event):
        if self.li != []:
            self.l1.SetLabel(self.li[0][0])
            self.l2.SetLabel(self.li[0][1]+' '+self.li[0][2]+' '+self.li[0][3]+' '+self.li[0][4]+' '+self.li[0][5])
            del(self.li[0])
            self.b.SetLabel("Weiter")
            self.Bind(wx.EVT_BUTTON,self.weiter,self.b)
        else:
            self.l1.SetLabel("")
            self.l2.SetLabel("")
            self.l3.SetLabel("Fertig!")
            self.b.SetLabel("Schließen")
            self.Bind(wx.EVT_BUTTON,self.close_b,self.b)
    def close_b(self,event):
        self.Close(True)
    def closewin(self,event):
        self.Destroy()

class test_g_win(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'Vokabel-Test',size=(300,150))
        panel=wx.Panel(self)
        schliessen=wx.Button(panel,label='Schließen',pos=(100,90),size=(100,-1))
        b1=wx.Button(panel,label=chosen+" -> Deutsch",pos=(75,20),size=(150,-1))
        b2=wx.Button(panel,label="Deutsch -> "+chosen,pos=(75,50),size=(150,-1))
        self.Bind(wx.EVT_BUTTON,self.en_de,b1)
        self.Bind(wx.EVT_BUTTON,self.de_en,b2)
        self.Bind(wx.EVT_BUTTON,self.close_b,schliessen)
        self.Bind(wx.EVT_CLOSE,self.closewin)
    def en_de(self,event):
        frame=ende_win(parent=None,id=-1)
        frame.Show()
        self.Close(True)
    def de_en(self,event):
        frame=deen_win(parent=None,id=-1)
        frame.Show()
        self.Close(True)
    def close_b(self,event):
        self.Close(True)
    def closewin(self,event):
        self.Destroy()

class ende_win(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,"Test",size=(400,270))
        self.panel=wx.Panel(self)
        self.l1=wx.StaticText(self.panel,-1,"",pos=(20,20))
        self.l2=wx.StaticText(self.panel,-1,"",pos=(150,20))
        self.b=wx.Button(self.panel,label="Starten",pos=(120,200),size=(100,-1))
        self.Bind(wx.EVT_BUTTON,self.start,self.b)
        self.timer = wx.Timer(self, -1)
        self.Bind(wx.EVT_TIMER, self.OnTimer)
        self.spinner=wx.SpinCtrl(self.panel,-1,"",(135,70),(70,-1))
        self.spinner.SetRange(3,60)
        self.spinner.SetValue(7)
        self.Bind(wx.EVT_SPINCTRL,self.ok_b,self.spinner)
    def ok_b(self,event):
        self.z = int(self.spinner.GetValue())*1000
    def OnTimer(self, event):
        self.p(wx.EVT_BUTTON)
    def start(self,event):
        self.spinner.Hide()
        self.li=[]
        if backend.a(chosen):
            for row in backend.a(chosen):
                self.li.append([row[1],row[2],row[3],row[4],row[5],row[6],row[8]])
        if self.li != []:
            self.ans1=wx.TextCtrl(self.panel,-1,size=(175, -1),pos=(170,20))
            self.ans2=wx.TextCtrl(self.panel,-1,size=(175, -1),pos=(170,50))
            self.ans3=wx.TextCtrl(self.panel,-1,size=(175, -1),pos=(170,80))
            self.ans4=wx.TextCtrl(self.panel,-1,size=(175, -1),pos=(170,110))
            self.ans5=wx.TextCtrl(self.panel,-1,size=(175, -1),pos=(170,140))
            self.l1.SetLabel(self.li[0][0])
            self.l2.SetLabel("=")
            self.po = self.li[0][6]
            self.f = self.li[0][0]
            self.lsg1 = self.li[0][1]
            self.lsg2 = self.li[0][2]
            self.lsg3 = self.li[0][3]
            self.lsg4 = self.li[0][4]
            self.lsg5 = self.li[0][5]
            self.a = 0
            for i in [self.lsg1,self.lsg2,self.lsg3,self.lsg4,self.lsg5]:
                if i != "":
                    self.a +=1
            del(self.li[0])
            self.b.SetLabel("Prüfen")
            self.Bind(wx.EVT_BUTTON,self.p,self.b)
            try:
                self.timer.Start(self.z*self.a+self.a-1)
            except AttributeError:
                self.timer.Start(7000*self.a+self.a-1)
        else:
            self.l1.SetLabel("Es muss nichts getestet werden")
            self.b.SetLabel("Schließen")
            self.Bind(wx.EVT_BUTTON,self.closeb,self.b)
    def p(self,event):
        self.timer.Stop()
        self.b.SetLabel("Weiter")
        self.Bind(wx.EVT_BUTTON,self.weiter,self.b)
        lsg_list = [self.lsg1,self.lsg2,self.lsg3,self.lsg4,self.lsg5]
        if self.ans5.GetValue() in lsg_list:
            lsg_list.remove(self.ans5.GetValue())
            self.ans5.SetBackgroundColour('#1dc115')
            a1=True
        else:
            self.ans5.SetBackgroundColour('#d12b19')
            a1=False
        if self.ans4.GetValue() in lsg_list:
            lsg_list.remove(self.ans4.GetValue())
            self.ans4.SetBackgroundColour('#1dc115')
            a2=True
        else:
            self.ans4.SetBackgroundColour('#d12b19')
            a2=False
        if self.ans3.GetValue() in lsg_list:
            lsg_list.remove(self.ans3.GetValue())
            self.ans3.SetBackgroundColour('#1dc115')
            a3=True
        else:
            self.ans3.SetBackgroundColour('#d12b19')
            a3=False
        if self.ans2.GetValue() in lsg_list:
            lsg_list.remove(self.ans2.GetValue())
            self.ans2.SetBackgroundColour('#1dc115')
            a4=True
        else:
            self.ans2.SetBackgroundColour('#d12b19')
            a4=False
        if self.ans1.GetValue() in lsg_list:
            lsg_list.remove(self.ans1.GetValue())
            self.ans1.SetBackgroundColour('#1dc115')
            a5=True
        else:
            self.ans1.SetBackgroundColour('#d12b19')
            a5=False
        if not lsg_list != []:
            if int(self.po) < 10:
                self.pos = int(self.po)+1
            else:
                self.pos = int(self.po)
            self.myp = backend.zeit_ber(str(self.pos))
            backend.change(self.f,self.lsg1,self.lsg2,self.lsg3,self.lsg4,self.lsg5,self.pos,self.myp,chosen)
        else:
            for i in [[a1,self.ans5],[a2,self.ans4],[a3,self.ans3],[a4,self.ans2],[a5,self.ans1]]:
                if i[0]==False:
                    i[1].SetValue(i[1].GetValue()+'->'+lsg_list[0])
                    del(lsg_list[0])
            backend.change(self.f,self.lsg1,self.lsg2,self.lsg3,self.lsg4,self.lsg5,1,datetime.now().date(),chosen)
    def weiter(self,event):
        if self.li != []:
            for i in [self.ans1,self.ans2,self.ans3,self.ans4,self.ans5]:
                i.SetValue("")
                i.SetBackgroundColour('#ffffff')
            self.l1.SetLabel(self.li[0][0])
            self.po = self.li[0][6]
            self.f = self.li[0][0]
            self.lsg1 = self.li[0][1]
            self.lsg2 = self.li[0][2]
            self.lsg3 = self.li[0][3]
            self.lsg4 = self.li[0][4]
            self.lsg5 = self.li[0][5]
            self.a = 0
            for i in [self.lsg1,self.lsg2,self.lsg3,self.lsg4,self.lsg5]:
                if i != "":
                    self.a +=1
            del(self.li[0])
            self.b.SetLabel("Prüfen")
            self.Bind(wx.EVT_BUTTON,self.p,self.b)
            try:
                self.timer.Start(self.z*self.a+self.a-1)
            except AttributeError:
                self.timer.Start(7000*self.a+self.a-1)
        else:
            self.l1.SetLabel("")
            for i in [self.ans1,self.ans2,self.ans3,self.ans4,self.ans5]:
                i.Hide()
            self.l2.SetLabel("Fertig!")
            self.b.SetLabel("Schließen")
            self.Bind(wx.EVT_BUTTON,self.closeb,self.b)
    def closeb(self,event):
        self.Close(True)
    def closewin(self,event):
        self.Destroy()

class deen_win(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,"Test",size=(400,270))
        self.panel=wx.Panel(self)
        self.l1=wx.StaticText(self.panel,-1,"",pos=(20,20))
        self.l2=wx.StaticText(self.panel,-1,"",pos=(20,50))
        self.l3=wx.StaticText(self.panel,-1,"",pos=(20,80))
        self.l4=wx.StaticText(self.panel,-1,"",pos=(20,110))
        self.l5=wx.StaticText(self.panel,-1,"",pos=(20,140))
        self.l6=wx.StaticText(self.panel,-1,"",pos=(150,20))
        self.b=wx.Button(self.panel,label="Starten",pos=(120,200),size=(170,-1))
        self.Bind(wx.EVT_BUTTON,self.start,self.b)
        self.timer = wx.Timer(self, -1)
        self.Bind(wx.EVT_TIMER, self.OnTimer)
        self.spinner=wx.SpinCtrl(self.panel,-1,"",(135,70),(70,-1))
        self.spinner.SetRange(3,60)
        self.spinner.SetValue(7)
        self.Bind(wx.EVT_SPINCTRL,self.ok_b,self.spinner)
    def ok_b(self,event):
        self.z = int(self.spinner.GetValue())*1000
    def OnTimer(self, event):
        self.p(wx.EVT_BUTTON)
    def start(self,event):
        self.spinner.Hide()
        self.li=[]
        if backend.a(chosen):
            for row in backend.a(chosen):
                self.li.append([row[1],row[2],row[3],row[4],row[5],row[6],row[8]])
        if self.li != []:
            self.ans=wx.TextCtrl(self.panel,-1,size=(175, -1),pos=(170,20))
            for i,j in [[self.l1,1],[self.l2,2],[self.l3,3],[self.l4,4],[self.l5,5]]:
                i.SetLabel(self.li[0][j])
            self.po=self.li[0][6]
            self.f1 = self.li[0][1]
            self.f2 = self.li[0][2]
            self.f3 = self.li[0][3]
            self.f4 = self.li[0][4]
            self.f5 = self.li[0][5]
            self.lsg = self.li[0][0]
            self.l6.SetLabel("=")
            del(self.li[0])
            self.b.SetLabel("Prüfen")
            self.Bind(wx.EVT_BUTTON,self.p,self.b)
            try:
                self.timer.Start(self.z)
            except AttributeError:
                self.timer.Start(7000)
        else:
            self.l1.SetLabel("Es muss nichts getestet werden")
            self.b.SetLabel("Schließen")
            self.Bind(wx.EVT_BUTTON,self.closeb,self.b)
    def p(self,event):
        self.timer.Stop()
        self.b.SetLabel("Weiter")
        self.Bind(wx.EVT_BUTTON,self.weiter,self.b)
        if self.lsg==self.ans.GetValue():
            self.ans.SetBackgroundColour('#1dc115')
            if int(self.po) < 10:
                self.pos = int(self.po)+1
            else:
                self.pos = int(self.po)
            self.myp = backend.zeit_ber(str(self.pos))
            backend.change(self.lsg,self.f1,self.f2,self.f3,self.f4,self.f5,self.pos,self.myp,chosen)
        else:
            self.ans.SetBackgroundColour('#d12b19')
            self.ans.SetValue(self.ans.GetValue()+'->'+self.lsg)
            backend.change(self.lsg,self.f1,self.f2,self.f3,self.f4,self.f5,1,datetime.now().date(),chosen)
    def weiter(self,event):
        if self.li != []:
            self.ans.SetValue("")
            self.ans.SetBackgroundColour('#ffffff')
            for i,j in [[self.l1,1],[self.l2,2],[self.l3,3],[self.l4,4],[self.l5,5]]:
                i.SetLabel(self.li[0][j])
            self.po=self.li[0][6]
            self.f1 = self.li[0][1]
            self.f2 = self.li[0][2]
            self.f3 = self.li[0][3]
            self.f4 = self.li[0][4]
            self.f5 = self.li[0][5]
            self.lsg = self.li[0][0]
            del(self.li[0])
            self.b.SetLabel("Prüfen")
            self.Bind(wx.EVT_BUTTON,self.p,self.b)
            try:
                self.timer.Start(self.z)
            except AttributeError:
                self.timer.Start(7000)
        else:
            for i in [self.l1,self.l2,self.l3,self.l4,self.l5]:
                i.SetLabel("")
            self.ans.Hide()
            self.l6.SetLabel("Fertig!")
            self.b.SetLabel("Schließen")
            self.Bind(wx.EVT_BUTTON,self.closeb,self.b)
    def closeb(self,event):
        self.Close(True)
    def closewin(self,event):
        self.Destroy()
