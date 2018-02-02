import requests
import csv
import re

input_file = 'Community-2.csv'
output_file = 'matched.csv'
output_file2 = 'rejected.txt'

matched = {}
rejected = []

def get_data(disease_name):
    url = 'http://www.findzebra.com/api/call/json/query?q=%22disease_name%22=' + disease_name
    r = requests.get(url)
    data = r.json()
    docs = data['response']['docs']
    for doc in docs:
        cui = doc['cui']
        if re.match(r'c\d+', cui):
            display_title = doc['display_title']
            if display_title.strip() in disease_name:
                matched[cui] = display_title
                print 'Matched:', cui, display_title
            else:
                rejected.append([cui, display_title])
                print 'Rejected:', cui, display_title
       
if __name__ == '__main__':
    with open(input_file, 'rb') as fin:
        reader = csv.reader(fin)
        reader.next()
        for idx, row in enumerate(reader, start=1):
            print 'Row %s: %s'%(idx, row[1])
            get_data(row[1])
    
    fout = open(output_file, 'wb')
    writer = csv.writer(fout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
    writer.writerow(['cui', 'display_title'])
    for cui, display_title in matched.items():
        writer.writerow([cui, display_title])
    fout.close()
    
    fout2 = open(output_file2, 'w')
    for pair in rejected:
        fout2.write('%s\t%s\n'%(pair[0], pair[1]))
    fout2.close()
