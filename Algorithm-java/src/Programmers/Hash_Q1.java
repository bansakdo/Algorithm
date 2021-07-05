package Programmers;

import java.util.HashMap;
import java.util.Set;

public class Hash_Q1 {

    public static void main(String[] args) {

        String[] participant = {"leo", "kiki", "eden"};
        String[] completion = {"eden", "kiki"};

        System.out.println(solution(participant, completion));
    }

    public static String solution(String[] participant, String[] completion) {
        String answer = "";
        HashMap<String, Integer> hm = new HashMap<>();
//        for(String p: participant) {
//            int v = hm.getOrDefault(p, 0);
//            hm.put(p, v + 1);
//        }
        for(String p: participant)
            hm.put(p, hm.getOrDefault(p, 0) + 1);

//        for(String c: completion) {
//            int v = hm.get(c);
//            if(v == 1) {
//                hm.remove(c);
//            } else {
//                hm.put(c, v - 1);
//            }
//        }
        for (String c: completion)
            hm.put(c, hm.get(c) - 1);

//        Set<String> keySet = hm.keySet();
//        if(!keySet.isEmpty()){
//            answer = keySet.toString().replace("[", "").replace("]", "");
//        }
        for (String key: hm.keySet()) {
            if (hm.get(key) == 1)
                answer = key;
        }

        return answer;
    }
}