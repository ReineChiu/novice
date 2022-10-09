// 先建立 
let new_element = document.createElement('div')

// 再追加 
let my_container = document.getElementById("my-container")

my_container.appendChild(new_element);

// 新建立標籤屬性，用js設定 
new_element.setAttribute('id', 'new-element-id')

new_element.classList.add('lorem')

new_element.classList.add('ipsum')

//添加多個元素
let giants = ['marx', 'engels', 'lenin']

for(i=0; i < xxxxx  ;i++){
    let g = document.createElement('div');

    g.setAttribute('id', giants[i]);
    
    document.body.appendChild(g);
    
}

//下面 將添加5次的div(包括圖像和跨度和跨度文本)與一些數據。
insert_divs = function() {

    let parent = document.getElementsByClassName("panel-body")[0];

    let installments = ['Installment 1', 'Installment 2', 'Installment 3', 'Installment 4', 'Installment 5'];
    
    installments.forEach(function(e){
    
    let sp = document.createElement('span');
    
    let img = document.createElement('img');
    
    let installment = document.createElement('div');
    
    let span_text = document.createTextNode(e);
    
    sp.appendChild(span_text);
    
    img.setAttribute('src', 'https://cdn3.iconfinder.com/data/icons/google-material-design-icons/48/ic_cancel_48px-128.png')
    
    installment.classList.add('panel-more1');
    
    installment.appendChild(img);
    
    installment.appendChild(sp);
    
    parent.appendChild(installment);
    
    });
    }

    //建立一個box，下有imagebox & textbox
    let image = document.createElement("img");


      ///////////////用js建立一個box(包含imagebox textbox)///////////////////////////
      let box = document.createElement("div");






      //////////////////////////////////////////////

                      ////////成功加入一個box///////
/*                
        let newblock = document.getElementById("block");
        newblock.setAttribute("id", "block");

        let newbox = document.createElement("div");
        newbox.setAttribute("id", "newbox");
        newblock.appendChild(newbox)

        let g = document.createElement("img");
        g.src = imageList1[0];
        g.setAttribute("id", "allImage");
        newbox.appendChild(g)

        let t = document.createElement("div");
        t.setAttribute("id", "newtTextbox"); 
        t.textContent = newSite2[0]
        newbox.appendChild(t)
*/
//*****變數宣告的擺放位置要注意，位置不同結果差很多******
                ///////加入八個box////////
/*
        let newblock = document.getElementById("block");
        newblock.setAttribute("id", "block");

        for (let i=0;i<8;i++){
            for (let j=0;j<8;j++){
                if (i != j){
                    continue;
                }
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
*/
