out_doc = []
spamer={}
b=0
with open("nginx_logs.txt", encoding='utf-8') as file_log:
    for line in file_log:
        # print(line, end='')
        ip_addr = line[0:line.find(" - - ")]
        req_type = line[line.find('"') + 1:line.find('"') + 4]
        req_res = line[line.find('"') + 5:line.find('"', line.find('"') + 1)]
        all_req = (ip_addr, req_type, req_res)
        out_doc.append(all_req)
        spamer.update({ip_addr:b})
    print(out_doc)
        # print(spamer[ip_addr])
with open("nginx_logs.txt", encoding='utf-8') as file_log:
    for line in file_log:
        ip_addr = line[0:line.find(" - - ")]
        spamer.update({ip_addr: spamer[ip_addr]+1})
key=''
val=0
for k,v in spamer.items():
    if val<v:
        key=k
        val=v

print(f'\n СПАМЕР:ip адрес:{key}, колличество запросов: {val}')
