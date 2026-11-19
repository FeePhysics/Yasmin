const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:794,height:1123},deviceScaleFactor:2.5});
await p.goto('file://'+process.cwd()+'/origkey.html');await p.evaluate(()=>document.fonts.ready);
const el=await p.$('.pg');await el.screenshot({path:'เฉลย_ทบทวนก่อนสอบ_สมการบวกลบ_48ข้อ.png'});await b.close()})()
