from django.shortcuts import render
import subprocess
import os
from django.http import HttpResponse

def server_verify(request):
    os.system("sh /var/lib/digivalet/digivalet-config/digiutils/pms/scripts/Server_verification.sh")
    os.system("cat server_verify.txt? >> server_verify.txt")
    os.system("cp server_verify.txt? server_verify.txt")
    f = open('/var/lib/digivalet/digivalet-config/digiutils/pms/server_verify.txt', 'r')
    file_content2 = f.read()
    f.close()
    os.system("rm server_verify.txt? server_verify.txt")
    context = {'file_content2': file_content2}
    # return HttpResponse(file_content2, content_type="text/plain", )
    return render(request, 'serververify/server_verify.html', context)
