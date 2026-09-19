import javax.swing.*;
import java.awt.*;

public class TimerGUI {
    private int seconds = 0;
    public TimerGUI() {
        JFrame frame = new JFrame("Simple Timer");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLayout(new FlowLayout());
        JLabel label = new JLabel("Time: 0s");
        Timer timer = new Timer(1000, e -> label.setText("Time: " + (++seconds) + "s"));
        JButton start = new JButton("Start");
        JButton stop = new JButton("Stop");
        start.addActionListener(e -> timer.start());
        stop.addActionListener(e -> timer.stop());
        frame.add(label); frame.add(start); frame.add(stop);
        frame.setSize(300, 150);
        frame.setVisible(true);
    }
    public static void main(String[] args) { new TimerGUI(); }
}
