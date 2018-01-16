var fs = require('fs');
 

var contents = fs.readFileSync('problem24.input', 'utf8');
console.log(contents);

var array = contents.split("\n");

//test
//contents="2/2,2/3,3/4,3/5,0/1,10/1,9/10,0/2"
//var array = contents.split(",");

console.log(array);

function strength(bridges){
    var br=bridges;
    while(br.indexOf(" - ")>-1){
        br=br.replace(" - ","/");
    }
    br=br.substring(0,br.length-1);
    
    var a=br.split("/");
    var sum = a.reduce(function(a, b) { return parseInt(a) + parseInt(b); }, 0);
    
    return sum;    
}

function path(deep, bridges, size, length, arr) {
    if (deep==2) {
        console.log(Array(deep).join(" ")+"path ", deep, size, length, bridges);
    }

    var max=length;  
    var maxd=deep;  
 
    for (var i in arr) {
        var els = arr[i].split("/");
        var a=parseInt(els[0]);
        var b=parseInt(els[1]);



        if (a==size) {
            var size2=b;
            //console.log("blah", arr[i]);

            var currlength=length+a+b;
            var arr2=arr.join(";").split(";");
            arr2.splice(i,1);
            var bridges2 = bridges+ arr[i]+ " - ";
    
            var l=path(deep+1, bridges2, size2, currlength, arr2);
            if (l.length>maxd) {
                maxd=l.length;
                max=l.strength;
            }
            if (l.length==maxd && l.strength>max) {
                    max=l.strength;
            }

        }

        else if (b==size) {
            var size2=a;
            //console.log("blah", arr[i]);

            var currlength=length+a+b;
            var arr2=arr.join(";").split(";");
            arr2.splice(i,1);
            var bridges2 = bridges+ arr[i]+ " - ";
    
            var l=path(deep+1, bridges2, size2, currlength, arr2);
            if (l.length>maxd) {
                maxd=l.length;
                max=l.strength;
            }
            if (l.length==maxd && l.strength>max) {
                    max=l.strength;
            }
        }
    }    
    //console.log(Array(deep).join(" ")+"max ",max, deep);
    //console.log();
    //console.log(deep, Array(deep).join(" ")+"path ", length, bridges, arr.length);        

    return {strength:max, length:maxd};
}

var answer = path(1, "", 0, 0, array);
console.log("answer is: ", answer);

