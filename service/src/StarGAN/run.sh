echo "hello"
#source activate python36
python /home/wings/temp/ferwebapp/fer-service/src/StarGAN/tran.py
python /home/wings/temp/ferwebapp/fer-service/src/StarGAN/main.py --mode test --dataset RaFD --image_size 128 --c_dim 5 \
                 --selected_attrs Black_Hair Blond_Hair Brown_Hair Male Young \
                 --model_save_dir='/home/wings/temp/ferwebapp/fer-service/src/StarGAN/stargan_celeba_128/models' \
                 --result_dir='/home/wings/temp/ferwebapp/fer-service/src/StarGAN/stargan_celeba_128/results' \
                 --rafd_image_dir="/home/wings/temp/ferwebapp/fer-service/src/StarGAN/data/test/"

# rm -rf data/test/0
# mkdir data/test/0

# rm -rf data/ori
# mkdir data/ori
if [ $? -eq 0 ];then
    echo "python success"
else
    echo "python fail"
fi
echo "finish"
