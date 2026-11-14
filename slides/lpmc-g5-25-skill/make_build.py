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
# สีตามหน้าปก Sigma Junior ป.5: น้ำเงินเข้ม #01286D · ฟ้าสด #177DFB · ม่วง #6A5CE5 · เหลืองดาว #FECA54 · พื้นฟ้าขาว #F4F7FC
COLORS = {
  # ข้อจริง (น้ำเงิน-ฟ้า)
  '#1C3A6B': '#01286D', '#2F5FA8': '#177DFB', '#4A86D8': '#5FA8FC', '#10244A': '#0A2463', '#5B7FB5': '#3D8BF7',
  '#8FB1E0': '#99C8FC', '#C9D6EA': '#CFE3FB', '#D4DDEB': '#D6E4F7', '#9DB6DA': '#99C8FC', '#6C9BDC': '#5FA8FC',
  '#CFE0F6': '#D8E9FD', '#E3ECF8': '#E4EFFD', '#EAF0F8': '#EAF2FE', '#E9EEF6': '#EAF2FE', '#DCE5F2': '#DDEAFB', '#E9EEF6': '#EAF2FE', '#4A5C78': '#3A4F7A',
  # ครีม/เหลือง → ฟ้าขาว + เหลืองดาว
  '#F8F3E4': '#F4F7FC', '#E8C877': '#FECA54', '#F3E7C9': '#FFF1CC', '#F7EEDA': '#FFF6DD', '#F0DFB0': '#FFE7A6', '#D9B866': '#F2BE45',
  '#C9B26A': '#F2BE45', '#B8923C': '#E0A92E', '#EFD793': '#FED97F', '#F6EAC8': '#FFF1C9', '#4A3A10': '#5A4300',
  # Mock Test (เทาอมฟ้า → ม่วง)
  '#3E566E': '#3B2C9A', '#6B7F99': '#6A5CE5', '#97A8BF': '#A79CF2', '#B7C4D6': '#D1C9FC', '#DCE4F0': '#ECE9FE', '#C7D3E4': '#DCD6FD',
  '#D5DFEE': '#E6E1FE', '#8AA0BC': '#8F84EE', '#E5ECF6': '#F1EEFE', '#7C93B0': '#7F72EA', '#2B3E55': '#2A1F7A', '#F3F5F9': '#F5F3FE', '#E6EBF3': '#ECE9FE',
}
s = s.replace('rgba(217,112,26,.25)', 'rgba(1,40,109,.22)').replace('rgba(47,138,78,.25)', 'rgba(106,92,229,.25)')
s = re.sub('|'.join(re.escape(k) for k in COLORS), lambda m: COLORS[m.group(0).upper()], s, flags=re.I)
s = s.replace('.cvr{padding:0;background:#F4F7FC}', '.cvr{padding:0;background:#F4F7FC}')
s = s.replace('.steps .inl.wide{min-height:34mm}', '.dg{display:inline-block;min-width:1.35em;text-align:center;border:.5mm solid currentColor;border-radius:1mm;margin-right:1.2mm;line-height:1.3;background:#fff}.pimg .crop,.aimg .crop{background:#fff}img.img{object-fit:contain}.below .pimg img.crop{max-height:46mm;height:auto;max-width:92%}.below .pimg img[src$=\"q27.png\"]{height:74mm;max-height:74mm;width:auto}.steps .inl.wide:has(img){min-height:40mm}.steps .inl.wide img{max-height:44mm !important}\n.steps .inl.wide{min-height:34mm}')
s = s.replace('.sl.mock{background:url(assets/bg_mock.jpg)', '.sl.mock{background:url(assets/bg_mock.jpg)')
s = s.replace('.steps .inl.wide{min-height:34mm}', '.prob ul{list-style:none;margin:1.5mm 0 0 2mm}.prob ul.opts{display:flex;flex-wrap:wrap;gap:1.2mm 6mm;margin-left:0}.prob ul.opts li{background:#EEF2F9;border-radius:3mm;padding:0 3mm;margin:0}.below .pimg .img{height:46mm}.steps .tb2{font-size:.62em;margin-top:1.5mm}.steps .tb2 th,.steps .tb2 td{padding:.6mm 2.6mm}\n.steps .inl.wide{min-height:34mm}')
s = s.replace('.cover .big{font-size:34pt', '.cover .big{font-size:31pt')
open('build_lp.py', 'w').write(s)
print('ok')
