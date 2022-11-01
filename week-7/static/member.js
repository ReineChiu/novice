function searchData(){
    let search=document.getElementById("searchUsername").value;
    fetch("/api/member?username="+search, {method:"GET"}).then((response) => {
        return response.json();
    }).then((data) => {
        let list=data["data"];
        document.getElementById("searchResult").innerHTML="";
        let result = document.getElementById("searchResult");
        let searchResult = document.createElement("div");
        searchResult.setAttribute("id", "searchUsername");
        searchResult.textContent = list["name"] + '('+list["username"]+')';
        result.appendChild(searchResult);
    }).catch((fail) => {
        searchResult.textContent ="查無此使用者";
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
        return response.json();
    }).then((data) => {
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