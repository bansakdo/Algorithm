package BOJ.Silver;

import java.io.*;
import java.util.Arrays;

public class Q1149 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine().trim());
        int rst = Integer.MAX_VALUE;
        int[][] board = new int[n][3];

        board[0] = Arrays.stream(br.readLine().trim().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();
        for (int i = 1; i < n; i++) {
            board[i] = Arrays.stream(br.readLine().trim().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();
            board[i][0] += Math.min(board[i - 1][1], board[i - 1][2]);
            board[i][1] += Math.min(board[i - 1][0], board[i - 1][2]);
            board[i][2] += Math.min(board[i - 1][0], board[i - 1][1]);
        }

        rst = Arrays.stream(board[n - 1]).min().getAsInt();




//        int[][] order = {{0, 1, 2}, {0, 2, 1}, {1, 0, 2}, {1, 2, 0}, {2, 0, 1}, {2, 1, 0}};

//        int[][] costs = new int[n][3];
//        for (int i = 0; i < n; i++) {
//            costs[i] = Arrays.stream(br.readLine().trim().split(" "))
//                    .mapToInt(Integer::parseInt)
//                    .toArray();
//        }

//        for (int i = 0; i < 6; i++) {
//            int val = 0;
//            for (int j = 0; j < n; j++) {
//                int idx = j % 3;
//                val += costs[j][order[j][idx]];
//            }
//            rst = Math.min(rst, val);
//        }

        bw.write(String.valueOf(rst));
        bw.flush();

    }
}
/*
3
26 40 83
49 60 57
13 89 99

3
1 100 100
100 1 100
100 100 1

*
* */