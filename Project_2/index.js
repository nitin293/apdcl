const searchValueFire = document.querySelector(".searchValueFire");



function Upload() {
    var fileUpload = document.getElementById("fileUpload");
    var regex = /^([a-zA-Z0-9\s_\\.\-:])+(.csv|.txt)$/;
    if (regex.test(fileUpload.value.toLowerCase())) {
        if (typeof (FileReader) != "undefined") {
            var reader = new FileReader();
            reader.onload = function (e) {
                var table = document.createElement("table");
                var rows = e.target.result.split("\n");
                for (var i = 0; i < rows.length; i++) {
                    var cells = rows[i].split(",");
                    if (cells.length > 1) {
                        var row = table.insertRow(-1);
                        for (var j = 0; j < cells.length; j++) {
                            var cell = row.insertCell(-1);
                            cell.innerHTML = cells[j];
                        }
                    }
                }
                const td = table.querySelectorAll('td');
                console.log(td);
                td.forEach(item=>{
                    console.log(item.toString());
                    item.forEach(ele=>console.log(ele))
                    searchValueFire.addEventListener("click", (e)=>{
                        const searchValue = document.querySelector(".searchValue");
                        e.preventDefault();
                        console.log(searchValue.value)
                        const h1 = document.querySelector('h1');
                        if(searchValue === item.toString()){
                            h1.innerText = item;
                        }
                        else{
                            h1.innerText = "nahi hoga";
                        }
                    })
                })

               

                var dvCSV = document.getElementById("dvCSV");
                dvCSV.innerHTML = "";
                dvCSV.appendChild(table);


                // search on the basic of user input
            
            }
            // searchValue=document.getElementsByClassName('searchValue');
            reader.readAsText(fileUpload.files[searchValue]);
        } else {
            alert("This browser does not support HTML5.");
        }
    } else {
        alert("Please upload a valid CSV file.");
    }
}

