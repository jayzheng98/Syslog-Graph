import pandas as pd
import csv

def find_Index(column_name):
    with open('syslog.csv', 'r', encoding='utf-8', newline='')as s:
        rs = csv.reader(s)
        lines_s = list(rs)
        list_index = lines_s[0]
        index = 0,
        for i in range(0, len(list_index)):
            if list_index[i] == column_name:
                index = i
    s.close()
    return index

def process():
    data = pd.read_csv('syslog.csv', header=0, dtype={"Keywords": str, "SourceModuleName": str, "SourceName": str, "SyslogFacility": str, "SyslogSeverity": str})
    a = data.drop_duplicates(subset=['ProcessGuid'], keep='first', inplace=False, ignore_index=True).dropna(
        subset=['ProcessGuid'])
    a['_key'] = list(range(1, a.shape[0] + 1))
    a[['_key', 'ProcessGuid', 'LocalIP']].to_csv('process.csv', index=False)

def SyslogSyslog():
    index = find_Index('ProcessGuid')
    with open('syslog.csv', 'r', encoding='utf-8', newline='')as s:
        r = csv.reader(s)
        lines = list(r)
    with open('SyslogSyslog.csv', 'w', encoding='utf-8', newline='')as ss:
        csv_write = csv.writer(ss)
        csv_write.writerow(['_from', '_to'])
        for i in range(1, len(lines)):
            temp = lines[i][index]
            if temp:
                for j in range(i + 1, len(lines)):
                    if lines[j][index] == temp:
                        csv_write.writerow(['syslog/' + str(lines[i][0]), 'syslog/' + str(lines[j][0])])
                        break
    ss.close()
    s.close()

def SyslogProcess():
    index = find_Index('ProcessGuid')
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
                s_ID = lines_s[j][index]
                if s_ID == p_ID:
                    csv_write.writerow(['syslog/' + str(lines_s[j][0]),
                                        'process/' + str(lines_p[i][0])])
                    break
    sp.close()
    s.close()
    p.close()

def ProcessProcess(EventID):
    id_index = find_Index('EventID')
    if EventID == '1':
        line_num1 = find_Index('ParentProcessGuid')
        line_num2 = find_Index('ProcessGuid')
        file_name = 'ParentpChildp.csv'
    elif EventID == '10':
        line_num1 = find_Index('SourceProcessGUID')
        line_num2 = find_Index('TargetProcessGUID')
        file_name = 'ProcessProcess.csv'
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
            if lines_s[i][id_index] == EventID:
                from_ID = lines_s[i][line_num1]
                to_ID = lines_s[i][line_num2]
                _to = 0
                _from = 0
                for j in range(1, len(lines_p)):
                    p_ID = lines_p[j][1]
                    if p_ID == from_ID:
                        _from = lines_p[j][0]
                    elif p_ID == to_ID:
                        _to = lines_p[j][0]

                    if _to and _from:
                        csv_write.writerow(['process/' + str(_from), 'process/' + str(_to)])
                        break

    f.close()
    s.close()
    p.close()

if __name__ == '__main__':
    process()
    SyslogSyslog()
    SyslogProcess()
    ProcessProcess('1')
    ProcessProcess('10')
