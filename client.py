import requests
from requests.auth import HTTPProxyAuth

def getClient(address):
   proxies = {"http":"trend3.sbab.ad:8080"}
   auth = HTTPProxyAuth("icor", "passwd")
   resp = requests.get(address, proxies=proxies, auth=auth)
   
   if resp.status_code != 200:
      # This means something went wrong.
      raise Exception('GET localhost {}'.format(resp))
   print(resp)


if __name__=='__main__':
   getClient('http://localhost')
