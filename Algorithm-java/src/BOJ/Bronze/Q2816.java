package BOJ.Bronze;

import java.io.*;
import java.util.ArrayList;
import java.util.List;

public class Q2816 {
    static List<String> list;
    static int idx1, idx2, now, n;
    static StringBuilder cmdList;

    public static void move(int cmd) {
        switch (cmd) {
            case 1:
                if (now < n - 1) {
                    cmdList.append(cmd);
                    now++;
                }
                break;
            case 2:
                if (now > 0) {
                    cmdList.append(cmd);
                    now--;
                }
                break;
            case 3:
                if (now < n - 1) {
                    cmdList.append(cmd);
                    if (now == idx1) idx1++;
                    else if (now + 1 == idx1) idx1--;
                    if (now == idx2) idx2++;
                    else if (now + 1 == idx2) idx2--;
                    list.add(now, list.remove(now + 1));
                    now++;
                }
                break;
            case 4:
                if (now > 0) {
                    cmdList.append(cmd);
                    if (now == idx1) idx1--;
                    else if (now - 1 == idx1) idx1++;
                    if (now == idx2) idx2--;
                    else if (now - 1 == idx2) idx2++;
                    list.add(now, list.remove(now - 1));
                    now--;
                }
        }
        System.out.println(cmd + " - " + now + ": " + String.join(" ", list));

    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        n = Integer.parseInt(br.readLine().trim());
        list = new ArrayList<>();

        idx1 = -1;
        idx2 = -1;
        now = 0;
        cmdList = new StringBuilder();

        for (int i = 0; i < n; i++) {
            String ch = br.readLine().trim();
            list.add(ch);
            if (ch.equals("KBS1")) {
                idx1 = i;
            } else if (ch.equals("KBS2")) {
                idx2 = i;
            }
        }

        while(idx1 != 0 || idx2 != 1) {
            if (idx1 < idx2) {
                while(now < idx1) {
                    move(3);
                }
                if (idx1 == 0 && idx2 == 1) break;
                move(2);
                while(now > 0) {
                    move(4);
                }
                if (idx1 == 0 && idx2 == 1) break;
                move(1);
                while(now < idx2) {
                    move(3);
                }
                if (idx1 == 0 && idx2 == 1) break;
                move(2);
                while(now > 1) {
                    move(4);
                }
            } else {
                if(idx2 == 0 && idx1 == 1) {
                    move(3);
                    break;
                }
                while(now < idx2) {
                    move(3);
                }
                if (idx1 == 0 && idx2 == 1) break;
                move(2);
                while(now > 0) {
                    move(4);
                }
                if (idx1 == 0 && idx2 == 1) break;
                move(1);
                while(now < idx1) {
                    move(3);
                }
                if (idx1 == 0 && idx2 == 1) break;
                move(2);
                while(now > 0) {
                    move(4);
                }
            }

        }
        String cmdAll = cmdList.toString();
        while(cmdAll.contains("21") || cmdAll.contains("21")) {
            cmdAll = cmdAll.replaceAll("21", "");
            cmdAll = cmdAll.replaceAll("12", "");
        }
        while(cmdAll.contains("34") || cmdAll.contains("43")) {
            cmdAll = cmdAll.replaceAll("34", "");
            cmdAll = cmdAll.replaceAll("43", "");
        }

        bw.write(cmdAll);
        bw.flush();
    }
}
