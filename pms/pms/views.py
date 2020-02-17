from django.shortcuts import render 
import subprocess, os,sys 
from django.core.validators import validate_ipv46_address
from .forms import PostForm
from gitpull.models import SSHauth
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required



@login_required
def inputip(request):
  server_IP = request.session['server_ip']
  os.system("ssh -i /var/lib/digivalet/digiutils_new/pms/key -p42111 -o 'StrictHostKeyChecking no' update-manager@"+server_IP+" 'grep '^PMS_SERVER=' /var/lib/digivalet/digivalet-config/dgjava | cut -d '=' -f 2- >> /tmp/ip.txt' ")
  os.system("scp -P42111 -o 'StrictHostKeyChecking no' -i /var/lib/digivalet/digiutils_new/pms/key update-manager@"+server_IP+":/tmp/ip.txt /var/lib/digivalet/digiutils_new/pms/pms/ ")
  os.system("ssh -i /var/lib/digivalet/digiutils_new/pms/key -p42111 -o 'StrictHostKeyChecking no' update-manager@"+server_IP+" 'rm -rf /tmp/ip.txt' ")
  f = open('/var/lib/digivalet/digiutils_new/pms/pms/ip.txt', 'r')
  var = f.read()
  f.close()
  os.system("rm /var/lib/digivalet/digiutils_new/pms/pms/ip.txt")
  form = PostForm() 
  return render(request, 'pms/index.html',{'form':form,'var':var})


@login_required
def dg_file(request):
  server_IP = request.session['server_ip']
  os.system("scp -P42111 -o 'StrictHostKeyChecking no' -i /var/lib/digivalet/digiutils_new/pms/key update-manager@"+server_IP+":/var/lib/digivalet/digivalet-config/dgjava /var/lib/digivalet/digiutils_new/pms/pms/")
  f = open('/var/lib/digivalet/digiutils_new/pms/pms/dgjava', 'r')
  file_content2 = f.read()
  f.close()
  os.system(" rm /var/lib/digivalet/digiutils_new/pms/pms/dgjava ")
  return HttpResponse(file_content2, content_type="text/plain", )

@login_required
def script(request):
  if request.method == 'POST':
    server_IP = request.session['server_ip']
    form = PostForm(request.POST)
    if form.is_valid():
      pmsServerIp = form.cleaned_data['your_IP']
      request.session['your_IP'] = form.cleaned_data['your_IP']
      print(your_IP)
      os.system("echo "+pmsServerIp+" >> /tmp/inputip.txt")
      os.system("scp -P 42111 -o 'StrictHostKeyChecking no' -i /var/lib/digivalet/digiutils_new/pms/key /tmp/inputip.txt update-manager@"+server_IP+":/tmp")
      try:
        os.system("ssh -i /var/lib/digivalet/digiutils_new/pms/key -p42111 -o 'StrictHostKeyChecking no' update-manager@"+server_IP+" 'inputip=`sed -n '1p' /tmp/inputip.txt` && sed -i 's/PMS_SERVER=.*/PMS_SERVER='$inputip'/' /var/lib/digivalet/digivalet-config/dgjava && systemctl stop digivalet-pmsi && systemctl start digivalet-pmsi' ")
        os.system("ssh -i /var/lib/digivalet/digiutils_new/pms/key -p42111 -o 'StrictHostKeyChecking no' update-manager@"+server_IP+" 'grep '^PMS_SERVER=' /var/lib/digivalet/digivalet-config/dgjava | cut -d '=' -f 2- >> /tmp/ip.txt' ")
        os.system("scp -P42111 -o 'StrictHostKeyChecking no' -i /var/lib/digivalet/digiutils_new/pms/key update-manager@"+server_IP+":/tmp/ip.txt /var/lib/digivalet/digiutils_new/pms/pms/")
      except Exception as ex:
        errmsg="Somthing Went Wrong"
        form = PostForm() 
        return render(request, 'pms/index.html',{'form':form,'errmsg':errmsg})
      os.system("ssh -i /var/lib/digivalet/digiutils_new/pms/key -p42111 -o 'StrictHostKeyChecking no' update-manager@"+server_IP+" 'rm -rf /tmp/inputip.txt /tmp/ip.txt' ")
      f = open('/var/lib/digivalet/digiutils_new/pms/pms/ip.txt', 'r')
      var = f.read()
      f.close()
      os.system("rm /var/lib/digivalet/digiutils_new/pms/pms/ip.txt")
      msg="IP changed Successfully and Services Restarted"
      return render(request, 'pms/index.html',{'form':form, 'msg':msg, 'var':var})
    else:
      form = PostForm()
      errmsg="Something Went Wrong"
      return render(request, 'pms/index.html', {'errmsg':errmsg, 'form':form}) 
  else:
    form = PostForm()
    return render(request, 'pms/index.html', {'form':form}) 
      