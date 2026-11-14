NEW_COVER = """cv1 = '<section class="sl cvr2"><h1 style="position:absolute;left:-9999px">หน้าปก</h1><div class="cvc"><div class="cvl"><img src="assets/logo.png"></div><div class="cvchip">สไลด์ติวสอบแข่งขัน · ระดับประถมศึกษาตอนปลาย</div><div class="cvt">การแข่งขันสอบวัดทักษะวิชาการระดับชาติ (สวช.)<br>ชิงถ้วยพระราชทานฯ</div><div class="cvs">วิชา<b>คณิตศาสตร์</b> · พ.ศ. 2567 · รหัสชุดข้อสอบ 201010</div><div class="cvm">ข้อจริง 30 ข้อ + Mock Test 60 ข้อ + เฉลยทุกหน้า</div></div><div class="cvf"><span class="brand">Math by T’Yasmin</span></div></section>'
cover = '<section class="sl cover"><h1 style="position:absolute;left:-9999px">สารบัญ</h1><div class="chip">สารบัญ</div><div class="big">ข้อสอบ สวช. <b>คณิตศาสตร์</b> พ.ศ. 2567 · รหัสชุด 201010</div><div class="meta">ข้อจริง 30 ข้อ · Mock Test 60 ข้อ (ข้อละ 2 ข้อ) · เฉลยทุกข้อ</div><div class="list">'+''.join(f'<div><b>ข้อ {n}</b> {html.escape(ALL[n]["topic"])}</div>' for n in range(1,31))+'<div style="grid-column:span 6;text-align:center;--c:#E8C877">ลำดับ: ข้อจริง → เฉลย → Mock Test 1 → เฉลย → Mock Test 2 → เฉลย · เขียนวิธีคิดบนสไลด์ด้วยปากกาใน GoodNotes</div></div><div class="ft"><span></span><span class="brand">Math by T’Yasmin</span></div></section>'
"""
NEW_CSS = """
.cvr2{padding:0;background:linear-gradient(135deg,#1C3A6B 0%,#2F5FA8 60%,#4A86D8 100%);color:#fff;align-items:center;justify-content:center;text-align:center}
.cvr2 .cvc{display:flex;flex-direction:column;align-items:center;gap:7mm}
.cvr2 .cvl{background:#fff;border-radius:50%;width:62mm;height:62mm;display:flex;align-items:center;justify-content:center;box-shadow:0 0 0 2.4mm #F3E7C9}
.cvr2 .cvl img{width:50mm;height:auto}
.cvr2 .cvchip{background:#F3E7C9;color:#1C3A6B;border-radius:8mm;padding:2mm 10mm;font-weight:700;font-size:17pt}
.cvr2 .cvt{font-size:30pt;font-weight:700;line-height:1.35}
.cvr2 .cvs{font-size:19pt;font-weight:600;color:#DCE4F0}.cvr2 .cvs b{color:#F3E7C9}
.cvr2 .cvm{font-size:15pt;font-weight:600;background:rgba(255,255,255,.14);border-radius:6mm;padding:2mm 8mm}
.cvr2 .cvf{position:absolute;right:11mm;bottom:6mm}.cvr2 .cvf .brand{font-family:Mali,sans-serif;font-weight:700;color:#F3E7C9;font-size:13.5pt}
"""
