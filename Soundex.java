
import java.lang.System;
import java.util.Scanner;

public class Soundex {


    public static void main(String[] args) {

        //Scan in name
        Scanner scan = new Scanner(System.in);

        //inf loop for testing, to turn off set t to false
        boolean t = false;
        do {
            System.out.print("Enter a name: ");
            String name = scan.nextLine();
            //call soundex method
            String result = runSoundex(name);

            System.out.println(result);
        } while (t == true)
    }

    protected static String runSoundex(String name){
        // logic: for each letter in string after the first letter,
        // drop a, e, h, i, o, u, w, y
        // replace:
        // b , f, p, v with 1
        // c,g,j,k,q,s,x,z with 2
        // d, t with 3
        // i with 4
        // m, n with 5
        // r with 6
        // then for each seq of identical numbers replace with 1 of same number
        // then make 4 char string, by dropping every thin past third or add ecxtra 0's
        // Based on Odell and Russell, 1922; Knuth, 1973.

        // modified name, i.e. result (r)
        String r = "" + name.toLowerCase().charAt(0);

        //loop through string
        for(int i = 1; i < name.length(); i++){
            char c = name.toLowerCase().charAt(i);

            //switch
            switch(c){

                //case 1: remove
                case 'a':
                case 'e':
                case 'h':
                case 'i':
                case 'o':
                case 'u':
                case 'w':
                case 'y':
                    //drop it
                    continue;
                case 'b':
                case 'f':
                case 'p':
                case 'v':
                    if(!(r.charAt(r.length()-1) == '1')) {
                        r += "1";
                    }
                    break;
                case 'c':
                case 'g':
                case 'j':
                case 'k':
                case 'q':
                case 's':
                case 'x':
                case 'z':
                    if(!(r.charAt(r.length()-1) == '2')) {
                        r += "2";
                    }
                    break;
                case 'd':
                case 't':
                    if(!(r.charAt(r.length()-1) == '3')) {
                        r += "3";
                    }
                    break;
                case 'l':
                    if(!(r.charAt(r.length()-1) == '4')) {
                        r += "4";
                    }
                    break;
                case 'm':
                case 'n':
                    if(!(r.charAt(r.length()-1) == '5')) {
                        r += "5";
                    }
                    break;
                case 'r':
                    if(!(r.charAt(r.length()-1) == '6')) {
                        r += "6";
                    }
                    break;
                default:
                    continue;
            }
        }
        //return only 4 digits, and return 0's if less than 4
        if(r.length() > 4) {
            return r.substring(0,4);
        }else{
            int l = 4-r.length();
            for(int i = 0; i < l; i++){
                r += 0;
            }
            return r;
        }
    }
}
