from flask import jsonify,json
from app.zabbix import zapi
from app.cmdb import blueprint


@blueprint.route('/network', methods=['GET', 'POST'])
def testing():
    r = zapi.hostgroup.get(output=['name'], real_hosts='true')
    groupList = []
    temp = []
    for i in r:
        temp.append(i['groupid'])
    groupList.append({'value': temp, 'lable': '所有'})
    print(groupList)
    # r = zapi.host.get(output=['host'], groupids=['30', '16'])
    # print(r)
    response = json.dumps(groupList)
    print(response)
    return jsonify(response)
