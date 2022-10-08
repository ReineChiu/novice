fetch("https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json").then(function(response){
        return response.json();
    }).then(function(data){
        let result=document.querySelector("#result");
        let clist=data["result"]["results"];
                    
        let site = [];
        let web = [];
        for(let i=0;i<clist.length;i++){
            let product=clist[i]; 
            site.push(product.stitle);
            web.push(product.file)
        }
        
        let newImg =[];
        for(let i=0;i<web.length;i++){
            let strWed=web[i];
            let newStrWed=strWed.replace("JPG","jpg");
            let objImg = newStrWed.split("jpg");
            let Img = objImg[0]+"jpg";
            newImg.push(Img)
        }

        let stext = document.getElementsByClassName("stext");
       
        for (let j = 0 ; j<2 ; j++){
            for (let i = 0 ; i<2 ; i++){  
                if (i != j){
                    continue;
                }
                stext[i].textContent = site[j];    
            }
        }
       
        newSite1 = site.slice(2);
        let text = document.getElementsByClassName("text");
        for (let j = 0 ; j<newSite1.length-2 ; j++){
            for (let i = 0 ; i<newSite1.length-2; i++){ 
                if (i != j){
                    continue;
                }
                text[i].textContent = newSite1[j];
            }
        }
        
        const image0 = document.createElement("img");
        image0.src = newImg[0];       
        image0.setAttribute('width', 80); // width in px  
        image0.setAttribute('height', 50); // height in px    
        const box = document.getElementById("box");
        box.appendChild(image0);

        const image1 = document.createElement("img");
        image1.src = newImg[1];       
        image1.setAttribute('width', 80); 
        image1.setAttribute('height', 50); 
        const box1 = document.getElementById("box1");
        box1.appendChild(image1);
        

        imageList = newImg.slice(2);
        for (let i=0;i<imageList.length;i++){
            for (let j=0;j<imageList.length;j++){
                if (i != j){
                    continue;
                }
                //*****變數宣告的擺放位置要注意，位置不同結果差很多******/
                let image = document.createElement("img");
                image.src = imageList[i];   
                image.setAttribute("id", "allImage");
                let photo = document.getElementById("image"+j);
                photo.appendChild(image);
            }
        }
        //****loadmore******/
        let btn = document.querySelector("#loadmore");
        let boxes = document.querySelectorAll(".box");
        let currentItem = 8;
        btn.addEventListener("click",function(){  
            
            for (let i=currentItem; i<currentItem+8; i++){
                boxes[i].style.display = "block";
            }
            currentItem +=8;
            
            if(currentItem >= boxes.length){
                btn.style.display = "none";    
            } 
        });
    }  
)    
    