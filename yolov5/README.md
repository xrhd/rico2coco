# Experiments with yolov5 model

## Run 

`sh start_yolov5_docker.sh` 

`docker cp rico2coco_clickable.yaml yolov5:/usr/src/app/data`

`python train.py --save_period 1 --data rico2coco_clickable.yaml --project demo_rico2coco_test_1`
