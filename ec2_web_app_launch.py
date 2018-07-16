
from ec2_web import Swarm_Leader
import boto3
import time
import yaml
import mpu.io
from subprocess import call



direc = "flaskproject"
github_clone = " git clone https://github.com/sande2jm/" + direc + ".git"
rm_repo = 'sudo rm -r ' + direc

with open("ec2_web_app.yaml", 'r') as stream:
	config = yaml.load(stream)

size = 1
swarm_name = config['instance']['name']
leader = Swarm_Leader(size=size,config=config['instance'])
pip_installs = []


leader.init(dependencies=pip_installs)
leader.populate()
leader.describe()
print(leader.locusts)


leader.gather(size = 1,group='web_app')
print(leader.swarm.items())
# leader.inject_code(rm_repo)
# leader.inject_code(github_clone)
for x,params in leader.swarm.items():
	ssh = "ssh -i ../DLNAkey.pem ubuntu@" + params['public_dns_name']
	call(ssh.split(" "))	
