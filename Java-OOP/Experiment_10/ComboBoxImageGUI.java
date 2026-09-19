import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class ComboBoxImageGUI {
    public ComboBoxImageGUI() {
        JFrame frame = new JFrame("ComboBox Image Demo");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLayout(new FlowLayout());
        String[] options = {"Java", "Python", "C++"};
        JComboBox<String> combo = new JComboBox<>(options);
        JLabel imgLabel = new JLabel("Select an option");
        imgLabel.setPreferredSize(new Dimension(200, 200));
        imgLabel.setBorder(BorderFactory.createLineBorder(Color.GRAY));
        combo.addItemListener(e -> {
            if (e.getStateChange() == ItemEvent.SELECTED) {
                imgLabel.setText("Image for: " + combo.getSelectedItem());
            }
        });
        frame.add(combo); frame.add(imgLabel);
        frame.setSize(400, 300);
        frame.setVisible(true);
    }
    public static void main(String[] args) { new ComboBoxImageGUI(); }
}
