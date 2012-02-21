import tw2.core as twc
import tw2.qrcode

def request_local_tst():
    global _request_local, _request_id
# if _request_id is None:
# raise KeyError('must be in a request')
    if _request_local == None:
        _request_local = {}
    try:
        return _request_local[_request_id]
    except KeyError:
        rl_data = {}
        _request_local[_request_id] = rl_data
        return rl_data

twc.core.request_local = request_local_tst
_request_local = {}
_request_id = 'whatever'

def setup():
    twc.core.request_local = request_local_tst
    twc.core.request_local()['middleware'] = twc.make_middleware()


def test_exception_no_id():
    w = tw2.qrcode.QRCodeWidget(data="I am the cheese", qr_type=4)
    try:
        w.display()
        assert(False)
    except ValueError as e:
        assert(str(e) == 'QRCodeWidget must be supplied an id')

def test_exception_nodata():
    w = tw2.qrcode.QRCodeWidget(id='foobar', qr_type=1)
    try:
        w.display()
        assert(False)
    except ValueError as e:
        assert(str(e) == 'QRCodeWidget data parameter must be a string')

def test_exception_bad_qr_type():
    w = tw2.qrcode.QRCodeWidget(id='foobar', data="I am the cheese")
    try:
        w.display()
        assert(False)
    except ValueError as e:
        assert(str(e) == 'QRCodeWidget qr_type must be between 1 and 40 inclusive')


def test_exception_bad_correction_level():
    w = tw2.qrcode.QRCodeWidget(id='foobar', data="I am the cheese", qr_type=4, correction_level=None)
    try:
        w.display()
        assert(False)
    except ValueError as e:
        assert(str(e) == 'QRCodeWidget correction_level must be a string containing one of the following options: H, Q, M, L')
