from django.http import JsonResponse 
from django.views.decorators.http import require_POST 
from django.views.decorators.csrf import csrf_exempt
import subprocess
from subprocess import call
import crypt

from bch_vpn.models import *
import json

#import logging
#logger = logging.getLogger(__name__)
#logger.setLevel(logging.DEBUG)     
#handler = logging.FileHandler('/tmp/api.log') 
#handler.setLevel(logging.DEBUG)
#formatter = logging.Formatter( 
#    '%(asctime)s - %(name)s - %(levelname)s - %(lineno)d  - %(message)s')
#handler.setFormatter(formatter)
#logger.addHandler(handler)
#
#logger = logging.getLogger(__name__)
#logger.setLevel(logging.DEBUG)

#def dump_req(req_dict):
#    req = json.loads(req_dict)
#    fh = open('/tmp/req_1', 'w')
#    fh.write(req)
#    fh.close()
#    return

@require_POST
@csrf_exempt
def add(request):
    req = json.loads(request.body.decode("utf-8"))
    d = json.loads(req['payment']['buttonData'])
    user = d['user']
    password = d['pass']
    passcrypt = crypt.crypt(password)
    #must run as root
    p = subprocess.call(['/usr/sbin/useradd', '-d/dev/null', '-M', '-N','-s/bin/false', '-p' + passcrypt, user])
    #p = subprocess.Popen(executable='/usr/sbin/useradd', args=('-d /dev/null -M -N -s /bin/false -p' + passcrypt))
    #dump_req(req)
    #logger.debug("ran process", p)
    return JsonResponse(req)
