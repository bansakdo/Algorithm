package BOJ.Bronze;

import java.io.*;
import java.util.Arrays;

public class Q11050 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int[] input = Arrays.stream(br.readLine().trim().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();
        int N = input[0];
        int K = input[1];

        int rst = 1;
        for (int i = K + 1; i <= N; i++) {
            rst *= i;
        }
        for (int i = 2; i <= N - K; i++) {
            rst /= i;
        }

        bw.write(String.valueOf(rst));
        bw.flush();
    }
}
