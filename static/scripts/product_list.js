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

    })    
    );
}