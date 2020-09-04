import os
model_base_path='/content/drive/Shared drives/songyi1999/PESR/check_point/my_model/train/'
dataset_list=['Set5','Set14']
save_base_path='/content/drive/Shared drives/songyi1999/PESR/results/'

for dataset in  dataset_list:
  for i in range(200):
      num=i+1
      cmd="python test.py --dataset {} --perceptual_model '{}' --psnr_model '/content/drive/Shared drives/songyi1999/PESR/check_point/my_model/pretrain/best_model.pt' --save_path '{}'".format(dataset,model_base_path+"model_"+str(num)+".pt" ,save_base_path+"/"+str(num)   )
      print(cmd)
      os.system(cmd)
