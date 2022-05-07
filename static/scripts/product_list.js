async function send_url(url, store_id, category_id) {
    // функция отправляет на сервер store_id и canonical_url подкатегории с продуктами
    data = [url, store_id];
    let response = await fetch('http://127.0.0.1:8080/send_product_list', {
        method: 'POST', 
        headers: {
            'Content-Type': 'application/json;charset=utf-8'
        },
        body: JSON.stringify(data)
    })    
    .then(response => response.json()    
    .then(products => {
        //console.log(products.find(item => item.price == 92.99));  
        rendering_markets_cards(products, category_id);

    })     
    );
}
console.log(products);
function rendering_markets_cards(products, category_id) {
    // функция создает картточки с продуктами
    let div  = document.getElementById('products-' + category_id);

    products.forEach(product => {             
        let div_card = document.createElement('div');  
        let image = product.image_urls[0]        
        div_card.innerHTML = `
          <div class='card'>
            <img src="${image}" class='card-img-top'>
            <div class='card-body'>
              <h5 class='card-title'>${product.name}</h5>
              <p class='card-text'>${product.price} руб</p>
              <button type='button' class='btn btn-outline-primary' 
                data-id="${product.id}" 
                data-name="${product.name}" 
                data-price="${product.price}" 
                onclick='add_to_cart(this.dataset.id, this.dataset.name, 
                  this.dataset.price)'>
                Добавить в корзину
              </button>
            </div>
          </div>`;
        div_card.setAttribute('id', product.legacy_product_id);
        div_card.setAttribute('class', 'col');
        div.appendChild(div_card);    
    })
    
}
