package YBMCosProLv1.Test2;// 다음과 같이 import를 사용할 수 있습니다.
import java.util.*;

class Question05 {
    public int solution(int[] arr) {
        // 여기에 코드를 작성해주세요.
        int answer = 0;
        int last = -1;
        int num = 0;
        for (int i : arr) {
            if (i > last){
                num += 1;
            } else {
                answer = Math.max(answer, num);
                num = 1;
            }
            last = i;
        }

        return answer;
    }

    // 아래는 테스트케이스 출력을 해보기 위한 main 메소드입니다.
    public static void main(String[] args) {
        Question05 sol = new Question05();
        int[] arr = {3, 1, 2, 4, 5, 1, 2, 2, 3, 4};
        int ret = sol.solution(arr);

        // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
        System.out.println("solution 메소드의 반환 값은 " + ret + " 입니다.");
    }
}