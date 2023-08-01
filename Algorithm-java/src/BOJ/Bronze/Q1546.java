package BOJ.Bronze;

import java.io.*;
import java.util.Arrays;

public class Q1546 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine().trim());
        int[] scores = Arrays.stream(br.readLine().trim().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        int max_score = Arrays.stream(scores).max().getAsInt();
        double tot = Arrays.stream(scores).sum();
        double rst = (tot / max_score) * 100 / n;

        bw.write(String.valueOf(rst));
        bw.flush();

    }
}
