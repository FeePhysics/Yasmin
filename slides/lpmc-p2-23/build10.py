import re, html, sys
sys.path.insert(0,'.')
import data10
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
assert sorted(ALL)==list(range(1,31)),sorted(ALL)
src=open('gen3.py').read()
FONTS=re.search(r"fonts='''(.*?)'''",src,re.S).group(1)+''.join(re.findall(r"fonts\+='''(.*?)'''",src,re.S))
css=FONTS+"""@font-face{font-family:Itim;font-weight:400;src:url(ff/itim-thai-400-normal.woff2);unicode-range:U+0E01-0E5B,U+200B-200D,U+25CC}
@font-face{font-family:Itim;font-weight:400;src:url(ff/itim-latin-400-normal.woff2);unicode-range:U+0000-00FF,U+2013-2014,U+2018-201F,U+2212,U+00D7,U+00F7,U+2026}

@page{size:297mm 210mm;margin:0}
*{box-sizing:border-box}
:root{--cream:#F8F3E4;--paper:#FFFFFF;--orange:#2F5FA8;--dorange:#1C3A6B;--yellow:#E8C877;--syellow:#F3E7C9;--green:#6B7F99;--dgreen:#3E566E;--sgreen:#E6EBF3;--brown:#10244A;--mbrown:#1C3A6B;--line:#D4DDEB}
body{margin:0;font-family:Mali,sans-serif;font-weight:500;color:var(--brown)}
.sl{position:relative;width:297mm;height:210mm;padding:8mm 11mm 12mm;page-break-after:always;display:flex;flex-direction:column;gap:4mm;overflow:hidden;background:url(assets/bg.jpg) center/100% 100% no-repeat,var(--cream)}
.sl:last-child{page-break-after:auto}
.wm{position:absolute;left:50%;top:60%;width:112mm;transform:translate(-50%,-50%);z-index:0}
.sl>*:not(.wm){position:relative;z-index:1}
.bar{background:linear-gradient(90deg,var(--dorange),var(--orange) 60%,#4A86D8);border-radius:7mm;border-bottom:2.2mm solid var(--yellow);display:flex;align-items:center;gap:5mm;padding:2.6mm 7mm;color:#fff;box-shadow:0 1.2mm 0 rgba(217,112,26,.25)}
.a .bar{background:linear-gradient(90deg,var(--dgreen),var(--green) 60%,#97A8BF);border-bottom-color:var(--yellow);box-shadow:0 1.2mm 0 rgba(47,138,78,.25)}
.no{width:14mm;height:14mm;border-radius:50%;background:var(--yellow);color:var(--brown);border:1.1mm solid #fff;box-shadow:0 0 0 .8mm var(--yellow);display:flex;align-items:center;justify-content:center;font-weight:700;font-size:18pt;flex:0 0 14mm}
.mock .no{background:#fff;color:var(--dorange);box-shadow:0 0 0 .8mm #fff}
.a.mock .no{color:var(--dgreen)}
.bar h1{margin:0;font-size:20pt;font-weight:700;line-height:1.15}
.bar .sub{font-size:11pt;color:#E9EEF6;font-weight:600}
.tag{margin-left:auto;border-radius:7mm;padding:1.5mm 6mm;font-weight:700;font-size:13pt;white-space:nowrap;box-shadow:0 .6mm 0 rgba(0,0,0,.14)}
.real .tag{background:var(--yellow);color:var(--brown)}.mock .tag{background:#fff;color:var(--dorange)}.a .tag{background:#fff;color:var(--dgreen)}
.prob{background:var(--paper);border:1.6px solid var(--line);border-radius:6mm;box-shadow:0 1.4mm 0 #C9D6EA;padding:5.5mm 9mm;font-family:Mali,sans-serif;font-weight:600;font-size:var(--fs,26pt);line-height:1.55;color:var(--brown);display:flex;gap:7mm;align-items:center;position:relative}
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
.pl{font:700 26px Mali,sans-serif;fill:#10244A}.lg{font:600 19px Mali,sans-serif;fill:#10244A}.gt{font:600 11px Mali,sans-serif;fill:#4A5C78}.gt2{font:700 13px Mali,sans-serif;fill:#10244A}.bt{font:700 26px Mali,sans-serif;fill:#10244A}
.work{flex:1;min-height:30mm;border:1.8px dashed #9DB6DA;border-radius:6mm;background:#fff;position:relative}
.work span{position:absolute;left:9mm;top:-3.6mm;background:var(--yellow);color:var(--brown);border-radius:3mm;padding:.2mm 4mm;font-size:11.5pt;font-weight:700}
.ans{display:flex;align-items:center;justify-content:flex-end;gap:3mm;font-size:14pt;font-weight:700;color:var(--dorange);margin-top:-1mm}
.ans .box{width:72mm;height:10.5mm;border:1.8px solid var(--orange);border-radius:4mm;background:var(--paper)}
.abody{flex:1;display:flex;gap:6mm;min-height:0}
.steps{flex:1;min-width:0;overflow:hidden;font-family:Mali,sans-serif;font-weight:600;font-size:22pt;line-height:1.45;color:var(--brown);display:flex;flex-direction:column}
.steps ol{margin:0;padding:0;list-style:none;counter-reset:s;display:flex;flex-direction:column;gap:2.6mm}
.steps li{counter-increment:s;position:relative;background:var(--paper);border:1.6px solid var(--line);border-radius:5mm;box-shadow:0 1mm 0 #C9D6EA;padding:2.6mm 5mm 2.6mm 17mm}
.steps li:before{content:counter(s);position:absolute;left:4mm;top:50%;transform:translateY(-50%);width:9.5mm;height:9.5mm;border-radius:50%;background:var(--green);color:#fff;font-size:.8em;font-weight:700;display:flex;align-items:center;justify-content:center;line-height:1;box-shadow:0 0 0 .8mm var(--sgreen)}
.steps li:last-child{background:#F7EEDA;border-color:var(--orange);box-shadow:0 1mm 0 #8FB1E0}
.steps li:last-child:before{background:var(--orange);box-shadow:0 0 0 .8mm #CFE0F6}
.steps mark{background:#F0DFB0;color:var(--brown);padding:0 1.6mm;border-radius:2mm;font-weight:700}
.steps .ic{width:1.1em;height:1.1em}
.steps .inl{margin-top:2.4mm;background:var(--paper);border:1.6px solid var(--line);border-radius:5mm;padding:2mm}.steps .inl svg,.steps .inl img{width:auto;height:auto;max-height:30mm;max-width:100%;display:block;margin:0 auto}
.ansc{flex:0 0 34%;display:flex;flex-direction:column;gap:4mm;min-height:0}
.ansbox{background:linear-gradient(160deg,#7C93B0,var(--dgreen));border-radius:7mm;padding:3.5mm 6mm 4mm;text-align:center;color:#fff;box-shadow:0 1.6mm 0 #2B3E55}
.ansbox small{display:inline-block;background:var(--yellow);color:var(--brown);border-radius:4mm;padding:0 5mm;font-size:13pt;font-weight:700}
.ansbox b{display:block;font-family:Mali,sans-serif;font-size:50pt;line-height:1.1;font-weight:700;color:#fff;}
.aimg{flex:1;min-height:0;display:flex;justify-content:center;align-items:center;background:var(--paper);border:1.6px solid var(--line);border-radius:6mm;box-shadow:0 1.2mm 0 #C9D6EA;padding:2mm;overflow:hidden}
.aimg .img{width:100%;height:100%;max-width:100%;object-fit:contain}
.note{font-size:9.5pt;font-weight:600;color:#4A3A10;background:#F7EEDA;border:1px solid #D9B866;border-radius:3mm;padding:1.4mm 3mm;text-align:center}
.ft{position:absolute !important;left:11mm;right:11mm;bottom:3.8mm;display:flex;justify-content:space-between;align-items:center;font-size:9.5pt;color:var(--mbrown)}
.ft .brand{font-family:Fredoka,Mali,sans-serif;font-weight:600;color:var(--dorange);font-size:13.5pt;letter-spacing:.3mm}
.a .ft .brand{color:var(--dgreen)}
.cover{justify-content:center;align-items:center;text-align:center;gap:5mm}
.cover .wm{width:150mm;top:50%}
.cover .big{font-size:34pt;font-weight:700;line-height:1.3;color:var(--brown)}.cover .big b{color:var(--dorange)}
.cover .chip{background:var(--orange);color:#fff;border-radius:8mm;padding:2.2mm 10mm;font-weight:700;font-size:19pt;box-shadow:0 1mm 0 var(--dorange)}
.cover .meta{font-size:16pt;font-weight:600;color:var(--mbrown)}
.cover .list{display:grid;grid-template-columns:repeat(6,1fr);gap:2.6mm;width:275mm;margin-top:2mm}
.cover .list div{background:var(--paper);border:1.4px solid var(--line);border-top:1.8mm solid var(--c,var(--orange));border-radius:3mm;padding:1.6mm 2.4mm;font-size:9.4pt;font-weight:600;text-align:left;line-height:1.25}
.cover .list div b{color:var(--dorange);font-size:10.5pt}
.cover .list div:nth-child(3n+2){--c:var(--yellow)}.cover .list div:nth-child(3n){--c:var(--green)}

.cvr{padding:0;background:#F8F3E4}
.cvr .bgb{position:absolute !important;z-index:0 !important;left:-6mm;top:-6mm;width:calc(100% + 12mm);height:calc(100% + 12mm);object-fit:cover}.cvr .fg{position:absolute !important;z-index:1 !important;left:0;top:50%;transform:translateY(-50%);width:100%;height:auto}
.deco{position:absolute !important;left:0;top:0;width:297mm;height:210mm;z-index:0;pointer-events:none}
.sl.a .bar .tag{display:flex;align-items:center;gap:2mm}
.tag svg{width:5.4mm;height:5.4mm}
.steps ol{position:relative;gap:3.2mm}
.steps ol:before{content:"";position:absolute;left:8.2mm;top:9mm;bottom:9mm;border-left:1.4mm dotted #8FB1E0}
.steps li{padding:2.8mm 6mm 2.8mm 19mm;border:none;border-radius:6mm;box-shadow:0 1.1mm 0 var(--sc2),0 0 0 1.5px var(--sc1) inset;background:#FFFFFF}
.steps li:nth-child(3n+1){--sc1:#8FB1E0;--sc2:#C9D6EA;--bc:#2F5FA8}
.steps li:nth-child(3n+2){--sc1:#C9B26A;--sc2:#DCE5F2;--bc:#B8923C}
.steps li:nth-child(3n){--sc1:#B7C4D6;--sc2:#DCE4F0;--bc:#6B7F99}
.steps li:before{left:2.2mm;width:11.5mm;height:11.5mm;background:var(--bc);box-shadow:0 0 0 1.1mm #fff,0 0 0 1.9mm var(--sc1);font-size:.85em}
.steps li:last-child{background:linear-gradient(90deg,#E3ECF8,#F7EEDA);--sc1:#6B7F99;--sc2:#B7C4D6;padding-right:16mm}
.steps li:last-child:before{background:#3E566E;box-shadow:0 0 0 1.1mm #fff,0 0 0 1.9mm #6B7F99}
.steps li:last-child:after{content:"";position:absolute;right:4mm;top:50%;width:9mm;height:9mm;transform:translateY(-50%);border-radius:50%;background:#6B7F99 url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'><path d='M5 12.5l4.5 4.5L19 7.5' fill='none' stroke='white' stroke-width='3.4' stroke-linecap='round' stroke-linejoin='round'/></svg>") center/70% no-repeat}
.steps mark{font-weight:700;white-space:nowrap;background:#F3E7C9;border:1px solid #D9B866;padding:0 1.8mm;border-radius:3mm}
.steps li:last-child mark{background:#3E566E;border-color:#3E566E;color:#fff}
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
.real .bar{background:linear-gradient(90deg,#1C3A6B,#2F5FA8 60%,#4A86D8);border-bottom-color:#E8C877;box-shadow:0 1.2mm 0 rgba(217,112,26,.25)}
.mock .bar{background:linear-gradient(90deg,#3E566E,#6B7F99 60%,#97A8BF);border-bottom-color:#E8C877;box-shadow:0 1.2mm 0 rgba(47,138,78,.25)}
.a.real .bar{background:linear-gradient(90deg,#1C3A6B,#2F5FA8 60%,#4A86D8);border-bottom-color:#E8C877}
.a.mock .bar{background:linear-gradient(90deg,#3E566E,#6B7F99 60%,#97A8BF);border-bottom-color:#E8C877}
.sl.real{background:url(assets/bg_real.jpg) center/100% 100% no-repeat,#F8F3E4}
.sl.mock{background:url(assets/bg_mock.jpg) center/100% 100% no-repeat,#F3F5F9}
.real .no{background:#E8C877;color:#10244A}.mock .no{background:#fff;color:#3E566E;box-shadow:0 0 0 .8mm #fff}
.real .tag,.a.real .tag{background:#E8C877;color:#10244A}.mock .tag,.a.mock .tag{background:#fff;color:#3E566E}
.real .prob:before{background:#2F5FA8}.mock .prob:before{background:#6B7F99}
.real .prob{border-color:#D4DDEB;box-shadow:0 1.4mm 0 #C9D6EA}.mock .prob{border-color:#DCE4F0;box-shadow:0 1.4mm 0 #C7D3E4}
.real .work{border-color:#9DB6DA}.mock .work{border-color:#B7C4D6}
.mock .work span{background:#D5DFEE}
.real .ans{color:#1C3A6B}.real .ans .box{border-color:#2F5FA8}
.mock .ans{color:#3E566E}.mock .ans .box{border-color:#6B7F99}
.real .ft .brand,.a.real .ft .brand{color:#1C3A6B}.mock .ft .brand,.a.mock .ft .brand{color:#3E566E}
.real .steps ol:before{border-left-color:#8FB1E0}.mock .steps ol:before{border-left-color:#B7C4D6}
.real .steps li:nth-child(3n+1){--sc1:#8FB1E0;--sc2:#C9D6EA;--bc:#2F5FA8}
.real .steps li:nth-child(3n+2){--sc1:#C9B26A;--sc2:#DCE5F2;--bc:#B8923C}
.real .steps li:nth-child(3n){--sc1:#8FB1E0;--sc2:#C9D6EA;--bc:#5B7FB5}
.mock .steps li:nth-child(3n+1){--sc1:#B7C4D6;--sc2:#DCE4F0;--bc:#6B7F99}
.mock .steps li:nth-child(3n+2){--sc1:#C9B26A;--sc2:#DCE5F2;--bc:#B8923C}
.mock .steps li:nth-child(3n){--sc1:#B7C4D6;--sc2:#DCE4F0;--bc:#3E566E}
.real .steps li:last-child{background:linear-gradient(90deg,#F3E7C9,#F7EEDA);--sc1:#2F5FA8;--sc2:#8FB1E0}
.real .steps li:last-child:before{background:#1C3A6B;box-shadow:0 0 0 1.1mm #fff,0 0 0 1.9mm #2F5FA8}
.real .steps li:last-child:after{background-color:#2F5FA8}
.real .steps li:last-child mark,.real .steps mark.res:last-child{background:#1C3A6B;border-color:#1C3A6B;color:#fff}
.real .steps li:last-child mark.res{background:#1C3A6B;border-color:#1C3A6B;color:#fff}
.real .tb th{background:#F3E7C9}

.ansc{flex:0 0 64mm}
.steps .inl{flex:1 1 auto;min-height:44mm;margin-top:2.6mm;display:flex;align-items:center;justify-content:center;padding:2mm;background:var(--paper);border:1.6px solid var(--line);border-radius:5mm;box-shadow:0 1mm 0 #C9D6EA}
.steps .inl.wide{min-height:26mm}
.steps .inl svg,.steps .inl img{height:100%;max-height:100%;width:auto;max-width:100%;margin:0}
.mock .steps .inl{border-color:#DCE4F0;box-shadow:0 1mm 0 #C7D3E4}
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
.steps li .ar{position:absolute;left:13mm;bottom:-4.8mm;width:0;height:0;border-left:3.2mm solid transparent;border-right:3.2mm solid transparent;border-top:4.2mm solid var(--bc,#2F5FA8)}
.steps li{position:relative}

.sl.a:not(:has(.aimg)):not(:has(.dgm)):not(:has(.inl)) .ansc{position:absolute;right:11mm;bottom:12mm;width:46mm;flex:none}
.sl.a:not(:has(.aimg)):not(:has(.dgm)):not(:has(.inl)) .ansc .medal{width:44mm}

.steps .note{margin-top:2.4mm;text-align:left;font-size:10.5pt;align-self:flex-start;max-width:70%}

.extras{display:grid;grid-template-columns:1.25fr 1fr 1fr;gap:3mm;margin-top:auto;padding-top:3mm;flex:0 0 auto}
.ex{border-radius:4mm;padding:1.6mm 3mm 2mm;font-family:Mali,sans-serif;font-weight:600;font-size:11.5pt;line-height:1.35;border:1.4px solid;min-width:0}
.ex b{display:inline-block;font-size:11pt;font-weight:700;border-radius:3mm;padding:0 2.4mm;margin-bottom:.8mm}
.ex span{display:block;color:#10244A}
.ex.ck{background:#EAF0F8;border-color:#B7C4D6}.ex.ck b{background:#6B7F99;color:#fff}
.ex.tp{background:#F7EEDA;border-color:#D9B866}.ex.tp b{background:#E8C877;color:#10244A}
.ex.wn{background:#E9EEF6;border-color:#8FB1E0}.ex.wn b{background:#5B7FB5;color:#fff}
.sl.a:not(:has(.aimg)):not(:has(.dgm)):not(:has(.inl)) .extras{margin-right:62mm}

.steps .cl{display:inline-block;max-width:100%;vertical-align:baseline}
.steps .inl.dgm{height:50mm}

.steps li,.prob .ptxt{text-wrap:pretty}
.steps.hb .extras{font-size:10pt}
.steps.hb .ex{font-size:10pt}

.cvr2{padding:0;background:linear-gradient(135deg,#1C3A6B 0%,#2F5FA8 60%,#4A86D8 100%);color:#fff;align-items:center;justify-content:center;text-align:center}
.cvr2 .cvc{display:flex;flex-direction:column;align-items:center;gap:7mm}
.cvr2 .cvl{background:#fff;border-radius:50%;width:62mm;height:62mm;display:flex;align-items:center;justify-content:center;box-shadow:0 0 0 2.4mm #F3E7C9}
.cvr2 .cvl img{width:50mm;height:auto}
.cvr2 .cvchip{background:#F3E7C9;color:#1C3A6B;border-radius:8mm;padding:2mm 10mm;font-weight:700;font-size:17pt}
.cvr2 .cvt{font-size:30pt;font-weight:700;line-height:1.35}
.cvr2 .cvs{font-size:19pt;font-weight:600;color:#DCE4F0}.cvr2 .cvs b{color:#F3E7C9}
.cvr2 .cvm{font-size:15pt;font-weight:600;background:rgba(255,255,255,.14);border-radius:6mm;padding:2mm 8mm}
.cvr2 .cvf{position:absolute;right:11mm;bottom:6mm}.cvr2 .cvf .brand{font-family:Mali,sans-serif;font-weight:700;color:#F3E7C9;font-size:13.5pt}
.steps .inl.wide{min-height:34mm}.steps .inl.wide svg{max-height:46mm !important}
"""


