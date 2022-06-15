package YBMCosProLv1.Test4;// 다음과 같이 import를 사용할 수 있습니다.
import java.util.*;

class Question10 {
    public int solution(int a, int b) {
        Set<Integer> nums = new HashSet<>();
        int std_a = (int) Math.pow(a, 1.0 / 3.0) + 1;
        int std_b = (int) Math.sqrt(b);

        for (int i = std_a; i <= std_b ; i++) {
            if (Math.sqrt(i) % 1 == 0)
                continue;
            for (int j = 2; j <= 3; j++) {
                int n = (int) Math.pow(i, j);
                if (n >= a && n <= b)
                    nums.add(n);
            }
        }
        return nums.size();
    }

    // 아래는 테스트케이스 출력을 해보기 위한 main 메소드입니다.
    public static void main(String[] args){
        Question10 sol = new Question10();
        int a = 6;
        int b = 30;
        int ret = sol.solution(a, b);

        // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
        System.out.println("solution 메소드의 반환 값은 " + ret + " 입니다.");
    }
}