package BOJ.Silver;

import java.io.*;

public class Q11660 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String[] input = br.readLine().trim().split(" ");
        int N = Integer.parseInt(input[0]);
        int M = Integer.parseInt(input[1]);

        int[][] board = new int[N][N];
        int[][] sum_board = new int[N][N];
        for (int i = 0; i < N; i++) {
            input = br.readLine().trim().split(" ");
            for (int j = 0; j < N; j++) {
                board[i][j] = Integer.parseInt(input[j]);
            }
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                int num = board[i][j];
                if (i != 0)
                    num += sum_board[i - 1][j];
                if (j != 0)
                    num += sum_board[i][j - 1];
                if (i != 0 && j != 0)
                    num -= sum_board[i - 1][j - 1];

                sum_board[i][j] = num;
            }
        }


        for (int i = 0; i < M; i++) {
            input = br.readLine().trim().split(" ");
            int y1 = Integer.parseInt(input[0]) - 1;
            int x1 = Integer.parseInt(input[1]) - 1;
            int y2 = Integer.parseInt(input[2]) - 1;
            int x2 = Integer.parseInt(input[3]) - 1;

            int tot = sum_board[y2][x2];
            if (y1 != 0)
                tot -= sum_board[y1 - 1][x2];
            if (x1 != 0)
                tot -= sum_board[y2][x1 - 1];
            if (x1 != 0 && y1 != 0)
                tot += sum_board[y1 - 1][x1 - 1];

            bw.write(String.valueOf(tot) + "\n");
        }
        bw.flush();
    }
}
