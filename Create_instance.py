from shade import *
from json import dumps

simple_logging(debug=True)
conn = openstack_cloud(cloud='maas')

print("Images:")
images = conn.list_images()
for image in images:
    print(dumps(image,indent = 4, sort_keys=True))

print("Flavor:")
flavors =  conn.list_flavors()
for flavor in flavors:
    print(dumps(flavor,indent = 4, sort_keys=True))


image_id = '78ecb1ba-b44c-4277-833c-6268ae2045c1'
image = conn.get_image(image_id)
#print(dumps(image,indent = 4, sort_keys=True))


flavor_id = '0cb1f143-8b9a-4367-8ab3-9be101ceb305'
flavor = conn.get_flavor(flavor_id)
#print(dumps(flavor,indent = 4, sort_keys=True))


instance_name = 'Paulo-Proto2'
testing_instance = conn.create_server(wait=True, auto_ip=True,
    name=instance_name,
    image=image_id,
    flavor=flavor_id)
print(testing_instance)


#conn.delete_server(name_or_id='Proto2-Paulo')


instances = conn.list_servers()
for instance in instances:
    print(dumps(instance,indent = 4, sort_keys=True))
