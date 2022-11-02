function searchData(){
    let search=document.getElementById("searchUsername").value;
    //fetch(`/api/member?username=${search}`, {method:"GET"}) //此法也可，只是不懂
    //127.0.0.1:3000為何不用打？
    fetch("/api/member?username="+search, {method:"GET"}).then((response) => {
        //console.log(response)
        return response.json();
    }).then((data) => {
        let list=data["data"];
        //console.log(list);
        //清除原先節點，清空畫面,讓資料不要往下接
        document.getElementById("searchResult").innerHTML="";
        let result = document.getElementById("searchResult");
        let searchResult = document.createElement("div");
        searchResult.setAttribute("id", "searchUsername");
        searchResult.textContent = list["name"] + '('+list["username"]+')';
        //console.log(searchResult);
        result.appendChild(searchResult);
    }).catch((fail) => {//catch 用法需多了解
        searchResult.textContent ="查無此使用者";
        changeResult.setAttribute("id", "errorSearch");
        result.appendChild(searchResult)
    });
}

function changeData(){
    let newName=document.getElementById("changeName").value;
    fetch("/api/member", 
        {method:"PATCH",
        headers:{"content-Type":"application/json"},
        body: JSON.stringify({"name": newName})
        }).then((response) => {
        //console.log(response)
        return response.json();
    }).then((data) => {
         //清除原先節點，清空畫面,讓資料不要往下接
         //document.getElementById("changeResult").innerHTML="";
         let result = document.getElementById("changeResult");
         let changeResult = document.createElement("div");
         changeResult.setAttribute("id", "newUsername");
         changeResult.textContent ="更新成功";
         result.appendChild(changeResult);
         let newUserName = document.querySelector(".welcome");
         newUserName.textContent = newName+"，歡迎登入系統";
    }).catch((fail) => {
        changeResult.textContent ="更新失敗";
        changeResult.setAttribute("id", "errorUsername");
        result.appendChild(changeResult);
    });
}