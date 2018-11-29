from shade import *
from json import dumps

simple_logging(debug=True)
conn = openstack_cloud(cloud='maas')


instances = conn.list_servers()
for instance in instances:
    print(dumps(instance,indent = 4, sort_keys=True))

