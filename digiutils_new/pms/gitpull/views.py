from django.shortcuts import render
from .forms import GitPullForm,SSHForm
from .models import SSHauth
import subprocess
import os
from django.http import HttpResponse, HttpResponseNotFound, Http404,  HttpResponseRedirect




def dashboard(request):
    return render(request,'gitpull/dashboard.html')

def ssh_dashboard(request):
    count = SSHauth.objects.all().count()
    print(count)
    if (count == 0):
        if request.method == 'POST':
            form = SSHForm(request.POST)
            if form.is_valid():
                USER = form.cleaned_data['username']
                PASSWORD = form.cleaned_data['password']
                IP = form.cleaned_data['server_ip']
                print(IP)
                form.save()
                try:
                    resp = os.system("sshpass -p "+PASSWORD+" ssh -p42111 -o 'StrictHostKeyChecking no' "+USER+"@"+IP+" 'exit' ")
                    if (resp == 0):
                        return HttpResponseRedirect("dashboard/")
                    else:
                        form = SSHForm() 
                        SSHauth.objects.all().delete()
                        msg = "Seomething went wrong try again !!"
                        return render(request,'gitpull/ssh_dashboard.html',{'form':form, 'msg':msg})
                except Exception as ex:
                    msg = "Seomething went wrong try again !!"
                    form = SSHForm()
                    SSHauth.objects.all().delete()
                    return render(request,'gitpull/ssh_dashboard.html',{'form':form, 'msg':msg})
            else:
                form = SSHForm()
                return render(request,'gitpull/ssh_dashboard.html',{'form':form})
        else:
            form = SSHForm()
            return render(request,'gitpull/ssh_dashboard.html',{'form':form})
    else:
        return render(request, 'gitpull/buzy.html')


def delete(request):
    form = SSHForm()
    SSHauth.objects.all().delete()
    return render(request,'gitpull/ssh_dashboard.html',{'form':form})   




def output(request):
    form = GitPullForm()
    return render(request,'gitpull/gitpull.html',{'form':form})



def pullutility(request):
    username = SSHauth.objects.values_list('username',  flat=True)[0]
    password = SSHauth.objects.values_list('password',  flat=True)[0]
    server_IP = SSHauth.objects.values_list('server_ip',  flat=True)[0]
    if request.method == 'POST':
        form = GitPullForm(request.POST)
        if form.is_valid():
            GIT_USER = form.cleaned_data['username']
            GIT_PASSWORD = form.cleaned_data['password']
            print(GIT_PASSWORD)
            try:
                os.system("echo "+GIT_USER+" >> /tmp/cred.txt && echo "+GIT_PASSWORD+" >> /tmp/cred.txt")
                os.system(" sshpass -p '"+password+"' scp -P 42111 -o 'StrictHostKeyChecking no' /tmp/cred.txt "+username+"@"+server_IP+":/tmp ")              
                os.system(" sshpass -p "+password+" ssh -p42111 -o 'StrictHostKeyChecking no' "+username+"@"+server_IP+" 'variable=`sed -n '7p' /var/www/html/dv5/.git/config | cut -d '/' -f 3-` &&  cd /var/www/html/dv5/ && user=`sed -n '1p' /tmp/cred.txt` && pass=`sed -n '2p' /tmp/cred.txt` && git pull --progress http://$user:$pass@$variable >> /tmp/git_status.txt' ")
                os.system(" sshpass -p '"+password+"' scp -P42111 -o 'StrictHostKeyChecking no' "+username+"@"+server_IP+":/tmp/git_status.txt /var/lib/digivalet/digiutils_new/pms/gitpull/")
                os.system(" sshpass -p "+password+" ssh -p42111 -o 'StrictHostKeyChecking no' "+username+"@"+server_IP+" 'rm -rf /tmp/cred.txt /tmp/git_status.txt' ")
                f = open('/var/lib/digivalet/digiutils_new/pms/gitpull/git_status.txt', 'r')
                file_content = f.read()
                f.close()
                os.system("rm /var/lib/digivalet/digiutils_new/pms/gitpull/git_status.txt")
                return render(request,'gitpull/gitpull.html',{'form':form,'file_content': file_content})
            except Exception as ex:
                msg="Something Went Wrong !!! "
                return render(request,'gitpull/gitpull.html',{'msg':msg})
    else:
        form = GitPullForm()
    return render(request, 'gitpull/gitpull.html', {'form': form})
