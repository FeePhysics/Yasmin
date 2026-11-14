import html
from gen2 import I,C
T=lambda t,e,a,f:(t,e,a,f)
M=[
("สนามกีฬามีลูกฟุตบอลอยู่หลายลูก นักเรียนยืมไปเล่น 76 ลูก เหลือ 124 ลูก เดิมมีลูกฟุตบอลกี่ลูก","x − 76 = 124",200,lambda x:x-76==124),
("ชมรมวาดภาพมีสมาชิกอยู่หลายคน รับสมัครเพิ่มอีก 17 คน ทำให้มีสมาชิก 64 คน เดิมมีสมาชิกกี่คน","x + 17 = 64",47,lambda x:x+17==64),
("แม่ค้าขายส้มโอไปแล้ว 39 ผล เหลือส้มโอ 58 ผล เดิมมีส้มโอกี่ผล","x − 39 = 58",97,lambda x:x-39==58),
("จำนวนหนึ่งบวก 86 ได้ 203 จงหาจำนวนนั้น","x + 86 = 203",117,lambda x:x+86==203),
("จำนวนหนึ่งลบ 59 เหลือ 41 จงหาจำนวนนั้น","x − 59 = 41",100,lambda x:x-59==41),
("นำ 200 ลบด้วยจำนวนหนึ่ง ได้ 137 จงหาจำนวนนั้น","200 − x = 137",63,lambda x:200-x==137),
("แพรสะสมแสตมป์ไว้หลายดวง ได้รับเพิ่มอีก 25 ดวง ทำให้มีแสตมป์ 92 ดวง เดิมมีแสตมป์กี่ดวง","x + 25 = 92",67,lambda x:x+25==92),
("ตอนเช้ามีคนว่ายน้ำอยู่ในสระหลายคน ว่ายเสร็จขึ้นจากสระไป 44 คน เหลือคนในสระ 36 คน ตอนแรกมีคนในสระกี่คน","x − 44 = 36",80,lambda x:x-44==36),
("กล่องใบหนึ่งมีดินสอ 150 แท่ง แจกเด็ก ๆ ไปหลายแท่ง เหลือดินสอ 72 แท่ง แจกไปกี่แท่ง","150 − x = 72",78,lambda x:150-x==72),
("รถแท็กซี่วิ่งไปแล้ว 56 กิโลเมตร ต้องวิ่งอีกจึงถึงจุดหมายซึ่งอยู่ห่างจากจุดเริ่มต้น 140 กิโลเมตร ต้องวิ่งอีกกี่กิโลเมตร","56 + x = 140",84,lambda x:56+x==140),
("ห้องประชุมมีเก้าอี้ 120 ตัว เก็บเก้าอี้ออกไปหลายตัว เหลือ 85 ตัว เก็บออกไปกี่ตัว","120 − x = 85",35,lambda x:120-x==85),
("บนต้นไม้มีนกเกาะอยู่หลายตัว มีนกบินมาสมทบอีก 29 ตัว ทำให้มีนก 77 ตัว เดิมมีนกกี่ตัว","x + 29 = 77",48,lambda x:x+29==77),
("ชมพู่ฝากเงินไว้ในธนาคารหลายบาท ถอนออกมา 65 บาท เหลือเงินฝาก 135 บาท เดิมฝากไว้กี่บาท","x − 65 = 135",200,lambda x:x-65==135),
("ในตะกร้ามีแอปเปิล 45 ผล และสับปะรดอีกหลายผล รวมผลไม้ทั้งหมด 98 ผล มีสับปะรดกี่ผล","45 + x = 98",53,lambda x:45+x==98),
("ทางรถไฟสายหนึ่งยาว 175 กิโลเมตร สร้างเสร็จแล้วบางส่วน เหลืออีก 68 กิโลเมตร สร้างเสร็จแล้วกี่กิโลเมตร","x + 68 = 175",107,lambda x:x+68==175),
("หนังสือการ์ตูนเล่มหนึ่งหนา 160 หน้า ต้นอ่านไปแล้ว 78 หน้า ยังเหลืออีกกี่หน้า (ให้ x แทนจำนวนหน้าที่เหลือ)","78 + x = 160",82,lambda x:78+x==160),
("แปลงผักกาดมีผักอยู่หลายต้น ย้ายไปปลูกที่อื่น 27 ต้น เหลือ 63 ต้น เดิมแปลงนี้มีผักกาดกี่ต้น","x − 27 = 63",90,lambda x:x-27==63),
("ร้านขายตั๋วคอนเสิร์ตมีตั๋วทั้งหมด 150 ใบ ขายไปแล้วหลายใบ เหลือ 38 ใบ ขายไปแล้วกี่ใบ","x + 38 = 150",112,lambda x:x+38==150),
("ในเกมเก็บเหรียญ เมฆเก็บเหรียญไว้หลายเหรียญ นำไปแลกของรางวัล 48 เหรียญ เหลือ 79 เหรียญ เมฆเก็บเหรียญไว้กี่เหรียญ","x − 48 = 79",127,lambda x:x-48==79),
("คุณยายมีด้ายไหมพรมยาวหลายเมตร ใช้ถักผ้าพันคอไป 63 เมตร เหลือ 87 เมตร เดิมมีด้ายกี่เมตร","x − 63 = 87",150,lambda x:x-63==87),
]
D=[
("ตลาดสดมีไข่ไก่อยู่หลายฟอง ลูกค้าซื้อไป 56 ฟอง และพ่อค้านำมาเติม 38 ฟอง ตอนนี้มีไข่ไก่ 412 ฟอง เดิมมีไข่ไก่กี่ฟอง","x − 56 + 38 = 412",430,lambda x:x-56+38==412),
("รถยนต์คันหนึ่งมีน้ำมันอยู่ในถังหลายลิตร ใช้ไป 85 ลิตร เติมเพิ่ม 120 ลิตร แล้วใช้อีก 47 ลิตร เหลือน้ำมัน 98 ลิตร เดิมมีน้ำมันกี่ลิตร","x − 85 + 120 − 47 = 98",110,lambda x:x-85+120-47==98),
("ลานจอดรถห้างแห่งหนึ่งมีรถอยู่หลายคัน ออกไป 64 คัน เข้ามา 85 คัน แล้วออกไปอีก 39 คัน ตอนนี้มีรถ 120 คัน เดิมมีรถกี่คัน","x − 64 + 85 − 39 = 120",138,lambda x:x-64+85-39==120),
("ในโหลมีลูกอมอยู่หลายเม็ด พี่ชายหยิบไป 45 เม็ด น้องสาวหยิบไป 38 เม็ด เหลือลูกอมในโหล 67 เม็ด เดิมมีลูกอมกี่เม็ด","x − 45 − 38 = 67",150,lambda x:x-45-38==67),
("ภูมีสติกเกอร์ 140 แผ่น ฟ้ามีสติกเกอร์อยู่จำนวนหนึ่ง ภูให้ฟ้า 25 แผ่น ทำให้สองคนมีสติกเกอร์เท่ากันพอดี เดิมฟ้ามีสติกเกอร์กี่แผ่น","140 − 25 = x + 25",90,lambda x:140-25==x+25),
("ปลามีเงิน 95 บาท ส้มมีเงินอยู่จำนวนหนึ่ง ปลาให้เงินส้ม 18 บาท ทำให้ส้มมีเงินมากกว่าปลา 6 บาท เดิมส้มมีเงินกี่บาท","x + 18 = 95 − 18 + 6",65,lambda x:x+18==95-18+6),
("ปัจจุบันยายอายุ 68 ปี อีก 15 ปีข้างหน้ายายจะอายุมากกว่าหลาน 50 ปี ปัจจุบันหลานอายุกี่ปี","68 + 15 − (x + 15) = 50",18,lambda x:68+15-(x+15)==50),
("คลังสินค้ามีพัสดุอยู่หลายกล่อง รับเข้ามาเพิ่ม 245 กล่อง ส่งออกไป 76 กล่อง และรับเข้ามาอีก 130 กล่อง ตอนนี้มีพัสดุ 600 กล่อง เดิมมีพัสดุกี่กล่อง","x + 245 − 76 + 130 = 600",301,lambda x:x+245-76+130==600),
("ต้นสอบ 3 วิชา คณิตศาสตร์ได้ 85 คะแนน ศิลปะได้ 72 คะแนน รวมสามวิชาได้ 240 คะแนน วิชาภาษาไทยได้กี่คะแนน","85 + x + 72 = 240",83,lambda x:85+x+72==240),
("ร้านกาแฟมีลูกค้านั่งอยู่หลายคน ช่วงแรกเข้ามา 14 คน ออกไป 8 คน ช่วงที่สองเข้ามา 22 คน ออกไป 17 คน ตอนนี้มีลูกค้า 45 คน เดิมมีลูกค้ากี่คน","x + 14 − 8 + 22 − 17 = 45",34,lambda x:x+14-8+22-17==45),
("แม่ให้เงินเตยไปโรงเรียนหลายบาท เตยซื้อขนม 35 บาท ซื้อน้ำ 18 บาท เหลือเงิน 47 บาท แม่ให้เงินเตยไปโรงเรียนกี่บาท","x − 35 − 18 = 47",100,lambda x:x-35-18==47),
("สวนสาธารณะมีต้นไม้อยู่หลายต้น ตายไป 34 ต้น แล้วปลูกใหม่ 80 ต้น ตอนนี้มีต้นไม้ 296 ต้น เดิมมีต้นไม้กี่ต้น","x − 34 + 80 = 296",250,lambda x:x-34+80==296),
("ร้านตุ๊กตามีตุ๊กตา 220 ตัว วันจันทร์ขายไปหลายตัว วันอังคารขายอีก 45 ตัว เหลือ 98 ตัว วันจันทร์ขายไปกี่ตัว","220 − x − 45 = 98",77,lambda x:220-x-45==98),
("ตะกร้าผลไม้ใบหนึ่งชั่งน้ำหนักรวมตะกร้าได้ 175 กิโลกรัม ผลไม้หนัก 138 กิโลกรัม ตะกร้าเปล่าหนักกี่กิโลกรัม","x + 138 = 175",37,lambda x:x+138==175),
("จำนวนหนึ่งบวก 78 แล้วลบ 145 ได้ 56 จงหาจำนวนนั้น","x + 78 − 145 = 56",123,lambda x:x+78-145==56),
("จำนวนหนึ่งลบ 89 แล้วบวก 134 ได้ 205 จงหาจำนวนนั้น","x − 89 + 134 = 205",160,lambda x:x-89+134==205),
("นำ 300 ลบด้วยจำนวนหนึ่ง แล้วลบอีก 85 ได้ 112 จงหาจำนวนนั้น","300 − x − 85 = 112",103,lambda x:300-x-85==112),
("ฟ้ามีการ์ดสะสมอยู่หลายใบ แลกกับเพื่อนได้เพิ่ม 28 ใบ แล้วเสียไป 36 ใบ ต่อมาซื้อเพิ่มอีก 50 ใบ ตอนนี้มีการ์ด 142 ใบ เดิมมีการ์ดกี่ใบ","x + 28 − 36 + 50 = 142",100,lambda x:x+28-36+50==142),
("ร้านสะดวกซื้อรับน้ำดื่มมา 240 ขวด ขายตอนเช้าไปหลายขวด เติมสินค้าอีก 60 ขวด ขายตอนบ่ายอีก 85 ขวด เหลือ 74 ขวด ตอนเช้าขายไปกี่ขวด","240 − x + 60 − 85 = 74",141,lambda x:240-x+60-85==74),
("ถังข้าวสารมีข้าวอยู่หลายกิโลกรัม แม่ใช้ไป 12 กิโลกรัม พ่อซื้อมาเพิ่ม 50 กิโลกรัม ป้าขอแบ่งไป 25 กิโลกรัม เหลือข้าว 93 กิโลกรัม เดิมมีข้าวกี่กิโลกรัม","x − 12 + 50 − 25 = 93",80,lambda x:x-12+50-25==93),
]
S1=I+M; S2=C+D
for S in (S1,S2):
    assert len(S)==40
    for i,(t,e,a,f) in enumerate(S): assert f(a),(i+1,t)
