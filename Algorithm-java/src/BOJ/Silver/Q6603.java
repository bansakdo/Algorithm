package BOJ.Silver;

import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

public class Q6603 {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    static void comb(int[] arr, List<String> rst, Set<Integer> nums, int depth, int idx) throws IOException {
        if (idx > arr.length) return;
        if (depth == 6) {
            String s = nums.stream().sorted().map(String::valueOf).collect(Collectors.joining(" "));
            rst.add(s);
            return;
        }

        for (int i = idx; i < arr.length; i++) {
            if (!nums.contains(arr[i])) {
                nums.add(arr[i]);
                comb(arr, rst, nums, depth + 1, i + 1);
                nums.remove(arr[i]);
            }
        }
    }

    public static void main(String[] args) throws IOException {
        while (true) {
            String[] input = br.readLine().trim().split(" ");
            if (input[0].equals("0")) break;

            int n = Integer.parseInt(input[0]);
            int[] arr = new int[n];
            for (int i = 0; i < n; i++) {
                arr[i] = Integer.parseInt(input[i + 1]);
            }
            Arrays.sort(arr);

//            Set<String> rst = new HashSet<>();
            List<String> rst = new ArrayList<>();
            comb(arr, rst, new HashSet<>(), 0, 0);
//            rst.stream().sorted().forEach(x -> {
//                try {
//                    bw.write(x + "\n");
//                } catch (IOException e) {
//                    throw new RuntimeException(e);
//                }
//            });
            for (String s: rst) {
                bw.write(s + "\n");
            }
            bw.write("\n");
            bw.flush();
        }
    }
}
