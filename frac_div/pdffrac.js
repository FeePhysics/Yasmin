const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage();
await p.goto('file://'+process.cwd()+'/fracdetail.html');await p.evaluate(()=>document.fonts.ready);
console.log(await p.evaluate(()=>{const o=[];document.querySelectorAll('.fq').forEach((q,i)=>{const r=q.getBoundingClientRect();const c=q.querySelector('.chain');if(c.scrollWidth>c.clientWidth+1||q.querySelector('.ans').getBoundingClientRect().right>r.right+1)o.push('wide '+(i+1)+' '+c.scrollWidth+'/'+c.clientWidth);if(q.scrollHeight>q.clientHeight+1)o.push('tall '+(i+1))});return o}));
await p.pdf({path:'เฉลยละเอียด_การหารเศษส่วน_ทดสอบ2.pdf',width:'210mm',height:'297mm',printBackground:true,preferCSSPageSize:true});await b.close()})()
