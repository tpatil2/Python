from urllib import request


yahoo_url = "http://chart.finance.yahoo.com/table.csv?s=CUDA&a=2&b=7&c=2017&d=3&e=7&f=2017&g=d&ignore=.csv"

def dwnload_stock(csv_url):
    #connection to web
    responce = request.urlopen(csv_url)
    file = responce.read()
    data = str(file)
    lines = data.split("\\n")
    fw = open('file2.csv','w')

    for line in lines:
        fw.write(line +'\n')

    fw.close()

dwnload_stock(yahoo_url)