S1=[x for i,x in enumerate(S1) if i not in {8,23,24,39}]
S2=[x for i,x in enumerate(S2) if i not in {12,16,32,34}]
N1=[
("โรงอาหารมีน้ำส้มอยู่หลายแก้ว ขายไป 67 แก้ว เหลือ 83 แก้ว เดิมมีน้ำส้มกี่แก้ว","x − 67 = 83",150,lambda x:x-67==83),
("ช่างไม้มีตะปูอยู่หลายตัว ซื้อมาเพิ่มอีก 125 ตัว ทำให้มีตะปู 310 ตัว เดิมมีตะปูกี่ตัว","x + 125 = 310",185,lambda x:x+125==310),
("ฟาร์มโคนมรีดนมได้ตอนเช้า 85 ลิตร ตอนบ่ายรีดได้อีกหลายลิตร รวมทั้งวัน 160 ลิตร ตอนบ่ายรีดนมได้กี่ลิตร","85 + x = 160",75,lambda x:85+x==160),
("ร้านรองเท้ามีรองเท้าอยู่หลายคู่ ขายไป 74 คู่ เหลือ 96 คู่ เดิมมีรองเท้ากี่คู่","x − 74 = 96",170,lambda x:x-74==96),
("แม่ครัวทำขนมครกได้หลายชิ้น แบ่งให้เพื่อนบ้าน 48 ชิ้น เหลือ 72 ชิ้น ทำขนมครกได้กี่ชิ้น","x − 48 = 72",120,lambda x:x-48==72),
("ร้านขายผ้ามีผ้าไหม 200 เมตร ตัดขายไปหลายเมตร เหลือ 118 เมตร ตัดขายไปกี่เมตร","200 − x = 118",82,lambda x:200-x==118),
("คุณครูซื้อสีน้ำไว้หลายกล่อง ซื้อเพิ่มอีก 24 กล่อง รวมมีสีน้ำ 61 กล่อง เดิมซื้อสีน้ำไว้กี่กล่อง","x + 24 = 61",37,lambda x:x+24==61),
("บัตรรถไฟฟ้ามีเงินอยู่หลายบาท เติมเงินเพิ่ม 150 บาท ทำให้มีเงินในบัตร 235 บาท เดิมมีเงินในบัตรกี่บาท","x + 150 = 235",85,lambda x:x+150==235),
("ตู้แช่ในร้านสะดวกซื้อมีนมกล่องอยู่หลายกล่อง ลูกค้าซื้อไป 39 กล่อง เหลือ 61 กล่อง เดิมมีนมกี่กล่อง","x − 39 = 61",100,lambda x:x-39==61),
("จำนวนหนึ่งบวก 96 ได้ 215 จงหาจำนวนนั้น","x + 96 = 215",119,lambda x:x+96==215),
("ฟาร์มผึ้งเก็บน้ำผึ้งได้ 180 ขวด ส่งขายไปหลายขวด เหลือ 94 ขวด ส่งขายไปกี่ขวด","180 − x = 94",86,lambda x:180-x==94),
("สวนสัตว์ขายตั๋วเข้าชมตอนเช้าได้หลายใบ ตอนบ่ายขายได้อีก 73 ใบ รวมทั้งวัน 168 ใบ ตอนเช้าขายได้กี่ใบ","x + 73 = 168",95,lambda x:x+73==168),
]
N2=[
("ลานสเก็ตมีผู้เล่นอยู่หลายคน ออกไป 29 คน เข้ามาใหม่ 54 คน แล้วออกไปอีก 37 คน เหลือผู้เล่น 88 คน เดิมมีผู้เล่นกี่คน","x − 29 + 54 − 37 = 88",100,lambda x:x-29+54-37==88),
("ศูนย์ซ่อมรถมีรถรอซ่อมอยู่หลายคัน ซ่อมเสร็จส่งคืน 18 คัน รับรถใหม่เข้ามา 25 คัน แล้วส่งคืนอีก 23 คัน เหลือรถรอซ่อม 35 คัน เดิมมีรถรอซ่อมกี่คัน","x − 18 + 25 − 23 = 35",51,lambda x:x-18+25-23==35),
("พิมมีเงินเก็บอยู่จำนวนหนึ่ง ได้ค่าขนมเพิ่ม 200 บาท ซื้อชุดนักเรียน 135 บาท ซื้อกระเป๋า 90 บาท เหลือเงิน 175 บาท เดิมพิมมีเงินเก็บกี่บาท","x + 200 − 135 − 90 = 175",200,lambda x:x+200-135-90==175),
("ถังเอมีน้ำ 180 ลิตร ถังบีมีน้ำอยู่จำนวนหนึ่ง เทน้ำจากถังเอไปถังบี 35 ลิตร ทำให้สองถังมีน้ำเท่ากันพอดี เดิมถังบีมีน้ำกี่ลิตร","180 − 35 = x + 35",110,lambda x:180-35==x+35),
("ปัจจุบันคุณป้าอายุ 54 ปี เมื่อ 7 ปีที่แล้วคุณป้าอายุมากกว่าหลาน 38 ปี ปัจจุบันหลานอายุกี่ปี","54 − 7 − (x − 7) = 38",16,lambda x:54-7-(x-7)==38),
("ประกวดร้องเพลงมีผู้เข้าประกวดอยู่หลายคน รอบแรกตกรอบ 38 คน สมัครเพิ่ม 15 คน รอบสองตกรอบ 29 คน เหลือ 42 คน เดิมมีผู้เข้าประกวดกี่คน","x − 38 + 15 − 29 = 42",94,lambda x:x-38+15-29==42),
("ตู้เสื้อผ้ามี 3 ลิ้นชัก ลิ้นชักบนมีเสื้อ 24 ตัว ลิ้นชักกลางมี 35 ตัว ลิ้นชักล่างมีอีกหลายตัว รวมทั้งหมด 98 ตัว ลิ้นชักล่างมีเสื้อกี่ตัว","24 + 35 + x = 98",39,lambda x:24+35+x==98),
("โรงสีมีข้าวโพดอยู่หลายกระสอบ ส่งออก 56 กระสอบ รับเข้าเพิ่ม 90 กระสอบ แล้วส่งออกอีก 48 กระสอบ เหลือ 120 กระสอบ เดิมมีข้าวโพดกี่กระสอบ","x − 56 + 90 − 48 = 120",134,lambda x:x-56+90-48==120),
("แป้งมีลูกปัด 126 เม็ด ฝ้ายมีลูกปัดอยู่จำนวนหนึ่ง ฝ้ายให้ลูกปัดแป้ง 14 เม็ด ทำให้แป้งมีลูกปัดมากกว่าฝ้าย 20 เม็ด เดิมฝ้ายมีลูกปัดกี่เม็ด","126 + 14 − (x − 14) = 20",134,lambda x:126+14-(x-14)==20),
("ร้านซักรีดมีเงินทอน 450 บาท ตอนสายรับค่าซักผ้าเพิ่มหลายบาท แล้วจ่ายค่าน้ำ 135 บาท เหลือเงิน 390 บาท ตอนสายรับค่าซักผ้าเพิ่มกี่บาท","450 + x − 135 = 390",75,lambda x:450+x-135==390),
("นักปีนเขาเริ่มปีนจากระดับความสูง 120 เมตร ปีนขึ้นไปหลายเมตร ไหลลงมา 35 เมตร แล้วปีนต่ออีก 60 เมตร ถึงยอดเขาสูง 300 เมตร ปีนขึ้นครั้งแรกกี่เมตร","120 + x − 35 + 60 = 300",155,lambda x:120+x-35+60==300),
("ฟาร์มกุ้งมีกุ้งอยู่หลายตัว จับขายรอบแรก 120 ตัว ปล่อยลูกกุ้งเพิ่ม 200 ตัว จับขายรอบสอง 85 ตัว เหลือกุ้ง 330 ตัว เดิมมีกุ้งกี่ตัว","x − 120 + 200 − 85 = 330",335,lambda x:x-120+200-85==330),
]
for L in (N1,N2):
    for i,(t,e,a,f) in enumerate(L): assert f(a),t
