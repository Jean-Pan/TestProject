from flask import jsonify
# from app.zabbix import zapi
from app.cmdb import blueprint


@blueprint.route('/network', methods=['GET', 'POST'])
def testing():
    # r = zapi.hostgroup.get(output=['name'], real_hosts='true')
    # groupList = []
    # temp = []
    # for i in r:
    #     temp.append(i['groupid'])
    # groupList.append({'value': temp, 'lable': '所有'})
    # r = zapi.host.get(output=['host'], groupids=['30', '16'])
    # print(r)
    response = {'hostgroup': [{value: '1', label: 'A', 'children': []}]}

    return jsonify(response)
