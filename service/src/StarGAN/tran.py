from PIL import Image
import os.path
import glob
import cv2 


root='/home/wings/temp/ferwebapp/fer-service/src/StarGAN/data/ori/'
for (root, dirs, files) in os.walk(root):
    for filename in files:
        print(os.path.join(root,filename))
        ori_im_path=os.path.join(root,filename)
        ori_im=cv2.imread(ori_im_path)
        size= 256,256
        new_image = cv2.resize(ori_im,size)

        new_im_path=ori_im_path.replace('ori','test/0')
        cv2.imwrite(new_im_path, new_image)
    for dirc in dirs:
        print(os.path.join(root,dirc))

