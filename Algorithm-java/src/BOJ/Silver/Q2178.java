package BOJ.Silver;

import java.io.*;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Queue;

public class Q2178 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String[] inputs = br.readLine().trim().split(" ");
        int N = Integer.parseInt(inputs[0]);
        int M = Integer.parseInt(inputs[1]);

        int[][] board = new int[N][M];
        for (int i = 0; i < N; i++) {
            board[i] = Arrays.stream(br.readLine().trim().split(""))
                    .mapToInt(Integer::parseInt)
                    .toArray();
        }

        int[] dy = {0, -1, 0, 1};
        int[] dx = {1, 0, -1, 0};

        Queue<int[]> queue = new ArrayDeque<>();
        queue.add(new int[]{0, 0, 1});

        while(!queue.isEmpty()) {
            int[] pos = queue.poll();
            int cnt = pos[2];

            if (board[pos[0]][pos[1]] != 0 && board[pos[0]][pos[1]] != 1 && board[pos[0]][pos[1]] <= cnt)
                continue;

//            if (board[pos[0]][pos[1]] == 1 || board[pos[0]][pos[1]] > cnt)
            board[pos[0]][pos[1]] = cnt;

            if (pos[0] == N - 1 && pos[1] == M - 1)
                continue;

            for (int d = 0; d < 4; d++) {
                int ny = pos[0] + dy[d];
                int nx = pos[1] + dx[d];

                if (ny == pos[0] && nx == pos[1])
                    continue;

                if (ny >= 0 && ny < N && nx >= 0 && nx < M && board[ny][nx] != 0 && board[ny][nx] < cnt + 1) {
                    queue.add(new int[]{ny, nx, cnt + 1});
                }
            }
        }
        bw.write(String.valueOf(board[N - 1][M - 1]));
        bw.flush();

    }
}


/*
4 6
101111
101010
101011
111011

4 6
110110
110110
111111
111101

7 7
1011111
1110001
1000001
1000001
1000001
1000001
1111111

2 25
1011101110111011101110111
1110111011101110111011101


 */
