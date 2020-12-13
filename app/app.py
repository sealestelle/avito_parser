from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from app_utils import encode_to_base64, get_count, get_top, decode_from_base64
from time import time
from pymongo import MongoClient

app = FastAPI()
client = MongoClient(host=['mongodb:27017'])


@app.get('/add')
async def add(search: str, area: str):
    id_search_area = encode_to_base64(search + ':' + area)
    search_area = client.db[id_search_area]
    search_area.insert_one({'time': int(time()), 'count': get_count(search, area)})
    return jsonable_encoder({'id': id_search_area})


@app.get('/stat')
async def get(id_search_area: str, time_s: int, time_e: int):
    search_area = client.db[id_search_area]
    stat_ads = dict()
    for d in search_area.find():
        if time_s <= d['time'] <= time_e:
            stat_ads[d['time']] = d['count']
    return jsonable_encoder(stat_ads)


@app.get('/top')
async def top(id_search_area: str):
    search_area_string = decode_from_base64(id_search_area)
    search_area = search_area_string.split(':')
    top_ads = get_top(search_area[0], search_area[1])
    return {'top': top_ads}


if __name__ == '__main__':
    while True:
        for c in client.db:
            for ad in client.db[c]:
                last_ad = ad.find().sort('id', -1)[0]
                if int(time()) - int(last_ad['time']) > 3600:
                    search_area_string = decode_from_base64(c)
                    search_area = search_area_string.split(':')
                    last_ad.insert_one({'time': int(time()), 'count': get_count(search_area[0], search_area[1])})
