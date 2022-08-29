import os
import time
import boto3


interval = os.environ.get('INTERVAL')
ec2 = boto3.resource('ec2')


def find_running_ec2():
    count = 0
    response = ec2.instances.all()
    for instances in response:
        for tag in instances.tags:
            if instances.state['Code'] == 16:
                if tag['Key'] == 'Name' and tag['Value'] == 'devops':
                    print("Name: {0}".format(tag['Value']))
                elif tag['Key'] == 'k8s.io/role/master' and tag['Value'] == '1':
                    print("Id: {0}".format(instances.id))
    count = count + 1
    print("Number of instances running: " + str(count))


if interval == None:
    find_running_ec2()
else:
    while True:
        find_running_ec2()
        print("Sleep for {0} seconds".format(interval))
        time.sleep(int(interval))
