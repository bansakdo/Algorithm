package BOJ.Silver;

import java.io.*;

public class Q1929 {
    static boolean[] isPrime;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String[] input = br.readLine().trim().split(" ");
        int M = Integer.parseInt(input[0]);
        int N = Integer.parseInt(input[1]);
        isPrime = new boolean[N + 1];

        getPrime();
        for (int i = M; i <= N; i++)
            if (!isPrime[i])
                bw.write(String.valueOf(i) + "\n");
        bw.flush();
    }

    public static void getPrime() {
        isPrime[0] = isPrime[1] = true;
        for (int i = 2; i <= Math.sqrt(isPrime.length); i++) {
            if (isPrime[i]) continue;
            for (int j = i * i; j < isPrime.length; j += i) {
                isPrime[j] = true;
            }
        }
    }
}
