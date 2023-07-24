package BOJ.Bronze;

import java.io.*;
import java.util.*;

public class Q2609 {

    static int gcd(int a, int b) {
        if (b == 0) return a;
        return gcd(b, a % b);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String[] inputs = br.readLine().trim().split(" ");
        int num1 = Integer.parseInt(inputs[0]);
        int num2 = Integer.parseInt(inputs[1]);

        if (num1 > num2) {
            int tmp = num1;
            num1 = num2;
            num2 = tmp;
        }

        // 최대공약수
        int gcd = gcd(num1, num2);
        // 최소공배수
        int lcm = num1 * num2 / gcd;

        bw.write(String.valueOf(gcd) + "\n");
        bw.write(String.valueOf(lcm));
        bw.flush();
    }
}
