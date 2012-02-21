import tw2.core as twc
import tw2.jquery

import base

class QRCodeWidget(twc.Widget):
    '''
    Creates a QRCode using client side javascript.
    '''
    # declare static resources here
    # you can remove either or both of these, if not needed
    resources = [
        tw2.jquery.jquery_js,
        base.qrcode_js,
        base.qrcode_css,
    ]
    template = "mako:tw2.qrcode.templates.qrcode"

    data = twc.Param("(str) data to be encoded", default=None)

    correction_level = twc.Param("(str) QRCode Correction Level. Valid options: H, Q, M, L", default="H")

    qr_type = twc.Param("(int) The type of QRCode. Valid options: 1 - 40", default=None)

    width = twc.Param("(int) The total width of the widget in pixels", default=160)

    def prepare(self):
        if 'str' not in str(type(self.data)):
            raise ValueError, "QRCodeWidget data parameter must be a string"

        super(QRCodeWidget, self).prepare()
        # put code here to run just before the widget is displayed
        if 'str' not in str(type(self.correction_level)) and str(self.correction_level).upper() not in ['H', 'Q', 'M', 'L']:
            raise ValueError, 'QRCodeWidget correction_level must be a string containing one of the following options: H, Q, M, L'

        if 'int' not in str(type(self.qr_type)) or int(self.qr_type) <= 0 and int(self.qr_type) > 40:
            raise ValueError, "QRCodeWidget qr_type must be between 1 and 40 inclusive"

        if not hasattr(self, 'id') or 'id' not in self.attrs:
            raise ValueError, 'QRCodeWidget must be supplied an id'

        self.selector = self.attrs['id'].replace(':', '\\:') # grabed from tw2.jqplugins.ui
        self._width = str(self.width)

        self.add_call(base.js_draw_qr(self.selector, 
            self.data,
            self.qr_type,
            twc.js_symbol("QRErrorCorrectLevel.%s"%self.correction_level), 
            self.width))
