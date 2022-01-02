"""
Returns active window name.
Todo: cleanup, refactor
"""
import gi

gi.require_version("Wnck", "3.0")
from gi.repository import Wnck


def get_window():
    """
    Gets active window name.
    :return:
    :rtype:
    """
    scr = Wnck.Screen.get_default()
    scr.force_update()
    return scr.get_active_window().get_name()
