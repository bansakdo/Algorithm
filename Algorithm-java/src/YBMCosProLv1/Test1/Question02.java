package YBMCosProLv1.Test1;// You may use import as below.
import java.util.*;


class Question02 {
    public int solution(int n) {
        // Write code here.
        int answer = 0;

        if (n == 1)
            return 1;
        else if (n == 2)
            return 4;

        int[] arr = new int[n];
        int[] term = new int[n-1];

        arr[0] = 1;

        for (int i = 0 ; i < term.length ; i++) {
            if (i == 0)
                term[i] = 2 * n - 2;
            else if (i % 2 == 1)
                term[i] = term[i-1];
            else
                term[i] = term[i-1] - 4;

            arr[i + 1] = arr[i] + term[i];
        }
//
//        for (int i = 0 ; i < n ; i++)
//            System.out.print(arr[i] + " ");
//        System.out.println();
//        for (int i = 0 ; i < n-1 ; i++)
//            System.out.print(term[i] + " ");
//        System.out.println();

        for (int i = 0 ; i < n ; i++)
            answer += arr[i];

        /*
        * 1 -> 1
        * 2 -> 1 + 3 = 4
        *        2
        * 3 -> 1 + 5 + 9 = 15
        *        4   4
        * 4 -> 1 + 7 + 13 + 15 = 36
        *        6   6    2
        * 5 -> 1 + 9 + 17 + 21 + 25 = 73
        *        8   8    4    4
        * 6 -> 1 + 11 + 21 + 27 + 33 + 35 = 128
        *       10    10   6    6    2
        *
        *
        * */


        return answer;
    }

    // The following is main method to output testcase.
    public static void main(String[] args) {
        Question02 sol = new Question02();
        int n1 = 3;
        int ret1 = sol.solution(n1);

        
        // Press Run button to receive output. 
        System.out.println("Solution: return value of the method is " + ret1 + " .");
        
        int n2 = 5;
        int ret2 = sol.solution(n2);
        
        // Press Run button to receive output. 
        System.out.println("Solution: return value of the method is " + ret2 + " .");
    }
}