package YBMCosProLv1.Test4;// 다음과 같이 import를 사용할 수 있습니다.
import java.util.*;
import java.util.function.IntConsumer;

class Question08 {
    public int solution(int[] card, int n) {
        // 여기에 코드를 작성해주세요.
        Set<Integer> rst = new HashSet<>();
        int len = card.length;

        for (int i = 0; i < len; i++)
            permutation(card, new int[len], new boolean[len], 0, len, rst);

        ArrayList<Integer> list = new ArrayList<>(rst);
        Collections.sort(list);
        return list.indexOf(n);
    }

    public void permutation(int[] arr, int[] output, boolean[] visited, int depth, int n, Set<Integer> rst) {
        if (depth == n) {
            int rr = 0;
            for (int o: output) {
                rr *= 10;
                rr += o;
            }
            rst.add(rr);
            return;
        }

        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                visited[i] = true;
                output[depth] = arr[i];
                permutation(arr, output, visited, depth + 1, n, rst);
                visited[i] = false;
            }
        }
    }
    
    // 아래는 테스트케이스 출력을 해보기 위한 main 메소드입니다.
    public static void main(String[] args) {
        Question08 sol = new Question08();
        int card1[] = {1, 2, 1, 3};
        int n1 = 1312;
        int ret1 = sol.solution(card1, n1);

        // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
        System.out.println("solution 메소드의 반환 값은 " + ret1 + " 입니다.");

        int card2[] = {1, 1, 1, 2};
        int n2 = 1122;
        int ret2 = sol.solution(card2, n2);
        
        // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
        System.out.println("solution 메소드의 반환 값은 " + ret2 + " 입니다.");
    }    
}