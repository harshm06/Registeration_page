function rec (){

    var xmlhttp = new XMLHttpRequest();
    var data;

    xmlhttp.onreadystatechange = function () {
        
        if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
            
            data = JSON.parse(xmlhttp.response);
                .write(data[0].mobileno);

        }
    }
    
    xmlhttp.open("GET", "http://127.0.0.1:8000/test/data/", true);
    xmlhttp.send();
}
