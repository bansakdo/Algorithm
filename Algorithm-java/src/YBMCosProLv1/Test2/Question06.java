package YBMCosProLv1.Test2;// 다음과 같이 import를 사용할 수 있습니다.
import java.util.*;

class Question06 {
    public int[] solution(String commands) {
        // 여기에 코드를 작성해주세요.

        char[] comm_arr = commands.toCharArray();
        int x = 0;
        int y = 0;
        for (char c : comm_arr) {
            switch (c) {
                case 'L':
                    x -= 1;
                    break;
                case 'R':
                    x += 1;
                    break;
                case 'U':
                    y += 1;
                    break;
                case 'D':
                    y -= 1;
                    break;
            }
        }

        int[] answer = {x, y};
        return answer;
    }

    // 아래는 테스트케이스 출력을 해보기 위한 main 메소드입니다.
    public static void main(String[] args) {
        Question06 sol = new Question06();
        String commands = "URDDL";
        int[] ret = sol.solution(commands);

        // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
        System.out.println("solution 메소드의 반환 값은 " + Arrays.toString(ret) + " 입니다.");
    }
}