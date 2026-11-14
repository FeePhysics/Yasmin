const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage();
await p.goto('file://'+process.cwd()+'/deck_lp.html');await p.waitForSelector('body[data-done]',{timeout:180000});
const res=await p.evaluate(()=>{
const out={orphan:[],unit:[],resalone:[],tiny:[],cover:0,slides:document.querySelectorAll('section.sl').length};
function lines(el){const w=document.createTreeWalker(el,NodeFilter.SHOW_TEXT);const L={};let t;
 while(t=w.nextNode()){if(t.parentElement.closest('.ar,.ex'))continue;for(let k=0;k<t.length;k++){const ch=t.data[k];const rg=document.createRange();rg.setStart(t,k);rg.setEnd(t,k+1);const rc=rg.getClientRects()[0];if(!rc||rc.width===0)continue;const y=Math.round((rc.top+rc.height/2)/6);(L[y]=L[y]||[]).push([rc.left,ch,rc.right])}}
 return Object.keys(L).map(Number).sort((a,b)=>a-b).map(y=>{const a=L[y].sort((p,q)=>p[0]-q[0]);return {txt:a.map(x=>x[1]).join('').trim(),w:a[a.length-1][2]-a[0][0]}})}
const secs=[...document.querySelectorAll('section.sl')];
secs.forEach((s,i)=>{
 const tag=(s.querySelector('h1')||{}).textContent||'';
 s.querySelectorAll('.ptxt').forEach(el=>{const cw=el.clientWidth;const L=lines(el);
  L.forEach((l,j)=>{if(j<L.length-1&&/[\d,\.%]\s*$/.test(l.txt)&&/^(บาท|คน|ตัว|ลูก|ผล|เหรียญ|เซนติเมตร|กิโลกรัม|นาที|วินาที|ปี|ใบ|แผ่น|ขา|ล้อ|ชั้น|งวด|วิธี|เครื่อง|ลิตร|เมตร)/.test(L[j+1].txt))out.unit.push([i+1,tag,l.txt.slice(-20),L[j+1].txt.slice(0,12)])});
  if(L.length>1){const last=L[L.length-1];if(last.txt.length<=6&&last.w<cw*0.12)out.orphan.push([i+1,tag,'Q',last.txt])}});
 s.querySelectorAll('.steps li').forEach(li=>{const cw=li.clientWidth;const L=lines(li);
  if(L.length>1){const last=L[L.length-1];const first=L[0];
   if(last.w<cw*0.22||/^[=\-−+×÷)→]/.test(last.txt)&&last.txt.length<8)out.orphan.push([i+1,tag,'A',L.map(l=>l.txt).join(' ⏎ ').slice(0,140)]);
   if(L.some((l,j)=>j<L.length-1&&/[=+−×÷\-\(]\s*$/.test(l.txt)&&false))out.orphan.push([i+1,tag,'A-op',''])}
  const m=li.querySelector('mark.res');if(m&&L.length>1&&L[L.length-1].txt.replace(/\s/g,'')===m.textContent.replace(/\s/g,''))out.resalone.push([i+1,tag,m.textContent])});
 s.querySelectorAll('.steps').forEach(el=>{const f=parseFloat(getComputedStyle(el).fontSize)*0.75;if(f<17)out.tiny.push([i+1,tag,f.toFixed(1)])});
});
return out});
console.log(JSON.stringify({slides:res.slides,orphan:res.orphan.length,unit:res.unit,resalone:res.resalone,tiny:res.tiny},null,0));
console.log('ORPHANS:');res.orphan.forEach(o=>console.log(JSON.stringify(o)));
await b.close()})()
