import os,random
import xmltodict
from PIL import Image,ImageDraw,ImageFont

path = os.getcwd()
inpPar = os.path.join(path,'Dataset')
outPar = os.path.join(path,'Visualization')

if not os.path.exists(outPar):
    os.makedirs(outPar)

folders = os.listdir(inpPar)

cls_clr = {'car': '#9E52F4', 'lift': '#FC46FE', 'jetski': '#5390FB', 'dock': '#D67180', 'boat': '#63CE26'}

for folder in folders:
    input_dir = os.path.join(inpPar,folder,"labels")
    outChild = os.path.join(outPar,folder)

    if not os.path.exists(outChild):
        os.makedirs(outChild)

    files = os.listdir(input_dir)

    for item in files:
        fitem = os.path.join(input_dir,item)

        with open(fitem) as x :
            d = x.read()
            data = xmltodict.parse(d)

            imgname=data["annotation"]["filename"]

            image_path = os.path.join(inpPar,folder,"Images",imgname)
            out_img = os.path.join(outChild,imgname)

            if os.path.exists(image_path):
                print("Plotting_______________",image_path)
                img_obj=Image.open(image_path).convert("RGB")
                draw=ImageDraw.Draw(img_obj)
                font=ImageFont.truetype('arial.ttf',18)
                objects=data["annotation"]["object"]
                objects=[objects] if isinstance(objects,dict) else objects

                for obj in objects:
                    clsname=obj["name"]

                    # if clsname not in cls_clr:              
                    #     color = "#%06X" % random.randint(0, 0xFFFFFF)
                    #     cls_clr[clsname]=cls_clr[clsname]=color

                    clr = cls_clr[clsname]
                    xmin=float(obj["bndbox"]["xmin"])
                    ymin=float(obj["bndbox"]["ymin"])
                    xmax=float(obj["bndbox"]["xmax"])
                    ymax=float(obj["bndbox"]["ymax"])
                    draw.rectangle((xmin,ymin,xmax,ymax),outline=clr,width=2)
                    w,h=font.getbbox(clsname)[2:]
                    draw.rectangle((xmin, ymin-h, xmin+w, ymin), fill=clr)
                    draw.text((xmin,ymin-h),clsname,fill='white',font=font)

                img_obj.save(out_img)
            else:
                print('Image not exist : ',image_path)  

print(cls_clr)