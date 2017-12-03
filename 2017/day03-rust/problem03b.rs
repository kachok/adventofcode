//use std::num;
use std::process;

fn calc(x:usize,y:usize, a:[[usize; 100]; 100]) -> usize{
    let mut val=0;
    val=a[x+1][y]+a[x+1][y-1]+a[x+1][y+1]+a[x-1][y]+a[x-1][y+1]+a[x-1][y-1]+a[x][y-1]+a[x][y+1];
    val
}

// This is the main function
fn main() {
    // The statements here will be executed when the compiled binary is called

    let input=289326;
    //let input=806;

    println!("input is {}", input);


    let mut a: [[usize; 100]; 100] = [[0; 100]; 100];

    let mut x=50;
    let mut y=50;

    a[x][y]=1;

    println!("curr {0}, {1} size is {2}x{2}", x,y,a[50][50]);
    println!("val {}", a[x][y]);


    x=51;
    y=51;

    println!("curr {0}, {1} - {2}", x,y, a[x][y]);
    for i in 1..1000{
        println!(">>>>");

        //up
        for k in 0..i*2{
            println!("up");
            y=y-1;
            a[x][y]=calc(x,y,a);
            println!("curr {0}, {1} - {2}", x,y, a[x][y]);
            if a[x][y]>input {
                println!("Answer: {}", a[x][y]);
                process::exit(0x0100);            }
        }
        //left
        for k in 0..i*2{
            println!("left");
            x=x-1;            
            a[x][y]=calc(x,y,a);
            println!("curr {0}, {1} - {2}", x,y, a[x][y]);
            if a[x][y]>input {
                println!("Answer: {}", a[x][y]);
                process::exit(0x0100);            }
        }

        //down
        for k in 0..i*2{
            println!("down");
            y=y+1;                        
            a[x][y]=calc(x,y,a);
            println!("curr {0}, {1} - {2}", x,y, a[x][y]);
            if a[x][y]>input {
                println!("Answer: {}", a[x][y]);
                process::exit(0x0100);            }
        }
        //right
        for k in 0..i*2{
            println!("right");
            x=x+1;                        
            a[x][y]=calc(x,y,a);
            println!("curr {0}, {1} - {2}", x,y, a[x][y]);
            if a[x][y]>input {
                println!("Answer: {}", a[x][y]);
                process::exit(0x0100);            }
        }
        x=x+1;
        y=y+1;        
    }

    //println!("answer is {}", a);

    /*
    let mut n=0;
    for var in  0..10000 {
        if n*n > input {
            println!("n={}",n);
            return;
        }
        n=n+1;
        println!("{}",n);
    }    

    */
}