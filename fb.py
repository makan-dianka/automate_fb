import facebook as fb
import os

token = os.environ.get('fb_token')
grp_id = os.environ.get('grp_id')

res = fb.GraphAPI(token)
grp = res.get_object(grp_id)

print(grp.get('name'))