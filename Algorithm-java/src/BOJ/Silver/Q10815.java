package BOJ.Silver;

import java.io.*;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class Q10815 {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine().trim());
        String[] cards_input = br.readLine().trim().split(" ");
        int m = Integer.parseInt(br.readLine().trim());
        String[] nums_input = br.readLine().trim().split(" ");

//        int[] cards = new int[n];
        Set<Integer> cards = new HashSet<>();
        int[] nums = new int[m];
        int[] answer = new int[m];

//        for (int i = 0; i < n; i++) {
//            cards[i] = Integer.parseInt(cards_input[i]);
//        }

        for (String card: cards_input) {
            cards.add(Integer.parseInt(card));
        }
        for (int i = 0; i < m; i++) {
            nums[i] = Integer.parseInt(nums_input[i]);
        }
//        Arrays.sort(cards);
//        for (int i = 0; i < m; i++) {
//            int num = nums[i];
//            for (int j = 0; j < n; j++) {
//                if (cards[j] == num) {
//                    answer[i] = 1;
//                    break;
//                } else if (cards[j] > num) {
//                    break;
//                }
//            }
//        }

        for (int i = 0; i < m; i++) {
            if (cards.contains(nums[i])) {
               answer[i] = 1;
            }
        }

        for (int i = 0; i < m; i++) {
            bw.write(Integer.toString(answer[i]) + " ");
        }
        bw.flush();
    }
}
