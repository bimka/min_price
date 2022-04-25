async function send_url(url, store_id, retailer) {
    // функция отправляет на сервер store_id и canonical_url подкатегории с продуктами
    data = [url, store_id, retailer]
    let response = await fetch('http://127.0.0.1:8080/send_product_list', {
        method: 'POST', 
        headers: {
            'Content-Type': 'application/json;charset=utf-8'
        },
        body: JSON.stringify(data)
    })    
    .then(response => response.json()    
    .then(products => {
        console.log(products);  
        rendering_markets_list(products);

    })    
    );
}

function rendering_markets_list(products) {
    // функция создает ненумерованный список с продуктами
    let div  = document.getElementById('products');
    let ul = document.createElement('ul');
    div.appendChild(ul);

    for (let i = 0, ln = products.length; i < ln; i++) {
        let li = document.createElement('li');
        img_src = products[i].image_urls[0];
        product_name = products[i].name;
        price = products[i].price;
        //market_src = markets[i].store_id;
        //li.innerHTML = "<a href=\"/" + markets[i].retailer + "/sid=" + market_src + "\"><img src=\"" + img_src + "\" width=\"300px\" height=\"100px\" alt=\"market_logo\"></a>";
        //li.innerHTML += '<div class="market">'+markets[i].name+'</div>';
        li.innerHTML = product_name, price;
        li.setAttribute('id', products[i].legacy_product_id);
        ul.appendChild(li);
    }
}