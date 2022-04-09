package Programmers;

import java.util.*;

public class Heap_Q1 {

    public static int solution(int[] scoville, int K) {
        int answer = 0;

        Arrays.sort(scoville);
//        LinkedList<Integer> queue = new LinkedList<>();
        PriorityQueue<Integer> queue = new PriorityQueue<Integer>();
        for (int i : scoville) {
            queue.add(i);
        }

        while (queue.peek() < K && queue.size() >= 2) {
            System.out.println(queue);
            answer++;
            int first = queue.poll();
            int second = queue.poll();

            int mix = first + second * 2;
            queue.offer(mix);
        }
        if (queue.size() == 1 && queue.peek() < K)
            return -1;

        return answer;
    }
    public static void main(String[] args) {

        int[] scoville = {1, 2, 3, 9, 10, 12};
        int K = 1      ;

        System.out.println(solution(scoville, K));
    }


}
