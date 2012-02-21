import tw2.core as twc

qrcode_js = twc.JSLink(modname=__name__, filename='static/qrcode.js')
qrcode_css = twc.CSSLink(modname=__name__, filename='static/qrcode.css')

js_draw_qr = twc.js_function('draw_qrcode')
