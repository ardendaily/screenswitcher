#!/usr/bin/python
import urwid, subprocess, os

class MenuHolder:
    def __init__(self):
        self.item_list = []
    def add_item(self, item):
        self.item_list.append(item)
    def add_item_from_string(self, string):
        self.item_list.append(
            MenuItem(
                [string]
                )
            )
    def get_list(self):
        retval = []
        for x in range(0, len(self.item_list)):
            retval.append(self.item_list[x].get_menu_text())
        return retval

class MenuItem:
    def __init__(self, menu_list):
        self.menutext = menu_list
    def set_menu_text(self, menu_list):
        self.menutext = menu_list
    def get_menu_text(self):
        if len(self.menutext) > 1:
            return "%s\n  %s\n  %s" % (
                self.menutext[0], self.menutext[1], self.menutext[2])
        else:
            return self.menutext

screen_sessions = []
try:
    screen_sessions = subprocess.check_output( ["screen", "-list"] ).split('\n')
except subprocess.CalledProcessError:
    print "No running screens"
    exit()

menulist = MenuHolder()

for item in range(1, (len(screen_sessions) - 2 ) ):
    virt_tty = screen_sessions[item].split('\t')
    virt_tty.pop(0)
    menulist.add_item( MenuItem(virt_tty) )

menulist.add_item_from_string("exit")

def menu(title, choices):
    body = [urwid.Text(title), urwid.Divider()]
    for c in choices:
        button = urwid.Button(c)
        urwid.connect_signal(button, 'click', item_chosen, c)
        body.append(urwid.AttrMap(button, None, focus_map='reversed'))

    return urwid.ListBox(urwid.SimpleFocusListWalker(body))

def item_chosen(button, choice):
    if choice[0] != "exit":
        os.system('screen -r %s' % choice[0])
        os.system('reset')

    raise urwid.ExitMainLoop()

def exit_program(button):
    raise urwid.ExitMainLoop()

main = urwid.Padding(menu(u'running screens', menulist.get_list()), left=2, right=2)
top = urwid.Overlay(main, urwid.SolidFill(u'\\'),
    align='center', width=('relative', 60),
    valign='middle', height=('relative', 60),
    min_width=20, min_height=9)
urwid.MainLoop(top, palette=[('reversed', 'standout', '')]).run()