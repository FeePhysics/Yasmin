const {chromium}=require('playwright');
(async()=>{const [h,o]=process.argv.slice(2);const b=await chromium.launch();const p=await b.newPage();
await p.goto('file://'+process.cwd()+'/'+h);await p.evaluate(()=>document.fonts.ready);
await p.pdf({path:o,width:'210mm',height:'297mm',printBackground:true,preferCSSPageSize:true});await b.close()})()
