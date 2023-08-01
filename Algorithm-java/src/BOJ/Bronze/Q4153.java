package BOJ.Bronze;

import java.io.*;
import java.util.Arrays;

public class Q4153 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        while (true) {
            double[] lines = Arrays.stream(br.readLine().trim().split(" "))
                    .mapToDouble(Double::parseDouble)
                    .sorted()
                    .toArray();

            if (lines[0] == 0.0 && lines[1] == 0.0 && lines[2] == 0.0)
                break;
            if (Math.pow(lines[0], 2) + Math.pow(lines[1], 2) == Math.pow(lines[2], 2))
                bw.write("right\n");
            else
                bw.write("wrong\n");
        }
        bw.flush();
    }
}
