from django.shortcuts import render
import subprocess
import os
from .forms import VersionForm
from gitpull.models import SSHauth
from django.http import HttpResponse
  

def softwares_versions_view(request):
    form=VersionForm()
    return render(request, 'softwaresversions/version.html',{'form':form})


# def softwares_versions(request):
#     username = SSHauth.objects.values_list('username',  flat=True)[0]
#     password = SSHauth.objects.values_list('password',  flat=True)[0]
#     server_IP = SSHauth.objects.values_list('server_ip',  flat=True)[0]
#     os.system(" sshpass -p '"+password+"' scp -P 42111 -o 'StrictHostKeyChecking no' /var/lib/digivalet/digiutils_new/pms/scripts/softwares_versions.sh "+username+"@"+server_IP+":/tmp ")
#     os.system(" sshpass -p "+password+" ssh -p42111 -o 'StrictHostKeyChecking no' "+username+"@"+server_IP+" 'sh /tmp/softwares_versions.sh' ")
#     os.system(" sshpass -p '"+password+"' scp -P42111 -o 'StrictHostKeyChecking no' "+username+"@"+server_IP+":/tmp/final_output.txt /var/lib/digivalet/digiutils_new/pms/final_output.txt")
#     os.system(" sshpass -p "+password+" ssh -p42111 -o 'StrictHostKeyChecking no' "+username+"@"+server_IP+" 'rm -rf /tmp/final_output.txt /tmp/softwares_versions.sh' ")
#     f = open('/var/lib/digivalet/digiutils_new/pms/final_output.txt', 'r')
#     file_content = f.read()
#     f.close()
#     os.system("rm -rf /var/lib/digivalet/digiutils_new/pms/final_output.txt")
#     context = {'file_content': file_content}
#     # return render(request, 'softwaresversions/status_display.html', context)
#     return HttpResponse(file_content, content_type="text/plain", )



def softwares_versions(request):
    username = SSHauth.objects.values_list('username',  flat=True)[0]
    password = SSHauth.objects.values_list('password',  flat=True)[0]
    server_IP = SSHauth.objects.values_list('server_ip',  flat=True)[0]
    if request.POST:
        form = VersionForm(request.POST)
        if form.is_valid():
            if '_all' in request.POST:
                os.system(" sshpass -p '"+password+"' scp -P 42111 -o 'StrictHostKeyChecking no' /var/lib/digivalet/digiutils_new/pms/scripts/softwares_versions.sh "+username+"@"+server_IP+":/tmp ")
                os.system(" sshpass -p "+password+" ssh -p42111 -o 'StrictHostKeyChecking no' "+username+"@"+server_IP+" 'sh /tmp/softwares_versions.sh' ")
                os.system(" sshpass -p '"+password+"' scp -P42111 -o 'StrictHostKeyChecking no' "+username+"@"+server_IP+":/tmp/final_output.txt /var/lib/digivalet/digiutils_new/pms/final_output.txt")
                os.system(" sshpass -p "+password+" ssh -p42111 -o 'StrictHostKeyChecking no' "+username+"@"+server_IP+" 'rm -rf /tmp/final_output.txt /tmp/softwares_versions.sh' ")
                f = open('/var/lib/digivalet/digiutils_new/pms/final_output.txt', 'r')
                file_content = f.read()
                f.close()
                os.system("rm -rf /var/lib/digivalet/digiutils_new/pms/final_output.txt")
                context = {'file_content': file_content}
                return HttpResponse(file_content, content_type="text/plain", )
            elif '_single':
                select_software = form.cleaned_data['select_software']
                print(select_software)
                subprocess.call(['bash', '/var/lib/digivalet/digiutils_new/pms/scripts/software_tmp.sh', str(select_software)])
                os.system(" sshpass -p '"+password+"' scp -P 42111 -o 'StrictHostKeyChecking no' /var/lib/digivalet/digiutils_new/pms/scripts/single_soft_ver.sh /var/lib/digivalet/digiutils_new/pms/version.txt "+username+"@"+server_IP+":/tmp ")
                os.system("rm -rf /var/lib/digivalet/digiutils_new/pms/version.txt")
                os.system(" sshpass -p "+password+" ssh -p42111 -o 'StrictHostKeyChecking no' "+username+"@"+server_IP+" 'var=`sed -n '1p' /tmp/version.txt` && sh /tmp/single_soft_ver.sh $var' ")
                os.system(" sshpass -p '"+password+"' scp -P42111 -o 'StrictHostKeyChecking no' "+username+"@"+server_IP+":/tmp/soft_ver.txt /var/lib/digivalet/digiutils_new/pms/softwaresversions/")
                os.system(" sshpass -p "+password+" ssh -p42111 -o 'StrictHostKeyChecking no' "+username+"@"+server_IP+" 'rm -rf /tmp/single_soft_ver.sh /tmp/soft_ver.txt /tmp/version.txt' ")
                f = open('/var/lib/digivalet/digiutils_new/pms/softwaresversions/soft_ver.txt', 'r')
                file_content2 = f.read()
                f.close()
                os.system("rm -rf /var/lib/digivalet/digiutils_new/pms/softwaresversions/soft_ver.txt")
                return render(request,'softwaresversions/version.html',{'form':form,'file_content2': file_content2})
