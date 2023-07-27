package BOJ.Bronze;

import java.io.*;

public class Q1834 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine().trim());
        long rst = 0;

        for (long i = 1; i < n; i++) {
            rst += (n + 1) * i;
        }

        bw.write(String.valueOf(rst));
        bw.flush();
    }
}
