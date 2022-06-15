package YBMCosProLv1.Test4;// 다음과 같이 import를 사용할 수 있습니다.
import java.util.*;

class Question09 {
    public String solution(int hour, int minute) {

        float hour_angle = 360 / 12 * hour;
        float min_angle = 360 / 60 * minute;
        hour_angle += 360.0 / 12.0 / 60.0 * minute;
        return String.valueOf(Math.min(Math.abs(hour_angle - min_angle), Math.abs(min_angle - hour_angle)));
    }

    // 아래는 테스트케이스 출력을 해보기 위한 main 메소드입니다.
    public static void main(String[] args) {
        Question09 sol = new Question09();
        int hour = 3;
        int minute = 0;
        String ret = sol.solution(hour, minute);
        System.out.println("solution 메소드의 반환 값은 " + ret + " 입니다.");

        ret = sol.solution(hour, 30);
        System.out.println("solution 메소드의 반환 값은 " + ret + " 입니다.");
    }
}