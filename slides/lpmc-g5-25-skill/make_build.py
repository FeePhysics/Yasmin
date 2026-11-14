# สร้าง build_lp.py จาก build10.py ของสกิล (deck_blue) — เปลี่ยนเฉพาะข้อมูล ข้อความปก/ป้าย และสี Mock Test เป็นโทนม่วง
import re
s = open('build10.py').read()
def rep(a, b, count=1):
    global s
    assert s.count(a) >= 1, a
    s = s.replace(a, b) if count == 0 else s.replace(a, b, count)
rep('import data10', 'import data_lp as data10')
rep('"ข้อจริง · ข้อสอบ สวช."', '"ข้อจริง · LPMC ครั้งที่ 25"')
cv = re.search(r"^cv1 = .*$", s, re.M).group(0)
s = s.replace(cv, """cv1 = '<section class="sl cvr"><h1 style="position:absolute;left:-9999px">หน้าปก Sigma Junior ป.5</h1><img class="bgb" src="assets/cover_blur.jpg"><img class="fg" src="assets/cover2.jpg"></section>'""")
cov = re.search(r"^cover = .*$", s, re.M).group(0)
new = (cov.replace('<div class="chip">สารบัญ</div>', '<div class="chip">สารบัญ · สไลด์ติวสอบแข่งขัน</div>')
          .replace('ข้อสอบ สวช. <b>คณิตศาสตร์</b> พ.ศ. 2567 · รหัสชุด 201010', 'ชิงแชมป์การคิดและแก้ปัญหา LPMC ครั้งที่ 25<br><b>คณิตศาสตร์</b> ป.5 · พ.ศ. 2567')
          .replace('ข้อจริง 30 ข้อ · Mock Test 60 ข้อ (ข้อละ 2 ข้อ) · เฉลยทุกข้อ', 'ทั้งหมด 30 ข้อ · ข้อจริง → เฉลย → Mock Test 1 → เฉลย → Mock Test 2 → เฉลย'))
assert new != cov
s = s.replace(cov, new)
rep("STAIR={1,2,3,4,5,6,7,8,9,12,13,14,15,16,17,18,19,20,21,22,23,24,25}", "STAIR={1,3,4,5,7,8,9,11,12,13,14,16,17,18,19,20,21,23,25,28,29,30}")
rep("if it['aimg'] and no in (24,25,28,30): inl=f'<div class=\"inl{\" wide\" if no in (24,25,28,30) else \"\"}\">{it[\"aimg\"]}</div>'; it=dict(it,aimg='')",
    "if it['aimg'] and no in (27,): inl=f'<div class=\"inl wide\">{it[\"aimg\"]}</div>'; it=dict(it,aimg='')")
rep("BELOW=set()", "BELOW={3,4,12,27}")
rep("<title>สไลด์ข้อสอบ สวช. 201010 (30 ข้อ)</title>", "<title>สไลด์ติว LPMC ป.5 ครั้งที่ 25 (30 ข้อ)</title>")
rep("open('deck10.html','w')", "open('deck_lp.html','w')")
# สี Mock Test: เทาอมฟ้า → ม่วง
PURPLE = {'#3E566E': '#4B3A86', '#6B7F99': '#6B4FBB', '#97A8BF': '#A493DA', '#B7C4D6': '#C9BEEA', '#DCE4F0': '#E9E3F7', '#C7D3E4': '#D9D0F0',
          '#D5DFEE': '#E3DCF5', '#8AA0BC': '#9C88D6', '#E5ECF6': '#EFE9FB', '#7C93B0': '#8A73CC', '#2B3E55': '#33285E', '#F3F5F9': '#F4F1FB'}
for a, b in PURPLE.items(): s = re.sub(re.escape(a), b, s, flags=re.I)
s = s.replace('.sl.mock{background:url(assets/bg_mock.jpg)', '.sl.mock{background:url(assets/bg_mock.jpg)')
s = s.replace('.steps .inl.wide{min-height:34mm}', '.prob ul{list-style:none;margin:1.5mm 0 0 2mm}.prob ul.opts{display:flex;flex-wrap:wrap;gap:1.2mm 6mm;margin-left:0}.prob ul.opts li{background:#EEF2F9;border-radius:3mm;padding:0 3mm;margin:0}.below .pimg .img{height:46mm}.steps .tb2{font-size:.62em;margin-top:1.5mm}.steps .tb2 th,.steps .tb2 td{padding:.6mm 2.6mm}\n.steps .inl.wide{min-height:34mm}')
s = s.replace('.cover .big{font-size:34pt', '.cover .big{font-size:31pt')
open('build_lp.py', 'w').write(s)
print('ok')
