function get():
    // функция создает ненумерованный список с продуктами
    let div  = document.getElementById('markets');
    let ul = document.createElement('ul');
    div.appendChild(ul);

    for (let i = 0, ln = markets.length; i < ln; i++) {
        let li = document.createElement('li');
        img_src = markets[i].logo_image;
        market_src = markets[i].store_id;
        li.innerHTML = "<a href=\"/" + markets[i].retailer + "/sid=" + market_src + "\"><img src=\"" + img_src + "\" width=\"300px\" height=\"100px\" alt=\"market_logo\"></a>";
        li.innerHTML += '<div class="market">'+markets[i].name+'</div>';
        li.setAttribute('id', markets[i].id);
        ul.appendChild(li);
    }
}