import tw2.core as twc
import tw2.jquery

import tw2.jquery
import tw2.jquery.base as tw2_jq_c_b
import tw2.jqplugins.ui.base as tw2_jq_ui

import base

class QRCodeWidget(tw2_jq_ui.JQueryUIWidget):
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

    data = twc.Param("The QRCode data", default="http://github.com/gregjurman/tw2.qrcode")

    correction_level = twc.Param("The QRCode Correction Level", default="H")

    level = twc.Param("The size of the QRCode", default=4)

    width = twc.Param("The total width of the entire QRCode", default=160)

    def prepare(self):
        super(QRCodeWidget, self).prepare()
        # put code here to run just before the widget is displayed
        if self.correction_level not in ['H', 'Q', 'M', 'L']:
            self.correction_level = 'H'
        if self.level <= 0 and self.level > 4:
            self.level = 4

        self.width = str(self.width)
        self.level = str(self.level)
