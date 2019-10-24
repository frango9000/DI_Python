import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class MainUi:
    def __init__(self):
        builder = Gtk.Builder()
        builder.add_from_file("Py_UI_01/UI1.glade")

        self.ventana = builder.get_object("mainWindow")
        self.label = builder.get_object("label")
        self.btn = builder.get_object("btn")
        self.txtField = builder.get_object("textField")
        self.txtArea = builder.get_object("textArea")

        signals = {
            "on_btn_activate": self.on_btn_activate,
            "on_txt_activate": self.on_txt_activate,
            "on_wind_destroy": Gtk.main_quit
        }
        builder.connect_signals(signals)
        self.ventana.show_all()
        self.label.set_text("hhhhh")

    def on_btn_activate(self, button):
        name = self.txtField.get_text()
        self.label.set_text("Hello " + name)

    def on_txt_activate(self, txtField):
        self.on_btn_activate(txtField)


if __name__ == "__main__":
    MainUi()
    Gtk.main()
