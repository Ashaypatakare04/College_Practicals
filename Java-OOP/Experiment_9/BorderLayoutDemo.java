import javax.swing.*;
import java.awt.*;

public class BorderLayoutDemo {
    public BorderLayoutDemo() {
        JFrame frame = new JFrame("BorderLayout Demo");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLayout(new BorderLayout(10, 10));

        JPanel north = new JPanel();
        north.add(new JLabel("Enter number:"));
        JTextField input = new JTextField(10);
        north.add(input);
        frame.add(north, BorderLayout.NORTH);

        JPanel center = new JPanel();
        String[] options = {"Binary", "Octal", "Hex"};
        int[] bases = {2, 8, 16};
        JTextField result = new JTextField(15);
        result.setEditable(false);

        for (int i = 0; i < options.length; i++) {
            JButton btn = new JButton(options[i]);
            int base = bases[i];
            btn.addActionListener(e -> {
                try {
                    int n = Integer.parseInt(input.getText());
                    result.setText(Integer.toString(n, base).toUpperCase());
                } catch (Exception ex) { result.setText("Error"); }
            });
            center.add(btn);
        }
        frame.add(center, BorderLayout.CENTER);

        JPanel south = new JPanel();
        south.add(new JLabel("Result:"));
        south.add(result);
        frame.add(south, BorderLayout.SOUTH);

        frame.setSize(350, 200);
        frame.setVisible(true);
    }
    public static void main(String[] args) { new BorderLayoutDemo(); }
}
