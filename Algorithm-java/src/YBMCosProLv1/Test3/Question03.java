package YBMCosProLv1.Test3;// 다음과 같이 import를 사용할 수 있습니다.
import java.util.*;
import java.util.function.IntConsumer;

class Question03 {
    public int solution(String[] bishops) {
        // 여기에 코드를 작성해주세요.
        int answer = 0;

        int[][] board = new int[8][8];

        for (String bishop : bishops) {
            int row = bishop.charAt(0) - 'A';
            int col = Integer.parseInt(bishop.substring(1)) - 1;

            board[row][col] = 1;

            int[] dx = {-1, -1, 1, 1};
            int[] dy = {-1, 1, -1, 1};

            for (int i = 0; i < 4; i++) {
                int x = row;
                int y = col;
                while (x >= 0 && x < 8 && y >= 0 && y < 8){
                    board[x][y] = 1;
                    x += dx[i];
                    y += dy[i];
                }
            }
        }
        for (int[] ints : board) {
            answer += Arrays.stream(ints).sum();
        }

        return 64 - answer;
    }

    // 아래는 테스트케이스 출력을 해보기 위한 main 메소드입니다.
    public static void main(String[] args) {
        Question03 sol = new Question03();
        String[] bishops1 = {new String("D5")};
        int ret1 = sol.solution(bishops1);
        
        // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
        System.out.println("solution 메소드의 반환 값은 " + ret1 + " 입니다.");

        String[] bishops2 = {new String("D5"), new String("E8"), new String("G2")};
        int ret2 = sol.solution(bishops2);
        
        // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
        System.out.println("solution 메소드의 반환 값은 " + ret2 + " 입니다.");
    }
}