S1+=N1;S2+=N2
assert len(S1)==48 and len(S2)==48
def pos(S,key): return [i+1 for i,x in enumerate(S) if key in x[0]][0]
fonts='''
@font-face{font-family:Looped;font-weight:500;src:url(ff/noto-sans-thai-looped-thai-500-normal.woff2);unicode-range:U+0E01-0E5B,U+200B-200D,U+25CC}
@font-face{font-family:Looped;font-weight:500;src:url(ff/noto-sans-thai-looped-latin-500-normal.woff2);unicode-range:U+0000-00FF,U+2013-2014,U+2018-201F,U+2212,U+00D7,U+00F7}
@font-face{font-family:Looped;font-weight:700;src:url(ff/noto-sans-thai-looped-thai-700-normal.woff2);unicode-range:U+0E01-0E5B,U+200B-200D,U+25CC}
@font-face{font-family:Looped;font-weight:700;src:url(ff/noto-sans-thai-looped-latin-700-normal.woff2);unicode-range:U+0000-00FF,U+2013-2014,U+2018-201F,U+2212,U+00D7,U+00F7}
@font-face{font-family:Mali;font-weight:700;src:url(ff/mali-thai-700-normal.woff2);unicode-range:U+0E01-0E5B,U+200B-200D,U+25CC}
@font-face{font-family:Mali;font-weight:700;src:url(ff/mali-latin-700-normal.woff2);unicode-range:U+0000-00FF,U+2013-2014,U+2018-201F,U+2212,U+00D7,U+00F7}
'''

