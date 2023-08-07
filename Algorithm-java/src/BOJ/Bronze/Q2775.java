package BOJ.Bronze;

import java.io.*;
import java.util.Arrays;

public class Q2775 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int T = Integer.parseInt(br.readLine().trim());

        for (int t = 0; t < T; t++) {
            int k = Integer.parseInt(br.readLine().trim());
            int n = Integer.parseInt(br.readLine().trim());

            int[][] house = new int[k][n];

            for (int i = 0; i < n; i++) {
                house[0][i] = i + 1;
            }
            for (int i = 1; i < k; i++) {
                int num = 0;
                for (int j = 0; j < n; j++) {
                    num += house[i - 1][j];
                    house[i][j] = num;
                }
            }
            int rst = Arrays.stream(house[k - 1]).sum();

            bw.write(String.valueOf(rst) + "\n");
        }
        bw.flush();
    }
}
