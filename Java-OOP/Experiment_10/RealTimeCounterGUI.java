import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class RealTimeCounterGUI {
    public RealTimeCounterGUI() {
        JFrame frame = new JFrame("Real-time Counter");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        JTextArea area = new JTextArea();
        JLabel label = new JLabel("Characters: 0 | Words: 0");
        area.addKeyListener(new KeyAdapter() {
            public void keyReleased(KeyEvent e) {
                String text = area.getText();
                String[] words = text.trim().split("\\s+");
                int wc = text.trim().isEmpty() ? 0 : words.length;
                label.setText("Characters: " + text.length() + " | Words: " + wc);
            }
        });
        frame.add(new JScrollPane(area), BorderLayout.CENTER);
        frame.add(label, BorderLayout.SOUTH);
        frame.setSize(400, 300);
        frame.setVisible(true);
    }
    public static void main(String[] args) { new RealTimeCounterGUI(); }
}
