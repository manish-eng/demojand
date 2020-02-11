cd /tmp/

echo $1 

if [ $1 == "dvs" ] 
then
    yum list installed | grep dvs.noarch >> demo.txt
    dashb=`cat demo.txt | awk '{print $2}'`
    rm -rf demo.txt
    echo $dashb >> demo.txt
    dashverb=`sed -e 's/\(.*\)-ga.el7.centos/\1/' demo.txt`
    rm -rf demo.txt
    (echo "dvs" ; echo $dashverb ; ) |tr '\n' '\t' >> soft_ver.txt
     
elif [ $1 == "dashboard" ]
then
    yum list installed | grep dashboard >> demo.txt
    dasha=`cat demo.txt | awk '{print $2}'`
    rm -rf demo.txt
    echo $dasha >> demo.txt
    dashvera=`sed -e 's/\(.*\)-ga.el7.centos/\1/' demo.txt`
    rm -rf demo.txt
    (echo "dashboard" ; echo $dashvera ; ) |tr '\n' '\t' >> soft_ver.txt
     
elif [ $1 == "oneauth.noarch" ]
then
    yum list installed | grep oneauth.noarch >> demo.txt
    dashc=`cat demo.txt | awk '{print $2}'`
    rm -rf demo.txt
    echo $dashc >> demo.txt
    dashverc=`sed -e 's/\(.*\)-ga.el7.centos/\1/' demo.txt`
    rm -rf demo.txt
    (echo "oneauth" ; echo $dashverc ; ) |tr '\n' '\t' >> soft_ver.txt
     
elif [ $1 == "push-manager" ]
then
    yum list installed | grep push-manager >> demo.txt
    dashd=`cat demo.txt | awk '{print $2}'`
    rm -rf demo.txt
    echo $dashd >> demo.txt
    dashverd=`sed -e 's/\(.*\)-ga.el7.centos/\1/' demo.txt`
    rm -rf demo.txt
    (echo "push-manager" ; echo $dashverd ; ) |tr '\n' '\t' >> soft_ver.txt
     
elif [ $1 == "system-monitor" ]
then
    yum list installed | grep system-monitor >> demo.txt
    dashe=`cat demo.txt | awk '{print $2}'`
    rm -rf demo.txt
    echo $dashe >> demo.txt
    dashvere=`sed -e 's/\(.*\)-ga.el7.centos/\1/' demo.txt`
    rm -rf demo.txt
    (echo "system-monitor" ; echo $dashvere ; ) |tr '\n' '\t' >> soft_ver.txt
     
elif [ $1 == "cms.noarch" ]
then
    yum list installed | grep cms.noarch >> demo.txt
    dashf=`cat demo.txt | awk '{print $2}'`
    rm -rf demo.txt
    echo $dashf >> demo.txt
    dashverf=`sed -e 's/\(.*\)-ga.el7.centos/\1/' demo.txt`
    rm -rf demo.txt
    (echo "cms" ; echo $dashverf ; ) |tr '\n' '\t' >> soft_ver.txt
     
elif [ $1 == "digivalet-api" ] 
then 
    yum list installed | grep digivalet-api >> demo.txt
    dashg=`cat demo.txt | awk '{print $2}'`
    rm -rf demo.txt
    echo $dashg >> demo.txt
    dashverg=`sed -e 's/\(.*\)-ga.el7.centos/\1/' demo.txt`
    rm -rf demo.txt
    (echo "digivalet-api" ; echo $dashverg ; ) |tr '\n' '\t' >> soft_ver.txt
     
elif [ $1 == "digivalet-cloud-api" ]
then
    yum list installed | grep digivalet-cloud-api >> demo.txt
    dashh=`cat demo.txt | awk '{print $2}'`
    rm -rf demo.txt
    echo $dashh >> demo.txt
    dashverh=`sed -e 's/\(.*\)-ga.el7.centos/\1/' demo.txt`
    rm -rf demo.txt
    (echo "digivalet-cloud-api" ; echo $dashverh ; ) |tr '\n' '\t' >> soft_ver.txt
     
