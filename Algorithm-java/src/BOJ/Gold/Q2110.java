package BOJ.Gold;

import java.io.*;
import java.util.Arrays;

public class Q2110 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String[] input = br.readLine().trim().split(" ");
        int N = Integer.parseInt(input[0]);
        int C = Integer.parseInt(input[1]);

        int[] pos = new int[N];
        for (int i = 0; i < N; i++)
            pos[i] = Integer.parseInt(br.readLine().trim());

        Arrays.sort(pos);

        int lt = 1;
        int rt = pos[N - 1] - pos[0];
        int rst = 0;

        while (lt <= rt) {
            int mid = (lt + rt) / 2;

            int cnt = 1;
            int lastLocate = pos[0];
            for (int i = 0; i < N; i++) {
                int locate = pos[i];
                if (locate - lastLocate >= mid) {
                    cnt++;
                    lastLocate = locate;
                }
            }
            if (cnt < C) {
                rt = mid - 1;
            } else {
                rst = mid;
                lt = mid + 1;
            }
        }

        bw.write(String.valueOf(rst));
        bw.flush();
    }
}
