#/bin/bash
cd /tmp/

echo $1     

if [ $1 == "printer-mailer" ] 
then
    a=`systemctl is-active printer-mailer`
    b=`systemctl status printer-mailer | sed -n '3p'`
    echo $b >> ss.txt   
    c=`sed -n -e 's/^.*since //p' ss.txt`
    rm -rf ss.txt
    (echo "last status :--" ; echo $a ; echo "since :"; echo $c ;) |tr '\n' '\t' >> service_restart.txt
    echo " " >> service_restart.txt
    systemctl stop printer-mailer
    systemctl start printer-mailer
    d=`systemctl is-active printer-mailer`
    e=`systemctl status printer-mailer | sed -n '3p'`
    echo $e >> ss.txt   
    f=`sed -n -e 's/^.*since //p' ss.txt`
    rm -rf ss.txt
    (echo "currenet status :--" ; echo $d ; echo "since :"; echo $f ;) |tr '\n' '\t' >> service_restart.txt
elif [ $1 == "digivalet-pmsi" ]
then
    a=`systemctl is-active digivalet-pmsi`
    b=`systemctl status digivalet-pmsi | sed -n '3p'`
    echo $b >> ss.txt   
    c=`sed -n -e 's/^.*since //p' ss.txt`
    rm -rf ss.txt
    (echo "last status :--" ; echo $a ; echo "since :"; echo $c ;) |tr '\n' '\t' >> service_restart.txt
    echo " " >> service_restart.txt
    systemctl stop digivalet-pmsi
    systemctl start digivalet-pmsi
    d=`systemctl is-active digivalet-pmsi`
    e=`systemctl status digivalet-pmsi | sed -n '3p'`
    echo $e >> ss.txt   
    f=`sed -n -e 's/^.*since //p' ss.txt`
    rm -rf ss.txt
    (echo "currenet status :--" ; echo $d ; echo "since :"; echo $f ;) |tr '\n' '\t' >> service_restart.txt
elif [ $1 == "nodejs-core" ]
then
    a=`systemctl is-active nodejs-core`
    b=`systemctl status nodejs-core | sed -n '3p'`
    echo $b >> ss.txt   
    c=`sed -n -e 's/^.*since //p' ss.txt`
    rm -rf ss.txt
    (echo "last status :--" ; echo $a ; echo "since :"; echo $c ;) |tr '\n' '\t' >> service_restart.txt
    echo " " >> service_restart.txt
    systemctl stop nodejs-core
    systemctl start nodejs-core
    d=`systemctl is-active nodejs-core`
    e=`systemctl status nodejs-core | sed -n '3p'`
    echo $e >> ss.txt   
    f=`sed -n -e 's/^.*since //p' ss.txt`
    rm -rf ss.txt
    (echo "currenet status :--" ; echo $d ; echo "since :"; echo $f ;) |tr '\n' '\t' >> service_restart.txt
elif [ $1 == "nodejs-cloud-core" ]
then
    a=`systemctl is-active nodejs-cloud-core`
    b=`systemctl status nodejs-cloud-core | sed -n '3p'`
    echo $b >> ss.txt   
    c=`sed -n -e 's/^.*since //p' ss.txt`
    rm -rf ss.txt
    (echo "last status :--" ; echo $a ; echo "since :"; echo $c ;) |tr '\n' '\t' >> service_restart.txt
    echo " " >> service_restart.txt
    systemctl stop nodejs-cloud-core
    systemctl start nodejs-cloud-core
    d=`systemctl is-active nodejs-cloud-core`
    e=`systemctl status nodejs-cloud-core | sed -n '3p'`
    echo $e >> ss.txt   
    f=`sed -n -e 's/^.*since //p' ss.txt`
    rm -rf ss.txt
    (echo "currenet status :--" ; echo $d ; echo "since :"; echo $f ;) |tr '\n' '\t' >> service_restart.txt
