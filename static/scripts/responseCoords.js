async function responseCoords(coords) {
    // функция responseCoords отправляет на сервер координаты доставки
    console.log('func responseCoord has been worked');
    let response = await fetch('https://mindeliveryprice.ru/', {
        method: 'POST', 
        mode: 'no-cors',
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
    div_row.setAttribute('class', 'row row-cols-xs-1 row-cols-sm-1 row-cols-md-2 row-cols-lg-3 row-cols-xl-4 row-cols-xxl-4');
    div.appendChild(div_row);

    for (let i = 0, ln = markets.length; i < ln; i++) {
        let a = document.createElement('a');        
        img_src = markets[i].retailer.appearance.logo_image;        
        market_src = markets[i].store_id;
        let delivery_info = '';
        if (markets[i].delivery_forecast_text) {
            delivery_info = markets[i].delivery_forecast_text;
            
        } else {
            delivery_info = markets[i].closest_shipping_options[0].summary;
        }
        let delivery_price = markets[i].min_order_amount;
        let background_color_text = '#ffffff';
        if (markets[i].retailer.appearance.background_color == '#ffffff') {
            background_color_text = '#000000';
        }
        a.setAttribute('href',  markets[i].retailer.slug + "/sid=" + market_src);
        a.innerHTML = `
          <img src="${img_src}"  alt="market_logo">
          <p>Доставка ${delivery_info}</p>
          <p>от ${delivery_price} руб</p>
          `;
        
        a.setAttribute('id', markets[i].id);
        a.setAttribute('class',  'market_info');
        a.style.backgroundColor = markets[i].retailer.appearance.background_color;
        a.style.color = background_color_text;
        div_row.appendChild(a);
    }
    div.appendChild(div_row);
}

