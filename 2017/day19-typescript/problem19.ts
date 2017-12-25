var fs  = require("fs");
var array = fs.readFileSync("problem19.input").toString().split('\n');

console.log(array);

var letters="";

var start = { "x": 27, "y": 0 };
var dir = {"name":"down","x":0,"y":1};

console.log(">"+array[start.y][start.x]+"<");

function step(curr, dir){
    curr.x=curr.x+dir.x;
    curr.y=curr.y+dir.y;
    return curr;
}

function el(array, pos){
    return array[pos.y][pos.x]
}

var curr=start;
while(1) {
    curr=step(curr, dir);
    console.log(curr);


    if (el(array, curr) == "+") {
        console.log("+");
        if (dir.name=="up" || dir.name=="down") {
            if (curr.x>0 && array[curr.y][curr.x-1]!=" ") {
                dir= {"name":"left","x":-1,"y":0};
            }
            if (array[curr.y][curr.x+1]!=" ") {
                dir= {"name":"right","x":+1,"y":0};
            }
        }
        else if (dir.name=="left" || dir.name=="right") {
            if (curr.y>0 && array[curr.y-1][curr.x]!=" ") {
                dir= {"name":"up","x":0,"y":-1};
            }
            if (array[curr.y+1][curr.x]!=" ") {
                dir= {"name":"down","x":0,"y":1};
            }
        }
    }
    else if (el(array, curr) == "|") {
        console.log("|");

    }
    else if (el(array, curr) == "-") {
        console.log("-");

    }
    else if (el(array, curr) != " ") {
        console.log("*");
        if (letters.indexOf(el(array, curr))>=0) {
            console.log("answer is: ");
            console.log(letters);
            process.exit(0);
        }
        letters=letters+el(array, curr);
        //console.log(letters);
    };
    //console.log(letters);

}