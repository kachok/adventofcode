//use std::num;

// This is the main function
fn main() {
    // The statements here will be executed when the compiled binary is called

    let input=289326;
    //let input=12;

    println!("input is {}", input);

    let n2= (input as f64).sqrt().ceil() as i64;

    let mut n=0;

    let mut ring=0;

    if n2 % 2 == 0 {
        ring = n2/2;
        n=n2+1;
    }
    else {
        ring=(n2-1)/2;
        n=n2;
    }


    let tr = (n-2)*(n-2)+n-1;
    let tl = n*n-n*2+2;
    let bl = n*n-n+1;
    let br = n*n;

    println!("matrix size {0} number of rings {1}", n, ring);
    println!("matrix corners  {0} {1} {2} {3}", tr, tl, bl, br);

    let mut a=n*2-(bl-input);

    if input == tr || input == tl || input == bl || input == br{
        a=ring;
    }

    if input<tr {
        a=(tr+(tr-n-2)-input-input).abs()/2+ring;
    }
    if input>tr && input <tl {
        a=(tr+tl-input-input).abs()/2+ring;
    }
    if input>tl && input<bl {
        a=(tr+bl-input-input).abs()/2+ring;
    }
    if input>bl && input <br {
        a=(bl+br-input-input).abs()/2+ring;
    }

    println!("answer is {}", a);

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