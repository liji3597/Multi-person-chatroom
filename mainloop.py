import wx

class MsbServer(wx.Frame):
    def __init__(self, *args, **kw):
        super(MsbServer, self).__init__(*args, **kw)
        self.InitUI()

    def InitUI(self):
        self.SetTitle('Patrick9313的服务器界面')
        self.SetSize((400, 470))
        pl = wx.Panel(self)  # 在窗口中初始化一个面板
        # 在面板里面会放一些按钮，文本框，文本输入框等，把这些对象统一放入一个盒子里面
        box = wx.BoxSizer(wx.VERTICAL)  # 在盒子里面垂直方向自动排版

        g1 = wx.FlexGridSizer(wx.HORIZONTAL)  # 可缩的网格布局,水平方向
        # 创建三个按钮
        start_server_button = wx.Button(pl, size=(133, 40), label="启动")
        record_save_button = wx.Button(pl, size=(133, 40), label="聊天记录保存")
        stop_server_button = wx.Button(pl, size=(133, 40), label="停止")
        g1.Add(start_server_button, 1, wx.TOP)
        g1.Add(record_save_button, 1, wx.TOP)
        g1.Add(stop_server_button, 1, wx.TOP)
        box.Add(g1, 1, wx.ALIGN_CENTER)  # ALIGN_CENTER 联合居中

        # 创建只读的文本框,显示聊天记录
        self.text = wx.TextCtrl(pl, size=(400, 400), style=wx.TE_MULTILINE | wx.TE_READONLY)
        box.Add(self.text, 1, wx.ALIGN_CENTER)
        pl.SetSizer(box)

if __name__ == '__main__':
    app = wx.App(False)
    server = MsbServer(None)
    server.Show()
    app.MainLoop()