package BOJ.Silver;

import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;

public class Q2485 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine().trim());
        int[] trees = new int[n];
        for (int i = 0; i < n; i++) {
            trees[i] = Integer.parseInt(br.readLine().trim());
        }
        Arrays.sort(trees);

        int[] terms = new int[n - 1];
        for (int i = 0; i < n -1; i++) {
            terms[i] = trees[i + 1] - trees[i];
        }

        Arrays.sort(terms);
        int rst = Integer.MAX_VALUE;
        for (int i = 1; i <= terms[0]; i++) {
            int tot = 0;
            boolean isDivisor = true;
            for (int j = 0; j < n - 1; j++) {
                if (terms[j] % i != 0){
                    isDivisor = false;
                    break;
                } else {
                    tot += (terms[j] / i) - 1;
                }
            }
            if (isDivisor) {
                rst = Math.min(rst, tot);
            }
        }

        bw.write(String.valueOf(rst));
        bw.flush();
    }
}
