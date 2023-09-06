package BOJ.Gold;

import java.io.*;
import java.util.*;

public class Q2906 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine().trim());
        int[] maxDP = Arrays.stream(br.readLine().trim().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();
        int[] minDP = new int[3];
        for (int i = 0; i < 3; i++)
            minDP[i] = maxDP[i];

        for (int i = 0; i < N - 1; i++) {
            int[] arr = Arrays.stream(br.readLine().trim().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();

            int max0 = arr[0] + Math.max(maxDP[0], maxDP[1]);
            int max1 = arr[1] + Math.max(Math.max(maxDP[0], maxDP[1]), maxDP[2]);
            int max2 = arr[2] + Math.max(maxDP[1], maxDP[2]);
            maxDP[0] = max0;
            maxDP[1] = max1;
            maxDP[2] = max2;

            int min0 = arr[0] + Math.min(minDP[0], minDP[1]);
            int min1 = arr[1] + Math.min(Math.min(minDP[0], minDP[1]), minDP[2]);
            int min2 = arr[2] + Math.min(minDP[1], minDP[2]);
            minDP[0] = min0;
            minDP[1] = min1;
            minDP[2] = min2;
        }

        bw.write(String.valueOf(Math.max(Math.max(maxDP[0], maxDP[1]), maxDP[2])) + " " + String.valueOf(Math.min(Math.min(minDP[0], minDP[1]), minDP[2])));
        bw.flush();

    }
}
