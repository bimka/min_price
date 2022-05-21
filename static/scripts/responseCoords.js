async function responseCoords(coords) {
    // функция responseCoords отправляет на сервер координаты доставки
    let response = await fetch('http://127.0.0.1:8080/', {
        method: 'POST', 
        headers: {
            'Content-Type': 'application/json;charset=utf-8'
        },
        body: JSON.stringify(coords)
    }) ; 
      markets = await response.json();
      rendering_markets_list(markets);
}


function rendering_markets_list(markets) {
    // функция создает ненумерованный список с магазинами
    let div  = document.getElementById('markets');
    let div_row = document.createElement('div');
    div_row.setAttribute('class', 'row row-cols-xs-1 row-cols-sm-2 row-cols-md-4 row-cols-lg-6 row-cols-xl-8 row-cols-xxl-10');
    div.appendChild(div_row);

    for (let i = 0, ln = markets.length; i < ln; i++) {
        let div_ch = document.createElement('div');
        img_src = markets[i].logo_image;
        market_src = markets[i].store_id;
        div_ch.innerHTML = "<a href=\"/" + markets[i].retailer + "/sid=" + market_src + "\"><img src=\"" + img_src + "\" width=\"300px\" height=\"100px\" alt=\"market_logo\"></a>";
        //div_ch.innerHTML = '<div class="market">'+markets[i].name+'</div>';
        div_ch.setAttribute('id', markets[i].id);
        //div_ch.setAttribute('class', );
        div_row.appendChild(div_ch);
    }
    div.appendChild(div_row);
}

