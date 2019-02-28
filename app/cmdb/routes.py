from flask import jsonify
from app.zabbix import zapi
from app.cmdb import blueprint


@blueprint.route('/network', methods=['GET', 'POST'])
def testing():
    result = zapi.hostgroup.get(output=['name'], real_hosts='true')
    hostgroup = []
    temp = []
    list = []

    for i in result:
        temp.append(i['groupid'])
        i['name'] = i['name'].split('/')
    hostgroup.append({'value': temp.copy(), 'lable': '所有'})
    temp.clear()

    key = result[1]['name'][0]
    for i in result[1:]:
        if key == i['name'][0]:
            temp.append(i['groupid'])
        else:
            list.append(i)
    hostgroup.append({'value': temp.copy(), 'lable': ''})

    print(hostgroup)

    response = {
        'hostgroup': [{'value': '1', 'label': 'A'}, {'value': '2', 'label': 'B', 'children': []}]}

    return jsonify(response)
