import javax.swing.*;
import java.awt.*;

public class FlowLayoutDemo {
    public FlowLayoutDemo() {
        JFrame frame = new JFrame("FlowLayout Demo");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLayout(new FlowLayout(FlowLayout.LEFT, 10, 20));
        frame.add(new JCheckBox("Java"));
        frame.add(new JCheckBox("Python"));
        frame.add(new JCheckBox("C++"));
        frame.setSize(300, 150);
        frame.setVisible(true);
    }
    public static void main(String[] args) { new FlowLayoutDemo(); }
}
