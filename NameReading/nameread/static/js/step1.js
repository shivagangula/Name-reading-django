                       // step_1 user array to vertcal array script:

var sub0 = [];
var sub1 = [];
var sub2 = [];
var sub3 = [];
var sub4 = [];

var vertical_array = [];

function heri_to_verti(){
      for(var l0 in selected_heri_array ){
          sub0.push(selected_heri_array[l0][0]);
          
      }
     for(var l1 in selected_heri_array ){
          sub1.push(selected_heri_array[l1][1]);
         
      }
     for(var l2 in selected_heri_array ){
          sub2.push(selected_heri_array[l2][2]);
      }
     for(var l3 in selected_heri_array ){
          sub3.push(selected_heri_array[l3][3]);
        
      }
     for(var l4 in selected_heri_array ){
          sub4.push(selected_heri_array[l4][4]);
         
      } 
    vertical_array.push(sub0);
    vertical_array.push(sub1);
    vertical_array.push(sub2);
    vertical_array.push(sub3);
    vertical_array.push(sub4);
}




//chapter:3
// next buttons for secound step:
function next_btn(){
     document.getElementById("step_1").style.display = "none";    
     document.getElementById("step_2").style.display = "block";
    
     document.getElementById("next_btn").style.display = "none";
     document.getElementById("final_btn").style.display = "block";
      show2();
   
}
