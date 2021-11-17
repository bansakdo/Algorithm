package BOJ;

import java.io.*;

import static java.lang.Math.min;

public class Q1300 {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine().trim());
        int k = Integer.parseInt(br.readLine().trim());

        long lt = 1;
        long rt = k;
        long ans = 1;
        while (lt <= rt){
            long mid = (lt + rt) / 2;
            int tot = 0;
            for (int i = 1 ; i <= n ; i++) {
                tot += min(mid / i, n);
            }
            if (tot >= k){
                rt = mid - 1;
                ans = mid;
            } else {
                lt = mid + 1;
            }
        }

        bw.write(String.valueOf(ans));
        bw.flush();

    }

}
