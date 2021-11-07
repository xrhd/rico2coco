docker build -t yolov5_wandb . &&
docker run -it -d --name yolov5 --ipc=host --gpus all  -v "$(pwd)"/new_dataset/:/usr/src/app/new_dataset yolov5_wandb
