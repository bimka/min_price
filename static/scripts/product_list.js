async function send_url(url, store_id, category_id) {
    // функция отправляет на сервер store_id и canonical_url подкатегории с продуктами
    data = [url, store_id]
    let response = await fetch('http://127.0.0.1:8080/send_product_list', {
        method: 'POST', 
        headers: {
            'Content-Type': 'application/json;charset=utf-8'
        },
        body: JSON.stringify(data)
    })    
    .then(response => response.json()    
    .then(products => {
        console.log(products, category_id);  
        rendering_markets_list(products, category_id);

    })    
    );
}

function rendering_markets_list(products, category_id) {
    // функция создает ненумерованный список с продуктами
    let div  = document.getElementById('products-' + category_id);
    let ul = document.createElement('ul');
    div.appendChild(ul);

    for (let i = 0, ln = products.length; i < ln; i++) {
        let li = document.createElement('li');
        img_src = products[i].image_urls[0];
        product_name = products[i].name;
        price = products[i].price;
        image = products[i].image_urls[0]
        li.innerHTML = "<span>"+product_name+"</span> - <span>"+price+" руб</span>";
        li.innerHTML += "<img src="+image+" class='img-fluid' alt='Изображение товара'>";
        li.setAttribute('id', products[i].legacy_product_id);
        li.setAttribute('class', 'product');
        ul.appendChild(li);
    }
}