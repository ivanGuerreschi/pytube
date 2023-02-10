# pytube.py
#
# Copyright (C) 2023 Ivan Guerreschi
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import gi, youtube_dl, threading

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="PyTube")
        self.set_border_width(10)

        self.state = "v"

        label = Gtk.Label(label="Enter YT link ")
        self.entry = Gtk.Entry()
        button_video = Gtk.RadioButton.new_with_label_from_widget(None, "Video")
        button_audio = Gtk.RadioButton.new_from_widget(button_video)
        button_audio.set_label("Audio")
        button = Gtk.Button(label="Download")

        grid = Gtk.Grid()
        grid.add(label)
        grid.attach(self.entry, 1, 0, 2, 1)
        grid.attach(button_video, 0, 1, 1, 1)
        grid.attach(button_audio, 1, 1, 1, 1)
        grid.attach(button,0, 2, 3, 1 )

        button_video.connect("toggled", self.on_video_audio_toggled)
        button_audio.connect("toggled", self.on_video_audio_toggled)
        button.connect("clicked", self.on_download_clicked)

        self.add(grid)

    def download(self):
        if self.state == "v":
            ydl_opts = {}
        else:
            ydl_opts = { 'format': 'bestaudio/best' }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([self.entry.get_text()])

    def start_thread_for_download(self):
        threading.Thread(target=self.download).start()

    def on_video_audio_toggled(self, button):
        if button.get_label() == "Video":
            self.state = "v"
        else:
            self.state = "a"

    def on_download_clicked(self, button):
        self.start_thread_for_download()

if __name__ == "__main__":
    win = MainWindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()
