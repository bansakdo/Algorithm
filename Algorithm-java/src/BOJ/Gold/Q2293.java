package BOJ.Gold;

import java.io.*;

public class Q2293 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String[] input = br.readLine().trim().split(" ");
        int n = Integer.parseInt(input[0]);
        int k = Integer.parseInt(input[1]);
        Integer[] coins = new Integer[n];
        for (int i = 0; i < n; i++) {
            coins[i] = Integer.parseInt(br.readLine().trim());
        }

        int[] dp = new int[k + 1];
        dp[0] = 1;

        for (int i = 0; i < n; i++) {
            for (int j = coins[i]; j < k + 1; j++) {
                dp[j] += dp[j - coins[i]];
            }
        }
        bw.write(String.valueOf(dp[k]));
        bw.flush();
    }
}
