import tw2.core as twc


class Qrcode(twc.Widget):
    template = "genshi:tw.qrcode.templates.qrcode"

    # declare static resources here
    # you can remove either or both of these, if not needed
    resources = [
        twc.JSLink(modname=__name__, filename='static/qrcode.js'),
        twc.CSSLink(modname=__name__, filename='static/qrcode.css'),
    ]

    @classmethod
    def post_define(cls):
        pass
        # put custom initialisation code here

    def prepare(self):
        super(Qrcode, self).prepare()
        # put code here to run just before the widget is displayed