fonts+='''@font-face{font-family:Mali;font-weight:500;src:url(ff/mali-thai-500-normal.woff2);unicode-range:U+0E01-0E5B,U+200B-200D,U+25CC}
@font-face{font-family:Mali;font-weight:500;src:url(ff/mali-latin-500-normal.woff2);unicode-range:U+0000-00FF,U+2013-2014,U+2018-201F,U+2212,U+00D7,U+00F7}
@font-face{font-family:Mali;font-weight:600;src:url(ff/mali-thai-600-normal.woff2);unicode-range:U+0E01-0E5B,U+200B-200D,U+25CC}
@font-face{font-family:Mali;font-weight:600;src:url(ff/mali-latin-600-normal.woff2);unicode-range:U+0000-00FF,U+2013-2014,U+2018-201F,U+2212,U+00D7,U+00F7}
'''
fonts+='''@font-face{font-family:Pacifico;font-weight:400;src:url(ff/pacifico-latin-400-normal.woff2);unicode-range:U+0000-00FF,U+2013-2014,U+2018-201F}
'''
fonts+='''@font-face{font-family:Fredoka;font-weight:600;src:url(ff/fredoka-latin-600-normal.woff2);unicode-range:U+0000-00FF,U+2013-2014,U+2018-201F}
'''
css=fonts+"""@page{size:A4;margin:0}
*{box-sizing:border-box}
body{margin:0;font-family:Mali,Looped,Loma,sans-serif;font-weight:500;font-size:8.5pt;color:#1c3a6b;line-height:1.3}
.pg{position:relative;width:210mm;height:297mm;padding:6mm 9mm 11mm;page-break-after:always;display:flex;flex-direction:column;gap:2mm;overflow:hidden;background:#fff}
.pg:last-child{page-break-after:auto}
.wm{position:absolute;left:50%;top:56%;width:112mm;transform:translate(-50%,-50%);opacity:.24;mix-blend-mode:multiply;z-index:0}
.pg>*:not(.wm){position:relative;z-index:1}
.bar{background:#1c3a6b;border-radius:5mm;border-bottom:2mm solid #f5b800;display:grid;grid-template-columns:30mm 1fr 34mm;align-items:center;padding:1.8mm 4mm 1.8mm;color:#fff;text-align:center}
.bar .ttl{display:flex;flex-direction:column;line-height:1.25}
.bar .main{font-weight:700;font-size:14.5pt;white-space:nowrap}
.bar .main{display:flex;align-items:center;justify-content:center;gap:3mm}.bar .main b{display:inline-flex;align-items:center;justify-content:center;width:10.5mm;height:10.5mm;border-radius:50%;background:#f5b800;color:#1c3a6b;border:1.1mm solid #fff;font-size:17pt;line-height:1;box-shadow:0 0 0 .6mm #f5b800}
.bar .lev{font-weight:700;font-size:10.5pt;color:#dfe9ff}
.pill{justify-self:end;background:#f5b800;color:#1c3a6b;border-radius:6mm;padding:1.3mm 4.4mm;font-weight:700;font-size:11.5pt;white-space:nowrap}
.info{background:#e8eefb;border-left:1.2mm solid #4a86e0;display:flex;align-items:flex-end;gap:2.5mm;padding:1.4mm 4mm 1.2mm;font-weight:700;font-size:10pt}
.info .fill{border-bottom:1px solid #6d86b5;height:4.8mm;display:inline-block}
.sec{display:flex;align-items:center;gap:3mm;padding-bottom:1.2mm;border-bottom:1px solid #1c3a6b}
.sec .p{background:#f5b800;border-radius:6mm;padding:.8mm 4mm;font-weight:700;font-size:11pt}
.sec .d{font-weight:700;font-size:10.4pt}
.sec .h{margin-left:auto;font-size:8.6pt;color:#4a6aa8}
.grid{flex:1;display:grid;grid-template-columns:1fr 1fr;gap:2.4mm 3.4mm;min-height:0}
.q{position:relative;background:rgba(255,255,255,.45);border:1.4px solid #c6d4ee;border-top:1.6mm solid var(--c);border-radius:4mm;padding:2.2mm 3mm 1.8mm 9.5mm;display:flex;flex-direction:column;gap:1mm;min-height:0}
.lf{display:flex;flex-direction:column;justify-content:space-between;gap:1mm;min-height:0}.rt{display:flex;flex-direction:column;gap:1.4mm;min-height:0}
.n{position:absolute;left:-1.4mm;top:-1.6mm;width:7.6mm;height:7.6mm;border-radius:50%;background:var(--c);color:var(--fg);text-align:center;line-height:7.6mm;font-weight:700;font-size:10pt}
.c0{--c:#1c3a6b;--fg:#fff}.c1{--c:#f5b800;--fg:#1c3a6b}.c2{--c:#4a86e0;--fg:#fff}
.t{font-weight:600;color:#10244a;line-height:1.38;font-size:8.8pt;text-align:justify;text-justify:inter-character;min-height:12.6mm}
.r{display:flex;align-items:flex-end;gap:2mm;font-size:8.8pt;color:#3d5a8c;font-weight:700}
.ta{margin-left:2mm}.ln.a{flex:0 0 27mm}.ln{flex:1;border-bottom:1.2px solid #7c97c8;height:4.2mm}
.w{position:relative;flex:1;min-height:10mm;margin:1.8mm 0 0;border:1.2px solid #9db6e0;border-radius:2.2mm;background:rgba(255,255,255,.5)}
.w span{position:absolute;left:3mm;top:-2.7mm;background:#fff;padding:0 1.4mm;font-size:8.4pt;color:#4a6aa8;font-weight:700}
.ans{display:flex;align-items:center;gap:2mm}
.r .box{flex:1;height:5.6mm;border:1.2px solid #7c97c8;border-radius:1.8mm;background:#eef3fc}
.ft{position:absolute !important;left:9mm;right:9mm;bottom:4.5mm;display:flex;justify-content:space-between;align-items:center;font-size:9pt;color:#4a6aa8}
.ft .brand{font-family:Fredoka,Mali,sans-serif;font-weight:600;color:#3a6cc2;font-size:12.5pt;letter-spacing:.3mm}
table{border-collapse:collapse;width:100%}td,th{border:1px solid #c6d4ee;padding:1.2mm 2.4mm;text-align:left;font-size:9.4pt;background:rgba(255,255,255,.55)}th{background:#1c3a6b;color:#fff}
.kc{display:flex;gap:5mm}
.tip{background:#e8eefb;border-left:1.2mm solid #4a86e0;padding:1.6mm 4mm;font-size:8.6pt;font-weight:600}
.kg{flex:1;display:grid;grid-template-columns:1fr 1fr;grid-auto-flow:column;grid-template-rows:repeat(24,1fr);gap:1.4mm 3.4mm;min-height:0}
.kq{position:relative;display:flex;align-items:center;gap:2mm;border:1.2px solid #c6d4ee;border-left:1.6mm solid var(--c);border-radius:2.4mm;padding:.4mm 2mm .4mm 1.6mm;background:rgba(255,255,255,.55);min-height:0}
.kq .n{position:static;flex:0 0 6.2mm;width:6.2mm;height:6.2mm;line-height:6.2mm;font-size:8pt}
.kt{display:flex;flex-direction:column;line-height:1.15;min-width:0}
.ke{font-size:7pt;color:#6b82ad;font-weight:500}
.ks{font-size:8.2pt;font-weight:600;color:#10244a;white-space:nowrap}
.ks b{background:#f5b800;color:#1c3a6b;border-radius:2mm;padding:0 1.6mm;margin-left:.4mm}

.note{background:#e8eefb;border-left:1.2mm solid #4a86e0;padding:2mm 4mm;font-weight:700}
"""
KEEP=['วันนี้','ตอนนี้','ตอนแรก','ตอนเช้า','ตอนบ่าย','ปัจจุบัน','เดิมมี','ทั้งหมด','สุดท้าย','ผู้โดยสาร','นักเรียน','จำนวนหนึ่ง','สติกเกอร์','กิโลเมตร','กิโลกรัม','เซนติเมตร','คะแนน','ภาษาไทย','คณิตศาสตร์']
UNITS=['กิโลเมตร','เซนติเมตร','กิโลกรัม','คะแนน','เหรียญ','กล่อง','แผ่น','เมตร','ลิตร','ขวด','ชิ้น','เล่ม','หน้า','แท่ง','เม็ด','ฟอง','บาท','ต้น','ดอก','ดวง','คัน','ตัว','ลูก','ผล','คน','ใบ','ปี','ชั้น','ที่']
import re
NUMRE=re.compile(r'(\d+) ('+'|'.join(UNITS)+')')
def prot(t):
    t=html.escape(t)
    t=NUMRE.sub(lambda m:f'<span style="white-space:nowrap">{m.group(1)}&nbsp;{m.group(2)}</span>',t)
    for w in KEEP: t=t.replace(w,f'<span style="white-space:nowrap">{w}</span>')
    return t
