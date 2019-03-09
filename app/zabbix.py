from pyzabbix import ZabbixAPI, ZabbixAPIException

# 定义URL及账户密码
zabbix_server = 'http://10.167.10.234/zabbix/api_jsonrpc.php'
# zabbix_server = 'http://192.168.100.234/zabbix/api_jsonrpc.php'
headers = {'Content-Type': 'application/json-rpc'}
username = 'Admin'
password = 'zabbix'

zapi = ZabbixAPI(zabbix_server)
zapi.login(username, password)
