fetch("https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json").then(function(response){
        return response.json();
    }).then(function(data){
        //把已經取得資料,把資料呈現到畫面上
        let result=document.querySelector("#result");
        let clist=data["result"]["results"];
                    
        let site = [];
        let web = [];
        for(let i=0;i<clist.length;i++){
            let product=clist[i]; //讓資料分別印出，就可以分別處理
            site.push(product.stitle);
            web.push(product.file)
        }//console.log(site);//取得(site、web)列表
        //console.log(typeof web);
        
        let newImg =[];
        for(let i=0;i<web.length;i++){
            let strWed=web[i];//讓陣列中的網址變成字串
            //console.log(typeof strWed); 
            let newStrWed=strWed.replace("JPG","jpg");//無法用多個分隔符,就把JPG換掉吧
            let objImg = newStrWed.split("jpg");//當引數為空時，則該方法會把整個字串作為一個元素的陣列返回
            let Img = objImg[0]+"jpg";
            newImg.push(Img)//newImg 得到所有第一張圖的陣列
        }

        let text1 = document.getElementsByClassName("text1");
        //console.log(text1);
        for (let j = 0 ; j<2 ; j++){
            for (let i = 0 ; i<2 ; i++){  //欲達成同標籤的文字都被修改，需用for迴圈
                if (i != j){
                    continue;
                }
                text1[i].textContent = site[j];
            }
        }
        newSite1 = site.slice(2);
        let text2 = document.getElementsByClassName("text2");
        for (let j = 0 ; j<2 ; j++){
            for (let i = 0 ; i<2 ; i++){ 
                if (i != j){
                    continue;
                }
                text2[i].textContent = newSite1[j];
            }
        }
        newSite2 = site.slice(4);
        let text3 = document.getElementsByClassName("text3");
        for (let j = 0 ; j<6 ; j++){//j<6 不是數字似乎會報錯
            for (let i = 0 ; i<6 ; i++){ 
                if (i != j){
                    continue;
                }
                text3[i].textContent = newSite2[j];
            }
        }

        const image = document.createElement("img");
        image.src = newImg[0];       
        image.setAttribute('width', 80); // width in px  
        image.setAttribute('height', 50); // height in px    
        const box = document.getElementById("box");
        box.appendChild(image);

        const image1 = document.createElement("img");
        image1.src = newImg[1];       
        image1.setAttribute('width', 80); // width in px  
        image1.setAttribute('height', 50); // height in px   
        const box1 = document.getElementById("box1");
        box1.appendChild(image1);
        
        const image2 = document.createElement("img");
        image2.src = newImg[2];   
        image2.setAttribute("id", "allImage");
        //image2.setAttribute('height', 100); // height in px
        //image2.setAttribute('width', 200); // width in px      
        const long = document.getElementById("long");
        long.appendChild(image2);

        const image3 = document.createElement("img");
        image3.src = newImg[3];       
        image3.setAttribute("id", "allImage");     
        const meet = document.getElementById("meet");
        meet.appendChild(image3);

        const image4 = document.createElement("img");
        image4.src = newImg[4];  
        image4.setAttribute("id", "allImage");   
        const text3Img1 = document.getElementById("text3Img1");
        text3Img1.appendChild(image4);

        const image5 = document.createElement("img");
        image5.src = newImg[5];  
        image5.setAttribute("id", "allImage");   
        const text3Img2 = document.getElementById("text3Img2");
        text3Img2.appendChild(image5);

        const image6 = document.createElement("img");
        image6.src = newImg[6];  
        image6.setAttribute("id", "allImage");   
        const text3Img3 = document.getElementById("text3Img3");
        text3Img3.appendChild(image6);

        const image7 = document.createElement("img");
        image7.src = newImg[7];  
        image7.setAttribute("id", "allImage");   
        const text3Img4 = document.getElementById("text3Img4");
        text3Img4.appendChild(image7);

        const image8 = document.createElement("img");
        image8.src = newImg[8];  
        image8.setAttribute("id", "allImage");   
        const text3Img5 = document.getElementById("text3Img5");
        text3Img5.appendChild(image8);

        const image9 = document.createElement("img");
        image9.src = newImg[9];  
        image9.setAttribute("id", "allImage");   
        const text3Img6 = document.getElementById("text3Img6");
        text3Img6.appendChild(image9);   
    }  
)    