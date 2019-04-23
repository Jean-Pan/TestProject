from flask import jsonify
from app.zabbix import zapi
from app.cmdb import blueprint


@blueprint.route('/network', methods=['GET'])
def get_hostgroup_list():
    # 创建一个节点类
    class Node:
        def __init__(self, value, label):
            self.value = [value]
            self.label = label
            self.child = []

        # 添加数值和子树
        def add_value(self, node):
            self.value.append(node.value[0])

        def add_child(self, node):
            self.child.append(node)

        def convert(self):
            if self.child:
                return {'value': self.value, 'label': self.label, 'children': [i.convert() for i in self.child]}
            else:
                return {'value': self.value, 'label': self.label}

    # 创建一个多叉树
    class Tree:
        #
        def __init__(self, node=Node('', '')):
            self.head = node

        def search(self):
            for i in self.head.get_child():
                pass

        def insert(self, node_list):
            current = self.head

            for node in node_list:
                if current.child:
                    match = False
                    for cur in current.child:
                        if cur.label == node.label:
                            cur.add_value(node)
                            current = cur
                            match = True
                            break
                    if not match:
                        current.add_child(node)
                        current = node
                else:
                    current.add_child(node)
                    current = node

        def get_root(self):
            return self.head

    result = zapi.hostgroup.get(output=['groupid', 'name'], monitored_hosts='true', search={'name': 'Zabbix servers'},
                                excludeSearch='true')

    # 获取所有的节点
    temp = []
    for i in result:
        temp.append(i['groupid'])
        i['name'] = i['name'].split('/')
    all_group = Node(temp.copy(), '所有')

    # 创建树添加所有节点
    tree = Tree()
    tree.insert([all_group])

    # 添加子树的列
    for i in result:
        node_list = []
        for name in i['name']:
            node_list.append(Node(i['groupid'], name))
        tree.insert(node_list)

    response = {
        'hostgroup': tree.get_root().convert()['children']}
    print(response)
    return jsonify(response)


@blueprint.route('/network', methods=['POST'])
def get_host():
    result = zapi.host.get(
        output=['snmp_available', 'name', 'status'],
        selectInterfaces=['ip', 'main', 'type'],
        selectInventory=['vendor', 'model', 'type', 'tag'])
    respone = {'host': result}

    return jsonify(respone)
