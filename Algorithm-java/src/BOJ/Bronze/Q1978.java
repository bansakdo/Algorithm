package BOJ.Bronze;

import java.io.*;

public class Q1978 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine().trim());
        String[] inputs = br.readLine().trim().split(" ");
        int[] nums = new int[n];
        for (int i = 0; i < n; i++) {
            nums[i] = Integer.parseInt(inputs[i]);
        }

        int rst = 0;
        for(int num: nums) {
            if (num < 2) continue;
            boolean isPrime = true;
            for (int i = 2; i < num && isPrime; i++) {
                if (num % i == 0)
                    isPrime = false;
            }
            if (isPrime)
                rst++;
        }

        bw.write(String.valueOf(rst));
        bw.flush();
    }
}
