<%namespace name="tw" module="tw2.core.mako_util"/>
<div ${tw.attrs(attrs=w.attrs)} class="qr-code" style="width:${w.width}; height:${w.width};"></div>
<script type="text/javascript">
draw_qrcode('${w.selector}', '${w.data}', ${w.level}, QRErrorCorrectLevel.${w.correction_level}, ${w.width});
</script>
