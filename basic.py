from layouts.basic import layout
from loading import loading


def basic():
    """Функциональность основного экрана"""
    sp, act_us = loading()
    window = layout(sp)
    return window, act_us