def card(i,t):
    return f'<div class="q c{i%3}"><span class="n">{i+1}</span><div class="t">{prot(t)}</div><div class="r"><span>สมการ</span><span class="ln"></span><span class="ta">ตอบ</span><span class="ln a"></span></div><div class="w"><span>วิธีคิด</span></div></div>'
def header(no,level,right=None):
    return f'<div class="bar"><span></span><div class="ttl"><span class="main"><b>1</b>หาจำนวนที่ไม่ทราบค่า : บวกและลบ</span><span class="lev">({level})</span></div><span class="pill">{right or "ใบงานชุดที่ "+str(no)}</span></div>'
def footer(n=None):
    mid=f'<span>{n}</span>' if n else '<span></span>'
    return f'<div class="ft"><span style="width:40mm"></span>{mid}<span class="brand">Math by T’Yasmin</span></div>'
def build(S,no,level,hint,pages):
    out='';k=0
    for pi,cnt in enumerate(pages):
        cards=''.join(card(k+j,S[k+j][0]) for j in range(cnt)); a=k+1; k+=cnt
        info=''
        if pi==0:
            info='<div class="info"><span>ชื่อ - นามสกุล</span><span class="fill" style="flex:1"></span><span>ชั้น</span><span class="fill" style="width:22mm"></span><span>เลขที่</span><span class="fill" style="width:16mm"></span><span>คะแนน</span><span class="fill" style="width:20mm"></span><span>/ 48</span></div>'
        out+=f'<div class="pg"><img class="wm" src="logo.png">{header(no,level)}{info}<div class="sec"><span class="p">ตอนที่ 1</span><span class="d">ข้อ {a}–{k}</span><span class="h">{hint}</span></div><div class="grid" style="grid-template-rows:repeat({cnt//2},1fr)">{cards}</div>{footer(pi+1)}</div>'
    return out
