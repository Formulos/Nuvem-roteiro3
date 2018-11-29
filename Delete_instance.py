from shade import *
from json import dumps

simple_logging(debug=True)
conn = openstack_cloud(cloud='maas')

conn.delete_server(name_or_id='Paulo-Proto2')