elif [ $1 == "digivalet-pmsi" ]
then
    yum list installed | grep digivalet-pmsi >> demo.txt
    dashi=`cat demo.txt | awk '{print $2}'`
    rm -rf demo.txt
    echo $dashi >> demo.txt
    dashveri=`sed -e 's/\(.*\)-ga.el7.centos/\1/' demo.txt`
    rm -rf demo.txt
    (echo "digivalet-pmsi" ; echo $dashveri ; ) |tr '\n' '\t' >> soft_ver.txt
     
elif [ $1 == "digivalet-posi" ]
then
    yum list installed | grep digivalet-posi >> demo.txt
    dashj=`cat demo.txt | awk '{print $2}'`
    rm -rf demo.txt
    echo $dashj >> demo.txt
    dashverj=`sed -e 's/\(.*\)-ga.el7.centos/\1/' demo.txt`
    rm -rf demo.txt
    (echo "digivalet-posi" ; echo $dashverj ; ) |tr '\n' '\t' >> soft_ver.txt
     

elif [ $1 == "dv-services-api" ]
then
    yum list installed | grep dv-services-api >> demo.txt
    dashk=`cat demo.txt | awk '{print $2}'`
    rm -rf demo.txt
    echo $dashk >> demo.txt
    dashverk=`sed -e 's/\(.*\)-ga.el7.centos/\1/' demo.txt`
    rm -rf demo.txt
    (echo "dv-services-api" ; echo $dashverk ; ) |tr '\n' '\t' >> soft_ver.txt
     
elif [ $1 == "dv-services-cloud-api" ]
then
    yum list installed | grep dv-services-cloud-api >> demo.txt
    dashl=`cat demo.txt | awk '{print $2}'`
    rm -rf demo.txt
    echo $dashl >> demo.txt
    dashverl=`sed -e 's/\(.*\)-ga.el7.centos/\1/' demo.txt`
    rm -rf demo.txt
    (echo "dv-services-cloud-api" ; echo $dashverl ; ) |tr '\n' '\t' >> soft_ver.txt
     
elif [ $1 == "gateway-services" ]
then
    yum list installed | grep gateway-services >> demo.txt
    dashm=`cat demo.txt | awk '{print $2}'`
    rm -rf demo.txt
    echo $dashm >> demo.txt
    dashverm=`sed -e 's/\(.*\)-ga.el7.centos/\1/' demo.txt`
    rm -rf demo.txt
    (echo "gateway-services" ; echo $dashverm; ) |tr '\n' '\t' >> soft_ver.txt
     
elif [ $1 == "printer-mailer" ]
then
    yum list installed | grep printer-mailer >> demo.txt
    dashn=`cat demo.txt | awk '{print $2}'`
    rm -rf demo.txt
    echo $dashn >> demo.txt
    dashvern=`sed -e 's/\(.*\)-ga.el7.centos/\1/' demo.txt`
    rm -rf demo.txt
    (echo "printer-mailer" ; echo $dashvern ; ) |tr '\n' '\t' >> soft_ver.txt
     
elif [ $1 == "service-assistance" ]
then
    yum list installed | grep service-assistance >> demo.txt
    dasho=`cat demo.txt | awk '{print $2}'`
    rm -rf demo.txt
    echo $dasho >> demo.txt
    dashvero=`sed -e 's/\(.*\)-ga.el7.centos/\1/' demo.txt`
    rm -rf demo.txt
    (echo "service-assistance" ; echo $dashvero ; ) |tr '\n' '\t' >> soft_ver.txt
     
elif [ $1 == "digivalet-butler" ]
then
    yum list installed | grep digivalet-butler >> demo.txt
    dashp=`cat demo.txt | awk '{print $2}'`
    rm -rf demo.txt
    echo $dashp >> demo.txt
    dashverp=`sed -e 's/\(.*\)-ga.el7.centos/\1/' demo.txt`
    rm -rf demo.txt
    (echo "digivalet-butler" ; echo $dashverp ; ) |tr '\n' '\t' >> soft_ver.txt
     
elif [ $1 == "butler-system" ]
then
    yum list installed | grep butler-system >> demo.txt
    dashq=`cat demo.txt | awk '{print $2}'`
    rm -rf demo.txt
    echo $dashq >> demo.txt
    dashverq=`sed -e 's/\(.*\)-ga.el7.centos/\1/' demo.txt`
    rm -rf demo.txt
    (echo "butler-system" ; echo $dashverq ; ) |tr '\n' '\t' >> soft_ver.txt
     
 

