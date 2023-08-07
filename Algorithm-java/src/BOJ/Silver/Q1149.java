package BOJ.Silver;

import java.io.*;
import java.util.Arrays;

public class Q1149 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine().trim());
        int rst = Integer.MAX_VALUE;
        int[][] order = {{0, 1, 2}, {0, 2, 1}, {1, 0, 2}, {1, 2, 0}, {2, 0, 1}, {2, 1, 0}};

        int[][] costs = new int[n][3];
        for (int i = 0; i < n; i++) {
            costs[i] = Arrays.stream(br.readLine().trim().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();
        }

        for (int i = 0; i < 6; i++) {
            int val = 0;
            for (int j = 0; j < n; j++) {
                int idx = j % 3;
                val += costs[j][order[j][idx]];
            }
            rst = Math.min(rst, val);
        }

        bw.write(String.valueOf(rst));
        bw.flush();

    }
}
