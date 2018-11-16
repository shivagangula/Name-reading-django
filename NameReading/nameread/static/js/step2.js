//chapter:4
//step_2 script:


// function for show alphabts in step2:
function show2(){
    heri_to_verti();
    for(var i in sub0){
        document.getElementById("alpha11").innerHTML+= sub0[i]+ "  ";
    }
    for(var i in sub1){
        document.getElementById("alpha22").innerHTML+= sub1[i]+ "  ";
    }
    for(var i in sub2){
        document.getElementById("alpha33").innerHTML+= sub2[i]+ "  ";
    }
    for(var i in sub3){
        document.getElementById("alpha44").innerHTML+= sub3[i]+ "  ";
    }
    for(var i in sub4){
        document.getElementById("alpha55").innerHTML+= sub4[i]+ "  ";
    }
    console.log("h",vertical_array);
}

// array for storing single array form user:
var gussing_name_array = [];

//counts for circles and gussing array index:
 var clicks2 = -1;
function g_count(){
    clicks2 += 1;
    return clicks2;
}



//funtions for pushing words into gussing array:
function step2_btn_1(){
   var k = g_count();
    gussing_name_array.push( sub0[k] );
    btn11();
}
function step2_btn_2(){
   var k = g_count();
    gussing_name_array.push( sub1[k] );
    btn22();
}
function step2_btn_3(){
  var k = g_count();
    gussing_name_array.push( sub2[k] );
    btn33();
}
function step2_btn_4(){
   var k = g_count();
    gussing_name_array.push( sub3[k] );
    btn44();
}
function step2_btn_5(){
   var k = g_count();
    gussing_name_array.push( sub4[k] );
    btn55();
}
function f4(){
    console.log("k",gussing_name_array);
}








