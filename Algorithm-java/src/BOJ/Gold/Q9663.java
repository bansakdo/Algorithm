package BOJ.Gold;

import java.io.*;

public class Q9663 {

    static int[][] board;
    static int N;
    static int[] dx = {-1, 0, 1};
    static int[] dy = {1, 1, 1};

    static int dfs(int depth) {
        if (depth == N) {
            return 1;
        }

        int rst = 0;

        int row = depth;
//        for (int row = depth; row < N; row++) {
            for (int col = 0; col < N; col++) {
                if (board[row][col] == 0) {
                    board[row][col]++;

                    for (int d = 0; d < 3; d++) {
                        int nx = col;
                        int ny = row;

                        while (ny + dy[d] >= 0 && ny + dy[d] < N && nx + dx[d] >= 0 && nx + dx[d] < N) {
                            ny += dy[d];
                            nx += dx[d];
                            board[ny][nx]++;
                        }
                    }
                    rst += dfs(depth + 1);

                    for (int d = 0; d < 3; d++) {
                        int nx = col;
                        int ny = row;

                        while (ny + dy[d] >= 0 && ny + dy[d] < N && nx + dx[d] >= 0 && nx + dx[d] < N) {
                            ny += dy[d];
                            nx += dx[d];
                            board[ny][nx]--;
                        }
                    }
                    board[row][col]--;
                }
            }
//        }

        return rst;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        N = Integer.parseInt(br.readLine().trim());
        board = new int[N][N];

        bw.write(String.valueOf(dfs(0)));
        bw.flush();
    }
}
