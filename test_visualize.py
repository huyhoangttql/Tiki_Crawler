import json
from datetime import datetime

f = open('data.json')
data = json.load(f)
new_data=[]
for i in range(len(data)):
    item = data[i]
    item_id = item['id']
    item_name = item['name']
    item_url = item['url_path']
    item_brand_name = item['brand_name']
    item_price = item['price']
    item_image = item['thumbnail_url']
    try:
        item_tikinow = (item['badges_new'][0]['code']=='tikinow')
    except:
        continue
    item_discount_rate = item['discount_rate']
    item_rating_average = item['rating_average']
    item_review_count = item['review_count']
    item_quantity = item['stock_item']['qty']
    item_seller_product_id = item['seller_product_id']
    try:
        item_all_time_quantity_sold = item['all_time_quantity_sold']
    except:
        continue


    new_data.append(
        {
            "item_id": item['id'],
            "item_name": item['name'],
            "item_url": item['url_path'],
            "item_image_url": item['thumbnail_url'],
            "item_brand_name": item['brand_name'],
            "item_price": item['price'],
            "item_tikinow": item_tikinow,
            "item_discount_rate": item['discount_rate'],
            "item_rating_average": item['rating_average'],
            "item_review_count": item['review_count'],
            "item_quantity": item['stock_item']['qty'],
            "item_seller_product_id": item['seller_product_id'],
            "item_all_time_quantity_sold": item_all_time_quantity_sold,
            "item_fetched_timestamp": datetime.timestamp(datetime.now())

        }
    )
print(new_data)
f1 = open('data1.json','w+')
json.dump(new_data,f1,indent=4)
