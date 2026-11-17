const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:794,height:1123}});
for(const [f,o] of [['p4set1','ใบงานชุดที่1_สมการ_ป4_48ข้อ.pdf'],['p4key1','เฉลยชุดที่1_สมการ_ป4.pdf']]){
await p.goto('file://'+process.cwd()+'/'+f+'.html');await p.evaluate(()=>document.fonts.ready);
const r=await p.evaluate(()=>{const out=[];
 document.querySelectorAll('.t').forEach((t,i)=>{const lh=parseFloat(getComputedStyle(t).lineHeight);const rs=[...t.getClientRects()];
  // count lines via range rects
  const rg=document.createRange();rg.selectNodeContents(t);const tops=new Set([...rg.getClientRects()].map(x=>Math.round(x.top)));
  if(tops.size>3) out.push('lines>3 q'+(i+1)+':'+tops.size);
  if(t.scrollHeight>t.clientHeight+1) out.push('overflow t'+(i+1));});
 document.querySelectorAll('.sec').forEach(s=>{const h=s.querySelector('.h');if(h&&h.getBoundingClientRect().right>s.getBoundingClientRect().right+1)out.push('hint clipped')});document.querySelectorAll('.q,.kq,.pg,.grid,.bar .main,.ks').forEach((e,i)=>{if(e.scrollHeight>e.clientHeight+1||e.scrollWidth>e.clientWidth+1)out.push('ovf '+e.className+' '+i+' '+e.textContent.slice(0,30))});
 const w=document.querySelector('.q .w');if(w)out.push('workbox h(px)='+w.getBoundingClientRect().height.toFixed(0));
 return out});
console.log(f,r);
await p.pdf({path:o,width:'210mm',height:'297mm',printBackground:true,preferCSSPageSize:true});
await p.screenshot({path:process.env.S+'/'+f+'.png',fullPage:true});}
await b.close()})()
