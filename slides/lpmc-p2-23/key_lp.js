const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage();
for(const [i,o] of [['key_lp.html','key_lp.pdf'],['tips_lp.html','tips_lp.pdf']]){
await p.goto('file://'+process.cwd()+'/'+i);await p.evaluate(()=>document.fonts.ready);
await p.pdf({path:o,format:'A4',printBackground:true,preferCSSPageSize:true});}
await b.close()})()
