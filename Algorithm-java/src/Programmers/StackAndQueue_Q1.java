package Programmers;

import java.util.*;

public class StackAndQueue_Q1 {

    public static void main(String[] args) {

//        int[] progresses = {93, 30, 55};
//        int[] speeds = {1, 30, 5};
//        int[] progresses = {50, 20 , 30, 40, 30};
//        int[] speeds = {10, 10, 10, 10, 10, 10};        // 1, 4
        int[] progresses = {90, 80, 55, 70};
        int[] speeds = {5, 9, 10, 6};
        int[] result = solution(progresses, speeds);
        System.out.println(Arrays.toString(result));

//        for(int x: result)
//            System.out.print("{}".);

    }

    public static int[] solution(int[] progresses, int[] speeds) {
        int[] answer = {};
//        List<Integer> rst = new ArrayList<>();
//
//        int pointer = 0;
//
//        while(pointer < progresses.length){
//            int finished = 1;
//            int mul = (int) Math.ceil((float)(100 - progresses[pointer]) / speeds[pointer]);
//
//            for (int i = pointer ; i < progresses.length; i++)
//                progresses[i] += speeds[i] * mul;
//
//            for (int i = pointer + 1; i < progresses.length; i++){
//                if (progresses[i] < 100)
//                    break;
//                finished++;
//            }
//            pointer += finished;
//            rst.add(finished);
//            System.out.println(mul + Arrays.toString(progresses));
//        }
//
//        answer = new int[rst.size()];
//        for (int i = 0; i < rst.size(); i++) {
//            answer[i] = rst.get(i);
//        }


        Queue<Integer> q = new LinkedList<>();
        List<Integer> answerList = new ArrayList<>();

        for (int i = 0; i < progresses.length; i++) {
            double remain = (100 - progresses[i]) / (double) speeds[i];
            int date = (int) Math.ceil(remain);


            if (!q.isEmpty() && q.peek() < date) {
                answerList.add(q.size());
                q.clear();
            }

            q.offer(date);
//            System.out.print(q.peek() + " ");
        }

        answerList.add(q.size());
//
//        System.out.println();
//        for (Integer x: answerList ) {
//            System.out.print(x + " ");
//        }
//        System.out.println();

        answer = new int[answerList.size()];

        for (int i = 0; i < answer.length; i++) {
            answer[i] = answerList.get(i);
        }

        return answer;
    }
}
