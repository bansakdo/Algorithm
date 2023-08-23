package BOJ.Silver;

import java.io.*;
import java.util.*;

public class Q11650 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        PriorityQueue<int[]> heap = new PriorityQueue<>(new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                if (o1[0] == o2[0]) return o1[1] - o2[1];
                return o1[0] - o2[0];
            }
        });
        int N = Integer.parseInt(br.readLine().trim());

        for (int i = 0; i < N; i++) {
            int[] dot = Arrays.stream(br.readLine().trim().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();

            heap.add(dot);
        }

        for (int i = 0; i < N; i++) {
            int[] dot = heap.poll();
            bw.write(String.valueOf(dot[0]) + " " + String.valueOf(dot[1]) + "\n");
        }
        bw.flush();

    }
}
