# สรุปคำตอบครู 1 หน้า + ใบจุดสังเกต/ข้อควรระวัง
import html, sys
sys.path.insert(0, '.')
import data_p2 as data_lp
F = '''@font-face{font-family:Mali;font-weight:500;src:url(ff/mali-thai-500-normal.woff2);unicode-range:U+0E01-0E5B,U+200B-200D,U+25CC}
@font-face{font-family:Mali;font-weight:500;src:url(ff/mali-latin-500-normal.woff2);unicode-range:U+0000-00FF,U+2013-2014,U+2018-201F,U+2212,U+00D7,U+00F7}
@font-face{font-family:Mali;font-weight:700;src:url(ff/mali-thai-700-normal.woff2);unicode-range:U+0E01-0E5B,U+200B-200D,U+25CC}
@font-face{font-family:Mali;font-weight:700;src:url(ff/mali-latin-700-normal.woff2);unicode-range:U+0000-00FF,U+2013-2014,U+2018-201F,U+2212,U+00D7,U+00F7}
@page{size:A4;margin:11mm}body{font-family:Mali,sans-serif;color:#2E3A12;font-size:9.6pt;margin:0}h1{font-size:13.5pt;margin:0 0 1mm}.s{color:#A88418;font-weight:700;margin-bottom:3mm}
table{border-collapse:collapse;width:100%}td,th{border:1px solid #DDE3BF;padding:1.1mm 2.6mm;text-align:left;vertical-align:top}th{background:#3F4F1E;color:#fff}th.m{background:#A88418}
tr:nth-child(odd) td{background:#FAF5E6}.c{text-align:center;font-weight:700;width:20mm}.f{margin-top:3mm;font-size:9pt;color:#7A5C0E}'''
P = data_lp.P
rows = ''.join(f"<tr><td class=c>{p['no']}</td><td>{html.escape(p['topic'])}</td>" + ''.join(f"<td class=c>{it['ans']}</td>" for k, it in enumerate(p['items'])) + '</tr>' for p in P)
notes = [it['note'] for p in P for it in p['items'] if it['note']]
open('key_lp.html', 'w').write(f"<!doctype html><meta charset=utf-8><style>{F}</style><h1>สรุปคำตอบสำหรับครู · LPMC ป.2 ครั้งที่ 23 (2565) ข้อ 16–30</h1><div class=s>ข้อจริง 15 ข้อ + Mock Test 30 ข้อ · Math by T’Yasmin</div>"
    f"<table><tr><th>ข้อ</th><th>หัวข้อ</th><th>ข้อจริง</th><th class=m>Mock 1</th><th class=m>Mock 2</th></tr>{rows}</table>"
    f"<div class=f>ข้อที่ตีความเอง: " + ' · '.join(html.escape(n) for n in notes) + " · ไม่มีเฉลยทางการมาเทียบ คำตอบคำนวณด้วยโปรแกรมทุกข้อ</div>")
trows = ''.join(f"<tr><td class=c>{p['no']}</td><td><b>{html.escape(p['topic'])}</b></td><td>💡 {html.escape(p['tip'])}</td><td>⚠ {html.escape(p['warn'])}</td></tr>" for p in P)
open('tips_lp.html', 'w').write(f"<!doctype html><meta charset=utf-8><style>{F} td.c{{width:9mm}}</style><h1>สรุปจุดสังเกต–ข้อควรระวัง (อ่านทวนก่อนสอน)</h1><div class=s>LPMC ป.2 ครั้งที่ 23 · Math by T’Yasmin</div>"
    f"<table><tr><th>ข้อ</th><th>หัวข้อ</th><th>จุดสังเกต</th><th class=m>ข้อควรระวัง</th></tr>{trows}</table>")
print('ok')
