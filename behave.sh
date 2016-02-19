#!/bin/bash
if [ ! -d "pyEnvJenkins" ]; then
        virtualenv pyEnvJenkins
fi
. pyEnvJenkins/bin/activate
pip install -r requirements.txt 
cd BrowserStackBehave/
behave --junit

deactivate