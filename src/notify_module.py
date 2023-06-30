# this is part of the DYGtube Downloader project.
#
# Release: v3.0-rc8
#
# Copyright ©  2022 - 2023  Juan Bindez  <juanbindez780@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#  
# repo: https://github.com/juanBindez


import time

from pytube.cli import on_progress
from tkinter import *
from tkinter import messagebox
from tkinter import ttk


def notify_dowload():
    """mix option progress bar interface"""

    window_progress = Tk()
    window_progress.title("DYGTube Downloader")
    window_progress.geometry("400x100")
    window_progress.resizable(False, False)
    window_progress.attributes('-alpha', 9.1)

    label = Label(window_progress,
                  text="Dowload Concluído!",).place(x=140, y=60)
    time.sleep(5)
    window_progress.destroy()
