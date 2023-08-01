package BOJ.Silver;

import java.io.*;
import java.util.*;

public class Q2583 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String[] input = br.readLine().trim().split(" ");
        int m = Integer.parseInt(input[0]);
        int n = Integer.parseInt(input[1]);
        int k = Integer.parseInt(input[2]);

        int[][] squares = new int[k][4];

        for (int i = 0; i < k; i++) {
            input = br.readLine().trim().split(" ");
            int[] sqare = {Integer.parseInt(input[0]), Integer.parseInt(input[1]), Integer.parseInt(input[2]), Integer.parseInt(input[3])};
            squares[i] = sqare;
        }

        int[][] board = new int[m][n];
        List<Integer> rst = new ArrayList<>();

        for (int i = 0; i < k; i++) {
            int[] square = squares[i];
            for (int j = square[1]; j < square[3]; j++) {
                for (int l = square[0]; l < square[2]; l++) {
                    board[j][l] = 1;
                }
            }
        }

        int[][] chk = new int[m][n];
        int[] dx = {0, -1, 0, 1};
        int[] dy = {1, 0, -1, 0};

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == 0 && chk[i][j] == 0) {
                    Deque queue = new ArrayDeque();
                    queue.offer(new int[]{i, j});
                    int cnt = 0;
                    while (!queue.isEmpty()) {
                        int[] pos = (int[]) queue.poll();
                        int y = pos[0];
                        int x = pos[1];
                        if (chk[y][x] == 0) {
                            chk[y][x] = 1;
                            cnt++;

                            for (int l = 0; l < 4; l++) {
                                int nx = x + dx[l];
                                int ny = y + dy[l];

                                if (nx >= 0 && nx < n && ny >= 0 && ny < m && board[ny][nx] == 0 && chk[ny][nx] == 0) {
                                    queue.offer(new int[]{ny, nx});
                                }
                            }
                        }
                    }
                    rst.add(cnt);
                }
            }
        }

        Collections.sort(rst);
        bw.write(String.valueOf(rst.size()) + "\n");
        for (int num: rst) {
            bw.write(String.valueOf(num) + " ");
        }
        bw.flush();
    }
}
