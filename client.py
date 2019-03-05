import requests
from requests.auth import HTTPProxyAuth

def getClient(address):
   resp = requests.get(address)
   
   if resp.status_code != 200:
      # This means something went wrong.
      raise Exception('GET localhost {}'.format(resp))
   print resp


if __name__=='__main__':
   getClient('http://0.0.0.0/gettasks')
