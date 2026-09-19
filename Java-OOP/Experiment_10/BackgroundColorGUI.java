import javax.swing.*;
import java.awt.*;

public class BackgroundColorGUI {
    public BackgroundColorGUI() {
        JFrame frame = new JFrame("Background Color Changer");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLayout(new FlowLayout());
        JButton r = new JButton("Red"), g = new JButton("Green"), b = new JButton("Blue");
        r.addActionListener(e -> frame.getContentPane().setBackground(Color.RED));
        g.addActionListener(e -> frame.getContentPane().setBackground(Color.GREEN));
        b.addActionListener(e -> frame.getContentPane().setBackground(Color.BLUE));
        frame.add(r); frame.add(g); frame.add(b);
        frame.setSize(400, 200);
        frame.setVisible(true);
    }
    public static void main(String[] args) { new BackgroundColorGUI(); }
}