CUSTOM={
"185 − 30 = x + 30":"185 − 30 = 155 → x = 155 − 30",
"140 − 25 = x + 25":"140 − 25 = 115 → x = 115 − 25",
"x + 18 = 95 − 18 + 6":"95 − 18 + 6 = 83 → x = 83 − 18",
"68 + 15 − (x + 15) = 50":"อายุต่างกันเท่าเดิม → 68 − x = 50 → x = 68 − 50",
"54 − 7 − (x − 7) = 38":"อายุต่างกันเท่าเดิม → 54 − x = 38 → x = 54 − 38",
"58 − 11 = x + 11":"58 − 11 = 47 → x = 47 − 11",
"180 − 35 = x + 35":"180 − 35 = 145 → x = 145 − 35",
"126 + 14 − (x − 14) = 20":"126 + 14 = 140 → 140 − 20 = 120 → x = 120 + 14",
}
def sol(e,a):
    if e in CUSTOM: return CUSTOM[e]+f' = {a}'
    ee=e.replace('−','-').replace('×','*').replace('÷','/')
    l,r=[p.strip() for p in ee.split('=')]
    toks=re.findall(r'([+-]?)\s*(x|\d+)',l.replace(' ',''))
    sx=1;cs=[]
    for sg,v in toks:
        sg=-1 if sg=='-' else 1
        if v=='x': sx=sg
        else: cs.append(sg*int(v))
    R=int(r)
    if sx==1:
        txt=str(R)+''.join(f' {"−" if c>0 else "+"} {abs(c)}' for c in cs)
    else:
        txt=''.join((f'{abs(c)}' if k==0 and c>0 else f' {"+" if c>0 else "−"} {abs(c)}') for k,c in enumerate(cs)).strip()+f' − {R}'
    val=eval(txt.replace('−','-'))
    assert val==a,(e,txt,val,a)
    return f'x = {txt} = {a}'
