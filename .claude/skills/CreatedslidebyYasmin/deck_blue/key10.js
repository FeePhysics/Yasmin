const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage();
await p.goto('file://'+process.cwd()+'/key10.html');await p.evaluate(()=>document.fonts.ready);
await p.pdf({path:'key10.pdf',format:'A4',printBackground:true,preferCSSPageSize:true});await b.close()})()
