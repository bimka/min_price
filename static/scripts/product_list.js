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
    //let div_card_group = document.createElement('div');
    //div.appendChild(div);

    for (let i = 0, ln = products.length; i < ln; i++) {
        let div_card = document.createElement('div');
        img_src = products[i].image_urls[0];
        product_name = products[i].name;
        price = products[i].price;
        image = products[i].image_urls[0]
        div_card.innerHTML = "<div class='card'>\
                              <img src="+image+" class='card-img-top'>\
                              <div class='card-body'>\
                                  <h5 class='card-title'>"+product_name+"</h5>\
                                  <p class='card-text'>"+price+" руб</p>\
                                  <button type='button' class='btn btn-outline-primary'>Добавить в корзину</button>\
                              </div>\
                              </div>";
                              
        //div_card.innerHTML = "ola";
        //li.innerHTML += "<img src="+image+" class='img-fluid' alt='Изображение товара'>";
        div_card.setAttribute('id', products[i].legacy_product_id);

        div_card.setAttribute('class', 'col');
        div.appendChild(div_card);
    }
}