# %%
from faker import Faker
import json
import numpy as np
import uuid
from datetime import datetime
# %%
fake = Faker('pt_BR')

products = ['SSD Externo Samsung',
            'Placa de Vídeo RTX 3060',
            'Mouse Gamer HyperX',
            'Monitor Gamer Asus',
            'Tablet Samsung Galaxy',
            'Memória Gamer Husky',
            'Smartwatch Hit',
            'Smart TV Samsung',
            'HD Toshiba L200',
            'Microfone HyperX',
            'Teclado e Mouse Microsoft']

#%%
products_id = []

for i in range(11):
   id = str(uuid.uuid4())
   products_id.append(id)

#%%

products_price = [299.90,
                  3500.00,
                  130.00,
                  1499.99,
                  599.99,
                  89.90,
                  700.00,
                  2599.80,
                  342.90,
                  860.89,
                  200.00]

#%%

orders_data = []
orders = 5000

for i in range(orders):
    random_product = np.random.randint(0,10)

    data = {
            "order_id": str(uuid.uuid1()),
            "order_total": products_price[random_product],
            "product_info":{
                            "product_id": products_id[random_product],
                            "product_description": products[random_product],
                            },            
            "customer_info":
                            {
                             "customer_id": str(uuid.uuid4()),
                             "customer_name": fake.name(),
                             "customer_phone_number": fake.phone_number()
                             },
            "payment_info": {
                             "payment_type": "credit_card",
                             "card_number": fake.credit_card_number(),
                             "provider": fake.credit_card_provider(),
                             "expire": fake.credit_card_expire(),
                             "security_code": fake.credit_card_security_code(),
                            },
            "delivery_address": {
                                    "zip_code": fake.postcode(formatted=False),
                                    "country": fake.current_country(),
                                    "state": fake.estado_nome(),
                                    "street": fake.street_name(),
                                    "number": fake.building_number()
                                },
            "order_created_at": str(fake.date_time_between_dates(datetime(2023, 6, 1), datetime(2023, 6, 25)))
            }
    
    orders_data.append(data)

print(orders_data)

# Serializing json
json_object = json.dumps(orders_data, ensure_ascii=False)
 
# Writing to sample.json
with open("sample_data.json", "w", encoding='utf8') as outfile:
    outfile.write(json_object)
# %%
