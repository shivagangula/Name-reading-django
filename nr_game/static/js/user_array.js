//chapter:1
//default arrays for step1:

var harizontal_array_line_0 = ["A","B","C","D","E"];
var harizontal_array_line_1 = ["F","G","H","I","J"];
var harizontal_array_line_2 = ["K","L","M","N","O"];
var harizontal_array_line_3 = ["P","Q","R","S","T"];
var harizontal_array_line_4 = ["U","V","W","X","Y"];
var harizontal_array_line_5 = ["Z"," "," "," "," "];


// function for show alphabts in step1:
function show(){
   
    for(var i in harizontal_array_line_0){
        document.getElementById("alpha1").innerHTML+= harizontal_array_line_0[i]+ "  ";
    }
    for(var i in harizontal_array_line_1){
        document.getElementById("alpha2").innerHTML+= harizontal_array_line_1[i]+ "  ";
    }
    for(var i in harizontal_array_line_2){
        document.getElementById("alpha3").innerHTML+= harizontal_array_line_2[i]+ "  ";
    }
    for(var i in harizontal_array_line_3){
        document.getElementById("alpha4").innerHTML+= harizontal_array_line_3[i]+ "  ";
    }
    for(var i in harizontal_array_line_4){
        document.getElementById("alpha5").innerHTML+= harizontal_array_line_4[i]+ "  ";
    }
    for(var i in harizontal_array_line_5){
        document.getElementById("alpha6").innerHTML+= harizontal_array_line_5[i]+ "  ";
    }
}

  alert("welcome to name reading game please read instructions carefully then play");
//functions for getting seleted array:

function selectting_heri_line_buttion1(){
    selected_heri_array.push(harizontal_array_line_0);
    btn1();
    
}
function selectting_heri_line_buttion2(){
     selected_heri_array.push(harizontal_array_line_1);
    btn2(); 
}
function selectting_heri_line_buttion3(){
     selected_heri_array.push(harizontal_array_line_2);
   btn3();
}
function selectting_heri_line_buttion4(){
     selected_heri_array.push(harizontal_array_line_3);
   btn4();
}
function selectting_heri_line_buttion5(){
     selected_heri_array.push(harizontal_array_line_4);
    btn5();
}
function selectting_heri_line_buttion6(){
     selected_heri_array.push(harizontal_array_line_5);
    btn6();
}

//harizentol array from selction to vertical array for secound step conversion:
var selected_heri_array = [];
