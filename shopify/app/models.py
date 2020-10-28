# models.py

products =[ 
    {"id":1,
    "title": "Bag",
    "price":109.95,
    "description": "Fjallraven - Foldsack No. 1 Backpack, Fits 15 Laptops",
    "category":"men clothing",
    "stock_quantity" : 10,
    "image":"https://fakestoreapi.com/img/81fPKd-2AYL._AC_SL1500_.jpg"},
    
    
    {"id":2,
    "title": "Shirt",
    "price":22.3,
    "description": "Mens Casual Premium Slim Fit T-Shirts ",
    "category":"men clothing",
    "stock_quantity" : 10,
    "image":"https://fakestoreapi.com/img/71-3HjGNDUL._AC_SY879._SX._UX._SY._UY_.jpg"},
    
    {"id":3,
    "title": "Jacket",
    "price":55.99,
    "description": "Mens Cotton Jacket",
    "category":"men clothing",
    "stock_quantity" : 10,
    "image":"https://fakestoreapi.com/img/71li-ujtlUL._AC_UX679_.jpg"},
    
    {"id":4,
    "title": "Shirt",
    "price":15.99,
    "description": "Mens Casual Slim Fit",
    "category":"men clothing",
    "stock_quantity" : 10,
    "image":"https://fakestoreapi.com/img/71YXzeOuslL._AC_UY879_.jpg"},
    
    {"id":5,
    "title": "Bracelet",
    "price":695,
    "description": "John Hardy Women's Legends Naga Gold & Silver Dragon Station Chain Bracelet",
    "category":"jewelery",
    "stock_quantity" : 10,
    "image":"https://fakestoreapi.com/img/71pWzhdJNwL._AC_UL640_QL65_ML3_.jpg"},
    
    {"id":6,
    "title":"Bracelet",
    "price":168,
    "description":"Solid Gold Petite Micropave ",
    "category":"jewelery",
    "stock_quantity" : 10,
    "image":"https://fakestoreapi.com/img/61sbMiUnoGL._AC_UL640_QL65_ML3_.jpg"},
    
    {"id":7,
    "title": "Ring",
    "price":9.99,
    "description": "White Gold Plated Princess",
    "category":"jewelery",
    "stock_quantity" : 10,
    "image":"https://fakestoreapi.com/img/71YAIFU48IL._AC_UL640_QL65_ML3_.jpg"},
   
    {"id":8,
    "title": "Ring",
    "price":10.99,
    "description": "Pierced Owl Rose Gold Plated Stainless Steel Double",
    "category":"jewelery",
    "stock_quantity" : 10,
    "image":"https://fakestoreapi.com/img/51UDEzMJVpL._AC_UL640_QL65_ML3_.jpg"},
    
    {"id":9,
    "title": "External Hard Drive",
    "price":64,
    "description": "WD 2TB Elements Portable External Hard Drive - USB 3.0 ",
    "category":"electronics",
    "stock_quantity" : 10,
    "image":"https://fakestoreapi.com/img/61IBBVJvSDL._AC_SY879_.jpg"},
    
    {"id":10,
    "title":"SSD",
    "price":109,
    "description": "SanDisk SSD PLUS 1TB Internal SSD - SATA III 6 Gb/s",
    "category":"electronics",
    "stock_quantity" : 10,
    "image":"https://fakestoreapi.com/img/61U7T1koQqL._AC_SX679_.jpg"},
    
    {"id":11,
    "title": "SSD",
    "price":109,
    "description": "Silicon Power 256GB SSD 3D NAND A55 SLC Cache Performance Boost SATA III 2.5",
    "category":"electronics",
    "stock_quantity" : 10,
    "image":"https://fakestoreapi.com/img/71kWymZ+c+L._AC_SX679_.jpg"},
    
    {"id":12,
    "title":"External Hard Drive",
    "price":114,
    "description":"WD 4TB Gaming Drive Works with Playstation 4 Portable External Hard Drive",
    "category":"electronics",
    "stock_quantity" : 10,
    "image":"https://fakestoreapi.com/img/61mtL65D4cL._AC_SX679_.jpg"},
    
    {"id":13,
    "title":"Computer Screen",
    "price":599,
    "description": "Acer SB220Q bi 21.5 inches Full HD (1920 x 1080) IPS Ultra-Thin",
    "category":"electronics",
    "stock_quantity" : 10,
    "image":"https://fakestoreapi.com/img/81QpkIctqPL._AC_SX679_.jpg"},
    
    {"id":14,
    "title":"Computer Screen",
    "price":999.99,
    "description":"Samsung 49-Inch CHG90 144Hz Curved Gaming Monitor (LC49HG90DMNXZA) – Super Ultrawide Screen QLED ",
    "category":"electronics",
    "stock_quantity" : 10,
    "image":"https://fakestoreapi.com/img/81Zt42ioCgL._AC_SX679_.jpg"},
    
    {"id":15,
    "title":"Jacket",
    "price":56.99,
    "description":"BIYLACLESEN Women's 3-in-1 Snowboard Jacket Winter Coats",
    "category":"women clothing",
    "stock_quantity" : 10,
    "image":"https://fakestoreapi.com/img/51Y5NI-I5jL._AC_UX679_.jpg"},
    
    {"id":16,
    "title":"Jacket",
    "price":29.95,
    "description":"Lock and Love Women's Removable Hooded Faux Leather Moto Biker Jacket",
    "category":"women clothing",
    "stock_quantity" : 10,
    "image":"https://fakestoreapi.com/img/81XH0e8fefL._AC_UY879_.jpg"},
    
    {"id":17,
    "title":"Jacket",
    "price":39.99,
    "description":"Rain Jacket Women Windbreaker Striped Climbing Raincoats",
    "category":"women clothing",
    "stock_quantity": 10,
    "image":"https://fakestoreapi.com/img/71HblAHs5xL._AC_UY879_-2.jpg"},
    
    {"id":18,
    "title":"Shirt",
    "price":9.85,
    "description":"MBJ Women's Solid Short Sleeve Boat Neck V ",
    "category":"women clothing",
    "stock_quantity" : 10,
    "image":"https://fakestoreapi.com/img/71z3kpMAYsL._AC_UY879_.jpg"},
    
    {"id":19,
    "title":"Shirt",
    "price":7.95,
    "description":"Opna Women's Short Sleeve Moisture",
    "category":"women clothing",
    "stock_quantity" : 10,
    "image":"https://fakestoreapi.com/img/51eg55uWmdL._AC_UX679_.jpg"},
    
    {"id":20,
    "title":"Shirt",
    "price":12.99,
    "description":"DANVOUY Womens T Shirt Casual Cotton Short",
    "category":"women clothing",
    "stock_quantity" : 10,
    "image":"https://fakestoreapi.com/img/61pHAEJ4NML._AC_UX679_.jpg"}]