elif [ $1 == "digivalet-zigbee" ]
then
    yum list installed | grep digivalet-zigbee >> demo.txt
    dashr=`cat demo.txt | awk '{print $2}'`
    rm -rf demo.txt
    echo $dashr >> demo.txt
    dashverr=`sed -e 's/\(.*\)-ga.el7.centos/\1/' demo.txt`
    rm -rf demo.txt
    (echo "digivalet-zigbee" ; echo $dashverr ; ) |tr '\n' '\t' >> soft_ver.txt
     
elif [ $1 == "digivalet-entertainment" ]
then
    yum list installed | grep digivalet-entertainment >> demo.txt
    dashs=`cat demo.txt | awk '{print $2}'`
    rm -rf demo.txt
    echo $dashs >> demo.txt
    dashvers=`sed -e 's/\(.*\)-ga.el7.centos/\1/' demo.txt`
    rm -rf demo.txt
    (echo "digivalet-entertainment" ; echo $dashvers ; ) |tr '\n' '\t' >> soft_ver.txt
     
elif [ $1 == "digivalet-cloud-db" ]
then 
    yum list installed | grep digivalet-cloud-db >> demo.txt
    dasht=`cat demo.txt | awk '{print $2}'`
    rm -rf demo.txt
    echo $dasht >> demo.txt
    dashvert=`sed -e 's/\(.*\)-ga.el7.centos/\1/' demo.txt`
    rm -rf demo.txt
    (echo "digivalet-cloud-db" ; echo $dashvert ; ) |tr '\n' '\t' >> soft_ver.txt
     
elif [ $1 == "digivalet-db" ]
then 
    yum list installed | grep digivalet-db >> demo.txt
    dashu=`cat demo.txt | awk '{print $2}'`
    rm -rf demo.txt
    echo $dashu >> demo.txt
    dashveru=`sed -e 's/\(.*\)-ga.el7.centos/\1/' demo.txt`
    rm -rf demo.txt
    (echo "digivalet-db" ; echo $dashveru ; ) |tr '\n' '\t' >> soft_ver.txt
     
elif [ $1 == "digivalet-dvs-db" ]
then 
    yum list installed | grep digivalet-dvs-db >> demo.txt
    dashv=`cat demo.txt | awk '{print $2}'`
    rm -rf demo.txt
    echo $dashv >> demo.txt
    dashverv=`sed -e 's/\(.*\)-ga.el7.centos/\1/' demo.txt`
    rm -rf demo.txt
    (echo "digivalet-dvs-db" ; echo $dashverv ; ) |tr '\n' '\t' >> soft_ver.txt
     
elif [ $1 == "digivalet-mymovie-db" ]
then
    yum list installed | grep digivalet-mymovie-db >> demo.txt
    dashw=`cat demo.txt | awk '{print $2}'`
    rm -rf demo.txt
    echo $dashw >> demo.txt
    dashverw=`sed -e 's/\(.*\)-ga.el7.centos/\1/' demo.txt`
    rm -rf demo.txt
    (echo "digivalet-mymovie-db" ; echo $dashverw ; ) |tr '\n' '\t' >> soft_ver.txt
     
elif [ $1 == "digivalet-oneauth-db" ]
then
    yum list installed | grep digivalet-oneauth-db >> demo.txt
    dashx=`cat demo.txt | awk '{print $2}'`
    rm -rf demo.txt
    echo $dashx >> demo.txt
    dashverx=`sed -e 's/\(.*\)-ga.el7.centos/\1/' demo.txt`
    rm -rf demo.txt
    (echo "digivalet-oneauth-db" ; echo $dashverx ; ) |tr '\n' '\t' >> soft_ver.txt
     
elif [ $1 == "digivalet-butler-db" ]
then
    yum list installed | grep digivalet-butler-db >> demo.txt
    dashy=`cat demo.txt | awk '{print $2}'`
    rm -rf demo.txt
    echo $dashy >> demo.txt
    dashvery=`sed -e 's/\(.*\)-ga.el7.centos/\1/' demo.txt`
    rm -rf demo.txt
    (echo "digivalet-butler-db" ; echo $dashvery ; ) |tr '\n' '\t' >> soft_ver.txt
     

fi