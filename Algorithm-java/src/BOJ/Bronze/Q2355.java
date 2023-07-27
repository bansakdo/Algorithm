package BOJ.Bronze;

import java.io.*;

public class Q2355 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String[] input = br.readLine().trim().split(" ");
        long a, b;
        if (Integer.parseInt(input[0]) < Integer.parseInt(input[1])) {
            a = Long.parseLong(input[0]);
            b = Long.parseLong(input[1]);
        } else {
            a = Long.parseLong(input[1]);
            b = Long.parseLong(input[0]);
        }

        long rst = 0;
        if (a < 0 && b > 0) {
            long aa = Math.abs(a);
            long bb = Math.abs(b);
            if (aa <=bb) {
                for (long i = -a + 1; i <= b; i++)
                    rst += i;
            } else {
                for (long i = a; i < -b; i++)
                    rst += i;
            }
        } else {
            for (long i = a; i <= b; i++)
                rst += i;
        }

        bw.write(String.valueOf(rst));
        bw.flush();
    }
}
