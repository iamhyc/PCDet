SHELL:=/bin/bash
MODEL_FILE:=../model/PartA2.pth
CONFIG_FILE:=cfgs/PartA2_car.yaml
BATCH_SIZE:=4

all:install

install:install-spconv
	sudo apt install python3 python3-pip -y
	pip3 install -r requirements.txt --user -i https://mirrors.sustc.us/pypi/simple
	python3 setup.py develop --user

install-spconv:
	@read -p 'Please ensure you have CUDA 9.0+ and cuDNN installed! (press ENTER to continue...)'

	sudo apt-get install libboost-all-dev -y
	sudo apt install python3 python3-pip -y
	pip3 install cmake --user --upgrade -i https://mirrors.sustc.us/pypi/simple
	pip3 install "torch>=1.1,<1.4" --user -i https://mirrors.sustc.us/pypi/simple
	
	rm -rf build/spconv && git clone https://github.com/traveller59/spconv.git build/spconv --recursive
	cd build/spconv; python3 setup.py bdist_wheel; cd ./dist; pip3 install *.whl --user
	#git reset --hard 8da6f967fb9a054d8870c3515b1b44eca2103634;

remove-spconv:
	pip3 uninstall spconv

test:
	cd tools; \
	python3 test.py --cfg_file $(CONFIG_FILE) --batch_size $(BATCH_SIZE) --ckpt $(MODEL_FILE) \
    --set MODEL.RPN.BACKBONE.NAME UNetV0 MODEL.RPN.RPN_HEAD.ARGS use_binary_dir_classifier:True

train:
	cd tools; \
	python3 train.py --cfg_file $(CONFIG_FILE) --batch_size $(BATCH_SIZE)

clean:
	rm -rf output