import re, html, sys
sys.path.insert(0,'.')
import data_p2 as data10
import re as _re
def _plain(t):
    t=_re.sub(r'<span class="fr"><i>(.*?)</i><i>(.*?)</i></span>',r'\1/\2',t)
    return _re.sub(r'<[^>]+>','',t)
class _D: DIAG={}
diag=_D()
class _E:
    CHK={};TIP={};WARN={}
extras=_E()
ALL={}
for p in data10.P:
    ALL[p['no']]=p
    extras.TIP[p['no']]=p['tip'];extras.WARN[p['no']]=p['warn']
    for k,it in enumerate(p['items']): extras.CHK[(p['no'],k)]=_plain(it['chk'])
assert sorted(ALL)==list(range(16,31)),sorted(ALL)
src=open('gen3.py').read()
FONTS=re.search(r"fonts='''(.*?)'''",src,re.S).group(1)+''.join(re.findall(r"fonts\+='''(.*?)'''",src,re.S))
css=FONTS+"""@font-face{font-family:Itim;font-weight:400;src:url(ff/itim-thai-400-normal.woff2);unicode-range:U+0E01-0E5B,U+200B-200D,U+25CC}
@font-face{font-family:Itim;font-weight:400;src:url(ff/itim-latin-400-normal.woff2);unicode-range:U+0000-00FF,U+2013-2014,U+2018-201F,U+2212,U+00D7,U+00F7,U+2026}

@page{size:297mm 210mm;margin:0}
*{box-sizing:border-box}
:root{--cream:#FAF5E6;--paper:#FFFFFF;--orange:#5E6E2B;--dorange:#3F4F1E;--yellow:#F2C230;--syellow:#FBEFC2;--green:#A88418;--dgreen:#7A5C0E;--sgreen:#F7EED0;--brown:#2E3A12;--mbrown:#3F4F1E;--line:#DCDDC4}
body{margin:0;font-family:Mali,sans-serif;font-weight:500;color:var(--brown)}
.sl{position:relative;width:297mm;height:210mm;padding:8mm 11mm 12mm;page-break-after:always;display:flex;flex-direction:column;gap:4mm;overflow:hidden;background:url(assets/bg.jpg) center/100% 100% no-repeat,var(--cream)}
.sl:last-child{page-break-after:auto}
.wm{position:absolute;left:50%;top:60%;width:112mm;transform:translate(-50%,-50%);z-index:0}
.sl>*:not(.wm){position:relative;z-index:1}
.bar{background:linear-gradient(90deg,var(--dorange),var(--orange) 60%,#8A9A48);border-radius:7mm;border-bottom:2.2mm solid var(--yellow);display:flex;align-items:center;gap:5mm;padding:2.6mm 7mm;color:#fff;box-shadow:0 1.2mm 0 rgba(63,79,30,.22)}
.a .bar{background:linear-gradient(90deg,var(--dgreen),var(--green) 60%,#D4B13C);border-bottom-color:var(--yellow);box-shadow:0 1.2mm 0 rgba(168,132,24,.25)}
.no{width:14mm;height:14mm;border-radius:50%;background:var(--yellow);color:var(--brown);border:1.1mm solid #fff;box-shadow:0 0 0 .8mm var(--yellow);display:flex;align-items:center;justify-content:center;font-weight:700;font-size:18pt;flex:0 0 14mm}
.mock .no{background:#fff;color:var(--dorange);box-shadow:0 0 0 .8mm #fff}
.a.mock .no{color:var(--dgreen)}
.bar h1{margin:0;font-size:20pt;font-weight:700;line-height:1.15}
.bar .sub{font-size:11pt;color:#F1F3E4;font-weight:600}
.tag{margin-left:auto;border-radius:7mm;padding:1.5mm 6mm;font-weight:700;font-size:13pt;white-space:nowrap;box-shadow:0 .6mm 0 rgba(0,0,0,.14)}
.real .tag{background:var(--yellow);color:var(--brown)}.mock .tag{background:#fff;color:var(--dorange)}.a .tag{background:#fff;color:var(--dgreen)}
.prob{background:var(--paper);border:1.6px solid var(--line);border-radius:6mm;box-shadow:0 1.4mm 0 #DDE3BF;padding:5.5mm 9mm;font-family:Mali,sans-serif;font-weight:600;font-size:var(--fs,26pt);line-height:1.55;color:var(--brown);display:flex;gap:7mm;align-items:center;position:relative}
.prob:before{content:"โจทย์";position:absolute;left:8mm;top:-3.6mm;background:var(--orange);color:#fff;border-radius:3mm;padding:.2mm 4mm;font:700 11pt Mali,sans-serif}
.prob.below{flex-direction:column;align-items:stretch;gap:2mm}
.ptxt{flex:1}
.pimg{flex:0 0 auto;max-width:46%;display:flex;justify-content:center;align-items:center}
.below .pimg{max-width:100%}
.pimg .img,.img{height:60mm;width:auto;max-width:100%;display:block}
.below .pimg .img{height:34mm}
.pimg .crop{border-radius:3mm}
.prob ul{margin:1.5mm 0 0 8mm;padding:0;font-size:.82em;font-weight:500;line-height:1.5}
.prob li{margin:0 0 .8mm}
.fr{display:inline-flex;flex-direction:column;align-items:center;vertical-align:middle;margin:0 1mm;line-height:1.05;font-size:.86em}
.fr i{font-style:normal;padding:0 1mm}.fr i:first-child{border-bottom:.45mm solid currentColor}
.math{display:block;text-align:center;white-space:nowrap;margin-top:2.5mm;font-size:1.14em;letter-spacing:.2mm}.dots{letter-spacing:.5mm}.nw{white-space:nowrap}
.tb{border-collapse:collapse;margin-top:2mm;font-size:.9em}.tb th,.tb td{border:1.5px solid var(--mbrown);padding:1.5mm 5mm;text-align:center}.tb th{background:var(--syellow)}
.tb2{border-collapse:collapse;font-size:11pt}.tb2 th,.tb2 td{border:1px solid var(--mbrown);padding:1mm 4mm}
.eqs{display:flex;gap:12mm;margin:2mm 0;flex-wrap:wrap}.eq{display:inline-flex;align-items:center;gap:2mm;font-size:1.05em}.ic{vertical-align:middle}
.pl{font:700 26px Mali,sans-serif;fill:#2E3A12}.lg{font:600 19px Mali,sans-serif;fill:#2E3A12}.gt{font:600 11px Mali,sans-serif;fill:#4A5426}.gt2{font:700 13px Mali,sans-serif;fill:#2E3A12}.bt{font:700 26px Mali,sans-serif;fill:#2E3A12}
.work{flex:1;min-height:30mm;border:1.8px dashed #B8C27E;border-radius:6mm;background:#fff;position:relative}
.work span{position:absolute;left:9mm;top:-3.6mm;background:var(--yellow);color:var(--brown);border-radius:3mm;padding:.2mm 4mm;font-size:11.5pt;font-weight:700}
.ans{display:flex;align-items:center;justify-content:flex-end;gap:3mm;font-size:14pt;font-weight:700;color:var(--dorange);margin-top:-1mm}
.ans .box{width:72mm;height:10.5mm;border:1.8px solid var(--orange);border-radius:4mm;background:var(--paper)}
.abody{flex:1;display:flex;gap:6mm;min-height:0}
.steps{flex:1;min-width:0;overflow:hidden;font-family:Mali,sans-serif;font-weight:600;font-size:22pt;line-height:1.45;color:var(--brown);display:flex;flex-direction:column}
.steps ol{margin:0;padding:0;list-style:none;counter-reset:s;display:flex;flex-direction:column;gap:2.6mm}
.steps li{counter-increment:s;position:relative;background:var(--paper);border:1.6px solid var(--line);border-radius:5mm;box-shadow:0 1mm 0 #DDE3BF;padding:2.6mm 5mm 2.6mm 17mm}
.steps li:before{content:counter(s);position:absolute;left:4mm;top:50%;transform:translateY(-50%);width:9.5mm;height:9.5mm;border-radius:50%;background:var(--green);color:#fff;font-size:.8em;font-weight:700;display:flex;align-items:center;justify-content:center;line-height:1;box-shadow:0 0 0 .8mm var(--sgreen)}
.steps li:last-child{background:#FCF4D9;border-color:var(--orange);box-shadow:0 1mm 0 #B8C27E}
.steps li:last-child:before{background:var(--orange);box-shadow:0 0 0 .8mm #E4E8CC}
.steps mark{background:#F9E49A;color:var(--brown);padding:0 1.6mm;border-radius:2mm;font-weight:700}
.steps .ic{width:1.1em;height:1.1em}
.steps .inl{margin-top:2.4mm;background:var(--paper);border:1.6px solid var(--line);border-radius:5mm;padding:2mm}.steps .inl svg,.steps .inl img{width:auto;height:auto;max-height:30mm;max-width:100%;display:block;margin:0 auto}
.ansc{flex:0 0 34%;display:flex;flex-direction:column;gap:4mm;min-height:0}
.ansbox{background:linear-gradient(160deg,#B8962A,var(--dgreen));border-radius:7mm;padding:3.5mm 6mm 4mm;text-align:center;color:#fff;box-shadow:0 1.6mm 0 #5C4508}
.ansbox small{display:inline-block;background:var(--yellow);color:var(--brown);border-radius:4mm;padding:0 5mm;font-size:13pt;font-weight:700}
.ansbox b{display:block;font-family:Mali,sans-serif;font-size:50pt;line-height:1.1;font-weight:700;color:#fff;}
.aimg{flex:1;min-height:0;display:flex;justify-content:center;align-items:center;background:var(--paper);border:1.6px solid var(--line);border-radius:6mm;box-shadow:0 1.2mm 0 #DDE3BF;padding:2mm;overflow:hidden}
.aimg .img{width:100%;height:100%;max-width:100%;object-fit:contain}
.note{font-size:9.5pt;font-weight:600;color:#4A3A10;background:#FCF4D9;border:1px solid #E2B42A;border-radius:3mm;padding:1.4mm 3mm;text-align:center}
.ft{position:absolute !important;left:11mm;right:11mm;bottom:3.8mm;display:flex;justify-content:space-between;align-items:center;font-size:9.5pt;color:var(--mbrown)}
.ft .brand{font-family:Fredoka,Mali,sans-serif;font-weight:600;color:var(--dorange);font-size:13.5pt;letter-spacing:.3mm}
.a .ft .brand{color:var(--dgreen)}
.cover{justify-content:center;align-items:center;text-align:center;gap:5mm}
.cover .wm{width:150mm;top:50%}
.cover .big{font-size:31pt;font-weight:700;line-height:1.3;color:var(--brown)}.cover .big b{color:var(--dorange)}
.cover .chip{background:var(--orange);color:#fff;border-radius:8mm;padding:2.2mm 10mm;font-weight:700;font-size:19pt;box-shadow:0 1mm 0 var(--dorange)}
.cover .meta{font-size:16pt;font-weight:600;color:var(--mbrown)}
.cover .list{display:grid;grid-template-columns:repeat(5,1fr);gap:2.6mm;width:275mm;margin-top:2mm}
.cover .list div{background:var(--paper);border:1.4px solid var(--line);border-top:1.8mm solid var(--c,var(--orange));border-radius:3mm;padding:1.6mm 2.4mm;font-size:9.4pt;font-weight:600;text-align:left;line-height:1.25}
.cover .list div b{color:var(--dorange);font-size:10.5pt}
.cover .list div:nth-child(3n+2){--c:var(--yellow)}.cover .list div:nth-child(3n){--c:var(--green)}

.cvr{padding:0;background:#FAF5E6}
.cvr .bgb{position:absolute !important;z-index:0 !important;left:-6mm;top:-6mm;width:calc(100% + 12mm);height:calc(100% + 12mm);object-fit:cover}.cvr .fg{position:absolute !important;z-index:1 !important;left:0;top:50%;transform:translateY(-50%);width:100%;height:auto}
.deco{position:absolute !important;left:0;top:0;width:297mm;height:210mm;z-index:0;pointer-events:none}
.sl.a .bar .tag{display:flex;align-items:center;gap:2mm}
.tag svg{width:5.4mm;height:5.4mm}
.steps ol{position:relative;gap:3.2mm}
.steps ol:before{content:"";position:absolute;left:8.2mm;top:9mm;bottom:9mm;border-left:1.4mm dotted #B8C27E}
.steps li{padding:2.8mm 6mm 2.8mm 19mm;border:none;border-radius:6mm;box-shadow:0 1.1mm 0 var(--sc2),0 0 0 1.5px var(--sc1) inset;background:#FFFFFF}
.steps li:nth-child(3n+1){--sc1:#B8C27E;--sc2:#DDE3BF;--bc:#5E6E2B}
.steps li:nth-child(3n+2){--sc1:#E2B42A;--sc2:#E6E9D2;--bc:#B8901A}
.steps li:nth-child(3n){--sc1:#EAD58C;--sc2:#F7EED0;--bc:#A88418}
.steps li:before{left:2.2mm;width:11.5mm;height:11.5mm;background:var(--bc);box-shadow:0 0 0 1.1mm #fff,0 0 0 1.9mm var(--sc1);font-size:.85em}
.steps li:last-child{background:linear-gradient(90deg,#EEF0DD,#FCF4D9);--sc1:#A88418;--sc2:#EAD58C;padding-right:16mm}
.steps li:last-child:before{background:#7A5C0E;box-shadow:0 0 0 1.1mm #fff,0 0 0 1.9mm #A88418}
.steps li:last-child:after{content:"";position:absolute;right:4mm;top:50%;width:9mm;height:9mm;transform:translateY(-50%);border-radius:50%;background:#A88418 url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'><path d='M5 12.5l4.5 4.5L19 7.5' fill='none' stroke='white' stroke-width='3.4' stroke-linecap='round' stroke-linejoin='round'/></svg>") center/70% no-repeat}
.steps mark{font-weight:700;white-space:nowrap;background:#FBEFC2;border:1px solid #E2B42A;padding:0 1.8mm;border-radius:3mm}
.steps li:last-child mark{background:#7A5C0E;border-color:#7A5C0E;color:#fff}
.medal{width:100%;display:block}
.medal svg{width:100%;height:auto;max-height:74mm;display:block;margin:0 auto}
.ansc{gap:3mm}

.steps li:has(.res){display:flex;align-items:flex-end;justify-content:space-between;gap:5mm}
.steps li .lt{flex:1 1 auto;min-width:0}
.steps mark.res{flex:0 0 auto;align-self:flex-end;margin-left:auto;font-size:1.08em;padding:0 3.2mm;line-height:1.35}

.abody{align-items:stretch}
.ansc{flex:0 0 58mm;justify-content:flex-end;gap:3mm}
.ansc .aimg{flex:0 1 56mm;min-height:0}
.ansc .medal svg{max-height:none;width:100%}
.real .bar{background:linear-gradient(90deg,#3F4F1E,#5E6E2B 60%,#8A9A48);border-bottom-color:#F2C230;box-shadow:0 1.2mm 0 rgba(63,79,30,.22)}
.mock .bar{background:linear-gradient(90deg,#7A5C0E,#A88418 60%,#D4B13C);border-bottom-color:#F2C230;box-shadow:0 1.2mm 0 rgba(168,132,24,.25)}
.a.real .bar{background:linear-gradient(90deg,#3F4F1E,#5E6E2B 60%,#8A9A48);border-bottom-color:#F2C230}
.a.mock .bar{background:linear-gradient(90deg,#7A5C0E,#A88418 60%,#D4B13C);border-bottom-color:#F2C230}
.sl.real{background:url(assets/bg_real.jpg) center/100% 100% no-repeat,#FAF5E6}
.sl.mock{background:url(assets/bg_mock.jpg) center/100% 100% no-repeat,#FFFBEF}
.real .no{background:#F2C230;color:#2E3A12}.mock .no{background:#fff;color:#7A5C0E;box-shadow:0 0 0 .8mm #fff}
.real .tag,.a.real .tag{background:#F2C230;color:#2E3A12}.mock .tag,.a.mock .tag{background:#fff;color:#7A5C0E}
.real .prob:before{background:#5E6E2B}.mock .prob:before{background:#A88418}
.real .prob{border-color:#DCDDC4;box-shadow:0 1.4mm 0 #DDE3BF}.mock .prob{border-color:#F7EED0;box-shadow:0 1.4mm 0 #EFE2AE}
.real .work{border-color:#B8C27E}.mock .work{border-color:#EAD58C}
.mock .work span{background:#F3E8BE}
.real .ans{color:#3F4F1E}.real .ans .box{border-color:#5E6E2B}
.mock .ans{color:#7A5C0E}.mock .ans .box{border-color:#A88418}
.real .ft .brand,.a.real .ft .brand{color:#3F4F1E}.mock .ft .brand,.a.mock .ft .brand{color:#7A5C0E}
.real .steps ol:before{border-left-color:#B8C27E}.mock .steps ol:before{border-left-color:#EAD58C}
.real .steps li:nth-child(3n+1){--sc1:#B8C27E;--sc2:#DDE3BF;--bc:#5E6E2B}
.real .steps li:nth-child(3n+2){--sc1:#E2B42A;--sc2:#E6E9D2;--bc:#B8901A}
.real .steps li:nth-child(3n){--sc1:#B8C27E;--sc2:#DDE3BF;--bc:#6F7F35}
.mock .steps li:nth-child(3n+1){--sc1:#EAD58C;--sc2:#F7EED0;--bc:#A88418}
.mock .steps li:nth-child(3n+2){--sc1:#E2B42A;--sc2:#E6E9D2;--bc:#B8901A}
.mock .steps li:nth-child(3n){--sc1:#EAD58C;--sc2:#F7EED0;--bc:#7A5C0E}
.real .steps li:last-child{background:linear-gradient(90deg,#FBEFC2,#FCF4D9);--sc1:#5E6E2B;--sc2:#B8C27E}
.real .steps li:last-child:before{background:#3F4F1E;box-shadow:0 0 0 1.1mm #fff,0 0 0 1.9mm #5E6E2B}
.real .steps li:last-child:after{background-color:#5E6E2B}
.real .steps li:last-child mark,.real .steps mark.res:last-child{background:#3F4F1E;border-color:#3F4F1E;color:#fff}
.real .steps li:last-child mark.res{background:#3F4F1E;border-color:#3F4F1E;color:#fff}
.real .tb th{background:#FBEFC2}

.ansc{flex:0 0 64mm}
.steps .inl{flex:1 1 auto;min-height:44mm;margin-top:2.6mm;display:flex;align-items:center;justify-content:center;padding:2mm;background:var(--paper);border:1.6px solid var(--line);border-radius:5mm;box-shadow:0 1mm 0 #DDE3BF}
.steps .inl.wide{min-height:26mm}
.steps .inl svg,.steps .inl img{height:100%;max-height:100%;width:auto;max-width:100%;margin:0}
.mock .steps .inl{border-color:#F7EED0;box-shadow:0 1mm 0 #EFE2AE}
.steps ol{flex:0 0 auto}

.ansc{flex:0 0 70mm}
.ansc .aimg{flex:1 1 auto;min-height:0}
.ansc .medal{flex:0 0 auto;width:58mm;align-self:center}

.ansc .medal{order:3}.ansc .aimg{order:1}.ansc .note{order:2}

.steps li:has(.res){display:block}
.steps .eqr{white-space:nowrap}
.steps mark.res{display:inline;margin-left:.5mm;align-self:auto}
.ansc{flex:0 0 52mm}
.ansc .medal{width:44mm}
.sl.a:has(.aimg) .ansc{flex:0 0 62mm}
.sl.a:has(.aimg) .ansc .medal{width:50mm}

.steps.hb li{min-width:0}.steps.hb ol{display:grid;grid-template-columns:1fr 1fr;gap:3mm 4mm;align-items:start}
.steps.hb ol:before{display:none}
.steps.hb li:last-child{grid-column:1/-1}
.steps .inl.dgm{flex:0 0 auto;min-height:0;height:60mm;margin:0 0 3mm;padding:1.5mm 3mm}
.steps .inl.dgm svg{height:100%;width:auto;max-width:100%}
.steps ol.stair{gap:5.4mm}
.steps ol.stair:before{display:none}
.steps li .ar{position:absolute;left:13mm;bottom:-4.8mm;width:0;height:0;border-left:3.2mm solid transparent;border-right:3.2mm solid transparent;border-top:4.2mm solid var(--bc,#5E6E2B)}
.steps li{position:relative}

.sl.a:not(:has(.aimg)):not(:has(.dgm)):not(:has(.inl)) .ansc{position:absolute;right:11mm;bottom:12mm;width:46mm;flex:none}
.sl.a:not(:has(.aimg)):not(:has(.dgm)):not(:has(.inl)) .ansc .medal{width:44mm}

.steps .note{margin-top:2.4mm;text-align:left;font-size:10.5pt;align-self:flex-start;max-width:70%}

.extras{display:grid;grid-template-columns:1.25fr 1fr 1fr;gap:3mm;margin-top:auto;padding-top:3mm;flex:0 0 auto}
.ex{border-radius:4mm;padding:1.6mm 3mm 2mm;font-family:Mali,sans-serif;font-weight:600;font-size:11.5pt;line-height:1.35;border:1.4px solid;min-width:0}
.ex b{display:inline-block;font-size:11pt;font-weight:700;border-radius:3mm;padding:0 2.4mm;margin-bottom:.8mm}
.ex span{display:block;color:#2E3A12}
.ex.ck{background:#F1F3E4;border-color:#EAD58C}.ex.ck b{background:#A88418;color:#fff}
.ex.tp{background:#FCF4D9;border-color:#E2B42A}.ex.tp b{background:#F2C230;color:#2E3A12}
.ex.wn{background:#F1F3E4;border-color:#B8C27E}.ex.wn b{background:#6F7F35;color:#fff}
.sl.a:not(:has(.aimg)):not(:has(.dgm)):not(:has(.inl)) .extras{margin-right:62mm}

.steps .cl{display:inline-block;max-width:100%;vertical-align:baseline}
.steps .inl.dgm{height:50mm}

.steps li,.prob .ptxt{text-wrap:pretty}
.steps.hb .extras{font-size:10pt}
.steps.hb .ex{font-size:10pt}

.cvr2{padding:0;background:linear-gradient(135deg,#3F4F1E 0%,#5E6E2B 60%,#8A9A48 100%);color:#fff;align-items:center;justify-content:center;text-align:center}
.cvr2 .cvc{display:flex;flex-direction:column;align-items:center;gap:7mm}
.cvr2 .cvl{background:#fff;border-radius:50%;width:62mm;height:62mm;display:flex;align-items:center;justify-content:center;box-shadow:0 0 0 2.4mm #FBEFC2}
.cvr2 .cvl img{width:50mm;height:auto}
.cvr2 .cvchip{background:#FBEFC2;color:#3F4F1E;border-radius:8mm;padding:2mm 10mm;font-weight:700;font-size:17pt}
.cvr2 .cvt{font-size:30pt;font-weight:700;line-height:1.35}
.cvr2 .cvs{font-size:19pt;font-weight:600;color:#F7EED0}.cvr2 .cvs b{color:#FBEFC2}
.cvr2 .cvm{font-size:15pt;font-weight:600;background:rgba(255,255,255,.14);border-radius:6mm;padding:2mm 8mm}
.cvr2 .cvf{position:absolute;right:11mm;bottom:6mm}.cvr2 .cvf .brand{font-family:Mali,sans-serif;font-weight:700;color:#FBEFC2;font-size:13.5pt}
.cvr2 .cvline{position:absolute !important;left:0;right:0;top:0;height:3.2mm;background:#F2C230}.cvr2 .cvline2{position:absolute !important;left:0;right:0;bottom:0;height:3.2mm;background:#F2C230}
.dg{display:inline-block;min-width:1.35em;text-align:center;border:.5mm solid currentColor;border-radius:1mm;margin-right:1.2mm;line-height:1.3;background:#fff}.pimg .crop,.aimg .crop{background:#fff}img.img{object-fit:contain}.below .pimg img.crop{max-height:54mm;height:auto;max-width:94%}.steps .inl.wide:has(img){min-height:40mm}.steps .inl.wide img{max-height:44mm !important}.ntri{margin:2mm auto 0;font-size:.9em;text-align:center}.ntr{display:flex;justify-content:center;gap:3mm;position:relative}.ntr span{min-width:2em}.ntr em{position:absolute;right:2mm;font-style:normal;font-size:.8em;color:#5E6E2B}
.prob ul{list-style:none;margin:1.5mm 0 0 2mm}.prob ul.opts{display:flex;flex-wrap:wrap;gap:1.2mm 6mm;margin-left:0}.prob ul.opts li{background:#F3F1E2;border-radius:3mm;padding:0 3mm;margin:0}.below .pimg .img{height:46mm}.steps .tb2{font-size:.62em;margin-top:1.5mm}.steps .tb2 th,.steps .tb2 td{padding:.6mm 2.6mm}
.isym{width:1.25em;height:1.25em;vertical-align:-.28em}.vstack{display:flex;flex-direction:column;gap:3mm;align-items:center;width:100%}.vstack svg{max-height:46%;width:auto;max-width:100%}.chips{display:flex;flex-direction:column;gap:2mm;font-size:13pt}.chg b{display:block;color:#5E6E2B;margin-bottom:.5mm}.chp{display:inline-block;background:#FFF1B8;border:1px solid #E2B42A;border-radius:2mm;padding:0 2mm;margin:0 1mm 1mm 0;font-weight:700}
.steps .inl.wide{min-height:34mm}.steps .inl.wide svg{max-height:60mm !important}.steps .inl.wide{min-height:44mm}.steps .inl.wide img{max-height:60mm !important}.steps .inl .vstack svg{height:30mm !important;max-height:30mm !important}.steps .inl .chips{font-size:16pt}.pimg .vstack svg{height:27mm;width:auto;max-width:100%}.below .pimg svg.img{height:50mm}
"""


