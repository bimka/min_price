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
        rendering_markets_cards(products, category_id);

    })     
    );
}

function rendering_markets_cards(products, category_id) {
    // функция создает картточки с продуктами
    let div  = document.getElementById('products-' + category_id);

    for (let i = 0, ln = products.length; i < ln; i++) {
        let div_card = document.createElement('div');        
        let id = products[i].id;
        let product_name = products[i].name;
        let price = products[i].price;
        let image = products[i].image_urls[0]
        
        div_card.innerHTML = `
          <div class='card'>
            <img src="${image}" class='card-img-top'>
            <div class='card-body'>
              <h5 class='card-title'>${product_name}</h5>
              <p class='card-text'>${price} руб</p>
              <button type='button' class='btn btn-outline-primary' 
                data-id="${id}" 
                data-name="${product_name}" 
                data-price="${price}" 
                onclick='add_to_cart(this.dataset.id, this.dataset.name, this.dataset.price)'>
                    Добавить в корзину
              </button>
            </div>
          </div>`;

        div_card.setAttribute('id', products[i].legacy_product_id);
        div_card.setAttribute('class', 'col');
        div.appendChild(div_card);
    }
}
