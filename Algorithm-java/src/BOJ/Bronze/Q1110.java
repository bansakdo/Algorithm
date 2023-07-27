package BOJ.Bronze;

import java.io.*;

public class Q1110 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int input = Integer.parseInt(br.readLine().trim());

        if (input < 10) input *= 10;
        int num = input;
        int cnt = 0;
        while (true) {
            cnt++;
            int ten = num / 10;
            int one = num % 10;
            num = (one * 10) + (ten + one) % 10;
            if (num == input) break;
        }
        bw.write(String.valueOf(cnt));
        bw.flush();
    }
}
