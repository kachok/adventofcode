import java.io.*;
import java.util.*;

public class problem23 {

    public static void main(String[] args) {
        try {
        Scanner sc = new Scanner(new File("problem23.input"));
        List<String> lines = new ArrayList<String>();
        while (sc.hasNextLine()) {
        lines.add(sc.nextLine());
        }

        String[] arr = lines.toArray(new String[0]);        



        Map<String, Integer> map = new HashMap<String, Integer>();
        map.put("a",0);
        map.put("b",0);
        map.put("c",0);
        map.put("d",0);
        map.put("e",0);
        map.put("f",0);
        map.put("g",0);
        map.put("h",0);

        int count=0;

        int i=0;
        while (true) {
            String[] a= arr[i].split("\\s+");
            String op=a[0];
            String reg=a[1];
            String val =a[2];
            int val2=0;
            int regval=0;


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


            System.out.println(i+ " "+ op + " "+reg + " "+val + " "+val2);

            
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
                count=count+1;
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

            System.out.println(map.get("a")+" "+map.get("b")+" "+map.get("c")+" "+map.get("d")+" "+map.get("e")+" "+map.get("f")+" "+map.get("g")+" "+map.get("h"));

            //System.out.println(i);

            if (i<0 || i>=32) {
                break;
            }

        }

            System.out.println("answer: ");
            System.out.println(count);
        }
        catch (Exception e) {
            System.out.println("Bad stuff happened");
            System.out.println(e);
        }
    }

}



