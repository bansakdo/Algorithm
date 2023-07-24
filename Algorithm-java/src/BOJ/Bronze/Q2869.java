package BOJ.Bronze;

import java.io.*;

public class Q2869 {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String[] inputs = br.readLine().trim().split(" ");
        int A = Integer.parseInt(inputs[0]);
        int B = Integer.parseInt(inputs[1]);
        int V = Integer.parseInt(inputs[2]);

        int v = V - A;
        int day = v / (A - B) + 1;
        if (v % (A - B) > 0) {
            day++;
        }

        bw.write(Integer.toString(day));
        bw.flush();
    }
}
