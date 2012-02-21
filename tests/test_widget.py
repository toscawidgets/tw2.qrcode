from tw2.core.testbase import WidgetTest
import tw2.qrcode

class TestWidget(WidgetTest):
    # place your widget at the TestWidget attribute
    widget = tw2.qrcode.QRCodeWidget
    # Initilization args. go here
    attrs={'id':'qrcodetest'}
    params={'data': 'This is a test of the emergency awesome system.', 'qr_type': 9}
    expected = """<div id="qrcodetest" class="qr-code" style="width:160; height:160;"></div>"""
