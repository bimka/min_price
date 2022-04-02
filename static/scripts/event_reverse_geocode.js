ymaps.ready(init);

function init() {
    var myPlacemark,
        myMap = new ymaps.Map('map', {
            center: [55.753994, 37.622093],
            zoom: 13
        }, {
            searchControlProvider: 'yandex#search'
        });

    // Слушаем клик на карте.
    myMap.events.add('click', function (e) {
        var coords = e.get('coords');

        // Если метка уже создана – просто передвигаем ее.
        if (myPlacemark) {
            myPlacemark.geometry.setCoordinates(coords);
        }
        // Если нет – создаем.
        else {
            myPlacemark = createPlacemark(coords);
            myMap.geoObjects.add(myPlacemark);
            // Слушаем событие окончания перетаскивания на метке.
            myPlacemark.events.add('dragend', function () {
                getAddress(myPlacemark.geometry.getCoordinates());
            });
        }
        getAddress(coords);
    });

    // Создание метки.
    function createPlacemark(coords) {
        return new ymaps.Placemark(coords, {
            iconCaption: 'поиск...'
        }, {
            preset: 'islands#violetDotIconWithCaption',
            draggable: true
        });
    }

    // Определяем адрес по координатам (обратное геокодирование).
    function getAddress(coords) {
        myPlacemark.properties.set('iconCaption', 'поиск...');
        ymaps.geocode(coords).then(function (res) {
            var firstGeoObject = res.geoObjects.get(0);

            myPlacemark.properties
                .set({
                    // Формируем строку с данными об объекте.
                    iconCaption: [
                        // Название населенного пункта или вышестоящее административно-территориальное образование.
                        firstGeoObject.getLocalities().length ? firstGeoObject.getLocalities() : firstGeoObject.getAdministrativeAreas(),
                        // Получаем путь до топонима, если метод вернул null, запрашиваем наименование здания.
                        firstGeoObject.getThoroughfare() || firstGeoObject.getPremise()
                    ].filter(Boolean).join(', '),
                    // В качестве контента балуна задаем строку с адресом объекта.
                    balloonContent: firstGeoObject.getAddressLine()
                });
                
                
            // подтвердим адрес пользователя: улица и дом 
            if (window.confirm("Ваш адрес " + firstGeoObject.getThoroughfare() + ", " + firstGeoObject.getPremiseNumber() + "?")) {   
            // выводим полученный адрес обратно в html документ
            // document.getElementById("address_confirm").innerHTML = firstGeoObject.getThoroughfare() + ", " + firstGeoObject.getPremiseNumber();
                document.getElementById("address_confirm").innerHTML = firstGeoObject.getThoroughfare() + ", " + firstGeoObject.getPremiseNumber()
                document.getElementById("adress_box").style.visibility = 'visible';

                async function responseCoords() {
                    let user = {
                    name: 'Dima'
                    };

                    let response = await fetch('http://127.0.0.1:8080/', {
                        method: 'POST', 
                        headers: {
                            'Content-Type': 'application/json;charset=utf-8'
                        },
                        body: JSON.stringify(coords)
                    })
                    .then(response => response.json()
                    .then(data => {
                        document.querySelector('#shop-box').innerHTML = data.ola;
        
                    }));
        
                    let result = await response.json();
                }
                responseCoords();
                
                /*
                let coord_data = fetch('adress.json').then(function(response) {  
                    console.log(coords);  
                    // сериализируем координаты доставки
                    let json = JSON.stringify(coords); 
                    console.log(json);
                });\
                

                var ws = new WebSocket("ws://localhost:8080/ws");
                ws.onmessage = function(event) {
                    var message = document.getElementById('shop-box')
                    //var message = document.createElement('p')
                    var content = document.createTextNode(event.data)
                    message.appendChild(content)
                    //messages.appendChild(message)
            };
                function sendMessage(event) {
                    var input = 'ola';
                    ws.send(input)
                    input.value = ''
                    event.preventDefault()
            }
            */
            }
            
        });
    }
}
