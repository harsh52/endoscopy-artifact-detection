from subprocess import *
#Continuation of easy_install_1

call("sudo su",shell=True)
call("echo 'export PATH=/usr/local/cuda-10.0/bin${PATH:+:${PATH}}' >> ~/.bashrc",shell=True)

call("echo 'export LD_LIBRARY_PATH=/usr/local/cuda-10.0/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}' >> ~/.bashrc",shell=True)

call("source ~/.bashrc",shell=True)

call("sudo ldconfig",shell=True)
#installing numpy
call("pip install numpy",shell=True)

#installing opencv
call("pip install opencv-contrib-python",shell=True)