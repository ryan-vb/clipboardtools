import click
from tkinter import Tk
from clipboardtools.tk_windows.function_select import *

plugins = []


@click.command(name='start')
def start():
    """TODO"""
    root = Tk()


@click.command(name='run')
@click.Choice(choices=plugins)
def run_headless():
    """TODO"""
    root = Tk()
    root.withdraw()

if __name__ == '__main__':
    start()


