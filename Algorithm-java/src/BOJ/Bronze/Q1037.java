package BOJ.Bronze;

import java.io.*;

public class Q1037 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine().trim());
        String[] input = br.readLine().trim().split(" ");
        int[] nums = new int[n];
        for (int i = 0; i < n; i++) {
            nums[i] = Integer.parseInt(input[i]);
        }

        for (int i = n; i > 0 ; i--) {
            for (int j = 0; j < i - 1; j++) {
                if (nums[j] > nums[j + 1]) {
                    int tmp = nums[j];
                    nums[j] = nums[j + 1];
                    nums[j + 1] = tmp;
                }
            }
        }
        bw.write(String.valueOf(nums[0] * nums[n - 1]));
        bw.flush();
    }
}
