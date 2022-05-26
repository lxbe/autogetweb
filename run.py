try:
    import requests
except Exception as e:
    print(str(e) + "缺少requests模块")
#
def ggg():
	url = "https://usvm.coco88.tk"
	headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'
	}
	res = requests.get(url=url, headers=headers)
	print("连接状态:" + str(res.status_code))
ggg()
