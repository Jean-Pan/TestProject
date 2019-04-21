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
            self.parent = None

        # 添加数值和子树
        def add_child(self, node):
            self.value.appen(node.value[0])
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
                    flag = True
                    for cur in current.child:
                        if cur.label == node.label:
                            cur.add_children(node)
                            current=cur
                            flag = False
                            break
                    if flag:
                        cur.append(node)
                        cur = node.get_child()
                else:
                    current.add_child(node)

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
