async function responseCoords(coords) {
    // функция responseCoords отправляет на сервер координаты доставки
    let response = await fetch('http://127.0.0.1:8080/', {
        method: 'POST', 
        headers: {
            'Content-Type': 'application/json;charset=utf-8'
        },
        body: JSON.stringify(coords)
    })    
    .then(response => response.json()    
    .then(markets => {
        markets = JSON.parse(markets)
        console.log(markets);
        //document.querySelector('#shop-box').innerHTML = markets.id;    
        rendering_markets_list(markets);
        //markets_json = JSON.parse(markets);
        console.log(markets);

    })    
    );
}


function rendering_markets_list(markets) {
    // функция создает ненумерованный список с магазинами
    let div  = document.getElementById('markets');
    let ul = document.createElement('ul');
    div.appendChild(ul);

    for (let i = 0, ln = markets.length; i < ln; i++) {
        let li = document.createElement('li');
        img_src = markets[i].retailer.appearance.logo_image;
        li.innerHTML = "<img src=\"" + img_src + "\" width=\"300px\" height=\"100px\" alt=\"market_logo\">";
        li.innerHTML += '<div class="market">'+markets[i].name+'</div>';
        li.setAttribute('id', markets[i].id);
        ul.appendChild(li);
    }
}

// попробуем передать логотип магазина
function logo_rendering(id, img_src) {
    let el = document.getElementById(id);
    el.innerHTML="<img src=\"http://placehold.it/350x350\" width=\"400px\" height=\"150px\">";

}