import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class HeaderBarUI(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_default_size(400, 200)

        vbox1 = Gtk.VBox()
        self.add(vbox1)
        vbox1.set_border_width(10)
        vbox1.set_spacing(10)

        tophbox = Gtk.HBox()
        vbox1.add(tophbox)

        dataGrid = Gtk.Grid()
        dataGrid.set_column_spacing(75)
        dataGrid.set_row_spacing(3)

        dataGrid.attach(Gtk.Label("Data"), 0, 0, 1, 1)
        data_field = Gtk.Entry()
        dataGrid.attach(data_field, 1, 0, 1, 1)

        dataGrid.attach(Gtk.Label("Desde"), 0, 1, 1, 1)
        origen = Gtk.ComboBox()

        # origenstore = Gtk.ListStore(str)
        # origencell = Gtk.CellRendererText()
        # origen.pack_start(origencell, True)
        # origen.add_attribute(origencell, 'origen', 0)
        # origenstore.append(["Madrid"])
        # origenstore.append(["Barcelona"])
        # origen.set_model(origenstore)
        # origen.connect('changed', self.on_changed)
        origen.set_active(0)

        dataGrid.attach(origen, 1, 1, 1, 1)

        dataGrid.attach(Gtk.Label("Hasta"), 0, 2, 1, 1)
        destin = Gtk.ComboBox()
        dataGrid.attach(destin, 1, 2, 1, 1)

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
        tophbox.add(dataGrid)
        tophbox.add(radiosframe)

        txtarea = Gtk.TextView()
        txtarea.set_editable(False)
        txtarea.set_margin_start(5)
        txtarea.set_margin_end(5)
        txtarea.set_margin_bottom(5)
        txtarea.set_size_request(-1, 100)

        frame = Gtk.Frame()
        frame.set_label("Disponibles")

        frame.add(txtarea)

        vbox1.add(frame)

        buttons = Gtk.HBox()
        buscar = Gtk.Button("Buscar")
        comprar = Gtk.Button("Comprar")
        salir = Gtk.Button("Salir")
        buttons.add(buscar)
        buttons.add(comprar)
        buttons.add(salir)
        vbox1.add(buttons)

        self.connect("destroy", Gtk.main_quit)
        self.show_all()
        Gtk.main()


head = HeaderBarUI()
