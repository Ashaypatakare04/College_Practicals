import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class CounterApp {
    static int count = 0;

    public static void main(String[] args) {
        Label myLabel=new Label("Counter");
        JFrame frame = new JFrame("Counter");
        frame.setSize(300, 150);
        frame.setLayout(new FlowLayout());
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        
        JTextField textField = new JTextField("0", 10);
        JButton upBtn = new JButton("Count Up");
        JButton downBtn = new JButton("Count Down");
        JButton resetBtn = new JButton("Reset");

        frame.add(myLabel);
        frame.add(textField);
        frame.add(upBtn);
        frame.add(downBtn);
        frame.add(resetBtn);
        
        upBtn.addActionListener(e -> {
            count++;
            textField.setText(String.valueOf(count));
        });
        downBtn.addActionListener(e -> {
            count--;
            textField.setText(String.valueOf(count));
        });
        resetBtn.addActionListener(e -> {
            count = 0;
            textField.setText(String.valueOf(count));
        });
        frame.setVisible(true);
    }
}
