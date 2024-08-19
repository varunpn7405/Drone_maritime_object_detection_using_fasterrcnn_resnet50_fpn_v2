import os,shutil

path = os.getcwd()
inpPar = os.path.join(path,'Aerial Maritime.v9-tiled.voc')
outPar = os.path.join(path,'Dataset')

for folder in os.listdir(inpPar):
    
    if folder in ["test","train","valid"]:
        input_dir = os.path.join(inpPar,folder)
        outChild = os.path.join(outPar,folder)

        if not os.path.exists(outChild):
            os.makedirs(outChild)

        files = os.listdir(input_dir)

        for item in files:
            fname,ext=os.path.splitext(item)
            fitem = os.path.join(input_dir,item)

            if ext.lower() in [".png",".jpeg",".jpg"]:
                outChildImg=os.path.join(outChild,"Images")
                os.makedirs(outChildImg,exist_ok=True)
                shutil.copy(fitem,os.path.join(outChildImg,item))

            if ext.lower()==".xml":
                outChildLabel=os.path.join(outChild,"labels")
                os.makedirs(outChildLabel,exist_ok=True)
                shutil.copy(fitem,os.path.join(outChildLabel,item))



            