elif [ $1 == "nodejs-dashboard" ]
then
    a=`systemctl is-active nodejs-dashboard`
    b=`systemctl status nodejs-dashboard | sed -n '3p'`
    echo $b >> ss.txt   
    c=`sed -n -e 's/^.*since //p' ss.txt`
    rm -rf ss.txt
    (echo "last status :--" ; echo $a ; echo "since :"; echo $c ;) |tr '\n' '\t' >> service_restart.txt
    echo " " >> service_restart.txt
    systemctl stop nodejs-dashboard
    systemctl start nodejs-dashboard
    d=`systemctl is-active nodejs-dashboard`
    e=`systemctl status nodejs-dashboard | sed -n '3p'`
    echo $e >> ss.txt   
    f=`sed -n -e 's/^.*since //p' ss.txt`
    rm -rf ss.txt
    (echo "currenet status :--" ; echo $d ; echo "since :"; echo $f ;) |tr '\n' '\t' >> service_restart.txt
elif [ $1 == "digivalet-entertainment" ]
then
    a=`systemctl is-active digivalet-entertainment`
    b=`systemctl status digivalet-entertainment | sed -n '3p'`
    echo $b >> ss.txt   
    c=`sed -n -e 's/^.*since //p' ss.txt`
    rm -rf ss.txt
    (echo "last status :--" ; echo $a ; echo "since :"; echo $c ;) |tr '\n' '\t' >> service_restart.txt
    echo " " >> service_restart.txt
    systemctl stop digivalet-entertainment
    systemctl start digivalet-entertainment
    d=`systemctl is-active digivalet-entertainment`
    e=`systemctl status digivalet-entertainment | sed -n '3p'`
    echo $e >> ss.txt   
    f=`sed -n -e 's/^.*since //p' ss.txt`
    rm -rf ss.txt
    (echo "currenet status :--" ; echo $d ; echo "since :"; echo $f ;) |tr '\n' '\t' >> service_restart.txt
elif [ $1 == "push-manager" ]
then
    a=`systemctl is-active push-manager`
    b=`systemctl status push-manager | sed -n '3p'`
    echo $b >> ss.txt   
    c=`sed -n -e 's/^.*since //p' ss.txt`
    rm -rf ss.txt
    (echo "last status :--" ; echo $a ; echo "since :"; echo $c ;) |tr '\n' '\t' >> service_restart.txt
    echo " " >> service_restart.txt
    systemctl stop push-manager
    systemctl start push-manager
    d=`systemctl is-active push-manager`
    e=`systemctl status push-manager | sed -n '3p'`
    echo $e >> ss.txt   
    f=`sed -n -e 's/^.*since //p' ss.txt`
    rm -rf ss.txt
    (echo "currenet status :--" ; echo $d ; echo "since :"; echo $f ;) |tr '\n' '\t' >> service_restart.txt
elif [ $1 == "system-monitor" ]
then
    a=`systemctl is-active system-monitor`
    b=`systemctl status system-monitor | sed -n '3p'`
    echo $b >> ss.txt   
    c=`sed -n -e 's/^.*since //p' ss.txt`
    rm -rf ss.txt
    (echo "last status :--" ; echo $a ; echo "since :"; echo $c ;) |tr '\n' '\t' >> service_restart.txt
    echo " " >> service_restart.txt
    systemctl stop system-monitor
    systemctl start system-monitor
    d=`systemctl is-active system-monitor`
    e=`systemctl status system-monitor | sed -n '3p'`
    echo $e >> ss.txt   
    f=`sed -n -e 's/^.*since //p' ss.txt`
    rm -rf ss.txt
    (echo "currenet status :--" ; echo $d ; echo "since :"; echo $f ;) |tr '\n' '\t' >> service_restart.txt
