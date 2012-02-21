"""
Here you can create samples of your widgets by providing default parameters,
inserting them in a container widget, mixing them with other widgets, etc...
These samples will appear in the WidgetBrowser

See http://toscawidgets.org/documentation/WidgetBrowser for more information
"""

import widgets

class DemoQrcode(widgets.QRCodeWidget):
    # Provide default parameters, value, etc... here
    # default = <some-default-value>
    id = "demoqr"
    qr_type = 9
    data = "Test text qrcode. This has a lot of data in it."
    width = 300