import math as _m
def medal(ans,kind='real'):
    P={'real':('#6C9BDC','#1C3A6B','#EFD793','#F6EAC8'),'mock':('#8AA0BC','#3E566E','#EFD793','#E5ECF6')}[kind]
    n=len(ans);fs={1:125,2:112,3:92}.get(n,74)
    pt=lambda a,r:(150+r*_m.cos(_m.radians(a)),150+r*_m.sin(_m.radians(a)))
    rays=''.join('<polygon points="150,150 %.1f,%.1f %.1f,%.1f" fill="%s"/>'%(*pt(a-5,150),*pt(a+5,150),P[2] if (a//15)%2==0 else P[3]) for a in range(0,360,15))
    spark=''.join(f'<polygon transform="translate({x},{y}) scale({s})" points="0,-10 3,-3 10,0 3,3 0,10 -3,3 -10,0 -3,-3" fill="{c}"/>' for x,y,s,c in [(32,60,1.3,"#2F5FA8"),(268,70,1.6,"#E8C877"),(262,250,1.2,"#B7C4D6"),(40,248,1.5,"#E8C877"),(150,12,1.1,"#2F5FA8")])
    return (f'<svg viewBox="0 0 300 300"><defs><linearGradient id="g{kind}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{P[0]}"/><stop offset="1" stop-color="{P[1]}"/></linearGradient></defs>'
            f'{rays}{spark}<circle cx="150" cy="156" r="112" fill="#fff"/><circle cx="150" cy="156" r="102" fill="url(#g{kind})"/><circle cx="150" cy="156" r="92" fill="none" stroke="#fff" stroke-width="3" stroke-dasharray="3 9" stroke-linecap="round"/>'
            f'<text x="150" y="{156+fs*0.36:.0f}" text-anchor="middle" font-family="Mali" font-weight="700" font-size="{fs}" fill="#fff">{ans}</text>'
            f'<g transform="translate(150,52)"><path d="M-62,-18 H62 L72,0 L62,18 H-62 L-72,0 Z" fill="#E8C877" stroke="#fff" stroke-width="5" stroke-linejoin="round"/><text x="0" y="8" text-anchor="middle" font-family="Mali" font-weight="700" font-size="24" fill="#10244A">คำตอบ</text></g></svg>')
CHECK='<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="11" fill="#6B7F99"/><path d="M6.5 12.5l4 4 7-8" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg>'
def deco():
    sp=lambda x,y,s,c,o:f'<polygon transform="translate({x},{y}) scale({s})" points="0,-10 3,-3 10,0 3,3 0,10 -3,3 -10,0 -3,-3" fill="{c}" opacity="{o}"/>'
    sh=''.join([sp(1090,610,3.2,"#E8C877",.45),sp(1120,330,1.8,"#2F5FA8",.35),sp(60,540,2.6,"#B7C4D6",.45),sp(30,300,1.7,"#E8C877",.4),sp(610,35,1.5,"#E8C877",.4),
        '<circle cx="1105" cy="470" r="9" fill="#B7C4D6" opacity=".35"/><circle cx="25" cy="440" r="7" fill="#2F5FA8" opacity=".3"/><circle cx="1060" cy="140" r="6" fill="#E8C877" opacity=".4"/>'])
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
total=2+30*6
cv1 = '<section class="sl cvr2"><h1 style="position:absolute;left:-9999px">หน้าปก</h1><div class="cvc"><div class="cvl"><img src="assets/logo.png"></div><div class="cvchip">สไลด์ติวสอบแข่งขัน · ระดับประถมศึกษาตอนปลาย</div><div class="cvt">การแข่งขันสอบวัดทักษะวิชาการระดับชาติ (สวช.)<br>ชิงถ้วยพระราชทานฯ</div><div class="cvs">วิชา<b>คณิตศาสตร์</b> · พ.ศ. 2567 · รหัสชุดข้อสอบ 201010</div><div class="cvm">ข้อจริง 30 ข้อ + Mock Test 60 ข้อ + เฉลยทุกหน้า</div></div><div class="cvf"><span class="brand">Math by T’Yasmin</span></div></section>'
cover = '<section class="sl cover"><h1 style="position:absolute;left:-9999px">สารบัญ</h1><div class="chip">สารบัญ</div><div class="big">ข้อสอบ สวช. <b>คณิตศาสตร์</b> พ.ศ. 2567 · รหัสชุด 201010</div><div class="meta">ข้อจริง 30 ข้อ · Mock Test 60 ข้อ (ข้อละ 2 ข้อ) · เฉลยทุกข้อ</div><div class="list">'+''.join(f'<div><b>ข้อ {n}</b> {html.escape(ALL[n]["topic"])}</div>' for n in range(1,31))+'<div style="grid-column:span 6;text-align:center;--c:#E8C877">ลำดับ: ข้อจริง → เฉลย → Mock Test 1 → เฉลย → Mock Test 2 → เฉลย · เขียนวิธีคิดบนสไลด์ด้วยปากกาใน GoodNotes</div></div><div class="ft"><span></span><span class="brand">Math by T’Yasmin</span></div></section>'
slides.append(cv1)
slides.append(cover)
n=2
BELOW=set()
for no in range(1,31):
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
        slides.append(f'<section class="sl q {kind}"><div class="bar"><span class="no">{no}</span><div><h1>{title}</h1><span class="sub">{html.escape(p["topic"])}</span></div><span class="tag">{"ข้อจริง · ข้อสอบ สวช." if k==0 else "Mock Test "+str(k)+"/2"}</span></div><div class="prob{below}" data-fs="{fs}" style="--fs:{fs}pt"><div class="ptxt">{bind(it["q"])}</div>{img}</div><div class="work"><span>วิธีคิด</span></div><div class="ans">ตอบ<span class="box"></span></div><div class="ft"><span>สไลด์ {n} / {total}</span><span class="brand">Math by T’Yasmin</span></div></section>')
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
        STAIR={1,2,3,4,5,6,7,8,9,12,13,14,15,16,17,18,19,20,21,22,23,24,25}
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
        if it['aimg'] and no in (24,25,28,30): inl=f'<div class="inl{" wide" if no in (24,25,28,30) else ""}">{it["aimg"]}</div>'; it=dict(it,aimg='')
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
open('deck10.html','w').write(f'<!doctype html><meta charset=utf-8><title>สไลด์ข้อสอบ สวช. 201010 (30 ข้อ)</title><style>{css}</style>'+''.join(slides)+js)
print('slides',len(slides))
