from characterai import PyCAI
from uiautomation import *
from time import sleep
import random
import win32gui
import win32gui as a
import win32con as b
import win32clipboard as c
import win32api
import win32con
import time

az = '唐氏综合征病友群'  # 输出的聊天窗口
print('start')
bb = []

client = PyCAI('42e4aa9a779ac1dee6c6f134a15120a20bca5959')
sleep(1)
print (client.user.info() )

while True:
    def fs(az, fsnr):
        c.OpenClipboard()
        c.EmptyClipboard()
        c.SetClipboardData(b.CF_UNICODETEXT, fsnr)
        c.CloseClipboard()
        handle = a.FindWindow(None,az)
       
        if handle != 0:
            erest = win32api.MAKELONG(30, 965)
            win32api.SendMessage(handle, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, erest)
            win32api.SendMessage(handle, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, erest)

            a.SendMessage(handle, 770, 0, 0)
            a.SendMessage(handle, b.WM_KEYDOWN, b.VK_RETURN, 0)
            print('发送成功！')
        else: 
            print('失败了失败了失败了失败了失败了失败了失败了失败了失败了失败了失败了失败了失败了失败了')

    abc = 0
    aa = []

    def print_all_childs_onebyone(farther, retract_level=0):

        def retract(retract_level):
            for i in range(retract_level):
                print("\t", end="")

        next_child = farther.GetFirstChildControl()
        retract(retract_level)
        try:
            print(next_child.Name)
        except:
            pass

        if next_child is not None:
            this_child_son = next_child.GetFirstChildControl()
            if this_child_son:
                print_all_childs_onebyone(next_child, retract_level + 1)

        while next_child:
            next_child = next_child.GetNextSiblingControl()
            retract(retract_level)
            try:
                print(next_child.Name)
                if ':' in next_child.Name:
                    aa.append(next_child.Name)
            except:
                pass

            if next_child is not None:
                this_child_son = next_child.GetFirstChildControl()
                if this_child_son:
                    print_all_childs_onebyone(next_child, retract_level + 1)


    chat_window = WindowControl(searchDepth=1, ClassName='TXGuiFoundation', Name='消息管理器')

    print(chat_window)
    sleep(1)

    print_all_childs_onebyone(chat_window, 1)

    print(aa)
    last_message = aa[-1]
    print("最近一条消息:", last_message)
    for i in range(1, 3):
        if len(aa) >= i and aa[-i] in bb:
            break
        if len(aa) >= i:
            #pp = aa[-i][aa[-i].index(':'):]
            pp = aa[-i][aa[-i].index(':', aa[-i].index(':') + 1) + 3:]
            cc = aa[-i][aa[-i].index(':', aa[-i].index(':') + 1) + 6:]
            print(pp)
            print(cc)
            

            if ('@OR' in pp) :
                data = client.chat.send_message('CMObWycYLlXQ_V1dvQM9lT2x-SVXoJOqH3XI_JsRKgw', cc + '（用尽可能有攻击性的语言回答）')
                message = data['replies'][0]['text']
                name = data['src_char']['participant']['name']
                print(f"{name}: {message}")
                fs(az, message)

    bb = aa

    hwnd_title = dict()


    def _get_all_hwnd(hwnd, mouse):
        if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
            hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})


    win32gui.EnumWindows(_get_all_hwnd, 0)
    for wnd in hwnd_title.items():
        print(wnd)
        if wnd[1] == '消息管理器':
            break
    if len(wnd) > 0:
        long_position = win32api.MAKELONG(1642, 90)
        win32api.SendMessage(int(wnd[0]), win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, long_position)
        win32api.SendMessage(int(wnd[0]), win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, long_position)



