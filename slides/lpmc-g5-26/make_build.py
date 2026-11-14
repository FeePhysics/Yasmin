# สร้าง build_g5b.py จาก build10.py ของสกิล (deck_blue) — ข้อมูล LPMC ป.5 ครั้งที่ 26 โทนเขียวขี้ม้า-เหลือง-ขาว-ครีม
import re
s = open('build10.py').read()
def rep(a, b, count=1):
    global s
    assert s.count(a) >= 1, a
    s = s.replace(a, b) if count == 0 else s.replace(a, b, count)
rep('import data10', 'import data_g5b as data10')
rep('"ข้อจริง · ข้อสอบ สวช."', '"ข้อจริง · LPMC ครั้งที่ 26"')
cv = re.search(r"^cv1 = .*$", s, re.M).group(0)
s = s.replace(cv, """cv1 = '<section class="sl cvr2"><h1 style="position:absolute;left:-9999px">หน้าปก</h1><div class="cvline"></div><div class="cvline2"></div><div class="cvc"><div class="cvl"><img src="assets/logo.png"></div><div class="cvchip">สไลด์ติวสอบแข่งขัน · ระดับชั้นประถมศึกษาปีที่ 5</div><div class="cvt">ข้อสอบชิงแชมป์การคิดและการแก้ปัญหาคณิตศาสตร์<br>ครั้งที่ 26 (LPMC)</div><div class="cvs">วิชา<b>คณิตศาสตร์</b> · ปีการศึกษา 2568 · สอบวันอาทิตย์ที่ 16 พฤศจิกายน 2568</div><div class="cvm">ข้อจริง 30 ข้อ · Mock Test 60 ข้อ · เฉลยละเอียดทุกข้อ</div></div><div class="cvf"><span class="brand">Math by T’Yasmin</span></div></section>'""")
cov = re.search(r"^cover = .*$", s, re.M).group(0)
new = (cov.replace('<div class="chip">สารบัญ</div>', '<div class="chip">สารบัญ · สไลด์ติวสอบแข่งขัน</div>')
          .replace('ข้อสอบ สวช. <b>คณิตศาสตร์</b> พ.ศ. 2567 · รหัสชุด 201010', 'ชิงแชมป์การคิดและแก้ปัญหา LPMC ครั้งที่ 26<br><b>คณิตศาสตร์</b> ป.5 · พ.ศ. 2568')
          .replace('ข้อจริง 30 ข้อ · Mock Test 60 ข้อ (ข้อละ 2 ข้อ) · เฉลยทุกข้อ', 'ทั้งหมด 30 ข้อ · ข้อจริง → เฉลย → Mock Test 1 → เฉลย → Mock Test 2 → เฉลย'))
assert new != cov
s = s.replace(cov, new)
rep("STAIR={1,2,3,4,5,6,7,8,9,12,13,14,15,16,17,18,19,20,21,22,23,24,25}", "STAIR={1,2,3,5,6,7,8,9,10,12,13,15,16,17,18,19,20,21,22,23,24,25,26,28,29,30}")
rep("if it['aimg'] and no in (24,25,28,30): inl=f'<div class=\"inl{\" wide\" if no in (24,25,28,30) else \"\"}\">{it[\"aimg\"]}</div>'; it=dict(it,aimg='')",
    "if it['aimg'] and no in (6,11,18,27) and it['aimg']: inl=f'<div class=\"inl wide\">{it[\"aimg\"]}</div>'; it=dict(it,aimg='')")
