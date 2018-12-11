//chapter:6
function capitalize(string){
      var cstr = string.toLowerCase();
      return cstr;
                          }

function mySubmit(name) {
     document.getElementById('hiddenField').value = name;
     document.getElementById("myForm").submit();
                        }

function final_btn(){

    document.getElementById("step_2").style.display = "none";
    var str =  "";
    for(var j in gussing_name_array){
            str += gussing_name_array[j];
                                  }
    var s = capitalize(str);
    var gnai = str.search("undefined");
    if(gnai == -1){
        // document.getElementById("final_r").innerHTML = s;
        mySubmit(s)

    }else{
          document.getElementById("final_r").innerHTML = " you selected more lettrs in 2nd stage try again with restart......";
    };
    

    document.getElementById("final_btn").style.display = "none";
    document.getElementById("final_r").style.display = "block";
    console.log(gnai);
}