
#http://blog.csdn.net/liuxiao214/article/details/74502975


source activate tensorflow
cd /home/estel/PycharmProjects/spider/DCGAN-tensorflow-master/



python main.py --image_size 96 --output_size 48 --dataset xyjy --crop True --train True --epoch 300


python main.py --input_height=96 --output_height=96 --dataset nogizaka46 --train --epoch 300 --input_fname_pattern "*.jpg"


python main.py --input_height=96 --output_height=96 --dataset ddsm --train --epoch 2 --input_fname_pattern "*.jpg"
