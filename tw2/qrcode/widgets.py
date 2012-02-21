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

    level = twc.Param("(int) The size of the QRCode. Valid options: 0-4", default=4)

    width = twc.Param("(int) The total width of the widget in pixels", default=160)

    def prepare(self):
        if 'None' in str(type(self.data)):
            raise ValueError, "data parameter must be a string or unicode"

        super(QRCodeWidget, self).prepare()
        # put code here to run just before the widget is displayed
        if self.correction_level.upper() not in ['H', 'Q', 'M', 'L']:
            self.correction_level = 'H'
        if self.level <= 0 and self.level > 4:
            self.level = 4

        if not hasattr(self, 'id') or 'id' not in self.attrs:
            raise ValueError, 'JQueryWidget must be supplied an id'

        self.selector = self.attrs['id'].replace(':', '\\:') # grabed from tw2.jqplugins.ui
        #self.width = str(self.width)
        #self.level = str(self.level)
        self.add_call(base.js_draw_qr(self.selector, self.data, "QRErrorCorrectLevel.%s"%self.correction_level, self.width))
