package BOJ.Silver;

import java.io.*;
import java.util.LinkedList;

public class Q10866 {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine().trim());
        LinkedList<Integer> deque = new LinkedList<>();

        for (int i = 0; i < n; i++) {
            String cmd = br.readLine().trim();
            int c_num = -1;
            if (cmd.contains(" ")) {
                c_num = Integer.parseInt(cmd.split(" ")[1]);
                cmd = cmd.split(" ")[0];
            }

            int deque_size = deque.size();
            int print_num = -1;
            boolean print_yn = true;

            switch (cmd) {
                case "push_front":
                    print_yn = false;
                    deque.addFirst(c_num);
                    break;
                case "push_back":
                    print_yn = false;
                    deque.add(c_num);
                    break;
                case "pop_front":
                    if (deque_size > 0) {
                        print_num = deque.getFirst();
                        deque.removeFirst();
                    }
                    break;
                case "pop_back":
                    if (deque_size > 0) {
                        print_num = deque.getLast();
                        deque.removeLast();
                    }
                    break;
                case "size":
                    print_num = deque_size;
                    break;
                case "empty":
                    if (deque_size > 0)
                        print_num = 0;
                    else
                        print_num = 1;
                    break;
                case "front":
                    if (deque_size > 0)
                        print_num = deque.getFirst();
                    break;
                case "back":
                    if (deque_size > 0)
                        print_num = deque.getLast();
                    break;
            }

            if (print_yn)
                bw.write(Integer.toString(print_num) + "\n");
        }
        bw.flush();
    }

}
