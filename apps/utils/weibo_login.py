# -*- coding:UTF-8 -*-

def get_auth_url():
    weibo_auth_url = 'https://api.weibo.com/oauth2/authorize'
    redirect_url = 'http://127.0.0.1:8000/complete/weibo/'
    auth_url = weibo_auth_url+'?client_id={client_id}&redirect_uri={re_url}'.format(client_id=2113796513,re_url=redirect_url)
    print(auth_url)



def get_access_token(code='3ad8eb8a3595bf17f95eba158ae61b1f'):
    access_token_url = 'https://api.weibo.com/oauth2/access_token'
    import requests
    re_dict = requests.post(access_token_url,data={
        'client_id':2113796513,
        'client_secret':'9292dde7cc66450d7bc1a933fc800e88',
        'grant_type':'authorization_code',
        'code':code,
        'redirect_uri':'http://127.0.0.1:8000/complete/weibo/',
    })
    # '{"access_token":"2.00hgflGGJCRD_C4cefc7b386kFrOTC","remind_in":"157679998","expires_in":157679998,"uid":"5596816675","isRealName":"true"}'
    pass

def get_user_info(access_token='',uid=''):
    user_url = 'https://api.weibo.com/2/users/show/json?access_token={token}&uid={uid}'.format(token=access_token,uid=uid)
    print(user_url)

if __name__ == '__main__':
    # get_auth_url()
    # get_access_token(code='3ad8eb8a3595bf17f95eba158ae61b1f')
    get_user_info(access_token="2.00hgflGGJCRD_C4cefc7b386kFrOTC",uid="5596816675")
