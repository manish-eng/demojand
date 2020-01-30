from django.shortcuts import render
from .forms import AuthForm
from gitpull.models import SSHauth
import subprocess,os


def service_status_auth_view(request):
    form = AuthForm()
    return render (request, 'servicestatus/service_status_auth_view.html',{'form':form})


# def service_status_view(request):
#     return render (request, 'servicestatus/service_status_view.html',{'form':form})

def service_status(request):
    username = SSHauth.objects.values_list('username',  flat=True)[0]
    password = SSHauth.objects.values_list('password',  flat=True)[0]
    server_IP = SSHauth.objects.values_list('server_ip',  flat=True)[0]
    if request.POST:
        form = AuthForm(request.POST)
        if form.is_valid():
            select_service = form.cleaned_data['select_service']
            print(select_service)
            if '_status' in request.POST:
                subprocess.call(['bash', '/var/lib/digivalet/digiutils_new/pms/scripts/service_status_tmp.sh', str(select_service)])
                os.system(" sshpass -p '"+password+"' scp -P 42111 -o 'StrictHostKeyChecking no' /var/lib/digivalet/digiutils_new/pms/scripts/service_status.sh /var/lib/digivalet/digiutils_new/pms/file.txt "+username+"@"+server_IP+":/tmp ")
                os.system("rm -rf /var/lib/digivalet/digiutils_new/pms/file.txt")
                os.system(" sshpass -p "+password+" ssh -p42111 -o 'StrictHostKeyChecking no' "+username+"@"+server_IP+" 'var=`sed -n '1p' /tmp/file.txt` && sh /tmp/service_status.sh $var' ")
                os.system(" sshpass -p '"+password+"' scp -P42111 -o 'StrictHostKeyChecking no' "+username+"@"+server_IP+":/tmp/service_status.txt /var/lib/digivalet/digiutils_new/pms/servicestatus/")
                os.system(" sshpass -p "+password+" ssh -p42111 -o 'StrictHostKeyChecking no' "+username+"@"+server_IP+" 'rm -rf /tmp/service_status.* /tmp/file.txt' ")
                f = open('/var/lib/digivalet/digiutils_new/pms/servicestatus/service_status.txt', 'r')
                file_content1 = f.read()
                f.close()
                os.system("rm -rf /var/lib/digivalet/digiutils_new/pms/servicestatus/service_status.txt")
                return render(request,'servicestatus/service_status_auth_view.html',{'form':form,'file_content1': file_content1})
            elif '_restart':
                select_service = form.cleaned_data['select_service']
                subprocess.call(['bash', '/var/lib/digivalet/digiutils_new/pms/scripts/service_status_tmp.sh', str(select_service)])
                os.system(" sshpass -p '"+password+"' scp -P 42111 -o 'StrictHostKeyChecking no' /var/lib/digivalet/digiutils_new/pms/scripts/service_restart.sh /var/lib/digivalet/digiutils_new/pms/file.txt "+username+"@"+server_IP+":/tmp ")
                os.system("rm -rf /var/lib/digivalet/digiutils_new/pms/file.txt")
                os.system(" sshpass -p "+password+" ssh -p42111 -o 'StrictHostKeyChecking no' "+username+"@"+server_IP+" 'var=`sed -n '1p' /tmp/file.txt` && sh /tmp/service_restart.sh $var' ")
                os.system(" sshpass -p '"+password+"' scp -P42111 -o 'StrictHostKeyChecking no' "+username+"@"+server_IP+":/tmp/service_restart.txt /var/lib/digivalet/digiutils_new/pms/servicestatus/")
                os.system(" sshpass -p "+password+" ssh -p42111 -o 'StrictHostKeyChecking no' "+username+"@"+server_IP+" 'rm -rf /tmp/service_restart.* /tmp/file.txt' ")
                f = open('/var/lib/digivalet/digiutils_new/pms/servicestatus/service_restart.txt', 'r')
                file_content2 = f.read()
                f.close()
                os.system("rm -rf /var/lib/digivalet/digiutils_new/pms/servicestatus/service_restart.txt")
                return render(request,'servicestatus/service_status_auth_view.html',{'form':form,'file_content2': file_content2},{'form':form})
