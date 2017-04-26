#!/usr/bin/ksh
. <em>(path to setGrinderEnv.sh)</em>/setGrinderEnv.sh
java -classpath $CLASSPATH net.grinder.TCPProxy -console -http > grinder.py