
async function responseCoords(coords) {
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
        document.querySelector('#shop-box').innerHTML = data;        
    })    
    );
}