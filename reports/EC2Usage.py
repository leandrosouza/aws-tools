#!/usr/bin/python

import boto.ec2

def get_ec2_instances(region):
    ec2_conn = boto.ec2.connect_to_region(region)
    instances = ec2_conn.get_all_instances()
    for inst in instances:
        print region+':',inst.instances

def main():
    regions = ['us-east-1','us-west-1','us-west-2','eu-west-1','sa-east-1',
                'ap-southeast-1','ap-southeast-2','ap-northeast-1']
    
    for region in regions: get_ec2_instances(region)

if  __name__ =='__main__':main()