import math as _m
def medal(ans,kind='real'):
    P={'real':('#8A9A48','#3F4F1E','#F6D66A','#FCF0CB'),'mock':('#C9A43A','#7A5C0E','#F6D66A','#FBF4DC')}[kind]
    n=len(ans);fs={1:125,2:112,3:92}.get(n,74)
    pt=lambda a,r:(150+r*_m.cos(_m.radians(a)),150+r*_m.sin(_m.radians(a)))
    rays=''.join('<polygon points="150,150 %.1f,%.1f %.1f,%.1f" fill="%s"/>'%(*pt(a-5,150),*pt(a+5,150),P[2] if (a//15)%2==0 else P[3]) for a in range(0,360,15))
    spark=''.join(f'<polygon transform="translate({x},{y}) scale({s})" points="0,-10 3,-3 10,0 3,3 0,10 -3,3 -10,0 -3,-3" fill="{c}"/>' for x,y,s,c in [(32,60,1.3,"#5E6E2B"),(268,70,1.6,"#F2C230"),(262,250,1.2,"#EAD58C"),(40,248,1.5,"#F2C230"),(150,12,1.1,"#5E6E2B")])
    return (f'<svg viewBox="0 0 300 300"><defs><linearGradient id="g{kind}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{P[0]}"/><stop offset="1" stop-color="{P[1]}"/></linearGradient></defs>'
            f'{rays}{spark}<circle cx="150" cy="156" r="112" fill="#fff"/><circle cx="150" cy="156" r="102" fill="url(#g{kind})"/><circle cx="150" cy="156" r="92" fill="none" stroke="#fff" stroke-width="3" stroke-dasharray="3 9" stroke-linecap="round"/>'
            f'<text x="150" y="{156+fs*0.36:.0f}" text-anchor="middle" font-family="Mali" font-weight="700" font-size="{fs}" fill="#fff">{ans}</text>'
            f'<g transform="translate(150,52)"><path d="M-62,-18 H62 L72,0 L62,18 H-62 L-72,0 Z" fill="#F2C230" stroke="#fff" stroke-width="5" stroke-linejoin="round"/><text x="0" y="8" text-anchor="middle" font-family="Mali" font-weight="700" font-size="24" fill="#2E3A12">คำตอบ</text></g></svg>')
CHECK='<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="11" fill="#A88418"/><path d="M6.5 12.5l4 4 7-8" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg>'
def deco():
    sp=lambda x,y,s,c,o:f'<polygon transform="translate({x},{y}) scale({s})" points="0,-10 3,-3 10,0 3,3 0,10 -3,3 -10,0 -3,-3" fill="{c}" opacity="{o}"/>'
    sh=''.join([sp(1090,610,3.2,"#F2C230",.45),sp(1120,330,1.8,"#5E6E2B",.35),sp(60,540,2.6,"#EAD58C",.45),sp(30,300,1.7,"#F2C230",.4),sp(610,35,1.5,"#F2C230",.4),
        '<circle cx="1105" cy="470" r="9" fill="#EAD58C" opacity=".35"/><circle cx="25" cy="440" r="7" fill="#5E6E2B" opacity=".3"/><circle cx="1060" cy="140" r="6" fill="#F2C230" opacity=".4"/>'])
    return f'<svg class="deco" viewBox="0 0 1123 794">{sh}</svg>'


UN=['กิโลเมตร','เซนติเมตร','กิโลกรัม','ลูกบาศก์เซนติเมตร','ตารางเมตร','คะแนน','เหรียญ','กล่อง','แผ่น','เมตร','ลิตร','ขวด','ชิ้น','เล่ม','หน้า','แท่ง','เม็ด','ฟอง','บาท','ต้น','ดอก','ดวง','คัน','ตัว','ลูก','ผล','คน','ใบ','ปี','ชั้น','ที่','นาที','วินาที','ซม.','เดือน','วิธี','ก้อน','กระสอบ','ฉบับ','งวด','โซน','ขา','ล้อ','แถว','เครื่อง','ด้าน','หน่วย','ตารางหน่วย','ตารางเซนติเมตร','ส่วน','ชุด','จำนวน','มุม']
UN.sort(key=len,reverse=True)
_NUM=re.compile(r'(\d[\d,\.]*%?) ('+'|'.join(map(re.escape,UN))+')')
def numbind(q):
    parts=re.split(r'(<[^>]+>)',q)
    return ''.join(p if p.startswith('<') else _NUM.sub(lambda m:f"<span class='nw'>{m.group(1)}&nbsp;{m.group(2)}</span>",p) for p in parts)
def tailbind(q):
    if q.rstrip().endswith('>'): return q
    m=re.search(r'([^<>]*)$',q)
    t=m.group(1)
    if len(t)<6: return q
    k=min(11,len(t)-1)
    return q[:m.start(1)]+t[:-k]+"<span class='nw'>"+t[-k:]+"</span>"
def bind(q):
    q=tailbind(q)
    parts=re.split(r'(<[^>]+>)',q)
    return ''.join(p if p.startswith('<') else _NUM.sub(lambda m:f"<span class='nw'>{m.group(1)}&nbsp;{m.group(2)}</span>",p) for p in parts)

def fsize(q):
    n=len(re.sub('<[^>]+>','',q))
    return 29 if n<60 else 26 if n<110 else 23 if n<200 else 21 if n<320 else 19
slides=[]
total=2+15*6
cv1 = '<section class="sl cvr2"><h1 style="position:absolute;left:-9999px">หน้าปก</h1><div class="cvline"></div><div class="cvline2"></div><div class="cvc"><div class="cvl"><img src="assets/logo.png"></div><div class="cvchip">สไลด์ติวสอบแข่งขัน · ระดับชั้นประถมศึกษาปีที่ 2</div><div class="cvt">ข้อสอบชิงแชมป์การคิดและการแก้ปัญหาคณิตศาสตร์<br>ครั้งที่ 23 (LPMC) · ข้อ 16–30</div><div class="cvs">วิชา<b>คณิตศาสตร์</b> · ปีการศึกษา 2565 · ระดับ ป.2</div><div class="cvm">ข้อจริง 15 ข้อ · Mock Test 30 ข้อ · เฉลยด้วยรูปทุกข้อ</div></div><div class="cvf"><span class="brand">Math by T’Yasmin</span></div></section>'
cover = '<section class="sl cover"><h1 style="position:absolute;left:-9999px">สารบัญ</h1><div class="chip">สารบัญ · สไลด์ติวสอบแข่งขัน</div><div class="big">ชิงแชมป์การคิดและแก้ปัญหา LPMC ครั้งที่ 23<br><b>คณิตศาสตร์</b> ป.2 · พ.ศ. 2565 (ข้อ 16–30)</div><div class="meta">ทั้งหมด 15 ข้อ · ข้อจริง → เฉลย → Mock Test 1 → เฉลย → Mock Test 2 → เฉลย</div><div class="list">'+''.join(f'<div><b>ข้อ {n}</b> {html.escape(ALL[n]["topic"])}</div>' for n in range(16,31))+'<div style="grid-column:span 5;text-align:center;--c:#F2C230">ลำดับ: ข้อจริง → เฉลย → Mock Test 1 → เฉลย → Mock Test 2 → เฉลย · เขียนวิธีคิดบนสไลด์ด้วยปากกาใน GoodNotes</div></div><div class="ft"><span></span><span class="brand">Math by T’Yasmin</span></div></section>'
slides.append(cv1)
slides.append(cover)
n=2
BELOW={18,19,24}
for no in range(16,31):
    p=ALL[no]
    for k,it in enumerate(p['items']):
        kind='real' if k==0 else 'mock'
        label='ข้อจริง' if k==0 else f'Mock Test {k}'
        title=f'ข้อ {no} · {label}'
        # question slide
        n+=1
        img=f'<div class="pimg">{it["qimg"]}</div>' if it['qimg'] else ''
        below=' below' if (no in BELOW and it['qimg']) else ''
        fs=it['fs'] and int(it['fs'].replace('pt','')) or fsize(it['q'])
        slides.append(f'<section class="sl q {kind}"><div class="bar"><span class="no">{no}</span><div><h1>{title}</h1><span class="sub">{html.escape(p["topic"])}</span></div><span class="tag">{"ข้อจริง · LPMC ครั้งที่ 23" if k==0 else "Mock Test "+str(k)+"/2"}</span></div><div class="prob{below}" data-fs="{fs}" style="--fs:{fs}pt"><div class="ptxt">{bind(it["q"])}</div>{img}</div><div class="work"><span>วิธีคิด</span></div><div class="ans">ตอบ<span class="box"></span></div><div class="ft"><span>สไลด์ {n} / {total}</span><span class="brand">Math by T’Yasmin</span></div></section>')
        # answer slide
        n+=1
        def hl(s):
            if '=' not in s or s.lstrip().startswith('('): return s
            rest=''
            core=s
            m=re.search(r' \((?=[\u0e01-\u0e5b])',s)
            if m: core,rest=s[:m.start()],s[m.start():]
            if '=' not in core: return s
            h,_,t=core.rpartition('=')
            if '<' in t: return s
            t=t.strip()
            if '→' in t or '·' in t or len(t)>26: return s
            if rest: return f"{h}= <mark>{t}</mark>{rest}"
            hs=h.rstrip()
            plain=lambda x:re.sub('<[^>]+>','',x)
            cands=[(hs.rfind(' = '),3),(hs.rfind(': '),2),(hs.rfind(' → '),3),(hs.rfind(' · '),3)]
            ci,cl=max(cands)
            if ci>=0: pre,expr=hs[:ci+cl],hs[ci+cl:]
            else: pre,expr='',hs
            lim=16 if hasbar else 34
            if len(plain(expr))>lim or not expr.strip():
                parts=re.split(r' (?![^<]*>)',hs)
                pre,expr=((' '.join(parts[:-1])+' ',parts[-1]) if len(parts)>1 else ('',hs))
            return f"{pre}<span class='eqr'>{expr} = <mark class='res'>{t}</mark></span>"
        STAIR={16,17,19,20,21,22,23,24,25,26,27,28,29,30}
        hasbar=(no,k) in diag.DIAG
        stair=(no in STAIR) and not hasbar
        BRK=re.compile(r'(?= → )|(?= · )|(?= \((?=[\u0e01-\u0e5b]))|(?= ดังนั้น )|(?<=,) ')
        def clauses(h):
            parts=[x.strip() for x in BRK.split(h) if x and x.strip()]
            if len(parts)<2: return h
            return ' '.join(f"<span class='cl'>{x}</span>" for x in parts)
        def li(i,s):
            st=f' style="margin-left:{min(i,4)*9}mm"' if stair else ''
            ar='<i class="ar"></i>' if (stair and i<len(it['steps'])-1) else ''
            return f'<li{st}>{numbind(clauses(hl(s)))}{ar}</li>'
        steps=''.join(li(i,s) for i,s in enumerate(it['steps']))
        bar=f'<div class="inl dgm">{diag.DIAG[(no,k)](kind)}</div>' if hasbar else ''
        olc='stair' if stair else ''
        exb=('<div class="extras"><div class="ex ck"><b>✓ ตรวจคำตอบ</b><span>'+html.escape(extras.CHK[(no,k)])+'</span></div><div class="ex tp"><b>💡 จุดสังเกต</b><span>'+html.escape(extras.TIP[no])+'</span></div><div class="ex wn"><b>⚠ ข้อควรระวัง</b><span>'+html.escape(extras.WARN[no])+'</span></div></div>')
        inl=''
        if it['aimg'] and no in range(16,31): inl=f'<div class="inl wide">{it["aimg"]}</div>'; it=dict(it,aimg='')
        aimg=f'<div class="aimg">{it["aimg"]}</div>' if it['aimg'] else ''
        note=f'<div class="note">{html.escape(it["note"])}</div>' if it['note'] else ''
        slides.append(f'<section class="sl a {kind}">{deco()}<div class="bar"><span class="no">{no}</span><div><h1>เฉลย · {title}</h1><span class="sub">{html.escape(p["topic"])}</span></div><span class="tag">{CHECK}เฉลย</span></div><div class="abody"><div class="steps{" hb" if hasbar else ""}">{bar}<ol class="{olc}">{steps}</ol>{note}{inl}{exb}</div><div class="ansc"><div class="medal">{medal(it["ans"],kind)}</div>{aimg}</div></div><div class="ft"><span>สไลด์ {n} / {total}</span><span class="brand">Math by T’Yasmin</span></div></section>')
assert n==total,(n,total)
js="""<script>
document.fonts.ready.then(()=>{
 const MIN=36*3.78;
 document.querySelectorAll('.math').forEach(m=>{let f=parseFloat(getComputedStyle(m).fontSize);while(m.scrollWidth>m.clientWidth+1&&f>12){f-=1;m.style.fontSize=f+'px';}});
 document.querySelectorAll('.sl.q').forEach(s=>{const p=s.querySelector('.prob'),w=s.querySelector('.work');let fs=parseFloat(p.dataset.fs);while(w.clientHeight<MIN&&fs>12){fs-=1;p.style.setProperty('--fs',fs+'pt');}p.dataset.final=fs;});
 document.querySelectorAll('.sl.a .steps').forEach(el=>{let fs=el.classList.contains('hb')?22:(el.querySelector('ol.stair')?30:26);el.style.fontSize=fs+'pt';const med=el.closest('.sl').querySelector('.medal');const abs=getComputedStyle(med.parentElement).position=='absolute';
 const ov=()=>{if(!abs)return false;const m=med.getBoundingClientRect();return [...el.querySelectorAll('li,.ex')].some(l=>{const r=l.getBoundingClientRect();return r.right>m.left-10&&r.bottom>m.top-10&&r.left<m.right&&r.top<m.bottom})};
 const bad=()=>(el.scrollHeight>el.clientHeight+1||[...el.querySelectorAll('li')].some(l=>l.scrollWidth>l.clientWidth+1)||ov());
 const wraps=()=>{let n=0;el.querySelectorAll('li').forEach(li=>{const lh=parseFloat(getComputedStyle(li).fontSize)*1.1;const cs=[];const add=r=>{if(r.width>0&&r.height>0)cs.push(r.top+r.height/2)};
  const w=document.createTreeWalker(li,NodeFilter.SHOW_TEXT);let t;while(t=w.nextNode()){if(!t.data.trim())continue;if(t.parentElement.closest('.ar'))continue;const rg=document.createRange();rg.selectNodeContents(t);[...rg.getClientRects()].forEach(add);}
  li.querySelectorAll('.fr').forEach(f=>add(f.getBoundingClientRect()));cs.sort((a,b)=>a-b);let lines=cs.length?1:0;for(let i=1;i<cs.length;i++){if(cs[i]-cs[i-1]>lh*0.8)lines++;}if(lines>1)n++;});return n};
 while(bad()&&fs>10){fs-=0.5;el.style.fontSize=fs+'pt';}
 const fit=fs;
 if(!el.classList.contains('hb')){let best=null;let f=fit;while(f>=17){el.style.fontSize=f+'pt';if(!bad()){const w=wraps();if(w===0){best=[f,0];break;}if(w===1&&f>=19&&!best)best=[f,1];}f-=0.5;}
  if(best)fs=best[0];else fs=fit;el.style.fontSize=fs+'pt';el.dataset.wraps=wraps();}
 el.dataset.final=fs;});
 document.body.dataset.done=1;});
</script>"""
open('deck_p2.html','w').write(f'<!doctype html><meta charset=utf-8><title>สไลด์ติว LPMC ป.2 ครั้งที่ 23 (ข้อ 16–30)</title><style>{css}</style>'+''.join(slides)+js)
print('slides',len(slides))
