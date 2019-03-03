from flask import jsonify
from app.zabbix import zapi
from app.cmdb import blueprint


@blueprint.route('/network', methods=['GET', 'POST'])
def testing():
    class Node:
        def __init__(self, value, label):
            self.value = value
            self.label = label
            self.children = []

        # def __repr__(self):
        #     return {'value': self.value, 'label': self.label, 'children': self.children}

        # def __str__(self):
        #     return "{{'value': {}, 'label': {}, 'children': {}}}".format(self.value, self.label, self.children)
        def turn(self):
            return {'value': self.value, 'label': self.label, 'children': self.children}

        def getValue(self):
            return self.value

        def getLabel(self):
            return self.label

        def getChild(self):
            return self.children

        def next(self, node):
            if isinstance(self.value, str):
                self.value = [self.value].append(node.getValue())
            else:
                self.value = self.value.append(node.getValue())
            return self.children

    class Tree:
        def __init__(self, node):
            self.head = [node]

        # def __repr__(self):
        #     return self.head
        #
        # def __str__(self):
        #     return '{}'.format(self.head)

        def test(self):
            return [x.turn() for x in self.head]

        def insert(self, node_list):
            cur = self.head
            for node in node_list:
                if cur:
                    for x in cur:
                        print(1)
                        if x and node.getLabel() == x.getLabel():
                            print(2)
                            cur = x.next(node)
                        else:
                            print(3)
                            cur.append(node)
                            cur = node.getChild()
                            break
                else:
                    print(3)
                    cur.append(node)
                    cur = node.getChild()

    result = zapi.hostgroup.get(output=['name'], real_hosts='true')
    hostgroup = []
    temp = []

    for i in result:
        temp.append(i['groupid'])
        i['name'] = i['name'].split('/')
    root = Node(temp.copy(), '所有')
    temp.clear()

    tree = Tree(root)
    tree.insert([Node('a', 'test1'), Node('b', 'test2'), Node('c', 'test3')])
    print(tree.test())
    response = {
        'hostgroup': [{'value': '1', 'label': 'A'}, {'value': '2', 'label': 'B', 'children': []}]}

    return jsonify(response)
