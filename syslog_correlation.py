import pandas as pd
import csv

def process():
    data = pd.read_csv('syslog.csv', header=0)
    a = data.drop_duplicates(subset=['ProcessGuid'], keep='first', inplace=False, ignore_index=True).dropna(
        subset=['ProcessGuid'])
    a['_key'] = list(range(1, a.shape[0] + 1))
    a[['_key', 'ProcessGuid', 'LocalIP']].to_csv('process.csv', index=False)

def SyslogSyslog():
    with open('syslog.csv', 'r', encoding='utf-8', newline='')as s:
        r = csv.reader(s)
        lines = list(r)
    with open('SyslogSyslog.csv', 'w', encoding='utf-8', newline='')as ss:
        csv_write = csv.writer(ss)
        csv_write.writerow(['_from', '_to'])
        for i in range(1, len(lines)):
            temp = lines[i][37]
            for j in range(i + 1, len(lines)):
                if lines[j][37] == temp:
                    csv_write.writerow(['syslog/' + str(lines[i][0]), 'syslog/' + str(lines[j][0])])
                    break
    ss.close()
    s.close()

def SyslogProcess():
    with open('process.csv', 'r', encoding='utf-8', newline='')as p:
        rp = csv.reader(p)
        lines_p = list(rp)
    with open('syslog.csv', 'r', encoding='utf-8', newline='')as s:
        rs = csv.reader(s)
        lines_s = list(rs)
    with open('SyslogProcess.csv', 'w', encoding='utf-8', newline='')as sp:
        csv_write = csv.writer(sp)
        csv_write.writerow(['_from', '_to'])
        for i in range(1, len(lines_p)):
            p_ID = lines_p[i][1]
            for j in range(1, len(lines_s)):
                s_ID = lines_s[j][37]
                if s_ID == p_ID:
                    csv_write.writerow(['syslog/' + str(lines_s[j][0]),
                                        'process/' + str(lines_p[i][0])])
                    break
    sp.close()
    s.close()
    p.close()

def ProcessProcess(Event_ID):
    if Event_ID == '1':
        file_name = 'ParentpChildp.csv'
        line_num1 = 32
        line_num2 = 37
    elif Event_ID == '10':
        file_name = 'ProcessProcess.csv'
        line_num1 = 51
        line_num2 = 62
    else:
        return -1

    with open('process.csv', 'r', encoding='utf-8', newline='')as p:
        rp = csv.reader(p)
        lines_p = list(rp)
    with open('syslog.csv', 'r', encoding='utf-8', newline='')as s:
        rs = csv.reader(s)
        lines_s = list(rs)
    with open(file_name, 'w', encoding='utf-8', newline='')as f:
        csv_write = csv.writer(f)
        csv_write.writerow(['_from', '_to'])
        for i in range(1, len(lines_s)):
            if lines_s[i][13] == Event_ID:
                from_ID = lines_s[i][line_num1]
                to_ID = lines_s[i][line_num2]
                flag = 0
                for j in range(1, len(lines_p)):
                    p_ID = lines_p[j][1]
                    if p_ID == from_ID:
                        flag += 1
                        _from = lines_p[j][0]
                    if p_ID == to_ID:
                        flag += 1
                        _to = lines_p[j][0]

                    if flag == 2:
                        break
                csv_write.writerow(['process/' + str(_from), 'process/' + str(_to)])
    f.close()
    s.close()
    p.close()

if __name__ == '__main__':
    process()
    SyslogSyslog()
    SyslogProcess()
    ProcessProcess('1')
    ProcessProcess('10')
