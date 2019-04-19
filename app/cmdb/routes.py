from flask import jsonify
from app.zabbix import zapi
from app.cmdb import blueprint


@blueprint.route('/network', methods=['GET'])
def get_hostgroup_list():
    class Node:
        def __init__(self, value, label):
            self.value = value
            self.label = label
            self.children = []

        def get_value(self):
            return self.value

        def get_label(self):
            return self.label

        def get_child(self):
            return self.children

        def add(self, node):
            if isinstance(self.value, list):
                self.value.append(node.get_value())
            else:
                self.value = [self.get_value()]
                self.value.append(node.get_value())

            return self.children

        def convert(self):
            if self.children:
                return {'value': self.value, 'label': self.label, 'children': [i.convert() for i in self.children]}
            else:
                return {'value': self.value, 'label': self.label}

    class Tree:
        def __init__(self, node=Node('', 'root')):
            self.head = node

        def insert(self, node_list):
            cur = self.head.children

            for node in node_list:
                if cur:
                    flag = True
                    for i in cur:
                        if i.get_label() == node.get_label():
                            cur = i.add(node)
                            flag = False
                            break
                    if flag:
                        cur.append(node)
                        cur = node.get_child()
                else:
                    cur.append(node)
                    cur = node.get_child()

        def convert(self):
            return self.head.convert()

    result = zapi.hostgroup.get(output=['groupid', 'name'], monitored_hosts='true', search={'name': 'Zabbix servers'},
                                excludeSearch='true')

    print(result)
    temp = []
    # for i in result:
    #     temp.append(i['groupid'])
    #     i['name'] = i['name'].split('/')
    # any_group = Node(temp.copy(), '所有')
    #
    # tree = Tree()
    #
    # tree.insert([any_group])
    #
    # for item in result:
    #     node_list = []
    #     for name in item['name']:
    #         node_list.append(Node(item['groupid'], name))
    #     tree.insert(node_list)

    # response = {
    #     'hostgroup': tree.convert()['children']}

    response = []
    return jsonify(response)


@blueprint.route('/network', methods=['POST'])
def get_host():
    result = zapi.host.get(
        output=['snmp_available', 'name', 'status'],
        selectInterfaces=['ip', 'main', 'type'],
        selectInventory=['vendor', 'model', 'type', 'tag'])
    respone = {'host': result}

    return jsonify(respone)
