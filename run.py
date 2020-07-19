import boto3
import datetime
import pandas
import requests


def date_collector():
    dates = open('date_history.txt', 'r')
    last_date = ''
    no_history = False
    for d in dates:
        last_date = d
    if last_date and len(last_date) == 8:
        year = last_date[0:4]
        month = last_date[3:6]
        day = last_date[6:]
        try:
            datetime.datetime(year=year, month=month, day=day)
        except ValueError:
            no_history = True

    now = datetime.datetime.now()
    today = f'{now.year}{now.month:02d}{now.day:02d}'
    result = pandas.date_range(start=last_date, end=today).strftime('%Y%m%d').tolist()
    return result

def downloader(date_list):
    date_list =  date_collector()
    for date in date_list:
        response = requests.get('http://nginx.org/download/nginx-1.19.1.tar.gz', allow_redirects=True)
        _file = open(f'downloads/{date}.gz', 'wb').write(response.content)

def runner():
    date_list = date_collector()
    downloader(date_list)
    print('finished')

runner()
