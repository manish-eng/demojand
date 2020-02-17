from django.shortcuts import render
from .forms import ChangeConfigForm
import subprocess
import os
from gitpull.models import SSHauth
from django.http import HttpResponse

def replace(request):
    form = ChangeConfigForm()
    subprocess.call("awk 'NR==FNR{print; n=NR; next} {if(FNR > n) print}' /var/lib/digivalet/digivalet-config/app-config_autobkp /var/lib/digivalet/digivalet-config/app-config.json > app-config-diff.json  && cp /var/lib/digivalet/digivalet-config/digiutils/pms/app-config-diff.json /var/lib/digivalet/digivalet-config/app-config.json", shell=True)
    success="New app-config.json File Is Ready"
    return render(request,'changeconfig/changedash.html',{'success':success, 'form':form})

def no(request):
    form = ChangeConfigForm()
    subprocess.call("mv /var/lib/digivalet/digivalet-config/app-config_autobkp /var/lib/digivalet/digivalet-config/app-config.json", shell=True)
    ignore="app-config.json is not changed"
    return render(request,'changeconfig/changedash.html',{'form':form, 'ignore':ignore})


def changedash(request):
    form = ChangeConfigForm()
    return render(request,'changeconfig/changedash.html',{'form':form})

def app_file(request):
    server_IP = SSHauth.objects.values_list('server_ip',  flat=True)[0]
  # os.system(" sshpass -p '"+password+"' scp -P42111 -o 'StrictHostKeyChecking no' "+username+"@"+server_IP+":/var/lib/digivalet/digivalet-config/dgjava /var/lib/digivalet/digiutils_new/pms/pms/")
    os.system("scp -P42111 -o 'StrictHostKeyChecking no' -i /var/lib/digivalet/digiutils_new/pms/key update-manager@"+server_IP+":/var/lib/digivalet/digivalet-config/app-config.json /var/lib/digivalet/digiutils_new/pms/changeconfig/")
    f = open('/var/lib/digivalet/digiutils_new/pms/changeconfig/app-config.json', 'r')
    file_content2 = f.read()
    f.close()
    os.system(" rm /var/lib/digivalet/digiutils_new/pms/changeconfig/app-config.json")
    return HttpResponse(file_content2, content_type="text/plain", )

def diff_show(request):
    if request.method == 'POST':
        form = ChangeConfigForm(request.POST)
        if form.is_valid():
            USER = form.cleaned_data['username']
            PASSWORD = form.cleaned_data['password']
            fqdn = form.cleaned_data['site_fqdn']
            hotelId = form.cleaned_data['hotel_id']
            subprocess.call("cp -r /var/lib/digivalet/digivalet-config/app-config.json /var/lib/digivalet/digivalet-config/app-config_autobkp", shell=True)
            resp=subprocess.call("php /var/lib/digivalet/digivalet-config/digiutils/pms/scripts/create-app-config.php --git-user="+USER+" --git-password="+PASSWORD+" --env=qa --mds-server-fqdn=mds"+fqdn+" --oneauth-server-fqdn=das"+fqdn+" --dvs-server-fqdn=dvs"+fqdn+" --inpremise-his-server-fqdn=his"+fqdn+" --cloud-his-server-fqdn=his"+fqdn+" --butler-his-server-fqdn=butler"+fqdn+" --digisteward-folder-name=digisteward --digisteward-his-server-fqdn=his"+fqdn+" --analytics-his-server-fqdn=analytics"+fqdn+" --analytics-his-server-username=admin --analytics-his-server-password=adminadmin --jasper-his-server-fqdn=analytics"+fqdn+" --report-name=Digivalet_Reports --report-directory=DigiValet --hotelId="+hotelId+" ", shell=True)
            if(resp==0):
                subprocess.call("diff -a --suppress-common-lines -y /var/lib/digivalet/digivalet-config/app-config.json /var/lib/digivalet/digivalet-config/app-config_autobkp > /var/lib/digivalet/digivalet-config/diff.csv", shell=True)
                f = open('/var/lib/digivalet/digivalet-config/diff.csv', 'r')
                file_content1 = f.read()
                f.close()
                return render(request,'changeconfig/diff_show.html',{'file_content1':file_content1})
            else:
                mess="Something Went Wrong !!! "
                return render(request,'changeconfig/changedash.html',{'mess':mess,'form':form})
        else:
            form = ChangeConfigForm()
            return render(request, "changeconfig/diff_show.html", {})
    else:
        form = ChangeConfigForm()
        return render(request, "changeconfig/diff_show.html", {})
