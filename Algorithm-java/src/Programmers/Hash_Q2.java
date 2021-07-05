package Programmers;

import java.util.HashSet;
import java.util.Set;

public class Hash_Q2 {

    public static void main(String[] args) {

//        String[] phone_book = {"119", "97674223", "1195524421"};
        String[] phone_book = {"123","456","789"};
        System.out.println(solution(phone_book));

    }

    public static boolean solution(String[] phone_book) {
        boolean answer = true;

//        Set<String> phone = new HashSet<>();
//        for(String p: phone_book)
//            phone.add(p);
//
//        for(String pNum: phone){
//            String tmp = "";
//            for(int i = 0; i < pNum.length(); i++) {
//                tmp += pNum.charAt(i);
//
//                if (phone.contains(tmp) && !tmp.equals(pNum)) {
//                    System.out.println(tmp + pNum);
//                    answer = false;
//                    break;
//                }
//
//            }
//        }

        for(int i = 0; i < phone_book.length - 1; i++)
            for(int j = i + 1; j < phone_book.length; j++) {
                if(phone_book[i].startsWith(phone_book[j])) return false;
                if(phone_book[j].startsWith(phone_book[i])) return false;
            }

        return answer;
    }
}
