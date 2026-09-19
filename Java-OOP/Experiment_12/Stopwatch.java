import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
public class Stopwatch extends JFrame implements Runnable, ActionListener {
    JLabel label;
    JButton start, stop, reset;
    Thread t;
    boolean running = false;
    int sec = 0, min = 0, hr = 0;
    Stopwatch() {
        setTitle("Stopwatch");
        setSize(300, 200);
        setLayout(new FlowLayout());
        label = new JLabel("00:00:00");
        label.setFont(new Font("Arial", Font.BOLD, 25));
        start = new JButton("Start");
        stop = new JButton("Stop");
        reset = new JButton("Reset");
        add(label);
        add(start);
        add(stop);
        add(reset);
        start.addActionListener(this);
        stop.addActionListener(this);
        reset.addActionListener(this);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setVisible(true);
    }
    public void run() {
        while (running) {
            try {
                Thread.sleep(1000);
            } catch (Exception e) {}

            sec++;

            if (sec == 60) {
                sec = 0;
                min++;
            }

            if (min == 60) {
                min = 0;
                hr++;
            }

            label.setText(
                String.format("%02d:%02d:%02d", hr, min, sec)
            );
        }
    }
    public void actionPerformed(ActionEvent e) {

        if (e.getSource() == start) {
            if (!running) {
                running = true;
                t = new Thread(this);
                t.start();
            }
        }
        if (e.getSource() == stop) {
            running = false;
        }

        if (e.getSource() == reset) {
            running = false;
            hr = min = sec = 0;
            label.setText("00:00:00");
        }
    }
    public static void main(String[] args) {
        new Stopwatch();
    }
}
