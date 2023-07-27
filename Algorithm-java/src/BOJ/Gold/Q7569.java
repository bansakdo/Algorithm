package BOJ.Gold;

import java.io.*;
import java.util.*;

public class Q7569 {

    public static void main(String[] args) throws IOException {
        long startTime = System.currentTimeMillis();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String[] input = br.readLine().trim().split(" ");
        int m = Integer.parseInt(input[0]);
        int n = Integer.parseInt(input[1]);
        int h = Integer.parseInt(input[2]);

        List<List<List<Integer>>> tomatoes = new ArrayList<>();
        Deque<String> queue = new ArrayDeque<>();

        for (int i = 0; i < h; i++) {
            List<List<Integer>> list_y = new ArrayList<>();
            for (int j = 0; j < n; j++) {
                input = br.readLine().trim().split(" ");
                List<Integer> list_x = new ArrayList<>();
                for (int k = 0; k < m; k++) {
                    list_x.add(Integer.parseInt(input[k]));
                    if (Integer.parseInt(input[k]) == 1) {
                        queue.offer(String.join(",", String.valueOf(i), String.valueOf(j), String.valueOf(k)));
                    }
                }
                list_y.add(list_x);
            }
            tomatoes.add(list_y);
        }

        int[] dx = {-1, 0, 1, 0, 0, 0};
        int[] dy = {0, 1, 0, -1, 0, 0};
        int[] dz = {0, 0, 0, 0, 1, -1};


        while (!queue.isEmpty()) {
            String[] pos = queue.poll().split(",");
            int x = Integer.parseInt(pos[2]);
            int y = Integer.parseInt(pos[1]);
            int z = Integer.parseInt(pos[0]);

            int val = tomatoes.get(z).get(y).get(x);

            // 좌, 후, 우, 전, 상, 하
            for (int i = 0; i < 6; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                int nz = z + dz[i];

                if (nx >= 0 && nx < m && ny >= 0 && ny < n && nz >= 0 && nz < h
                        && (tomatoes.get(nz).get(ny).get(nx) == 0
//                        || tomatoes.get(nz).get(ny).get(nx) > val + 1
                )) {
                    tomatoes.get(nz).get(ny).remove(nx);
                    tomatoes.get(nz).get(ny).add(nx, val + 1);
                    String next = String.join(",", String.valueOf(nz), String.valueOf(ny), String.valueOf(nx));
                    //if (!queue.contains(next))
                        queue.offer(next);
                }
            }
        }

        int rst = 0;
        boolean notDone = false;
        for (int i = 0; i < h; i++) {
            for (int j = 0; j < n; j++) {
                List<Integer> list = tomatoes.get(i).get(j);
                for (int k = 0; k < list.size(); k++) {
                    int num = list.get(k);
                    if (num == 0){
                        notDone = true;
                        break;
                    }
                    rst = Math.max(rst, num);
                }
                if (notDone) break;
            }
            if (notDone) break;
        }

        if (notDone) rst = -1;
        else rst -= 1;
        bw.write(String.valueOf(rst) + "\n");
        bw.write(String.valueOf((System.currentTimeMillis() - startTime) / 1000.0));
        bw.flush();
    }
}
