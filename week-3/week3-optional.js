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
        for (let j = 0 ; j<8 ; j++){
            for (let i = 0 ; i<8; i++){ 
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
        const sbox = document.getElementById("sbox");
        sbox.appendChild(image0);

        const image1 = document.createElement("img");
        image1.src = newImg[1];       
        image1.setAttribute('width', 80); 
        image1.setAttribute('height', 50); 
        const sbox1 = document.getElementById("sbox1");
        sbox1.appendChild(image1);
              
        imageList = newImg.slice(2);
        for (let i=0;i<8;i++){
            for (let j=0;j<8;j++){
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
//*****變數宣告的擺放位置要注意，位置不同結果差很多******
        //****loadmore******/
        let newSite2 = site.slice(10);
        let imageList1 = newImg.slice(10);

        let btn = document.querySelector("#loadmore")
        let currentItem = 0;
        
        btn.addEventListener("click",function(){  
           
            for (let i=currentItem;i<currentItem+8 ;i++){
                for (let j=currentItem;j<currentItem+8;j++){
                    if (i != j){
                        continue;
                    }
                    //*****變數宣告的擺放位置要注意，位置不同結果差很多******
                    let newblock = document.getElementById("block");
                    newblock.setAttribute("id", "block");
            
                    let newbox = document.createElement("div");
                    newbox.setAttribute("id", "newbox");
                    newblock.appendChild(newbox)

                    let g = document.createElement("img");
                    g.src = imageList1[i];
                    g.setAttribute("id", "allImage");
                    newbox.appendChild(g)

                    let t = document.createElement("div");
                    t.setAttribute("id", "newtTextbox"); 
                    t.textContent = newSite2[j]
                    newbox.appendChild(t)
                }
            }
            currentItem += 8;  
            
            if(currentItem >=newSite2.length){
                btn.style.display = "none"
            }
        });
    }   
)    
    