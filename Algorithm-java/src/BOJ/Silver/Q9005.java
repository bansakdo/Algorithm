package BOJ.Silver;

import java.io.*;

public class Q9005 {
    public static int dfs(int n) {
        if (n == 0)
            return 1;
        int num = 0;
        if (n >= 3)
            num += dfs(n - 3);
        if (n >= 2)
            num += dfs(n - 2);
        if (n >= 1)
            num += dfs(n - 1);
        return num;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int T = Integer.parseInt(br.readLine().trim());
        for (int t = 0; t < T; t++) {
            int n = Integer.parseInt(br.readLine().trim());
            int num = dfs(n);
            bw.write(String.valueOf(num) + "\n");
        }
        bw.flush();
    }
}
