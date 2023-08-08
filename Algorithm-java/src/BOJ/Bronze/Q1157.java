package BOJ.Bronze;

import java.io.*;

public class Q1157 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int[] frequency = new int[26];

        String input = br.readLine().trim();

        for (int i = 0; i < input.length(); i++) {
            char c = Character.toUpperCase(input.charAt(i));
            int c_num = c - 'A';

            frequency[c_num]++;
        }
        int rst = 0;
        char c = '?';
        for (int i = 0; i < 26; i++) {
            if (frequency[i] > rst) {
                rst = frequency[i];
                c = (char) ('A' + i);
            } else if (frequency[i] == rst) {
                c = '?';
            }
        }

        bw.write(String.valueOf(c));
        bw.flush();
    }
}
