package BOJ.Bronze;

import java.io.*;

public class Q2292 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine().trim());

        int cnt = 1;
        int num = 1;
        int addNum = 0;

        while (n > num) {
            addNum += 6;
            num += addNum;
            cnt++;
        }

        bw.write(String.valueOf(cnt));
        bw.flush();
    }
}
