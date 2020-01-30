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
    (echo $a ; echo "since :"; echo $c ;) |tr '\n' '\t' >> service_status.txt
elif [ $1 == "digivalet-pmsi" ]
then
    a=`systemctl is-active digivalet-pmsi` 
    b=`systemctl status digivalet-pmsi | sed -n '3p'`
    echo $b >> ss.txt
    c=`sed -n -e 's/^.*since //p' ss.txt`
    rm -rf ss.txt
    (echo $a ; echo "since :"; echo $c ;) |tr '\n' '\t' >> service_status.txt
elif [ $1 == "nodejs-core" ]
then
    a=`systemctl is-active nodejs-core`
    b=`systemctl status nodejs-core | sed -n '3p'`
    echo $b >> ss.txt
    c=`sed -n -e 's/^.*since //p' ss.txt`
    rm -rf ss.txt
    (echo $a ; echo "since :"; echo $c ;) |tr '\n' '\t' >> service_status.txt
elif [ $1 == "nodejs-cloud-core" ]
then
    a=`systemctl is-active nodejs-cloud-core`
    b=`systemctl status nodejs-cloud-core | sed -n '3p'`
    echo $b >> ss.txt
    c=`sed -n -e 's/^.*since //p' ss.txt`
    rm -rf ss.txt
    (echo $a ; echo "since :"; echo $c ;) |tr '\n' '\t' >> service_status.txt
elif [ $1 == "nodejs-dashboard" ]
then
    a=`systemctl is-active nodejs-dashboard`
    b=`systemctl status nodejs-dashboard | sed -n '3p'`
    echo $b >> ss.txt
    c=`sed -n -e 's/^.*since //p' ss.txt`
    rm -rf ss.txt
    (echo $a ; echo "since :"; echo $c ;) |tr '\n' '\t' >> service_status.txt
elif [ $1 == "digivalet-entertainment" ]
then
    a=`systemctl is-active digivalet-entertainment` 
    b=`systemctl status digivalet-entertainment | sed -n '3p'`
    echo $b >> ss.txt
    c=`sed -n -e 's/^.*since //p' ss.txt`
    rm -rf ss.txt
    (echo $a ; echo "since :"; echo $c ;) |tr '\n' '\t' >> service_status.txt
elif [ $1 == "push-manager" ]
then
    a=`systemctl is-active push-manager` 
    b=`systemctl status push-manager | sed -n '3p'`
    echo $b >> ss.txt
    c=`sed -n -e 's/^.*since //p' ss.txt`
    rm -rf ss.txt
    (echo $a ; echo "since :"; echo $c ;) |tr '\n' '\t' >> service_status.txt
elif [ $1 == "system-monitor" ]
then
    a=`systemctl is-active system-monitor` 
    b=`systemctl status system-monitor | sed -n '3p'`
    echo $b >> ss.txt
    c=`sed -n -e 's/^.*since //p' ss.txt`
    rm -rf ss.txt
    (echo $a ; echo "since :"; echo $c ;) |tr '\n' '\t' >> service_status.txt
elif [ $1 == "digivalet-posi" ]
then
    a=`systemctl is-active digivalet-posi` 
    b=`systemctl status digivalet-posi | sed -n '3p'`
    echo $b >> ss.txt
    c=`sed -n -e 's/^.*since //p' ss.txt`
    rm -rf ss.txt
    (echo $a ; echo "since :"; echo $c ;) |tr '\n' '\t' >> service_status.txt
elif [ $1 == "gateway-services" ]
then
    a=`systemctl is-active gateway-services` 
    b=`systemctl status gateway-services | sed -n '3p'`
    echo $b >> ss.txt
    c=`sed -n -e 's/^.*since //p' ss.txt`
    rm -rf ss.txt
    (echo $a ; echo "since :"; echo $c ;) |tr '\n' '\t' >> service_status.txt
elif [ $1 == "service-assistance" ]
then
    a=`systemctl is-active service-assistance` 
    b=`systemctl status service-assistance | sed -n '3p'`
    echo $b >> ss.txt
    c=`sed -n -e 's/^.*since //p' ss.txt`
    rm -rf ss.txt
    (echo $a ; echo "since :"; echo $c ;) |tr '\n' '\t' >> service_status.txt
elif [ $1 == "nodejs-butler" ]
then
    a=`systemctl is-active nodejs-butler` 
    b=`systemctl status nodejs-butler | sed -n '3p'`
    echo $b >> ss.txt
    c=`sed -n -e 's/^.*since //p' ss.txt`
    rm -rf ss.txt
    (echo $a ; echo "since :"; echo $c ;) |tr '\n' '\t' >> service_status.txt
elif [ $1 == "digivalet-butler" ]
then
    a=`systemctl is-active digivalet-butler` 
    b=`systemctl status digivalet-butler | sed -n '3p'`
    echo $b >> ss.txt
    c=`sed -n -e 's/^.*since //p' ss.txt`
    rm -rf ss.txt
    (echo $a ; echo "since :"; echo $c ;) |tr '\n' '\t' >> service_status.txt
elif [ $1 == "digivalet-zigbee" ]
then
    a=`systemctl is-active  digivalet-zigbee` 
    b=`systemctl status  digivalet-zigbee | sed -n '3p'`
    echo $b >> ss.txt
    c=`sed -n -e 's/^.*since //p' ss.txt`
    rm -rf ss.txt
    (echo $a ; echo "since :"; echo $c ;) |tr '\n' '\t' >> service_status.txt
elif [ $1 == "content-service" ]
then
    a=`systemctl is-active  content-service` 
    b=`systemctl status  content-service | sed -n '3p'`
    echo $b >> ss.txt
    c=`sed -n -e 's/^.*since //p' ss.txt`
    rm -rf ss.txt
    (echo $a ; echo "since :"; echo $c ;) |tr '\n' '\t' >> service_status.txt
elif [ $1 == "content-service-celery-worker" ]
then
    a=`systemctl is-active  content-service-celery-worker` 
    b=`systemctl status  content-service-celery-worker | sed -n '3p'`
    echo $b >> ss.txt
    c=`sed -n -e 's/^.*since //p' ss.txt`
    rm -rf ss.txt
    (echo $a ; echo "since :"; echo $c ;) |tr '\n' '\t' >> service_status.txt
elif [ $1 == "content-service-celery-beat" ]
then
    a=`systemctl is-active  content-service-celery-beat` 
    b=`systemctl status  content-service-celery-beat | sed -n '3p'`
    echo $b >> ss.txt
    c=`sed -n -e 's/^.*since //p' ss.txt`
    rm -rf ss.txt
    (echo $a ; echo "since :"; echo $c ;) |tr '\n' '\t' >> service_status.txt
fi


unset a
unset b
unset c