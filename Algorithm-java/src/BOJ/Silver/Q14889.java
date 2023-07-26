package BOJ.Silver;

import java.io.*;

public class Q14889 {

    static int[] chk;
    static int[][] board;
    static int n;

    static int combination(int depth, int idx) {
        if (depth == n / 2) {
            int scoreA = 0;
            int scoreB = 0;
            for (int i = 0; i < n; i++) {
                boolean isTeamA = chk[i] == 1;
                for (int j = i + 1; j < n; j++) {
                    if (isTeamA && chk[j] == 1) {
                        scoreA += board[i][j] + board[j][i];
                    } else if (!isTeamA && chk[j] == 0) {
                        scoreB += board[i][j] + board[j][i];
                    }
                }
            }
            return Math.abs(scoreA - scoreB);
        } else if (idx == n) return Integer.MAX_VALUE;

        int val = Integer.MAX_VALUE;
        for (int i = idx; i < n - (n / 2) + depth; i++) {
            chk[i] = 1;
            val = Math.min(val, combination(depth + 1, i + 1));
            chk[i] = 0;
        }
        return val;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        n = Integer.parseInt(br.readLine().trim());
        board = new int[n][n];
        chk = new int[n];
        for (int i = 0; i < n; i++) {
            String[] input = br.readLine().trim().split(" ");
            for (int j = 0; j < n; j++) {
                board[i][j] = Integer.parseInt(input[j]);
            }
        }
        bw.write(String.valueOf(combination(0, 0)));
        bw.flush();
    }
}
