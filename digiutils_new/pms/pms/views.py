from django.shortcuts import render 
import subprocess, os,sys 
from django.core.validators import validate_ipv46_address
from .forms import PostForm
from gitpull.models import SSHauth
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required




def inputip(request):
  username = SSHauth.objects.values_list('username',  flat=True)[0]
  password = SSHauth.objects.values_list('password',  flat=True)[0]
  server_IP = SSHauth.objects.values_list('server_ip',  flat=True)[0]
  os.system(" sshpass -p "+password+" ssh -p42111 -o 'StrictHostKeyChecking no' "+username+"@"+server_IP+" 'grep '^PMS_SERVER=' /var/lib/digivalet/digivalet-config/dgjava | cut -d '=' -f 2- >> /tmp/ip.txt' ") 
  os.system(" sshpass -p '"+password+"' scp -P42111 -o 'StrictHostKeyChecking no' "+username+"@"+server_IP+":/tmp/ip.txt /var/lib/digivalet/digiutils_new/pms/pms/")
  os.system(" sshpass -p "+password+" ssh -p42111 -o 'StrictHostKeyChecking no' "+username+"@"+server_IP+" 'rm -rf /tmp/ip.txt' ")
  f = open('/var/lib/digivalet/digiutils_new/pms/pms/ip.txt', 'r')
  var = f.read()
  f.close()
  os.system("rm /var/lib/digivalet/digiutils_new/pms/pms/ip.txt")
  form = PostForm() 
  return render(request, 'pms/index.html',{'form':form,'var':var})

def dg_file(request):
  username = SSHauth.objects.values_list('username',  flat=True)[0]
  password = SSHauth.objects.values_list('password',  flat=True)[0]
  server_IP = SSHauth.objects.values_list('server_ip',  flat=True)[0]
  os.system(" sshpass -p '"+password+"' scp -P42111 -o 'StrictHostKeyChecking no' "+username+"@"+server_IP+":/var/lib/digivalet/digivalet-config/dgjava /var/lib/digivalet/digiutils_new/pms/pms/")
  f = open('/var/lib/digivalet/digiutils_new/pms/pms/dgjava', 'r')
  file_content2 = f.read()
  f.close()
  os.system(" rm /var/lib/digivalet/digiutils_new/pms/pms/dgjava ")
  return HttpResponse(file_content2, content_type="text/plain", )


def script(request):
  if request.method == 'POST':
    username = SSHauth.objects.values_list('username',  flat=True)[0]
    password = SSHauth.objects.values_list('password',  flat=True)[0]
    server_IP = SSHauth.objects.values_list('server_ip',  flat=True)[0]
    form = PostForm(request.POST)
    if form.is_valid():
      pmsServerIp = form.cleaned_data['your_IP']
      os.system("echo "+pmsServerIp+" >> /tmp/inputip.txt")
      os.system(" sshpass -p '"+password+"' scp -P 42111 -o 'StrictHostKeyChecking no' /tmp/inputip.txt "+username+"@"+server_IP+":/tmp ")
      try:
        os.system(" sshpass -p "+password+" ssh -p42111 -o 'StrictHostKeyChecking no' "+username+"@"+server_IP+" 'inputip=`sed -n '1p' /tmp/inputip.txt` && sed -i 's/PMS_SERVER=.*/PMS_SERVER='$inputip'/' /var/lib/digivalet/digivalet-config/dgjava && systemctl stop digivalet-pmsi && systemctl start digivalet-pmsi' ")
        os.system(" sshpass -p "+password+" ssh -p42111 -o 'StrictHostKeyChecking no' "+username+"@"+server_IP+" 'grep '^PMS_SERVER=' /var/lib/digivalet/digivalet-config/dgjava | cut -d '=' -f 2- >> /tmp/ip.txt' ")
        os.system(" sshpass -p '"+password+"' scp -P42111 -o 'StrictHostKeyChecking no' "+username+"@"+server_IP+":/tmp/ip.txt /var/lib/digivalet/digiutils_new/pms/pms/")
      except Exception as ex:
        errmsg="Somthing Went Wrong"
        form = PostForm() 
        return render(request, 'pms/index.html',{'form':form,'errmsg':errmsg})
      os.system(" sshpass -p '"+password+"' scp -P42111 -o 'StrictHostKeyChecking no' "+username+"@"+server_IP+":/tmp/ip.txt /var/lib/digivalet/digiutils_new/pms/pms/")
      os.system(" sshpass -p "+password+" ssh -p42111 -o 'StrictHostKeyChecking no' "+username+"@"+server_IP+" 'rm -rf /tmp/inputip.txt /tmp/ip.txt' ")
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
      
      
      
      # var=subprocess.check_output("grep '^PMS_SERVER=' /var/lib/digivalet/digivalet-config/dgjava | cut -d '=' -f 2- ",shell=True)
      # var=var.decode('utf-8')
      # try:
      #   validate_ipv46_address(PmsServerIp)
      # except Exception as ex:
      #   errmsg="Please Enter Valid IP"
      #   form = PostForm() 
      #   return render(request, 'pms/index.html',{'form':form,'errmsg':errmsg})
      # cmd="sed -i 's/PMS_SERVER=.*/PMS_SERVER="+PmsServerIp+"/' /var/lib/digivalet/digivalet-config/dgjava"
      # response = os.system(cmd)
      # if response == 0:
      #   print("inside block")
      #   output = subprocess.check_output("systemctl stop digivalet-pmsi",shell = True)
      #   output = subprocess.check_output("systemctl start digivalet-pmsi",shell = True)
        # msg="IP changed Successfully and Services Restarted"
        # return render(request, 'pms/index.html',{'form':form, 'msg':msg, 'var':var})

 
  