rep("BELOW=set()", "BELOW={6,11,14,18,27}")
rep("<title>สไลด์ข้อสอบ สวช. 201010 (30 ข้อ)</title>", "<title>สไลด์ติว LPMC ป.5 ครั้งที่ 26 (30 ข้อ)</title>")
rep("open('deck10.html','w')", "open('deck_g5b.html','w')")
# โทนเขียวขี้ม้า-เหลือง-ขาว-ครีม: ข้อจริง = เขียวขี้ม้าบนพื้นครีม · Mock Test = เหลืองมัสตาร์ดบนพื้นขาวอมเหลือง
COLORS = {
  # ข้อจริง (เขียวขี้ม้า)
  '#1C3A6B': '#3F4F1E', '#2F5FA8': '#5E6E2B', '#4A86D8': '#8A9A48', '#10244A': '#2E3A12', '#5B7FB5': '#6F7F35',
  '#8FB1E0': '#B8C27E', '#C9D6EA': '#DDE3BF', '#D4DDEB': '#DCDDC4', '#9DB6DA': '#B8C27E', '#6C9BDC': '#8A9A48',
  '#CFE0F6': '#E4E8CC', '#E3ECF8': '#EEF0DD', '#EAF0F8': '#F1F3E4', '#E9EEF6': '#F1F3E4', '#DCE5F2': '#E6E9D2', '#4A5C78': '#4A5426',
  # ครีม/เหลือง
  '#F8F3E4': '#FAF5E6', '#E8C877': '#F2C230', '#F3E7C9': '#FBEFC2', '#F7EEDA': '#FCF4D9', '#F0DFB0': '#F9E49A', '#D9B866': '#E2B42A',
  '#C9B26A': '#E2B42A', '#B8923C': '#B8901A', '#EFD793': '#F6D66A', '#F6EAC8': '#FCF0CB', '#4A3A10': '#4A3A10',
  # Mock Test (เหลืองมัสตาร์ด)
  '#3E566E': '#7A5C0E', '#6B7F99': '#A88418', '#97A8BF': '#D4B13C', '#B7C4D6': '#EAD58C', '#DCE4F0': '#F7EED0', '#C7D3E4': '#EFE2AE',
  '#D5DFEE': '#F3E8BE', '#8AA0BC': '#C9A43A', '#E5ECF6': '#FBF4DC', '#7C93B0': '#B8962A', '#2B3E55': '#5C4508', '#F3F5F9': '#FFFBEF', '#E6EBF3': '#F7EED0',
}
s = s.replace('rgba(217,112,26,.25)', 'rgba(63,79,30,.22)').replace('rgba(47,138,78,.25)', 'rgba(168,132,24,.25)')
s = re.sub('|'.join(re.escape(k) for k in COLORS), lambda m: COLORS[m.group(0).upper()], s, flags=re.I)
s = s.replace('.cvr{padding:0;background:#F4F7FC}', '.cvr{padding:0;background:#F4F7FC}')
s = s.replace('.steps .inl.wide{min-height:34mm}', '.cvr2 .cvline{position:absolute !important;left:0;right:0;top:0;height:3.2mm;background:#F2C230}.cvr2 .cvline2{position:absolute !important;left:0;right:0;bottom:0;height:3.2mm;background:#F2C230}\n.dg{display:inline-block;min-width:1.35em;text-align:center;border:.5mm solid currentColor;border-radius:1mm;margin-right:1.2mm;line-height:1.3;background:#fff}.pimg .crop,.aimg .crop{background:#fff}img.img{object-fit:contain}.below .pimg img.crop{max-height:54mm;height:auto;max-width:94%}.steps .inl.wide:has(img){min-height:40mm}.steps .inl.wide img{max-height:44mm !important}.ntri{margin:2mm auto 0;font-size:.9em;text-align:center}.ntr{display:flex;justify-content:center;gap:3mm;position:relative}.ntr span{min-width:2em}.ntr em{position:absolute;right:2mm;font-style:normal;font-size:.8em;color:#5E6E2B}\n.steps .inl.wide{min-height:34mm}')
s = s.replace('.sl.mock{background:url(assets/bg_mock.jpg)', '.sl.mock{background:url(assets/bg_mock.jpg)')
s = s.replace('.steps .inl.wide{min-height:34mm}', '.prob ul{list-style:none;margin:1.5mm 0 0 2mm}.prob ul.opts{display:flex;flex-wrap:wrap;gap:1.2mm 6mm;margin-left:0}.prob ul.opts li{background:#F3F1E2;border-radius:3mm;padding:0 3mm;margin:0}.below .pimg .img{height:46mm}.steps .tb2{font-size:.62em;margin-top:1.5mm}.steps .tb2 th,.steps .tb2 td{padding:.6mm 2.6mm}\n.steps .inl.wide{min-height:34mm}')
s = s.replace('.cover .big{font-size:34pt', '.cover .big{font-size:31pt')
open('build_g5b.py', 'w').write(s)
print('ok')
