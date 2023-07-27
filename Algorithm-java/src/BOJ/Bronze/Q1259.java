package BOJ.Bronze;

import java.io.*;

public class Q1259 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        while (true) {
            String input = br.readLine().trim();
            if (input.equals("0")) break;

            String reverse = (new StringBuilder(input)).reverse().toString();
            if (input.equals(reverse))
                bw.write("yes\n");
            else
                bw.write("no\n");
        }
        bw.flush();
    }
}
