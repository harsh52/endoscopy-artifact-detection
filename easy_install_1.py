from subprocess import *
call("sudo apt-get update",shell=True)
call("sudo apt-get upgrade -y",shell=True)
#Install virtualenv using pip
call("sudo pip3 install virtualenv ",call=True)
#Create virtualenv using Python3
call("sudo apt install python3-venv",shell=True)
call("virtualenv -p python3 myenv",shell=True)
#Activating virtual environment
call("source myenv/bin/activate",shell=True)

#installing tensorflow
call("pip install --upgrade tensorflow-gpu",shell=True)

#installing dependencied for CUDA 10.0
call("sudo apt-get install build-essential",shell=True)
call("sudo apt-get install cmake git unzip zip",shell=True)
call("sudo apt-get install python-dev python3-dev python-pip python3-pip",shell=True)

#Install linux kernel header
call("sudo apt-get install linux-headers-$(uname -r)",shell=True)

#Install NVIDIA CUDA 10.0:

#removing previous cuda version
call("sudo apt-get purge nvidia*",shell=True)
call("sudo apt-get autoremove",shell=True)
call("sudo apt-get autoclean",shell=True)
call("sudo rm -rf /usr/local/cuda*",shell=True)

print("\n\n\n\n\n\n")
print("Is your Ububtu version is 16.04 ?")


while(1):
	print("Type Yes or No:")
	responce = input()
	if(responce=="Yes" or responce=="yes"):
		#For Ubuntu 16.04 :
		call("sudo apt-key adv --fetch-keys http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64/7fa2af80.pub",shell=True)
		call('echo "deb https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64 /" | sudo tee /etc/apt/sources.list.d/cuda.list',shell=True)
		break
	elif(responce==No or responce == no):
		#For Ubuntu 18.04 :
		call("sudo apt-key adv --fetch-keys http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/7fa2af80.pub",shell=True)
		call('echo "deb https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64 /" | sudo tee /etc/apt/sources.list.d/cuda.list',shell=True)
		break
call("sudo reboot -h now",shell=True)