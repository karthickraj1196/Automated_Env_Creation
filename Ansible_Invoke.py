# -*- coding: utf-8 -*-
"""
Created on Fri sep 06 12:17:35 2019

@author: pushparajkarthick_d
"""

import xlrd
from subprocess import call
workbook = xlrd.open_workbook('/opt/QA_Migration/ansible_repo/server_cfg.xls')
worksheet = workbook.sheet_by_name('Sheet1')
row = worksheet.row(1)
Host_Machine = IP = row[0].value
Instance_name = row[1].value
server_grp = row[2].value
heap_size = row[3].value
groupname = row[4].value
lbname = row[5].value
nodename = row[6].value
jws_ip = row[7].value
domain_name = row[8].value
jws_service = row[9].value
print(IP,Instance_name,server_grp,heap_size,groupname,lbname,nodename,jws_ip,domain_name,jws_service)

with open('/opt/QA_Migration/ansible/roles/server_group/vars/cfg.yml', 'r') as file:
    filedata = file.read()
    chnge = filedata.replace('Solartis_Test', Instance_name).replace('V6_2Test', server_grp).replace('1024m', heap_size).replace('test', groupname).replace('testkblb', lbname).replace('05_test1.1', nodename).replace('0.0.0.0', jws_ip).replace('test.solartis.net', domain_name).replace('solartis-testkb-jws', jws_service)

with open('/opt/QA_Migration/ansible/roles/server_group/vars/main.yml', 'w') as file:
    file.write(chnge)

with open('/opt/QA_Migration/ansible_repo/Server_Group.yml', 'r') as file:
    hostdata = file.read()
    hostchange = hostdata.replace('all', Host_Machine)

with open('/opt/QA_Migration/ansible/Server_Group.yml', 'w') as file:
    file.write(hostchange)


call(['ansible-playbook', '-i', '/opt/QA_Migration/ansible/hosts', '/opt/QA_Migration/ansible/Server_Group.yml', '-vvv'])
