package YBMCosProLv1.Test1;// You may use import as below.
//import java.util.*;

import java.util.List;

class Question01 {
    public long solution(long num) {
        // Write code here.
        long answer = 0;

        num += 1;
        char[] cArr = String.valueOf(num).toCharArray();
        for (int i = cArr.length - 1 ; i >= 0 ; i--) {
            if (cArr[i] == '0' && i != 0) {
                cArr[i] = '1';
            }
        }
        answer = Long.parseLong(String.valueOf(cArr));

        return answer;
    }

    // The following is main method to output testcase.
    public static void main(String[] args) {
        Question01 sol = new Question01();
        long num = 9949999;
        long ret = sol.solution(num);

        // Press Run button to receive output. 
        System.out.println("Solution: return value of the method is " + ret + " .");
    }
}