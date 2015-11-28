#! /bin/sh

rc=$(./start-exit ; echo $?)

case $rc in 
    "13")
	echo PASS
	;;
    *)
	echo FAIL
esac
