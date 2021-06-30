import os
import json
f = open("./repo", "rb")
File = f.read().decode("utf8","ignore")
f.close()
Lines = File.splitlines()
print(Lines)

BOT_TOKEN="BOT_GITHUB_TOKEN"

OWNER="MHG-LAB"

for i in Lines:
    print(i)
    shell= '''curl -X GET -H "Authorization: token "'''+BOT_TOKEN+''' -H "Accept: application/vnd.github.v3+json" https://api.github.com/repos/'''+OWNER+'''/'''+i+'''/actions/workflows'''
    d=os.popen(shell)
    print(shell)
    f=d.read()
    #print(f)
    j = json.loads(f)
    for it in j['workflows']:
        #print(it['id'])
        id=str(it['id'])
        shell= '''curl -X PUT -H "Authorization: token "'''+BOT_TOKEN+''' -H "Accept: application/vnd.github.v3+json" https://api.github.com/repos/'''+OWNER+'''/'''+i+'''/actions/workflows/'''+id+'''/enable'''
        d=os.popen(shell)
        print(shell)
        f=d.read()
        print(f)

