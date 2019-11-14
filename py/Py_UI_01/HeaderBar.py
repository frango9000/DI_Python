import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class HeaderBarUI(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_default_size(400, 200)

        self.vbox1 = Gtk.VBox()
        self.add(self.vbox1)
        self.vbox1.set_border_width(10)
        self.vbox1.set_spacing(10)

        self.tophbox = Gtk.HBox()
        self.vbox1.add(self.tophbox)

        self.dataGrid = Gtk.Grid()
        self.dataGrid.set_column_spacing(75)
        self.dataGrid.set_row_spacing(3)

        self.dataGrid.attach(Gtk.Label("Data"), 0, 0, 1, 1)
        self.data_field = Gtk.Entry()
        self.dataGrid.attach(self.data_field, 1, 0, 1, 1)

        self.dataGrid.attach(Gtk.Label("Desde"), 0, 1, 1, 1)
        desdemodel = Gtk.ListStore(str)
        desdelist = ['Madrid', 'Vigo', 'Valencia']
        for row in desdelist:
            desdemodel.append([row])
        self.desdebox = Gtk.ComboBox.new_with_model(desdemodel)
        self.desdebox.connect("changed", self.on_desde_combo_changed)
        desdecell = Gtk.CellRendererText()
        self.desdebox.pack_start(desdecell, True)
        self.desdebox.add_attribute(desdecell, 'text', 0)
        self.desdebox.set_active(0)

        self.dataGrid.attach(self.desdebox, 1, 1, 1, 1)

        self.dataGrid.attach(Gtk.Label("Hasta"), 0, 2, 1, 1)
        hastamodel = Gtk.ListStore(str)
        for row in desdelist:
            hastamodel.append([row])

        self.hastabox = Gtk.ComboBox.new_with_model(hastamodel)
        self.hastabox.connect("changed", self.on_hasta_combo_changed)
        hastacell = Gtk.CellRendererText()
        self.hastabox.pack_start(hastacell, True)
        self.hastabox.add_attribute(hastacell, 'text', 0)
        self.hastabox.set_active(0)
        self.dataGrid.attach(self.hastabox, 1, 2, 1, 1)

        radiogrid = Gtk.Grid()
        radio1 = Gtk.RadioButton.new_with_label(None, "Radio 1")
        radiogrid.attach(radio1, 0, 1, 1, 1)
        radio2 = Gtk.RadioButton.new_with_label_from_widget(radio1, "Radio 2")
        radiogrid.attach(radio2, 0, 2, 1, 1)
        radio3 = Gtk.RadioButton.new_with_label_from_widget(radio1, "Radio 3")
        radiogrid.attach(radio3, 0, 3, 1, 1)
        radio4 = Gtk.RadioButton.new_with_label_from_widget(radio1, "Radio 4")
        radiogrid.attach(radio4, 0, 4, 1, 1)

        radiosframe = Gtk.Frame()
        radiosframe.set_label("Opciones")
        radiosframe.add(radiogrid)
        self.tophbox.add(self.dataGrid)
        self.tophbox.add(radiosframe)

        self.txtarea = Gtk.TextView()
        self.txtarea.set_editable(False)
        self.txtarea.set_margin_start(5)
        self.txtarea.set_margin_end(5)
        self.txtarea.set_margin_bottom(5)
        self.txtarea.set_size_request(-1, 100)

        frame = Gtk.Frame()
        frame.set_label("Disponibles")

        frame.add(self.txtarea)

        self.vbox1.add(frame)

        buttons = Gtk.HBox()
        self.buscar = Gtk.Button("Buscar")
        self.comprar = Gtk.Button("Comprar")
        self.salir = Gtk.Button("Salir")
        buttons.add(self.buscar)
        buttons.add(self.comprar)
        buttons.add(self.salir)
        self.vbox1.add(buttons)

        self.comprar.connect("clicked", self.on_comprar)

        self.connect("destroy", Gtk.main_quit)
        self.show_all()
        Gtk.main()

    def on_desde_combo_changed(self, combo):
        tree_iter = combo.get_active_iter()
        if tree_iter is not None:
            model = combo.get_model()
            desde = model[tree_iter][0]
            print("Desde %s" % desde)
    def on_hasta_combo_changed(self, combo):
            print("Desde %s" % self.get_combo_text(combo))
    def get_combo_text(self, combo):
        tree_iter = combo.get_active_iter()
        if tree_iter is not None:
            model = combo.get_model()
            return model[tree_iter][0]
    def on_comprar(self, btn):
        new_line = self.get_combo_text(self.desdebox) +" "+ self.get_combo_text(self.hastabox)
        buf = self.txtarea.get_buffer()
        buf.set_text(new_line)



head = HeaderBarUI()
