package YBMCosProLv1.Test3;// 다음과 같이 import를 사용할 수 있습니다.
import java.util.*;

class Question04 {
    public int solution(String s1, String s2) {
        // 여기에 코드를 작성해주세요.
/*

        int answer = s1.length() + s2.length();
        int min_size = Math.min(s1.length(), s2.length());

        for (int i = 1; i < min_size; i++) {
            String sub2 = s2.substring(0, i);
            String sub1 = s1.substring(s1.length() - i);
            if(sub1.equals(sub2))
                answer = s1.length() + s2.length() - i;
        }
        for (int i = 1; i < min_size; i++) {
            String sub1 = s1.substring(0, i);
            String sub2 = s2.substring(s1.length() - i);
            if(sub1.equals(sub2))
                answer = s1.length() + s2.length() - i;
        }
*/



        int answer = 0;
        int i = 0;
        int cnt = 0;
        int answer1 = 0;

        for (int j = i; j < s2.length(); j++) {
            if(s1.charAt(i) == s2.charAt(j)){
                i++;
                cnt++;
                answer = Math.max(cnt, answer);
            } else {
                cnt = 0;
            }
        }

        i = 0;
        cnt = 0;
        for (int j = i; j < s1.length(); j++) {
            if(s2.charAt(i) == s1.charAt(j)){
                i++;
                cnt++;
                answer = Math.max(cnt, answer);
            } else {
                cnt = 0;
            }
        }

        answer = Math.min(answer + s1.length(), answer + s2.length());


        return answer;
    }
    
    // 아래는 테스트케이스 출력을 해보기 위한 main 메소드입니다.
    public static void main(String[] args) {
        Question04 sol = new Question04();
        String s1 = new String("ababc");
        String s2 = new String("abcdab");
        int ret = sol.solution(s1, s2);
        
        // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
        System.out.println("solution 메소드의 반환 값은 " + ret + " 입니다.");
    }
}