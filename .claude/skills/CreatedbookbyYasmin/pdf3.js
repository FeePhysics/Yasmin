const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage();
for(const [f,o] of [['set1','ใบงานชุดที่1_ปานกลาง_40ข้อ.pdf'],['set2','ใบงานชุดที่2_แข่งขัน_40ข้อ.pdf'],['key1','เฉลยชุดที่1.pdf'],['key2b','เฉลยชุดที่2.pdf']]){
await p.goto('file://'+process.cwd()+'/'+f+'.html');await p.evaluate(()=>document.fonts.ready);await p.pdf({path:o,width:'210mm',height:'297mm',printBackground:true,preferCSSPageSize:true});}
await b.close()})()