elif [ $1 == "digivalet-posi" ]
then
    a=`systemctl is-active digivalet-posi`
    b=`systemctl status digivalet-posi | sed -n '3p'`
    echo $b >> ss.txt   
    c=`sed -n -e 's/^.*since //p' ss.txt`
    rm -rf ss.txt
    (echo "last status :--" ; echo $a ; echo "since :"; echo $c ;) |tr '\n' '\t' >> service_restart.txt
    echo " " >> service_restart.txt
    systemctl stop digivalet-posi
    systemctl start digivalet-posi
    d=`systemctl is-active digivalet-posi`
    e=`systemctl status digivalet-posi | sed -n '3p'`
    echo $e >> ss.txt   
    f=`sed -n -e 's/^.*since //p' ss.txt`
    rm -rf ss.txt
    (echo "currenet status :--" ; echo $d ; echo "since :"; echo $f ;) |tr '\n' '\t' >> service_restart.txt
elif [ $1 == "gateway-services" ]
then
    a=`systemctl is-active gateway-services`
    b=`systemctl status gateway-services | sed -n '3p'`
    echo $b >> ss.txt   
    c=`sed -n -e 's/^.*since //p' ss.txt`
    rm -rf ss.txt
    (echo "last status :--" ; echo $a ; echo "since :"; echo $c ;) |tr '\n' '\t' >> service_restart.txt
    echo " " >> service_restart.txt
    systemctl stop gateway-services
    systemctl start gateway-services
    d=`systemctl is-active gateway-services`
    e=`systemctl status gateway-services | sed -n '3p'`
    echo $e >> ss.txt   
    f=`sed -n -e 's/^.*since //p' ss.txt`
    rm -rf ss.txt
    (echo "currenet status :--" ; echo $d ; echo "since :"; echo $f ;) |tr '\n' '\t' >> service_restart.txt
elif [ $1 == "service-assistance" ]
then
    a=`systemctl is-active service-assistance`
    b=`systemctl status service-assistance | sed -n '3p'`
    echo $b >> ss.txt   
    c=`sed -n -e 's/^.*since //p' ss.txt`
    rm -rf ss.txt
    (echo "last status :--" ; echo $a ; echo "since :"; echo $c ;) |tr '\n' '\t' >> service_restart.txt
    echo " " >> service_restart.txt
    systemctl stop service-assistance
    systemctl start service-assistance
    d=`systemctl is-active service-assistance`
    e=`systemctl status service-assistance | sed -n '3p'`
    echo $e >> ss.txt   
    f=`sed -n -e 's/^.*since //p' ss.txt`
    rm -rf ss.txt
    (echo "currenet status :--" ; echo $d ; echo "since :"; echo $f ;) |tr '\n' '\t' >> service_restart.txt
elif [ $1 == "nodejs-butler" ]
then
    a=`systemctl is-active nodejs-butler`
    b=`systemctl status nodejs-butler | sed -n '3p'`
    echo $b >> ss.txt   
    c=`sed -n -e 's/^.*since //p' ss.txt`
    rm -rf ss.txt
    (echo "last status :--" ; echo $a ; echo "since :"; echo $c ;) |tr '\n' '\t' >> service_restart.txt
    echo " " >> service_restart.txt
    systemctl stop nodejs-butler
    systemctl start nodejs-butler
    d=`systemctl is-active nodejs-butler`
    e=`systemctl status nodejs-butler | sed -n '3p'`
    echo $e >> ss.txt   
    f=`sed -n -e 's/^.*since //p' ss.txt`
    rm -rf ss.txt
    (echo "currenet status :--" ; echo $d ; echo "since :"; echo $f ;) |tr '\n' '\t' >> service_restart.txt
elif [ $1 == "digivalet-butler" ]
then
    a=`systemctl is-active digivalet-butler`
    b=`systemctl status digivalet-butler | sed -n '3p'`
    echo $b >> ss.txt   
    c=`sed -n -e 's/^.*since //p' ss.txt`
    rm -rf ss.txt
    (echo "last status :--" ; echo $a ; echo "since :"; echo $c ;) |tr '\n' '\t' >> service_restart.txt
    echo " " >> service_restart.txt
    systemctl stop digivalet-butler
    systemctl start digivalet-butler
    d=`systemctl is-active digivalet-butler`
    e=`systemctl status digivalet-butler | sed -n '3p'`
    echo $e >> ss.txt   
    f=`sed -n -e 's/^.*since //p' ss.txt`
    rm -rf ss.txt
    (echo "currenet status :--" ; echo $d ; echo "since :"; echo $f ;) |tr '\n' '\t' >> service_restart.txt
