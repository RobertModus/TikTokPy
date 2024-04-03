from tiktokapipy.api import TikTokAPI

username = 'deen_akademie'
with TikTokAPI(navigation_retries=2, navigation_timeout=10) as api:
  u = api.user(username)
  for v in u.videos:
    print(v)

print(u)