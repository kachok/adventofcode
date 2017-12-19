import scala.language.postfixOps;
import scala.collection.mutable.ArrayBuffer

object day14 {
  val l=256;

  def main(args: Array[String]): Unit = {
        //var input = "flqrgnkx";
        var input="ugkiagan";

        var count=0;

        var x=0;
        var word="";
        for(x <- 0 to 127 ){
            word = input+"-"+x;
            //println(word)
            println(hash(word))
            var h = hash(word);
            var bs="";
            var i=0;
            for (i<-0 to 31) {
                var b = Integer.toBinaryString(Integer.parseInt(h.charAt(i).toString, 16));
                if (b.length()==1) {b="000"+b}
                if (b.length()==2) {b="00"+b}
                if (b.length()==3) {b="0"+b}
                
                bs=bs+ b;
            }

            
            println(bs)
            println(bs.length())

            count = count+bs.count(_ == '1')
        }        

        println("answer is: ")
        println(count)


  }

  def hash(word: String) : String = {
    //println("hashing word " + word)

    var chs=ArrayBuffer[Int]();


    var i: Int =0;
    for (i <- 0 until  word.length()) {
        var ch=word.charAt(i);
        //println("char ",ch);
        chs += ch;
    }    
    
    chs=chs++ArrayBuffer(17,31,73,47,23);

    var chars=chs.toArray;

    //println("chars");
    //println(chars.deep.mkString(", "))
    
    var curr=0;
    var skipsize=0;

    var array:Array[Int] = 0 to (l-1) toArray;
    //println("begin")
    //println(array.deep.mkString(", "))

    var k: Int =0;
    for (k<-0 to 63){
        //var i: Int =0;
        for (el <- chars) {
            //println("el ",el)

            var j=0;
            for (j <- 0 to el/2-1) {

                var j1=curr+j;
                j1=j1 % l;

                var j2=curr+el-j-1;
                j2=j2 % l;

                var a=array(j1);
                var b=array(j2);
                array(j1)=b;
                array(j2)=a;
            }

            // move current position by length
            curr=curr+el+skipsize;
            curr=curr % l;

            //increment skip at the end of each loop
            skipsize=skipsize+1;          

        }
    }
    

    var hash=ArrayBuffer(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
    for (i<-0 to 15){
        hash(i)=array(i*16);

        for (j<-1 to 15) {
            //println(" >>> ")
            //println(i)
            //println(j)
            hash(i)=hash(i)^array(i*16+j);

        }

    }

    //println("Answer is:")
    //println(hash.toArray.deep.mkString(" "))

    var s="";

    for (i<-0 to 15){
        //println(i)
        //println(hash(i))
        var s1=Integer.toHexString(hash(i))
        //println(s1)
        if (s1.length()==1) {
            s1="0"+s1;
        }
        s=s+s1
    }

    //println(s)
    //println(s.length())
    return s

  }
}