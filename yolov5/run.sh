python -m torch.distributed.launch --nproc_per_node 2 train.py --save_period 1 --data rico2coco_clickable.yaml --project rico2coco_clickable --name gpu12-test --freeze 10 --batch-size 128 --adam --patience 10

