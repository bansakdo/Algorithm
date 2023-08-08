package BOJ.Bronze;

import java.io.*;

public class Q1032 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine().trim());
        String[] filenames = new String[N];
        for (int i = 0; i < N; i++) {
            filenames[i] = br.readLine().trim();
        }
        int nameLen = filenames[0].length();
        StringBuilder rst = new StringBuilder();
        for (int i = 0; i < nameLen; i++) {
            char c = filenames[0].charAt(i);
            boolean allSame = true;
            for (int j = 1; j < N; j++) {
                if (filenames[j].charAt(i) != c) {
                    allSame = false;
                    break;
                }
            }
            if (allSame) {
                rst.append(c);
            } else {
                rst.append("?");
            }
        }
        bw.write(rst.toString());
        bw.flush();
    }
}
