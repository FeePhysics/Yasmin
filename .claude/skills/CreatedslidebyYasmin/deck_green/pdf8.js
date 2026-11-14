const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage();
await p.goto('file://'+process.cwd()+'/deck8.html');await p.waitForSelector('body[data-done]',{timeout:180000});
const info=await p.evaluate(()=>({a:[...document.querySelectorAll('.sl.a .steps')].map((e,i)=>[i,+e.dataset.final,+(e.dataset.wraps||0)]),q:[...document.querySelectorAll('.sl.q .prob')].map((e,i)=>[i,+e.dataset.final,+e.dataset.fs]).filter(a=>a[1]<a[2])}));
console.log('shrunk q:',JSON.stringify(info.q));
console.log('answer slides with wraps:',JSON.stringify(info.a.filter(x=>x[2]>0)));
console.log('min font:',Math.min(...info.a.map(x=>x[1])),' count<18:',info.a.filter(x=>x[1]<18).length);
await p.pdf({path:'deck8.pdf',width:'297mm',height:'210mm',printBackground:true,preferCSSPageSize:true,outline:true});
await b.close()})()
