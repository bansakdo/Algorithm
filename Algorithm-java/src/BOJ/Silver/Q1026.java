package BOJ.Silver;

import java.io.*;
import java.util.Arrays;

public class Q1026 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine().trim());
        String[] sa = br.readLine().trim().split(" ");
        String[] sb = br.readLine().trim().split(" ");

        int[] arr_a = new int[n];
        int[] arr_b = new int[n];

        for (int i = 0; i < n; i++) {
            arr_a[i] = Integer.parseInt(sa[i]);
            arr_b[i] = Integer.parseInt(sb[i]);
        }

        Arrays.sort(arr_a);
        Arrays.sort(arr_b);

        int tot = 0;
        for (int i = 0; i < n; i++) {
            tot += arr_a[i] * arr_b[n - i - 1];
        }

        bw.write(String.valueOf(tot));
        bw.flush();
    }
}
