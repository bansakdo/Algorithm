package Programmers;

import java.util.*;

public class StackAndQueue_Q2 {

    public static void main(String[] args) {


        int[] priorities = {2, 1, 3, 2};
        int location = 2;

        System.out.println(solution(priorities, location));

    }

    public static int solution(int[] priorities, int location) {
        int answer = 0;
        PriorityQueue<Integer> queue = new PriorityQueue<>();

        int[] maxToMin = Arrays.stream(priorities).sorted().toArray();
        System.out.println(Arrays.toString(maxToMin));
        int maxPointer = maxToMin.length - 1;

        for (int i: priorities)
            queue.offer(i);

//        while(location > 0){
//            int now = queue.poll(0);
//        }




        return answer;
    }
}
