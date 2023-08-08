package BOJ.Bronze;

import java.io.*;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Q15829 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int L = Integer.parseInt(br.readLine().trim());
        String str = br.readLine().trim();
        Map<Integer, List<Integer>> alphabet = new HashMap<>();
//        int[] alphabets = new int[26];
        boolean[] used = new boolean[27];

        long rst = 0L;
        int std_a = (int) 'a' - 1;
        for (int i = 0; i < L; i++) {
            char c = str.charAt(i);
            int c_num = (int) c - std_a;
            used[c_num] = true;
            List<Integer> list = alphabet.getOrDefault(c_num, new ArrayList<>());
            list.add(i);
            alphabet.put(c_num, list);
//            alphabets[c_num]++;
//            rst += (c_num * Math.pow(31, i)) % 10000000000L;
//            rst %= 10000000000L;
        }
        for (int i = 1; i <= 26; i++) {
            if (!used[i]) continue;
            long mul = 0L;
            List<Integer> list = alphabet.get(i);
            for (int j: list) {
//                mul += (long) Math.pow(31, j) % 1234567891L;
                long tmp = 1;
                for (int k = 0; k < j; k++) {
                    tmp *= 31;
                    tmp %= 1234567891L;
                }
                mul += tmp;
            }
            rst += (i * mul);
            rst %= 1234567891L;
        }


        rst %= 1234567891;
        bw.write(String.valueOf(rst));
        bw.flush();
    }
}
