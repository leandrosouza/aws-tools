#!/usr/bin/python

import boto.ec2
from collections import defaultdict, Counter

report = defaultdict(Counter)

def get_ec2_instances(region):
    ec2_conn = boto.ec2.connect_to_region(region)
    res = ec2_conn.get_all_instances()
    instances = [i for r in res for i in r.instances]
    vol = ec2_conn.get_all_volumes()
    for volumes in vol:
    	if volumes.attachment_state() == 'attached':
   			filter = {'block-device-mapping.volume-id':volumes.id}
   			volumesinstance = ec2_conn.get_all_instances(filters=filter)
			ids = [z for k in volumesinstance for z in k.instances]
			for s in ids:
				report[s.placement][s.instance_type] += 1
				#print 'Zone:' + s.placement,' - Instance ID:' + s.id + ' - Instance Type:' + s.instance_type + ' - Attached Volume ID:' + volumes.id +' - Device Name:' + volumes.attach_data.device


def main():
    regions = ['us-east-1','us-west-1','us-west-2','eu-west-1','sa-east-1',
                'ap-southeast-1','ap-southeast-2','ap-northeast-1']
    
    for region in regions:
    	get_ec2_instances(region)

    print report

if  __name__ =='__main__':main()