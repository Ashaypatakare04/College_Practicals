import javax.swing.*;
import java.awt.*;

public class GridLayoutDemo {
    public GridLayoutDemo() {
        JFrame frame = new JFrame("GridLayout Demo");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLayout(new GridLayout(2, 3));
        JButton[] buttons = new JButton[6];
        for (int i = 0; i < 6; i++) {
            buttons[i] = new JButton(String.valueOf(i + 1));
            int idx = i;
            buttons[i].addActionListener(e -> {
                int next = (idx + 1) % 6;
                String temp = buttons[idx].getText();
                buttons[idx].setText(buttons[next].getText());
                buttons[next].setText(temp);
            });
            frame.add(buttons[i]);
        }
        frame.setSize(300, 150);
        frame.setVisible(true);
    }
    public static void main(String[] args) { new GridLayoutDemo(); }
}