def key(S,no,level,note):
    def cell(i):
        t,e,a,f=S[i]
        sl=sol(e,a)
        sl=sl if sl.startswith('x =') or '→' in sl else sl
        pre,_,ans=sl.rpartition('= ')
        return f'<div class="kq c{i%3}"><span class="n">{i+1}</span><div class="kt"><div class="ke">{html.escape(e)}</div><div class="ks">{html.escape(pre)}= <b>{ans}</b></div></div></div>'
    cells=''.join(cell(i) for i in range(len(S)))
    tip='<div class="tip"><b>วิธีอ่านเฉลย</b> · ย้ายตัวเลขไปอีกข้างของ = แล้วเปลี่ยนเครื่องหมายเป็นตรงข้ามกัน (บวก ↔ ลบ) · ตัวเลขในช่องเหลืองคือค่าของ x หรือคำตอบของข้อนั้น</div>'
    return f'<div class="pg"><img class="wm" src="logo.png">{header(no,level,"เฉลยชุดที่ "+str(no))}{tip}<div class="kg">{cells}</div>{footer()}</div>'
h1='ให้ x แทนจำนวนที่ต้องการหา · เขียนสมการและแสดงวิธีทำ'
h2='โจทย์หลายขั้นตอน · ย้อนกลับจากผลลัพธ์ทีละขั้น · ให้ x แทนจำนวนที่ต้องการหา'
pages=[12,12,12,12]
L1='ระดับปานกลาง';L2='ระดับข้อสอบแข่งขัน'
wrap=lambda b:f'<!doctype html><meta charset=utf-8><style>{css}</style>'+b
open('set1.html','w').write(wrap(build(S1,1,L1,h1,pages)))
open('set2.html','w').write(wrap(build(S2,2,L2,h2,pages)))
open('key1.html','w').write(wrap(key(S1,1,L1,f'ข้อ {pos(S1,"จำนวนหน้าที่เหลือ")} ตอบจำนวนหน้าที่เหลืออ่าน (82 หน้า) ส่วนข้ออื่น ๆ ตอบค่าตามที่โจทย์ถาม')))
open('key2b.html','w').write(wrap(key(S2,2,L2,f'ข้อ {pos(S2,"ลุงอายุมากกว่าหลาน")} ตอบอายุหลาน 15 ปี ข้อ {pos(S2,"ยายจะอายุมากกว่าหลาน")} ตอบอายุหลาน 18 ปี ข้อ {pos(S2,"ปัจจุบันคุณป้า")} ตอบอายุหลาน 16 ปี ข้อ {pos(S2,"ทำให้สองคนมีเงินเท่ากัน")}, {pos(S2,"สติกเกอร์เท่ากัน")}, {pos(S2,"ส้มมีเงินมากกว่าปลา")}, {pos(S2,"ถังบีมีน้ำ")} และ {pos(S2,"ฝ้ายมีลูกปัด")} ตอบค่าเดิมของคนที่โจทย์ถาม')))
