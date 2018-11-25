//chapter:2 & 5
//circle for step1:

// function for when user selcted line then counted circle appeare:
     var clicks = 0;
function f1(){
    clicks += 1;            
    return clicks;
 }

// button functions for circle count:
function btn1(){
    var circle = document.createElement("div");
    circle.setAttribute("id","cir");
    z = f1();
    var node = document.createTextNode("letter no : "+z);
    circle.appendChild(node);
    var hari_line_arry1 = document.getElementById("line_block1");
    var line_btn1 = document.getElementById("line_btn1");
   
    if(line_btn1.value == 1){
        hari_line_arry1.insertBefore(circle,line_btn1);
        
    }
}
function btn2(){
    var circle = document.createElement("div");
                circle.setAttribute("id","cir");
    z = f1();
                 var node = document.createTextNode("letter no : "+z);
                 circle.appendChild(node);
    var hari_line_arry2 = document.getElementById("line_block2");
    var line_btn2 = document.getElementById("line_btn2");
    f1();
    if(line_btn2.value == 2){
        hari_line_arry2.insertBefore(circle,line_btn2);
        
    }
}
function btn3(){
    var circle = document.createElement("div");
                circle.setAttribute("id","cir");
    z = f1();
                 var node = document.createTextNode("letter no : "+z);
                 circle.appendChild(node);
    var hari_line_arry3 = document.getElementById("line_block3");
    var line_btn3 = document.getElementById("line_btn3");
   
    if(line_btn3.value == 3){
        hari_line_arry3.insertBefore(circle,line_btn3);
        
    }
}
function btn4(){
    var circle = document.createElement("div");
                circle.setAttribute("id","cir");
    z = f1();
                 var node = document.createTextNode("letter no : "+z);
                 circle.appendChild(node);
    var hari_line_arry4 = document.getElementById("line_block4");
    var line_btn4 = document.getElementById("line_btn4");
   
    if(line_btn4.value == 4){
        hari_line_arry4.insertBefore(circle,line_btn4);
        
    }
}
function btn5(){
    var circle = document.createElement("div");
                circle.setAttribute("id","cir");
    z = f1();
                var node = document.createTextNode("letter no : "+z);
                 circle.appendChild(node);
    var hari_line_arry5 = document.getElementById("line_block5");
    var line_btn5 = document.getElementById("line_btn5");
    
    if(line_btn5.value == 5){
        hari_line_arry5.insertBefore(circle,line_btn5);
        
    }
}
function btn6(){
    var circle = document.createElement("div");
                circle.setAttribute("id","cir");
    z = f1();
                var node = document.createTextNode("letter no : "+z);
                 circle.appendChild(node);
    var hari_line_arry6 = document.getElementById("line_block6");
    var line_btn6 = document.getElementById("line_btn6");
    
    if(line_btn6.value == 6){
        hari_line_arry6.insertBefore(circle,line_btn6);
        
    }
}







//chapter:5
//circles for step2:
   var clicking2 = 0
function clicks_2(){
    clicking2 += 1;
    return clicking2;
}
//functions for count circles:

function btn11(){
    var circle = document.createElement("div");
                circle.setAttribute("id","cir");
                   k= clicks_2();
                 var node = document.createTextNode("letter no: "+k);
                 circle.appendChild(node);
    var hari_line_arry11 = document.getElementById("line_block11");
    var line_btn11 = document.getElementById("line_btn11");
   
    if(line_btn11.value == 11){
        hari_line_arry11.insertBefore(circle,line_btn11);
        
    }
}
function btn22(){
    var circle = document.createElement("div");
                circle.setAttribute("id","cir");
    k= clicks_2();
               var node = document.createTextNode("letter no: "+k);
                 circle.appendChild(node);
    var hari_line_arry22 = document.getElementById("line_block22");
    var line_btn22 = document.getElementById("line_btn22");
    
    if(line_btn22.value == 22){
        hari_line_arry22.insertBefore(circle,line_btn22);
        
    }
}
function btn33(){
    var circle = document.createElement("div");
                circle.setAttribute("id","cir");
    k = clicks_2();
                var node = document.createTextNode("letter no: "+k);
                 circle.appendChild(node);
    var hari_line_arry33 = document.getElementById("line_block33");
    var line_btn33 = document.getElementById("line_btn33");
   
    if(line_btn33.value == 33){
        hari_line_arry33.insertBefore(circle,line_btn33);
        
    }
}
function btn44(){
    var circle = document.createElement("div");
                circle.setAttribute("id","cir");
    k = clicks_2();
                var node = document.createTextNode("letter no: "+k);
                 circle.appendChild(node);
    var hari_line_arry44 = document.getElementById("line_block44");
    var line_btn44 = document.getElementById("line_btn44");
   
    if(line_btn44.value == 44){
        hari_line_arry44.insertBefore(circle,line_btn44);
        
    }
}
function btn55(){
    var circle = document.createElement("div");
                circle.setAttribute("id","cir");
    k = clicks_2();
               var node = document.createTextNode("letter no: "+k);
                 circle.appendChild(node);
    var hari_line_arry55 = document.getElementById("line_block55");
    var line_btn55 = document.getElementById("line_btn55");
    
    if(line_btn55.value == 55){
        hari_line_arry55.insertBefore(circle,line_btn55);
        
    }
}
