import requests
import csv
import re

input_file = 'rdList1.csv'
output_file = 'rdUMLSnew.csv'

    datafile = get_data(rdList1.csv)
    rows = []
    data = get_data(rdUMLS2.csv)
    rows1 = []
	//url = 'http://www.findzebra.com/api/call/json/query?q=%22disease_name%22=' + disease_name
    //r = requests.get(url)
    //data = r.json()
    //docs = data['cui']['display_title']
    //for doc in docs:
      if rows[] == rows1[1]
        //if re.match(r'c\d+', cui):
            //display_title = doc['display_title'].encode('utf8')
            rows.append([cui])
            print cui
    return rows
       
if __name__ == '__main__':
    fout = open(output_file, 'wb')
    writer = csv.writer(fout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
    writer.writerow(['cui', 'display_title'])
    with open(input_file, 'rb') as fin:
        reader = csv.reader(fin)
        for row in reader:
            data = get_data(row[0])
            [writer.writerow(i) for i in data]
            
    fout.close()

