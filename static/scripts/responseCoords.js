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
    // функция список с блоками, содержащий магазины
    let div  = document.getElementById('markets');
    let div_row = document.createElement('div');
    div_row.setAttribute('class', 'row row-cols-xs-1 row-cols-sm-2 row-cols-md-4 row-cols-lg-6 row-cols-xl-8 row-cols-xxl-10');
    div.appendChild(div_row);

    for (let i = 0, ln = markets.length; i < ln; i++) {
        let a = document.createElement('a');        
        img_src = markets[i].retailer.appearance.logo_image;        
        market_src = markets[i].store_id;
        a.setAttribute('href',  markets[i].retailer.slug + "/sid=" + market_src);
        a.innerHTML = "<img src=\"" + img_src + "\"  alt=\"market_logo\">";
        a.setAttribute('id', markets[i].id);
        a.setAttribute('class',  'market_info');
        a.style.backgroundColor = markets[i].retailer.appearance.background_color;
        div_row.appendChild(a);
    }
    div.appendChild(div_row);
}

