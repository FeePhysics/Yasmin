from PIL import Image
import sys
def page(no,kind,k): return 2+(no-1)*6+k*2+(0 if kind=='q' else 1)
def sheet(pages,out,cols=2):
    ims=[Image.open(f'dk/p-{p:03d}.png') for p in pages]
    w,h=ims[0].size;rows=(len(ims)+cols-1)//cols
    c=Image.new('RGB',(w*cols,h*rows),'white')
    for i,im in enumerate(ims): c.paste(im,((i%cols)*w,(i//cols)*h))
    c.save(out)
if __name__=='__main__':
    sheet([1,page(1,'q',0),page(1,'a',0),page(2,'q',1),page(2,'a',1),page(3,'a',0)],'s1.png')
    sheet([page(7,'q',0),page(7,'a',0),page(12,'q',0),page(12,'a',0),page(17,'q',0),page(17,'a',0)],'s2.png')
    sheet([page(20,'q',0),page(20,'a',0),page(21,'q',1),page(21,'a',1),page(24,'a',0),page(26,'q',0)],'s3.png')
    sheet([page(26,'a',0),page(27,'q',0),page(27,'a',0),page(28,'q',0),page(28,'a',0),page(28,'a',1)],'s4.png')
    sheet([page(29,'q',0),page(29,'a',0),page(30,'q',0),page(30,'a',0),page(30,'q',2),page(30,'a',2)],'s5.png')
