import java.io.*;
import java.util.*;

public class problem23b {

    //checks whether an int is prime or not.
    public static boolean isPrime(int n) {
        for(int i=2;i<n;i++) {
            if(n%i==0)
                return false;
        }
        return true;
    }

    public static void main(String[] args) {
        try {
        Scanner sc = new Scanner(new File("problem23.input"));
        List<String> lines = new ArrayList<String>();
        while (sc.hasNextLine()) {
        lines.add(sc.nextLine());
        }

        String[] arr = lines.toArray(new String[0]);        



        Map<String, Integer> map = new HashMap<String, Integer>();
        map.put("a",1);
        map.put("b",0);
        map.put("c",0);
        map.put("d",0);
        map.put("e",0);
        map.put("f",0);
        map.put("g",0);
        map.put("h",0);

        int count=0;
        int count2=0;
        int opt1=0;
        int opt2=0;

        int i=0;

        Boolean opt=true;

        while (true) {
            String[] a= arr[i].split("\\s+");
            String op=a[0];
            String reg=a[1];
            String val =a[2];
            int val2=0;
            int regval=0;


            //if (i==11) {
            //    map.put("e",3-map.get("g")+1);
            //    map.put("g",1);
            //}

//3 1 -108397
//4 1 -108396

            if ("abcdefgh".indexOf(val) ==-1) {
                val2=Integer.parseInt(val);
            }
            else {
                val2=map.get(val);
            }

            if (op.equals("jnz") && "abcdefgh".indexOf(reg) ==-1) {
                regval=Integer.parseInt(reg);
            }
            else {
                regval=map.get(reg);
            }

            //if (i==11)
            //    System.out.println(map.get("a")+" "+map.get("b")+" "+map.get("c")+" "+map.get("d")+" "+map.get("e")+" "+map.get("f")+" "+map.get("g")+" "+map.get("h"));


            //System.out.println(i+ " "+ op + " "+reg + " "+val + " "+val2);

            //if (i==11) {
            //    System.out.println("i: "+i+" a: "+map.get("a")+" b: "+map.get("b")+" c: "+map.get("c")+" d: "+map.get("d")+" e:"+map.get("e")+" f: "+map.get("f")+" g: "+map.get("g")+" h: "+map.get("h"));
            //}

            if( i==24) {
                count=count+1;
                //System.exit(0);
            }

            if( i==8) {
                count2=count2+1;
                //System.exit(0);
            }            

            if (i==11) {
                System.out.println("optimizitaion #1");
                System.out.println("BEFORE i: "+i+" a: "+map.get("a")+" b: "+map.get("b")+" c: "+map.get("c")+" d: "+map.get("d")+" e:"+map.get("e")+" f: "+map.get("f")+" g: "+map.get("g")+" h: "+map.get("h"));
                if (!isPrime(map.get("b"))) {
                    map.put("f",0);
                }
                map.put("e",map.get("b"));
                map.put("g",0);
                //System.out.println(arr[i]);
                //System.out.println("i: "+i+" a: "+map.get("a")+" b: "+map.get("b")+" c: "+map.get("c")+" d: "+map.get("d")+" e:"+map.get("e")+" f: "+map.get("f")+" g: "+map.get("g")+" h: "+map.get("h"));
                i=20;
                System.out.println("AFTER  i: "+i+" a: "+map.get("a")+" b: "+map.get("b")+" c: "+map.get("c")+" d: "+map.get("d")+" e:"+map.get("e")+" f: "+map.get("f")+" g: "+map.get("g")+" h: "+map.get("h"));
                System.out.println("");

                opt1=opt1+1;
                continue;
                //System.exit(0);
            }
            

            if( i==20){
                System.out.println("optimizitaion #2");
                System.out.println("BEFORE i: "+i+" a: "+map.get("a")+" b: "+map.get("b")+" c: "+map.get("c")+" d: "+map.get("d")+" e:"+map.get("e")+" f: "+map.get("f")+" g: "+map.get("g")+" h: "+map.get("h"));
                map.put("d",map.get("b"));
                map.put("g",0);
                //System.out.println(arr[i]);
                //System.out.println("i: "+i+" a: "+map.get("a")+" b: "+map.get("b")+" c: "+map.get("c")+" d: "+map.get("d")+" e:"+map.get("e")+" f: "+map.get("f")+" g: "+map.get("g")+" h: "+map.get("h"));
                i=23;
                System.out.println("AFTER  i: "+i+" a: "+map.get("a")+" b: "+map.get("b")+" c: "+map.get("c")+" d: "+map.get("d")+" e:"+map.get("e")+" f: "+map.get("f")+" g: "+map.get("g")+" h: "+map.get("h"));
                System.out.println("");

                opt2=opt2+1;
                continue;
                //System.exit(0);
            }

            if (op.equals("set")){
                map.put(reg, val2);
                i=i+1;
            }
            else if (op.equals("sub")){
                map.put(reg, map.get(reg)-val2);
                i=i+1;
            }
            else if (op.equals("mul")){
                map.put(reg, map.get(reg)*val2);
                i=i+1;
            }
            else if (op.equals("jnz")){
                if (regval!=0) {
                    i=i+val2;
                }
                else {
                    i=i+1;
                }
            }

            //System.out.println(map.get("a")+" "+map.get("b")+" "+map.get("c")+" "+map.get("d")+" "+map.get("e")+" "+map.get("f")+" "+map.get("g")+" "+map.get("h"));
            System.out.println("i: "+i+" a: "+map.get("a")+" b: "+map.get("b")+" c: "+map.get("c")+" d: "+map.get("d")+" e:"+map.get("e")+" f: "+map.get("f")+" g: "+map.get("g")+" h: "+map.get("h"));

            //System.out.println(i);

            if (i<0 || i>=32) {
                break;
            }

        }

            System.out.println("count: ");
            System.out.println(count);

            System.out.println("count2: ");
            System.out.println(count2);

            System.out.println("opt1: ");
            System.out.println(opt1);

            System.out.println("opt2: ");
            System.out.println(opt2);

            System.out.println("answer: ");
            System.out.println(map.get("h"));
            //i: 1 a: 1 b: 84 c: 0 d: 0 e:0 f: 0 g: 0 h: 0

            //i: 32 a: 1 b: 125400 c: 125400 d: 125400 e:125400 f: 0 g: 0 h: 501
        }
        catch (Exception e) {
            System.out.println("Bad stuff happened");
            System.out.println(e);
        }
    }

}



