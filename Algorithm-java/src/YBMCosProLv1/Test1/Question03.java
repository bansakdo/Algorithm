package YBMCosProLv1.Test1;
// You may use import as below.
import java.util.*;

class Question03 {
    public int solution(String pos) {
        // Write code here.
        int answer = 8;

        char charCol = pos.charAt(0);
        int col = charCol - 'A';
        int row = Integer.parseInt(String.valueOf(pos.charAt(1))) - 1;

        if (col == 0 || col == 7){
            answer -= 4;
        } else if (col == 1 || col == 6) {
            answer -= 2;
        }
        if (row == 0 || row == 7){
            if (col == 0 || col == 7)
                answer -= 2;
            else if (col == 1 || col == 6)
                answer -= 1;
        } else if (row == 1 || row == 6) {
            if (col == 0 || col == 7)
                answer -= 1;
            else if (col == 1 || col == 6)
                answer -= 2;
        }

        return answer;
    }

    // The following is main method to output testcase.
    public static void main(String[] args) {
        Question03 sol = new Question03();
        String pos = "A7";
        int ret = sol.solution(pos);

        // Press Run button to receive output. 
        System.out.println("Solution: return value of the method is " + ret + " .");
    }
}