elif [ $1 == "digivalet-zigbee" ]
then
    a=`systemctl is-active digivalet-zigbee`
    b=`systemctl status digivalet-zigbee | sed -n '3p'`
    echo $b >> ss.txt   
    c=`sed -n -e 's/^.*since //p' ss.txt`
    rm -rf ss.txt
    (echo "last status :--" ; echo $a ; echo "since :"; echo $c ;) |tr '\n' '\t' >> service_restart.txt
    echo " " >> service_restart.txt
    systemctl stop digivalet-zigbee
    systemctl start digivalet-zigbee
    d=`systemctl is-active digivalet-zigbee`
    e=`systemctl status digivalet-zigbee | sed -n '3p'`
    echo $e >> ss.txt   
    f=`sed -n -e 's/^.*since //p' ss.txt`
    rm -rf ss.txt
    (echo "currenet status :--" ; echo $d ; echo "since :"; echo $f ;) |tr '\n' '\t' >> service_restart.txt
elif [ $1 == "content-service" ]
then
    a=`systemctl is-active content-service`
    b=`systemctl status content-service | sed -n '3p'`
    echo $b >> ss.txt   
    c=`sed -n -e 's/^.*since //p' ss.txt`
    rm -rf ss.txt
    (echo "last status :--" ; echo $a ; echo "since :"; echo $c ;) |tr '\n' '\t' >> service_restart.txt
    echo " " >> service_restart.txt
    systemctl stop content-service
    systemctl start content-service
    d=`systemctl is-active content-service`
    e=`systemctl status content-service | sed -n '3p'`
    echo $e >> ss.txt   
    f=`sed -n -e 's/^.*since //p' ss.txt`
    rm -rf ss.txt
    (echo "currenet status :--" ; echo $d ; echo "since :"; echo $f ;) |tr '\n' '\t' >> service_restart.txt
elif [ $1 == "content-service-celery-worker" ]
then
    a=`systemctl is-active content-service-celery-worker`
    b=`systemctl status content-service-celery-worker | sed -n '3p'`
    echo $b >> ss.txt   
    c=`sed -n -e 's/^.*since //p' ss.txt`
    rm -rf ss.txt
    (echo "last status :--" ; echo $a ; echo "since :"; echo $c ;) |tr '\n' '\t' >> service_restart.txt
    echo " " >> service_restart.txt
    systemctl stop content-service-celery-worker
    systemctl start content-service-celery-worker
    d=`systemctl is-active content-service-celery-worker`
    e=`systemctl status content-service-celery-worker | sed -n '3p'`
    echo $e >> ss.txt   
    f=`sed -n -e 's/^.*since //p' ss.txt`
    rm -rf ss.txt
    (echo "currenet status :--" ; echo $d ; echo "since :"; echo $f ;) |tr '\n' '\t' >> service_restart.txt
elif [ $1 == "content-service-celery-beat" ]
then
    a=`systemctl is-active content-service-celery-beat`
    b=`systemctl status content-service-celery-beat | sed -n '3p'`
    echo $b >> ss.txt   
    c=`sed -n -e 's/^.*since //p' ss.txt`
    rm -rf ss.txt
    (echo "last status :--" ; echo $a ; echo "since :"; echo $c ;) |tr '\n' '\t' >> service_restart.txt
    echo " " >> service_restart.txt
    systemctl stop content-service-celery-beat
    systemctl start content-service-celery-beat
    d=`systemctl is-active content-service-celery-beat`
    e=`systemctl status content-service-celery-beat | sed -n '3p'`
    echo $e >> ss.txt   
    f=`sed -n -e 's/^.*since //p' ss.txt`
    rm -rf ss.txt
    (echo "currenet status :--" ; echo $d ; echo "since :"; echo $f ;) |tr '\n' '\t' >> service_restart.txt
fi
