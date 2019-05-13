# coding: utf-8
import wx
import math
import random


def alignmidle(win):
    dw, dh = wx.DisplaySize()
    w, h = win.GetSize()
    x = (dw - w)/2
    y = (dh - h)/2
    win.SetPosition((x, y))


def generate_a():
    off = 20
    ttt = 80

    cag = (off + random.randrange(ttt))
    cag = cag*100 + (off + random.randrange(ttt))
    cag = cag * 100 + (off + random.randrange(ttt))
    cag = cag * 100 + (off + random.randrange(ttt))
    cag = str(cag)
    # return cag1,cag2,cag3,cag4
    return cag


def generate_b(codea):
    cap = int(codea)
    print(cap)
    ca4 = cap % 100
    cap = math.trunc(cap / 100)
    ca3 = cap % 100
    cap = math.trunc(cap / 100)
    ca2 = cap % 100
    cap = math.trunc(cap / 100)
    ca1 = cap
    cbp = 0
    cbp = (ca1 % 11 * 4) + cbp * 100
    cbp = (ca2 % 13 * 3) + cbp * 100
    cbp = (ca3 % 17 * 2) + cbp * 100
    cbp = (ca4 % 19 * 1) + cbp * 100
    return cbp


class ExamplePanel(wx.Panel):

    def __init__(self, parent):
        font1 = wx.Font(14, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, u'Consolas')
        font2 = wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, u'Consolas')
        font3 = wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, u'Consolas')

        wx.Panel.__init__(self, parent)
        # self.quote = wx.StaticText(self, label="Your quote :", pos=(20, 30))

        # Definicia Labelu nazov aplikacie
        self.lbl1 = wx.StaticText(self, label="Generator KoduB pre Beutler", pos=(10, 10))
        self.lbl1.SetFont(font2)

        # Definicia vstupneho policka
        self.lblnamea = wx.StaticText(self, label="Code A :", pos=(20, 60))
        self.editnamea = wx.TextCtrl(self, value=generate_a(), pos=(100, 50), size=(120, 30), style=wx.TE_CENTER)
        self.editnamea.SetBackgroundColour("green")
        self.editnamea.SetForegroundColour("black")
        self.editnamea.SetFont(font1)

        self.Bind(wx.EVT_TEXT, self.evttext, self.editnamea)
        # self.Bind(wx.EVT_CHAR, self.evtchar, self.editnamea)

        # Ddefinicia vystupneho policka
        self.lblnameb = wx.StaticText(self, label="Code B :", pos=(20, 100))
        self.editnameb = wx.TextCtrl(self, value="", pos=(100, 90), size=(120, 30), style=wx.TE_READONLY | wx.TE_CENTER)
        self.editnameb.SetBackgroundColour("red")
        self.editnameb.SetForegroundColour("blue")
        self.editnameb.SetFont(font1)

        # A Tlacitko
        self.button = wx.Button(self, label="Decode", pos=(90, 150))
        self.Bind(wx.EVT_BUTTON, self.onclick, self.button)

        self.lbl2 = wx.StaticText(self, label='For PWO designed by ®Eduard Bohacek 2019©', pos=(0, 200))
        self.lbl2.SetFont(font3)

    def onclick(self, event):
        txt = self.editnamea.GetValue()
        print txt
        codb = generate_b(txt)
        self.editnameb.SetValue('%d\n' % codb)
        # self.logger.AppendText(" Click on object with Id %d\n" % event.GetId())

    def evttext(self, event):
        coda = event.GetString()
        codb = generate_b(coda)
        self.editnameb.SetValue('%d\n' % codb)


app = wx.App(False)
frame = wx.Frame(None, title="Beutler", size=(300, 260), pos=(200, 150))
alignmidle(frame)
app.SetTopWindow(frame)
panel = ExamplePanel(frame)
frame.Show()
app.MainLoop()
