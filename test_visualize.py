import json

f = open('data.json')
data = json.load(f)
for i in range(len(data)):
    item = data[i]
    item_id = item['id']
    item_name = item['name']
    item_url = item['url_path']
    item_brand_name = item['brand_name']
    item_price = item['price']
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

    print(f"item_id: {item_id}" )
    print(f"item_name: {item_name}")
    print(f"item_url: http:://tiki.vn/{item_url}")
    print(f"item_brand_name: {item_brand_name}")
    print(f"item_price: {item_price}")
    print(f"item_discount_rate: {item_discount_rate}")
    print(f"item_rating_average: {item_rating_average}")
    print(f"item_review_count: {item_review_count}")
    print(f"item_quantity: {item_quantity}")
    print(f"item_seller_product_id: {item_seller_product_id}")
    print(f"item_tikinow: {item_tikinow}")
    print(f"item_all_time_quantity_sold: {item_all_time_quantity_sold}")
    print("----------------------------------------")