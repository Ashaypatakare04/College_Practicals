import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class RadioDemo {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Radio Button Demo");
        frame.setSize(300, 200);
        frame.setLayout(new FlowLayout());
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        
        JRadioButton male = new JRadioButton("Male");
        JRadioButton female = new JRadioButton("Female");
        ButtonGroup group = new ButtonGroup();
        group.add(male);
        group.add(female);

        JButton submit = new JButton("Submit");
        JLabel result = new JLabel("");
        frame.add(male);
        frame.add(female);
        frame.add(submit);
        frame.add(result);
        
        submit.addActionListener(e -> {
            if (male.isSelected()) {
                result.setText("Selected: Male");
            } else if (female.isSelected()) {
                result.setText("Selected: Female");
            } else {
                result.setText("No selection");
            }
        });
        frame.setVisible(true);
    }
}
